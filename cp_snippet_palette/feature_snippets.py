"""公開関数・クラスを、同じファイル内の依存定義とともに切り出す。"""

import ast
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
import re


@dataclass
class Feature:
    name: str
    abbreviation: str
    source: Path
    description: str
    code: str
    symbols: tuple[str, ...]


def slug(name):
    name = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1_\2", name)
    return re.sub(r"([a-z0-9])([A-Z])", r"\1_\2", name).lower()


def bound_names(node):
    if isinstance(node, (ast.FunctionDef, ast.ClassDef, ast.AsyncFunctionDef)):
        return {node.name}
    if isinstance(node, (ast.Import, ast.ImportFrom)):
        return {alias.asname or (alias.name.split(".")[0] if isinstance(node, ast.Import) else alias.name)
                for alias in node.names}
    return {n.id for n in ast.walk(node) if isinstance(n, ast.Name) and isinstance(n.ctx, ast.Store)}


def split_features(entry):
    """元のソース順・コメント・docstringを維持。補助関数は単独候補にしない。"""
    tree = ast.parse(entry.code)
    lines = entry.code.splitlines(keepends=True)
    nodes = [n for n in tree.body if not (isinstance(n, ast.Expr) and isinstance(n.value, ast.Constant))]
    definitions = {}
    for i, node in enumerate(nodes):
        if not isinstance(node, (ast.FunctionDef, ast.ClassDef, ast.Import, ast.ImportFrom, ast.Assign, ast.AnnAssign)):
            raise ValueError(f"分割未対応のトップレベル文: {entry.path}:{node.lineno}")
        for name in bound_names(node):
            definitions.setdefault(name, set()).add(i)
    for primary, node in enumerate(nodes):
        if not isinstance(node, (ast.FunctionDef, ast.ClassDef)) or node.name.startswith("_"):
            continue
        selected, pending = set(), [primary]
        while pending:
            index = pending.pop()
            if index in selected:
                continue
            selected.add(index)
            dependencies = {n.id for n in ast.walk(nodes[index])
                            if isinstance(n, ast.Name) and isinstance(n.ctx, ast.Load)}
            for name in dependencies:
                pending.extend(definitions.get(name, set()) - selected)
        selected.update(i for i, n in enumerate(nodes) if isinstance(n, ast.ImportFrom) and n.module == "__future__")
        pieces = []
        for i in sorted(selected):
            item = nodes[i]
            decorators = getattr(item, "decorator_list", [])
            start = min([item.lineno, *(d.lineno for d in decorators)]) - 1
            pieces.append("".join(lines[start:item.end_lineno]).rstrip())
        doc = ast.get_docstring(node) or node.name
        # 詳細な説明は元の定義内に保持。概要だけをモジュールの説明にする。
        code = repr(node.name + " — " + doc.splitlines()[0]) + "\n\n" + "\n\n\n".join(pieces) + "\n"
        compile(code, entry.path + "#" + node.name, "exec")
        symbols = tuple(nodes[i].name for i in sorted(selected) if isinstance(nodes[i], (ast.FunctionDef, ast.ClassDef)))
        yield Feature(node.name, slug(node.name), Path(entry.path), doc.splitlines()[0], code, symbols)


def collect_features(entries):
    """同じ幾何ヘルパー等は一つにまとめ、同名の別実装には元ファイル名を添える。"""
    grouped = defaultdict(list)
    for entry in entries:
        for feature in split_features(entry):
            signature = ast.dump(ast.parse(feature.code), include_attributes=False)
            if not any(other[0] == signature for other in grouped[feature.abbreviation]):
                grouped[feature.abbreviation].append((signature, feature))
    result = []
    names = set()
    for members in grouped.values():
        for _, feature in members:
            if len(members) > 1:
                feature.abbreviation += "_" + re.sub(r"^\d+_", "", feature.source.stem)
            if feature.abbreviation in names:
                raise ValueError(f"登録名が重複しています: {feature.abbreviation}")
            names.add(feature.abbreviation)
            result.append(feature)
    return sorted(result, key=lambda f: f.abbreviation)
