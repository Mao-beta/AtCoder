"""Offline CP Snippet Palette (stdlib only, no AI or network operations).

Reads JetBrains Live Template XML files without modifying them, plus local
.py snippets. Search, preview, copy, and inspect a configurable checklist.
"""

from __future__ import annotations

import argparse
import ast
import csv
import difflib
from functools import cached_property
import json
import os
from dataclasses import dataclass
from pathlib import Path
import re
import sys
import unicodedata
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parent
CONFIG = ROOT / "config.json"
WISHLIST = ROOT / "wishlist.json"
STATE = ROOT / ".palette_state.json"
IDENT = re.compile(r"\$([A-Za-z_][A-Za-z_0-9]*)\$")
METHOD = re.compile(r"^\s+def\s+([A-Za-z_]\w*)\s*\(", re.M)
TOP_NAME = re.compile(r"^class\s+([A-Za-z_]\w*)\b", re.M)

CATEGORIES = {
    "basic": "基本処理",
    "structures": "データ構造",
    "graphs": "グラフ・木",
    "strings": "文字列",
    "math": "数論・代数",
    "geometry": "幾何",
    "search": "探索",
    "user": "user / Python",
}
STARTER_ORDER = {
    name: i
    for i, name in enumerate(
        (
            "UnionFind",
            "BIT",
            "segtree",
            "lazy_segtree",
            "shortest_paths",
            "scc",
            "sequence",
            "combinatorics",
            "polynomial",
            "LCATree",
        )
    )
}
# 表記揺れと、コンテスト中に入力しやすい短い呼び名。
ALIASES = [
    (("segtree", "segtree"), "セグ木 せぐき セグメント木 segment tree"),
    (("lazy_segtree", "lazy_segtree"), "遅延セグ木 遅延評価 lazy segment tree"),
    (("dsu", "UnionFind"), "uf union find unionfind disjoint set 連結判定 素集合"),
    (("fenwick_tree", "BIT"), "bit fenwick tree フェニック木 フェンウィック木 区間和"),
    (("scc", "SCC"), "scc 強連結成分 強連結成分分解"),
    (("two_sat", "two_sat"), "2sat 2-sat two sat 充足可能性"),
    (
        ("dijkstra", "template_Dijkstra", "shortest_paths"),
        "最短路 さいたんろ ダイクストラ shortest path",
    ),
    (
        ("polynomial", "FPS"),
        "fps ntt fft 形式的冪級数 多項式 畳み込み たたみこみ",
    ),
    (("Comb", "combinatorics"), "ncr nck combination 組合せ 組み合わせ 二項係数"),
    (("lis_length", "lis_indices"), "lis 最長増加部分列"),
    (("compress", "sequence"), "座圧 座標圧縮 ざひょうあっしゅく"),
    (("LowLink",), "low link 橋 関節点"),
    (("HLD",), "hl分解 重軽分解 heavy light decomposition"),
    (("mf_graph",), "最大流 max flow dinic ディニック"),
    (("mcf_graph",), "最小費用流 min cost flow"),
    (("suffix_array",), "sa suffix array 接尾辞配列 サフィックスアレイ"),
    (("rolling_hash", "RollingHash"), "ローリングハッシュ rolling hash rh"),
    (("WaveletMatrix",), "wm ウェーブレット行列 ウェーブレットマトリクス 区間k番目"),
    (("LCATree",), "lca 最小共通祖先 lowest common ancestor"),
]


def norm(s: object) -> str:
    return unicodedata.normalize("NFKC", str(s)).casefold().strip()


def read_json(path: Path, fallback):
    if path.exists():
        with path.open("r", encoding="utf-8-sig") as f:
            return json.load(f)
    return fallback


def resolve_path(spec: str) -> Path:
    p = Path(os.path.expandvars(os.path.expanduser(spec)))
    return p if p.is_absolute() else ROOT / p


def config():
    return read_json(
        CONFIG,
        {
            "snippet_dirs": ["snippets"],
            "extra_template_dirs": [],
            "source_urls": {},
            "provenance": {},
            "default_provenance": "unknown",
        },
    )


