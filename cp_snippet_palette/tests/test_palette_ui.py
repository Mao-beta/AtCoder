"""画面を表示せず、アプリ自身の検索・選択・コピー経路を確認する。"""

from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import cp_palette as core
from palette_ui import PaletteApp
import tkinter as tk


class PaletteUITest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        try:
            self.root = tk.Tk()
        except tk.TclError as error:
            self.skipTest(str(error))
        self.root.withdraw()
        self.addCleanup(self.root.destroy)
        self.errors = []
        self.root.report_callback_exception = lambda *error: self.errors.append(error)
        self.file = core.Entry(
            "sum_tool",
            "File",
            "math",
            "区間の和",
            'def range_sum(a, l, r):\n    """半開区間の和。"""\n    return sum(a[l:r])\n',
            "sum_tool.py",
            methods=("range_sum",),
        )
        self.live = core.Entry(
            "macro",
            "Live",
            "user",
            "展開用",
            "print($VALUE$)\n$END$",
            "user.xml",
            "macro",
        )
        self.prefs = core.Preferences(Path(self.temp.name) / "state.json")
        self.app = PaletteApp(
            [self.file, self.live], root=self.root, preferences=self.prefs
        )
        self.root.update()

    def test_pending_search_copy_and_favorites(self):
        self.assertTrue(self.root.bind("<Return>"))
        with patch.object(self.app, "_clipboard") as copy:
            self.app.query_var.set("macro")  # 検索描画の65ms待ち中にEnter相当を実行。
            self.app.copy_selected(False)
            copy.assert_called_once_with("macro")
            self.assertEqual(self.prefs.recent, [self.live.key])
            self.assertEqual(self.root.winfo_exists(), 1)
            self.assertIn("コピーしました", self.app.status.cget("text"))
            self.app.search_for("range_sum")
            self.root.update()
            self.app.tree.focus_set()
            self.app.copy_selected(False)
            self.assertEqual(copy.call_args.args, (self.file.code,))
            self.app.toggle_favorite()
            self.assertIn(self.file.key, self.prefs.favorites)
            self.app.show_find()
            self.app.find_var.set("sum")
            self.assertEqual(len(self.app.find_matches), 2)
            self.app.query_var.set("no_such_snippet_zzzz")
            self.app.populate(preserve=False)
            self.assertIsNone(self.app.current)
            self.assertTrue(self.app.copy_button.instate(["disabled"]))
            self.assertEqual(self.app.preview.get("1.0", "end-1c"), "")
            self.assertEqual(self.app.find_matches, [])
            self.assertEqual(self.app.find_count.cget("text"), "0 / 0")
            self.app.copy_selected(False)
            self.assertEqual(copy.call_count, 2)
        self.assertFalse(self.errors)

    def test_preview_help_reload_and_copy_failure(self):
        self.app.search_for("range_sum")
        self.root.update()
        self.assertTrue(self.app.preview.tag_ranges("keyword"))
        self.assertIn("range_sum(a, l, r)", self.app.api.get("1.0", "end"))
        self.app.show_find()
        self.app.find_var.set("sum")
        self.assertEqual(len(self.app.find_matches), 2)
        self.app.find_next()
        self.app.hide_find()
        self.app.show_find()
        self.assertTrue(self.app.preview.tag_ranges("current_find"))
        self.app.hide_find()
        self.app.toggle_theme()
        self.app.resize_font(1)
        self.root.update()
        self.assertEqual(self.prefs.theme, "light")
        self.assertEqual(self.prefs.font_size, 12)
        with patch.object(
            self.app, "_clipboard", side_effect=tk.TclError("clipboard busy")
        ):
            self.app.copy_selected(False)
        self.assertEqual(self.prefs.recent, [])
        self.assertIn("コピーできません", self.app.status.cget("text"))
        with patch.object(core, "load_entries", side_effect=ValueError("bad json")):
            self.app.reload()
        self.assertEqual(self.app.entries, [self.file, self.live])
        changed = core.Entry(
            "sum_tool", "File", "math", "更新後", "print(2)\n", "sum_tool.py"
        )
        self.app.query_var.set("sum_tool")
        with patch.object(core, "load_entries", return_value=([changed], [])):
            self.app.reload()
        self.assertIs(self.app.current, changed)
        self.assertEqual(self.app.preview.get("1.0", "end-1c"), changed.code)
        self.root.update()
        self.assertFalse(self.errors)


if __name__ == "__main__":
    unittest.main()
