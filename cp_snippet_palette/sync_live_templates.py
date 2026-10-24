"""公開関数・クラス単位でPyCharmのuser/Python Live Templateへ登録する。既定はプレビュー。"""

import argparse
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
import os
import re
import tempfile
import xml.etree.ElementTree as ET

import cp_palette as core
from feature_snippets import collect_features


@dataclass
class Plan:
    target: Path
    before: bytes | None
    after: bytes
    added: list[str]
    updated: list[str]


def make_templates(entries, reserved_names=()):
    """接頭辞なしの略語を作る。既存名との重複時は元ファイル名を末尾に付ける。"""
    templates = []
    reserved_names = set(reserved_names)
    entries = [entry for entry in entries if entry.kind == "File" and
               any(Path(entry.path).resolve().is_relative_to(core.ROOT / folder) for folder in ("library", "snippets"))]
    features = collect_features(entries)
    used_names = reserved_names | {feature.abbreviation for feature in features}
    for feature in features:
        source = feature.source.resolve()
        relative = source.relative_to(core.ROOT).as_posix()
        name = feature.abbreviation
        if name in reserved_names:
            name += "_" + re.sub(r"^\d+_", "", source.stem)
            if name in used_names:
                raise ValueError(f"元ファイル名を付けても登録名が重複します。変更しません: {name}")
            used_names.add(name)
        item = ET.Element("template", {
            "name": name,
            "value": feature.code.replace("$", "$$") + "$END$",
            "description": f"{feature.description} [cp-palette: {relative}#{feature.name}]",
            "shortcut": "TAB", "toReformat": "false", "toShortenFQNames": "false",
        })
        context = ET.SubElement(item, "context")
        ET.SubElement(context, "option", {"name": "Python", "value": "true"})
        templates.append(item)
    if not templates:
        raise ValueError("登録対象の同梱Fileがありません。")
    return templates


def reserved_template_names(targets):
    """登録先の独自テンプレート名を予約する。管理対象の略語は次回も更新可能。"""
    return {item.get("name") for target in targets if target.exists()
            for item in ET.parse(target).getroot().findall("template")
            if core.template_source(item.get("description", "")) is None}


def build_plan(target, templates):
    """既存の略語・本文・コンテキストを保持し、自分が登録した同名項目だけを更新。"""
    target = Path(target)
    before = target.read_bytes() if target.exists() else None
    parser = ET.XMLParser(target=ET.TreeBuilder(insert_comments=True))
    root = ET.fromstring(before, parser=parser) if before else ET.Element("templateSet", {"group": "user"})
    if root.tag != "templateSet" or root.get("group") != "user":
        raise ValueError(f"userグループのXMLではありません: {target}")
    existing = {}
    for item in root.findall("template"):
        name = item.get("name")
        if name in existing:
            raise ValueError(f"既存の登録名が重複しています: {name}")
        existing[name] = item
    added, updated = [], []
    for template in templates:
        name = template.get("name")
        previous = existing.get(name)
        if previous is not None:
            if core.template_source(previous.get("description", "")) != core.template_source(template.get("description", "")):
                raise ValueError(f"既存のテンプレートと衝突しました。変更しません: {name}")
            if previous.attrib == template.attrib and [n.attrib for n in previous.findall("context/option")] == [n.attrib for n in template.findall("context/option")]:
                continue
            updated.append(name)
            root.remove(previous)
        else:
            added.append(name)
        # 各保存先のツリーが独立した要素を持つよう複製する。
        root.append(ET.fromstring(ET.tostring(template, encoding="utf-8")))
    if not added and not updated:
        return Plan(target, before, before, added, updated)
    ET.indent(root, space="  ")
    after = ET.tostring(root, encoding="utf-8", xml_declaration=True) + b"\n"
    return Plan(target, before, after, added, updated)