def jetbrains_dirs():
    """Find standard live template locations (including Settings Sync)."""
    bases = []
    if sys.platform == "win32":
        appdata = os.environ.get("APPDATA")
        if appdata:
            bases.append(Path(appdata) / "JetBrains")
    elif sys.platform == "darwin":
        bases.append(Path.home() / "Library/Application Support/JetBrains")
    else:
        bases.append(
            Path(os.environ.get("XDG_CONFIG_HOME", str(Path.home() / ".config")))
            / "JetBrains"
        )
    found = []
    for base in bases:
        if not base.exists():
            continue
        # Newer IDE configs first. Deduplicate identical templates afterwards.
        for ide in sorted(base.glob("PyCharm*"), reverse=True):
            for candidate in (ide / "templates", ide / "settingsSync" / "templates"):
                if candidate.is_dir():
                    found.append(candidate)
    return found


def template_source(description):
    """このツールで登録したLive Templateの元File。説明末尾の印だけを使う。"""
    match = re.search(r"\[cp-palette: ((?:library|snippets)/[^\]\n]+\.py)(?:#[A-Za-z_]\w*)?\]$", description)
    if match:
        path = (ROOT / match[1]).resolve()
        if path.is_relative_to(ROOT):
            return path
    return None


@dataclass
class Entry:
    name: str
    kind: str  # 'Live' or 'File'
    group: str
    description: str
    code: str
    path: str
    abbreviation: str = ""
    methods: tuple[str, ...] = ()
    classes: tuple[str, ...] = ()
    provenance: str = "unknown"
    source_url: str = ""
    keywords: str = ""
    source_path: str = ""  # 同梱Fileから登録したLive Templateの説明を結び付ける。
    source_symbol: str = ""

    @property
    def key(self):
        return norm(
            f"{self.kind}:{self.path}:{self.group}:{self.name}".replace("\\", "/")
        )

    @property
    def category(self):
        return CATEGORIES.get(self.group, self.group if self.group != "." else "その他")

    @cached_property
    def search_fields(self):
        symbols = [s for s in (*self.classes, *self.methods) if not s.startswith("_")]
        identifiers = {norm(s) for s in [self.name, *symbols]}
        aliases = " ".join(
            words
            for names, words in ALIASES
            if any(norm(n) in identifiers for n in names)
        )
        primary_aliases = " ".join(
            words
            for names, words in ALIASES
            if norm(self.name) in {norm(n) for n in names}
        )
        return {
            "name": norm(self.name),
            "abbrev": norm(self.abbreviation),
            "symbols": tuple(norm(s) for s in symbols),
            "meta": norm(
                " ".join(
                    (
                        self.group,
                        self.category,
                        self.description,
                        self.keywords,
                        aliases,
                    )
                )
            ),
            "aliases": norm(primary_aliases).split(),
            "code": norm(self.code),
        }

    @cached_property
    def module_doc(self):
        """ファイル冒頭の使い方を取得する。スニペットのコードは実行しない。"""
        try:
            tree = ast.parse(self.code.replace("$END$", ""))
        except (SyntaxError, ValueError):
            return ""
        return ast.get_docstring(tree) or ""

    @cached_property
    def outline(self):
        """(表示名, 呼び出し方, 行番号, docstring)。コードは実行しない。"""
        result = []
        try:
            tree = ast.parse(self.code.replace("$END$", ""))
        except (SyntaxError, ValueError):
            return result
        classes = {n.name: n for n in tree.body if isinstance(n, ast.ClassDef)}

        def constructor(node, seen=()):
            if node.name in seen:
                return None
            for method in node.body:
                if isinstance(method, ast.FunctionDef) and method.name == "__init__":
                    return method
            # 同じファイルで定義された親クラスのコンストラクタを表示する。
            for base in node.bases:
                if isinstance(base, ast.Name) and base.id in classes:
                    inherited = constructor(classes[base.id], (*seen, node.name))
                    if inherited:
                        return inherited
            return None

        for node in tree.body:
            if isinstance(node, ast.ClassDef) and not node.name.startswith("_"):
                init = constructor(node)
                args = signature_args(init) if init else ""
                result.append(
                    (
                        node.name,
                        f"{node.name}({args})",
                        node.lineno,
                        ast.get_docstring(node)
                        or (ast.get_docstring(init) if init else "")
                        or "",
                    )
                )
                for method in node.body:
                    if isinstance(
                        method, ast.FunctionDef
                    ) and not method.name.startswith("_"):
                        name = f"{node.name}.{method.name}"
                        is_property = any(
                            isinstance(d, ast.Name) and d.id == "property"
                            for d in method.decorator_list
                        )
                        signature = (
                            name if is_property else f"{name}({signature_args(method)})"
                        )
                        result.append(
                            (
                                name,
                                signature,
                                method.lineno,
                                ast.get_docstring(method) or "",
                            )
                        )
            elif isinstance(
                node, (ast.FunctionDef, ast.AsyncFunctionDef)
            ) and not node.name.startswith("_"):
                result.append(
                    (
                        node.name,
                        f"{node.name}({signature_args(node)})",
                        node.lineno,
                        ast.get_docstring(node) or "",
                    )
                )
        return result

    def searchable(self):
        return norm(
            " ".join(
                (
                    self.name,
                    self.group,
                    self.description,
                    self.abbreviation,
                    " ".join(self.methods),
                    " ".join(self.classes),
                    self.keywords,
                    self.code,
                )
            )
        )


