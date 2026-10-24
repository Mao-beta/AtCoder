"""機能ごとの依存関係と、PyCharm設定を保全した登録を確認する。"""

import builtins
from pathlib import Path
import symtable
import sys
import tempfile
import unittest
from unittest.mock import patch
import xml.etree.ElementTree as ET

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import cp_palette as core
from feature_snippets import collect_features
from sync_live_templates import make_templates, build_plan, apply_plans, reserved_template_names


class LiveTemplateTest(unittest.TestCase):
    def test_features_are_independent_and_keep_dependencies(self):
        with patch.object(core, "jetbrains_dirs", return_value=[]):
            entries, _ = core.load_entries({"snippet_dirs": ["library", "snippets"]})
        features = collect_features(entries)
        self.assertEqual(len(features), 274)
        spaces = {}

        def global_names(table):
            # symtableは名前がtopのメソッドをmodule_scope扱いするため、ローカルを除外。
            names = {s.get_name() for s in table.get_symbols()
                     if s.is_global() and s.is_referenced() and not s.is_local()}
            for child in table.get_children():
                names.update(global_names(child))
            return names

        for feature in features:
            namespace = {}
            exec(compile(feature.code, str(feature.source), "exec"), namespace)
            missing = global_names(symtable.symtable(feature.code, "feature", "exec")) - namespace.keys() - vars(builtins).keys()
            self.assertFalse(missing, (feature.abbreviation, missing))
            spaces[feature.abbreviation] = namespace
        self.assertNotIn("lis_length", spaces["compress"])
        self.assertEqual(spaces["compress"]["compress"]([40, 10, 40]), ([1, 0, 1], [10, 40]))
        self.assertEqual(spaces["inversion_count"]["inversion_count"]([3, 1, 2]), 2)
        self.assertIn("compress", spaces["inversion_count"])
        self.assertEqual(spaces["lis_length"]["lis_length"]([3, 1, 2, 2], strict=False), 3)
        seg = spaces["range_add_sum"]["range_add_sum"]([1, 2, 3])
        seg.apply(0, 2, 5)
        self.assertEqual(seg.prod(0, 3), 16)
        self.assertNotIn("range_add_min", spaces["range_add_sum"])
        self.assertEqual(spaces["fps_inverse"]["fps_inverse"]([1, -1], 4), [1, 1, 1, 1])
        self.assertEqual(spaces["heapq"]["Heapq"]([3, 1]).top(), 1)
        wavelet = spaces["wavelet_matrix"]["WaveletMatrix"]([3, 1, 3])
        self.assertEqual(wavelet.top(0, 3, 1), [(3, 2)])

    def test_merge_preserves_existing_templates_and_roundtrips_dollars(self):
        entry = core.Entry("example", "File", "basic", "テスト", 'def dollar():\n    """ドル文字を返す。"""\n    return "$HOME$ & 日本語"\n',
                           str(core.ROOT / "library/basic/sequence.py"))
        templates = make_templates([entry])
        self.assertEqual(make_templates([entry], {"dollar"})[0].get("name"), "dollar_sequence")
        with self.assertRaises(ValueError):
            make_templates([entry], {"dollar", "dollar_sequence"})
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp) / "templates/user.xml"
            target.parent.mkdir()
            target.write_text('<templateSet group="user"><template name="original" value="print($X$)&#10;$END$" description="元の内容" toReformat="true"><variable name="X" expression="" defaultValue="1" alwaysStopAt="true"/><context><option name="Python" value="true"/></context></template></templateSet>', encoding="utf8")
            before = target.read_bytes()
            original = ET.fromstring(before).find("template")
            plan = build_plan(target, templates)
            self.assertEqual(plan.added, ["dollar"])
            backup = apply_plans([plan], Path(temp) / "backups")
            self.assertEqual(next(backup.glob("*.xml")).read_bytes(), before)
            saved = ET.parse(target).getroot()
            self.assertEqual(saved.find("template").attrib, original.attrib)
            self.assertEqual(saved.find("template/variable").attrib, original.find("variable").attrib)
            with patch.object(core, "jetbrains_dirs", return_value=[]):
                loaded, _ = core.load_entries({"snippet_dirs": [], "extra_template_dirs": [str(target.parent)]})
            live = next(e for e in loaded if e.name == "dollar")
            self.assertEqual(live.source_symbol, "dollar")
            self.assertEqual(live.source_path, entry.path)
            self.assertNotIn("cp-palette", live.description)
            code = core.prepare_code(live)
            namespace = {}
            exec(code, namespace)
            self.assertEqual(namespace["dollar"](), "$HOME$ & 日本語")
            self.assertEqual(reserved_template_names([target]), {"original"})
            self.assertEqual(build_plan(target, templates).added, [])
            self.assertEqual(build_plan(target, templates).updated, [])
            # 印のない同名項目と、プレビュー後に変更された設定を保護する。
            saved.find("template[@name='dollar']").set("description", "ユーザーが独自に登録")
            target.write_bytes(ET.tostring(saved, encoding="utf-8"))
            with self.assertRaises(ValueError):
                build_plan(target, templates)
            with self.assertRaises(ValueError):
                apply_plans([plan], Path(temp) / "backups")


if __name__ == "__main__":
    unittest.main()