def apply_plans(plans, backup_root):
    """全保存先を事前確認し、バックアップ後に同じディレクトリ内で置換する。"""
    changed = [p for p in plans if p.added or p.updated]
    for plan in changed:
        current = plan.target.read_bytes() if plan.target.exists() else None
        if current != plan.before:
            raise ValueError(f"確認中に設定が変更されました。再実行してください: {plan.target}")
    if not changed:
        return None
    backup = Path(backup_root) / datetime.now().strftime("%Y%m%d-%H%M%S-%f")
    backup.mkdir(parents=True)
    for index, plan in enumerate(changed):
        if plan.before is not None:
            (backup / f"{index + 1}-{plan.target.parent.parent.name}-user.xml").write_bytes(plan.before)
    for plan in changed:
        plan.target.parent.mkdir(parents=True, exist_ok=True)
        staged = None
        try:
            with tempfile.NamedTemporaryFile(dir=plan.target.parent, prefix=".cp-palette-", suffix=".tmp", delete=False) as stream:
                staged = Path(stream.name)
                stream.write(plan.after)
            os.replace(staged, plan.target)
        finally:
            if staged is not None:
                staged.unlink(missing_ok=True)
    return backup


def write_catalog(templates):
    """登録する機能と略語の一覧を、登録データと同じ内容から更新する。"""
    source_count = len({core.template_source(item.get("description", "")) for item in templates})
    lines = ["# 機能別Live Template", "",
             f"同梱{source_count}ファイルから公開関数・クラスを切り出した{len(templates)}件。PyCharmのuserグループ、Pythonコンテキストへ登録する。",
             "",
             "関数は関数単位、クラスはメソッドを含むクラス単位。必要な補助関数・定数・importは一緒に展開する。元のFileはそのまま残す。略語に接頭辞は付けない。同名の別実装や既存の独自テンプレートとの重複時は、略語の末尾に元ファイル名を添える。",
             "",
             "検索画面の「Live · 略語」で絞り、選んだ略語をコピー → PyCharmで貼り付け → Tabで展開する。`lis_length`、`inversion_count`、`range_add_sum`などを直接入力してもよい。展開先は解答のmainより上。",
             "",
             "更新は[操作ガイド](LOCAL_USAGE.md#live-templateへの登録と更新)を参照。この一覧は登録スクリプトから生成し、各定義の説明は元Fileと共通。",
             "", "| 機能 | 略語 | 用途 |", "|---|---|---|"]
    for item in templates:
        description = item.get("description")
        match = re.search(r"\[cp-palette: (.+\.py)#([^\]]+)\]$", description)
        summary = description[:match.start()].strip().replace("|", "／").replace("\n", " ")
        lines.append(f"| [{match[2]}]({match[1]}) | `{item.get('name')}` | {summary} |")
    (core.ROOT / "LIVE_TEMPLATES.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ide-config", type=Path, required=True, help="PyCharm2026.2などの設定ディレクトリ")
    parser.add_argument("--apply", action="store_true", help="プレビューした登録・更新を適用する")
    args = parser.parse_args()
    if not args.ide_config.is_dir():
        parser.error("指定したIDE設定ディレクトリがありません。")
    # Liveの再読み込みやユーザー追加フォルダに依存せず、同梱Fileだけを登録する。
    entries, _ = core.load_entries({"snippet_dirs": ["library", "snippets"], "extra_template_dirs": []})
    targets = [args.ide_config / "templates" / "user.xml"]
    synced = args.ide_config / "settingsSync" / "templates"
    if synced.is_dir():
        targets.append(synced / "user.xml")
    templates = make_templates(entries, reserved_template_names(targets))
    plans = [build_plan(target, templates) for target in targets]
    for plan in plans:
        print(f"{plan.target}: 追加{len(plan.added)} / 更新{len(plan.updated)} / 機能 {len(templates)}")
        if plan.added:
            print("追加: " + ", ".join(plan.added[:12]) + (" ..." if len(plan.added) > 12 else ""))
        if plan.updated:
            print("更新: " + ", ".join(plan.updated))
    if args.apply:
        backup = apply_plans(plans, core.ROOT / ".live_template_backups")
        write_catalog(templates)
        print(f"登録完了。バックアップ: {backup}" if backup else "変更はありません。")
    else:
        print("プレビューです。適用する場合はPyCharmを終了し、--applyを付けて実行してください。")


if __name__ == "__main__":
    main()