def signature_args(node):
    # 注釈を除いた短いシグネチャ。posonly/keyword-only/defaultは保持する。
    import copy

    args = copy.deepcopy(node.args)
    for part in [args.posonlyargs, args.args, args.kwonlyargs]:
        for arg in part:
            arg.annotation = None
    if args.vararg:
        args.vararg.annotation = None
    if args.kwarg:
        args.kwarg.annotation = None
    if args.posonlyargs and args.posonlyargs[0].arg in {"self", "cls"}:
        args.posonlyargs.pop(0)
    elif args.args and args.args[0].arg in {"self", "cls"}:
        args.args.pop(0)
    return ast.unparse(args)


def code_description(code, fallback):
    try:
        tree = ast.parse(code)
        doc = ast.get_docstring(tree) or ""
        if not doc or doc.startswith("競プロ用スニペット"):
            doc = next(
                (
                    ast.get_docstring(n)
                    for n in tree.body
                    if isinstance(n, ast.ClassDef)
                    and not n.name.startswith("_")
                    and ast.get_docstring(n)
                ),
                "",
            )
        return doc.splitlines()[0] if doc else fallback
    except (SyntaxError, ValueError):
        return fallback


def inspect_python(s: str):
    methods = set(METHOD.findall(s))
    classes = set(TOP_NAME.findall(s))
    try:
        tree = ast.parse(s)
        for n in tree.body:
            if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)):
                methods.add(n.name)
            elif isinstance(n, ast.ClassDef):
                classes.add(n.name)
                for m in n.body:
                    if isinstance(m, (ast.FunctionDef, ast.AsyncFunctionDef)):
                        methods.add(m.name)
    except (SyntaxError, ValueError):
        pass
    return tuple(sorted(methods)), tuple(sorted(classes))


def metadata(name, path, cfg, packaged=False):
    prov = cfg.get("provenance", {})
    urls = cfg.get("source_urls", {})
    # Optional descriptive metadata; never used to restrict copying.
    default = "ai" if packaged else cfg.get("default_provenance", "unknown")
    origin = prov.get(str(path), prov.get(name, default))
    url = urls.get(str(path), urls.get(name, ""))
    return origin, url


