"""Run: python -m unittest discover -s tests -v"""

import tempfile
from pathlib import Path
import unittest
from unittest.mock import patch
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import cp_palette as p


class PaletteTest(unittest.TestCase):
    def setUp(self):
        # ユーザーの実テンプレートを読み込まず、テスト用XMLだけで検証する。
        mock_dirs = patch.object(p, "jetbrains_dirs", return_value=[])
        mock_dirs.start()
        self.addCleanup(mock_dirs.stop)

    def test_parse_search_clipboard_and_inventory(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "templates").mkdir()
            (root / "source").mkdir()
            (root / "templates" / "CP.xml").write_text(
                """<?xml version="1.0" encoding="UTF-8"?>
<templateSet group="user">
  <template name="scc" value="class SCC:&#10;    def groups(self): return []&#10;$END$" description="強連結成分 Strongly Connected Components"><context><option name="Python" value="true"/><option name="Python_Class" value="false"/></context></template>
  <template name="macro" value="print($FOO$)" description="variable"><context><option name="Python_Statement" value="true"/></context></template>
  <template name="html" value="&lt;div&gt;" description="HTML"><context><option name="HTML" value="true"/><option name="Python" value="false"/></context></template>
  <template name="no_context" value="print(1)"/>
</templateSet>""",
                encoding="utf8",
            )
            (root / "templates" / "Other.xml").write_text(
                """<templateSet group="Other"><template name="other" value="print(1)"><context><option name="Python" value="true"/></context></template></templateSet>""",
                encoding="utf8",
            )
            (root / "source" / "wavelet.py").write_text(
                "class WaveletMatrix:\n    def kth_smallest(self): return 1\n",
                encoding="utf8",
            )
            cfg = {
                "snippet_dirs": [str(root / "source")],
                "extra_template_dirs": [str(root / "templates")],
                "source_urls": {
                    "wavelet": "https://github.com/example/repo/blob/hash/wavelet.py"
                },
                "provenance": {"wavelet": "ai"},
                "keywords": {"scc": ["strong components"]},
            }
            loaded, _ = p.load_entries(cfg)
            self.assertEqual({e.name for e in loaded}, {"scc", "macro", "wavelet"})
            self.assertEqual(p.match_entries(loaded, "強連結")[0].name, "scc")
            self.assertEqual(p.match_entries(loaded, "kth_smallest")[0].name, "wavelet")
            self.assertEqual(
                p.prepare_code(next(e for e in loaded if e.name == "scc"), "abbrev"),
                "scc",
            )
            self.assertEqual(
                p.prepare_code(next(e for e in loaded if e.name == "scc")),
                "class SCC:\n    def groups(self): return []\n",
            )
            with self.assertRaises(ValueError):
                p.prepare_code(next(e for e in loaded if e.name == "macro"))
            copied = p.prepare_code(next(e for e in loaded if e.name == "wavelet"))
            self.assertEqual(
                copied, "class WaveletMatrix:\n    def kth_smallest(self): return 1\n"
            )
            self.assertEqual(
                p.prepare_code(
                    p.Entry("ai", "File", "", "", "x = 1", "", provenance="ai")
                ),
                "x = 1",
            )
            self.assertTrue(
                any(
                    w["name"] == "WaveletMatrix" and w["detected"]
                    for w in p.wishlist_items(loaded)
                )
            )
            self.assertTrue(
                any(
                    w["name"] == "SCC" and w["detected"]
                    for w in p.wishlist_items(loaded)
                )
            )
            p.export_inventory(loaded, root / "inv.tsv")
            self.assertIn(
                "WaveletMatrix", (root / "inv.tsv").read_text(encoding="utf-8-sig")
            )

    def test_shipped_snippets(self):
        items, _ = p.load_entries(
            {
                "snippet_dirs": ["snippets"],
                "extra_template_dirs": [],
                "provenance": {},
                "source_urls": {},
                "keywords": {},
            }
        )
        self.assertGreaterEqual(sum(e.kind == "File" for e in items), 17)
        for e in items:
            self.assertEqual(e.provenance, "ai")
            compile(e.code, e.path, "exec")
        yes = {w["name"] for w in p.wishlist_items(items) if w["detected"]}
        for n in (
            "segtree",
            "lazy_segtree",
            "BIT",
            "Point",
            "Segment",
            "Polygon",
            "ClosestPair",
        ):
            self.assertIn(n, yes)
        compat = next(e for e in items if e.name == "SegTree_compat")
        namespace = {}
        exec(compile(compat.code, compat.path, "exec"), namespace)
        tree = namespace["SegTree"]([3, 1, 4], min, float("inf"))
        tree.update(1, 5)
        self.assertEqual(tree.query(0, 3), 3)

    def test_eol_dollar_expansion(self):
        e = p.Entry("x", "Live", "Py", "", "a = $$\n$END$", "x", "x")
        self.assertEqual(p.prepare_code(e), "a = $\n")

    def test_search_ranking_filters_and_typo(self):
        entries = [
            p.Entry(
                "segtree",
                "File",
                "structures",
                "セグメント木",
                "class SegTree: pass",
                "segtree.py",
                classes=("SegTree",),
            ),
            p.Entry(
                "SegTree_compat",
                "File",
                "structures",
                "旧API",
                "class SegTree: pass",
                "compat.py",
                classes=("SegTree",),
            ),
            p.Entry(
                "segtree",
                "Live",
                "user",
                "セグメント木",
                "class SegTree: pass",
                "user.xml",
                "segtree",
                classes=("SegTree",),
            ),
            p.Entry(
                "other",
                "File",
                "graphs",
                "heavy light",
                "# SegTree is mentioned here",
                "other.py",
            ),
        ]
        for query in ("ＳｅｇＴｒｅｅ", "seg_tree", "セグ木", "segtreee"):
            with self.subTest(query=query):
                self.assertIs(p.match_entries(entries, query)[0], entries[0])
        self.assertEqual(p.match_entries(entries, "@file セグ木 -compat"), [entries[0]])
        self.assertEqual(p.match_entries(entries, '"heavy light"'), [entries[3]])
        self.assertEqual(p.match_entries(entries, "segtree", kind="Live"), [entries[2]])
        self.assertEqual(p.match_entries(entries, "", group="graphs"), [entries[3]])
        self.assertEqual(
            p.match_entries(entries, "", favorites=[entries[3].key], scope="favorites"),
            [entries[3]],
        )
        self.assertIs(
            p.match_entries(entries, "segtree", favorites=[entries[3].key])[0],
            entries[0],
        )
        self.assertEqual(
            p.match_entries(
                entries,
                "",
                favorites=[entries[0].key],
                recent=[entries[3].key, entries[0].key],
                scope="recent",
            ),
            [entries[3], entries[0]],
        )

    def test_preferences_and_api_help(self):
        entry = p.Entry(
            "BIT",
            "File",
            "structures",
            "",
            "class A:\n    def __init__(self, n=0): pass\n    @property\n    def size(self): return 1\n",
            str(p.ROOT / "snippets/structures/BIT.py"),
        )
        self.assertEqual(entry.outline[0][1], "A(n=0)")
        self.assertEqual(entry.outline[1][1], "A.size")
        docs = dict(p.documentation(entry))
        self.assertIn("FenwickTree", docs["ACLの呼び出し方"])
        self.assertIn("practice2_b", docs["verify問題"])
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "state.json"
            prefs = p.Preferences(path)
            prefs.toggle(entry)
            prefs.record(entry)
            prefs.record(entry)
            loaded = p.Preferences(path)
            self.assertEqual(loaded.favorites, {entry.key})
            self.assertEqual(loaded.recent, [entry.key])
            path.write_text("{broken", encoding="utf8")
            recovered = p.Preferences(path)
            self.assertEqual(recovered.favorites, set())
            self.assertTrue(recovered.error)


if __name__ == "__main__":
    unittest.main()