def load_entries(cfg=None, warnings=None):
    cfg = config() if cfg is None else cfg
    entries = []
    dirs = jetbrains_dirs()
    dirs += [resolve_path(s) for s in cfg.get("extra_template_dirs", [])]
    seen_xml = set()
    seen_files = set()

    def warn(message):
        if warnings is not None:
            warnings.append(message)
        elif sys.stderr is not None:
            print(f"[warning] {message}", file=sys.stderr)

    for directory in dirs:
        if not directory.is_dir():
            warn(f"テンプレートのフォルダがありません: {directory}")
            continue
        for path in sorted(directory.glob("*.xml")):
            try:
                doc = ET.parse(path)
                group = doc.getroot().get("group", path.stem)
                if norm(group) != "user":
                    continue
                for item in doc.findall(".//template"):
                    # Python subcontexts can be enabled without the parent context.
                    if not any(
                        option.get("value", "").lower() == "true"
                        and (
                            option.get("name", "") == "Python"
                            or option.get("name", "").startswith("Python_")
                        )
                        for option in item.findall("./context/option")
                    ):
                        continue
                    name = item.get("name", "").strip()
                    code = item.get("value", "")
                    if not name or not code:
                        continue
                    # Search old/current versions without duplicating identical templates.
                    signature = (name, code)
                    if signature in seen_xml:
                        continue
                    seen_xml.add(signature)
                    ms, cs = inspect_python(code)
                    origin, url = metadata(name, path, cfg)
                    description = item.get("description", "")
                    source = template_source(description)
                    feature = re.search(r"#([A-Za-z_]\w*)\]$", description) if source else None
                    if source:
                        description = description[:description.rfind("[cp-palette:")].rstrip()
                    entries.append(
                        Entry(
                            name,
                            "Live",
                            group,
                            description,
                            code,
                            str(path),
                            name,
                            ms,
                            cs,
                            origin,
                            url,
                            " ".join(cfg.get("keywords", {}).get(source.stem if source else name, [])),
                            str(source) if source else "",
                            feature[1] if feature else "",
                        )
                    )
            except (ET.ParseError, OSError, UnicodeError) as exc:
                warn(f"読み込めません: {path}\n{exc}")
    for spec in cfg.get("snippet_dirs", ["snippets"]):
        directory = resolve_path(spec)
        if not directory.is_dir():
            warn(f"スニペットのフォルダがありません: {directory}")
            continue
        for path in sorted(directory.rglob("*.py")):
            if any(d in {".git", ".venv", "venv", "__pycache__"} for d in path.parts):
                continue
            try:
                key = norm(str(path.absolute()))
                if key in seen_files:
                    continue
                seen_files.add(key)
                if path.stat().st_size > 300_000:
                    warn(f"300KBを超えるため読み込みを省略: {path}")
                    continue
                code = path.read_text(encoding="utf-8-sig")
            except (OSError, UnicodeError) as exc:
                warn(f"読み込めません: {path}\n{exc}")
                continue
            ms, cs = inspect_python(code)
            rel = path.relative_to(directory)
            name = path.stem
            origin, url = metadata(
                name, path, cfg, packaged=(ROOT / "snippets") in path.parents
            )
            hint = ", ".join(cs) if cs else ", ".join(ms[:8])
            description = cfg.get("descriptions", {}).get(
                name, code_description(code, hint)
            )
            entries.append(
                Entry(
                    name,
                    "File",
                    str(rel.parent),
                    description,
                    code,
                    str(path),
                    "",
                    ms,
                    cs,
                    origin,
                    url,
                    " ".join(cfg.get("keywords", {}).get(name, [])),
                )
            )
    entries.sort(key=lambda e: (e.kind != "Live", norm(e.name), norm(e.group)))
    return entries, dirs


@dataclass
class SearchHit:
    entry: Entry
    score: int
    reason: str


def query_terms(query):
    """AND、引用符付きフレーズ、-除外、@file/@live。"""
    terms, excluded, kind = [], [], ""
    for match in re.finditer(r'(-?)"([^"\n]+)"|(\S+)', norm(query)):
        minus, quoted, bare = match.groups()
        token = quoted if quoted is not None else bare
        if quoted is None and token in {"@file", "@live"}:
            kind = token[1:].title()
        elif minus or (quoted is None and token.startswith("-") and len(token) > 1):
            excluded.append(token if quoted is not None else token[1:])
        else:
            terms.append(token)
    return terms, excluded, kind


def compact(text):
    return re.sub(r"[\W_]+", "", text)


def token_score(entry, token, fuzzy=False):
    f = entry.search_fields
    name, abbreviation, symbols = f["name"], f["abbrev"], f["symbols"]
    flat = compact(token)
    if token in {name, abbreviation} or (flat and flat == compact(name)):
        return 170, "名前一致"
    if token in f["aliases"] and token not in {
        "tree",
        "path",
        "find",
        "set",
        "light",
        "heavy",
        "flow",
        "cost",
        "min",
        "max",
        "array",
        "rolling",
        "hash",
        "segment",
        "union",
        "disjoint",
        "two",
        "sat",
    }:
        return 165, "呼び名一致"
    if token in symbols or (flat and any(flat == compact(s) for s in symbols)):
        return 160, "API一致"
    if name.startswith(token) or (abbreviation and abbreviation.startswith(token)):
        return 135, "名前の先頭"
    if any(s.startswith(token) for s in symbols):
        return 125, "APIの先頭"
    if token in name or any(token in s for s in symbols):
        return 110, "名前・API"
    if token in f["meta"]:
        return 85, "説明・別名"
    if token in f["code"]:
        return 20, "コード本文"
    if fuzzy and len(token) >= 3 and token.isascii() and flat.isalnum():
        for candidate in (name, abbreviation, *symbols):
            candidate = compact(candidate)
            if not candidate:
                continue
            if (
                abs(len(flat) - len(candidate)) <= 2
                and difflib.SequenceMatcher(None, flat, candidate).ratio() >= 0.78
            ):
                return (70 if candidate == compact(name) else 55), "あいまい一致"
            # 短い略記は名前・クラス名だけ。本文の偶然の一致を拾わない。
            if (
                candidate in {compact(name), *(compact(s) for s in entry.classes)}
                and len(flat) >= 3
            ):
                it = iter(candidate)
                if len(candidate) <= len(flat) * 3 and all(c in it for c in flat):
                    return 35, "略記一致"
    return -1, ""


def search_entries(
    entries, query="", *, kind="", group="", favorites=(), recent=(), scope="all"
):
    terms, excluded, query_kind = query_terms(query)
    favorites = set(favorites)
    recent_order = {key: i for i, key in enumerate(recent)}
    candidates = []
    for e in entries:
        if (kind and e.kind != kind) or (query_kind and e.kind != query_kind):
            continue
        if group and e.group != group:
            continue
        if scope == "favorites" and e.key not in favorites:
            continue
        if scope == "recent" and e.key not in recent_order:
            continue
        # 除外は名前・API・メタデータ・本文に共通。あいまい検索はしない。
        if any(token_score(e, word)[0] >= 0 for word in excluded):
            continue
        candidates.append(e)

    def collect(fuzzy):
        hits = []
        for e in candidates:
            matches = [token_score(e, t, fuzzy) for t in terms]
            if any(score < 0 for score, _ in matches):
                continue
            score = sum(s for s, _ in matches)
            reason = min(matches, default=(0, ""), key=lambda m: m[0])[1]
            hits.append(SearchHit(e, score, reason))
        return hits

    hits = collect(False)
    if not hits and terms:
        hits = collect(True)
    # 検索一致度が最優先。お気に入り/履歴で完全一致より弱い候補を上にしない。
    hits.sort(
        key=lambda h: (
            -h.score,
            h.entry.key not in favorites if scope != "recent" else False,
            recent_order.get(h.entry.key, 100000),
            h.entry.kind != "File",
            STARTER_ORDER.get(h.entry.name, 100) if not terms else 0,
            norm(h.entry.name),
            h.entry.key,
        )
    )
    return hits


def rank(entry: Entry, query: str):
    hits = search_entries([entry], query)
    return hits[0].score if hits else -1


def match_entries(entries, query, **options):
    return [hit.entry for hit in search_entries(entries, query, **options)]


class Preferences:
    """お気に入り・直近20件・表示設定だけをローカルに保存する。"""

    def __init__(self, path=STATE):
        self.path = Path(path)
        self.error = ""
        try:
            data = read_json(self.path, {})
            if not isinstance(data, dict):
                raise ValueError("設定はJSONオブジェクトである必要があります")
        except (OSError, ValueError) as error:
            self.error = f"表示設定を読み込めません: {error}"
            data = {}
        self.favorites = (
            set(x for x in data.get("favorites", []) if isinstance(x, str))
            if isinstance(data.get("favorites", []), list)
            else set()
        )
        self.recent = (
            list(
                dict.fromkeys(x for x in data.get("recent", []) if isinstance(x, str))
            )[:20]
            if isinstance(data.get("recent", []), list)
            else []
        )
        self.theme = (
            data.get("theme", "dark")
            if data.get("theme", "dark") in {"dark", "light"}
            else "dark"
        )
        size = data.get("font_size", 11)
        self.font_size = max(9, min(20, size)) if isinstance(size, int) else 11
        geometry = data.get("geometry", "1240x800")
        # 位置は画面構成の変化で見えなくなるため保存しない。
        self.geometry = (
            geometry
            if isinstance(geometry, str) and re.fullmatch(r"\d{3,4}x\d{3,4}", geometry)
            else "1240x800"
        )

    def toggle(self, entry):
        if entry.key in self.favorites:
            self.favorites.remove(entry.key)
        else:
            self.favorites.add(entry.key)
        self.save()

    def record(self, entry):
        self.recent = [entry.key] + [key for key in self.recent if key != entry.key]
        self.recent = self.recent[:20]
        self.save()

    def save(self):
        data = {
            "favorites": sorted(self.favorites),
            "recent": self.recent,
            "theme": self.theme,
            "font_size": self.font_size,
            "geometry": self.geometry,
        }
        temp = self.path.with_suffix(".tmp")
        try:
            temp.write_text(
                json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf8"
            )
            temp.replace(self.path)
            self.error = ""
        except OSError as error:
            self.error = f"表示設定を保存できません: {error}"
        return not self.error


def documentation(entry):
    """選択ファイルの解説と逆引き・API・verify表を表示。コードは実行しない。"""
    try:
        rel = Path(entry.source_path or entry.path).relative_to(ROOT).as_posix()
    except ValueError:
        return []
    sections = []
    algorithms = ROOT / "ALGORITHMS.md"
    if algorithms.exists():
        marker = r"^対象: \[[^\n]+\]\(" + re.escape(rel) + r"\)\n"
        for section in algorithms.read_text(encoding="utf8").split("\n## "):
            match = re.search(marker, section, re.MULTILINE)
            if match:
                sections.append(
                    ("アルゴリズムの解説", section[match.end() :].strip())
                )
                break
    for filename, title in [
        ("LIBRARY_GUIDE.md", "目的から選ぶ"),
        ("ABC_TOOLKIT.md", "ABCでの使い分け"),
        ("SEGTREE_RECIPES.md", "セグ木の派生版・設計"),
        ("ACL_API.md", "ACLの呼び出し方"),
        ("VERIFY_PROBLEMS.md", "verify問題"),
    ]:
        path = ROOT / filename
        if not path.exists():
            continue
        content = path.read_text(encoding="utf8")
        purpose = title == "目的から選ぶ"
        if purpose:
            _, heading, content = content.partition("## 目的から探す逆引き\n")
            if not heading:
                continue
            content = content.split("\n## ", 1)[0]
            content = re.sub(r"<!-- navigator: .+? -->\s*", "", content)
        rows = []
        for line in content.splitlines():
            if f"]({rel})" in line and line.startswith("|"):
                cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
                if purpose and len(cells) == 4:
                    rows.append(
                        f"目的：{cells[0]}\n使うもの：{cells[1]}\n"
                        f"選ぶ条件：{cells[2]}\n検索語：{cells[3]}"
                    )
                elif not purpose:
                    shown = cells if title == "ABCでの使い分け" else cells[1:]
                    rows.append("\n".join(shown).replace("<br>", "\n"))
        if rows:
            sections.append((title, "\n\n".join(rows)))
    return sections


def wishlist_items(entries):
    """Conservative name/class matching, not proof that a library is absent."""
    targets = read_json(WISHLIST, [])
    registered = set()
    for e in entries:
        registered.update(
            norm(x) for x in (e.name, e.abbreviation, *e.classes, *e.methods)
        )
        registered.add(norm(re.sub(r"^\d+_", "", e.name)))
    result = []
    for w in targets:
        aliases = [w["name"], *w.get("identifiers", [])]
        found = any(norm(a) in registered for a in aliases)
        result.append({**w, "detected": found})
    return result


def prepare_code(entry: Entry, mode="code"):
    if mode == "abbrev":
        if entry.kind != "Live":
            raise ValueError("略語のないファイルスニペットです")
        return entry.abbreviation
    code = entry.code
    if entry.kind == "Live":
        # A dynamic Live Template cannot be safely flattened into raw code.
        marker = "\x00DOLLAR\x00"
        code = code.replace("$$", marker)
        code = code.replace("$END$", "")
        dynamic = IDENT.findall(code)
        if dynamic:
            raise ValueError(
                "動的変数を含むため、略語をコピーしてPyCharmで展開してください: "
                + ", ".join(dynamic[:5])
            )
        code = code.replace(marker, "$")
    return code


def export_inventory(entries, path):
    wish = wishlist_items(entries)
    with open(path, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f, delimiter="\t")
        w.writerow(
            [
                "種別",
                "名前",
                "略語",
                "グループ",
                "説明/クラス",
                "メソッド",
                "由来",
                "公開URL",
                "元ファイル",
            ]
        )
        for e in entries:
            w.writerow(
                [
                    e.kind,
                    e.name,
                    e.abbreviation,
                    e.group,
                    e.description,
                    ", ".join(e.methods),
                    e.provenance,
                    e.source_url,
                    e.path,
                ]
            )
        for item in wish:
            w.writerow(
                [
                    "チェックリスト（検出あり）"
                    if item["detected"]
                    else "チェックリスト（未検出）",
                    item["name"],
                    "",
                    item.get("category", ""),
                    item.get("description", ""),
                    "",
                    "",
                    "",
                    "",
                ]
            )


def gui(entries, search_dirs, initial="", warnings=None):
    from palette_ui import PaletteApp

    app = PaletteApp(entries, search_dirs, initial, warnings=warnings)
    app.run()


def main():
    p = argparse.ArgumentParser(
        description="Offline fuzzy finder for PyCharm Live Templates and CP .py snippets"
    )
    p.add_argument("--query", default="", help="search query, or preload GUI search")
    p.add_argument(
        "--list", action="store_true", help="list loaded snippets without GUI"
    )
    p.add_argument("--export-inventory", metavar="FILE", help="export TSV inventory")
    p.add_argument(
        "--check", action="store_true", help="show discovered paths and counts"
    )
    args = p.parse_args()
    warnings = []
    try:
        entries, paths = load_entries(warnings=warnings)
    except (OSError, ValueError, TypeError, AttributeError) as error:
        message = f"設定・スニペットを読み込めません。\n{CONFIG}\n\n{error}"
        if args.list or args.export_inventory or args.check:
            print(message, file=sys.stderr)
        else:
            import tkinter as tk
            from tkinter import messagebox

            root = tk.Tk()
            root.withdraw()
            messagebox.showerror("Snippet Paletteの起動", message, parent=root)
            root.destroy()
        raise SystemExit(1)
    if warnings and sys.stderr is not None:
        for warning in warnings:
            print(f"[warning] {warning}", file=sys.stderr)
    if args.check:
        print("Live template locations:")
        for path in paths:
            print("  ", path, "[found]" if path.exists() else "[not found]")
        print(
            "Loaded:",
            len(entries),
            "Live:",
            sum(e.kind == "Live" for e in entries),
            "Files:",
            sum(e.kind == "File" for e in entries),
        )
        print("Checklist:", len(wishlist_items(entries)), "items")
    if args.export_inventory:
        export_inventory(entries, resolve_path(args.export_inventory))
        print("Exported:", resolve_path(args.export_inventory))
    if args.list or (args.query and (args.check or args.export_inventory)):
        for e in match_entries(entries, args.query):
            print(f"{e.kind:4} {e.name:25} {e.group:20} {e.description[:90]}")
    if not (args.list or args.export_inventory or args.check):
        gui(entries, paths, args.query, warnings=warnings)


if __name__ == "__main__":
    main()
