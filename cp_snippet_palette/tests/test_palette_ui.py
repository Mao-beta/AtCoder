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
import tkinter.font as tkfont


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
        self.assertEqual(self.app.tabs.select(), str(self.app.api_page))
        with patch.object(self.app, "_clipboard") as copy:
            self.app.query_var.set("macro")  # 検索描画の65ms待ち中にEnter相当を実行。
            self.app.copy_button.invoke()
            copy.assert_called_once_with("macro")
            self.assertEqual(self.prefs.recent, [self.live.key])
            self.assertEqual(self.root.winfo_exists(), 1)
            self.assertIn("コピーしました", self.app.status.cget("text"))
            self.assertIn("コピーしました", self.app.copy_feedback.cget("text"))
            self.assertIn("略語", self.app.kind_badge.cget("text") + self.app.copy_hint.cget("text"))
            self.app.search_for("range_sum")
            self.root.update()
            self.app.tree.focus_set()
            self.app.copy_selected()
            self.assertEqual(copy.call_args.args, (self.file.code,))
            self.assertIn("File", self.app.kind_badge.cget("text"))
            self.assertIn("main", self.app.copy_hint.cget("text"))
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
            self.app.copy_selected()
            self.assertEqual(copy.call_count, 2)
        self.assertFalse(self.errors)
        with patch.object(self.app, "_clipboard") as copy:
            event = tk.Event()
            event.widget = self.app.theme_button
            self.app._activate_or_copy(event)
            copy.assert_not_called()
            self.assertEqual(self.prefs.theme, "light")
            self.root.update()

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
        self.assertEqual(tkfont.Font(font=self.app.api.cget("font")).actual("size"), 12)
        self.assertGreater(
            tkfont.Font(font=self.app.api.tag_cget("heading", "font")).actual("size"), 12
        )
        with patch.object(
            self.app, "_clipboard", side_effect=tk.TclError("clipboard busy")
        ):
            self.app.copy_selected()
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

    def test_purpose_guide_links_and_heading(self):
        entry = core.Entry(
            "BIT",
            "File",
            "structures",
            "",
            "class fenwick_tree: pass\n",
            str(core.ROOT / "snippets/structures/BIT.py"),
        )
        self.app.entries.append(entry)
        self.app.open_link("snippets/structures/BIT.py")
        self.assertIs(self.app.current, entry)
        self.assertEqual(self.app.tabs.select(), str(self.app.api_page))
        self.assertIn("一点を加算して区間の合計", self.app.api.get("1.0", "end"))
        self.assertIn("アルゴリズムの解説", self.app.api.get("1.0", "end"))
        self.assertIn("i & -i", self.app.api.get("1.0", "end"))
        window = tk.Toplevel(self.root)
        window.withdraw()
        with patch("palette_ui.tk.Toplevel", return_value=window):
            _, text = self.app.text_window("guide")
        with patch.object(self.app, "text_window", return_value=(window, text)):
            with patch.object(text, "see", wraps=text.see) as scroll:
                self.app.open_link("LIBRARY_GUIDE.md#目的から探す逆引き")
                index = scroll.call_args.args[0]
                self.assertEqual(
                    text.get(index, index + " lineend"), "目的から探す逆引き"
                )
        self.assertIn("一点加算 区間和", text.get("1.0", "end"))
        self.assertNotIn("<!-- navigator:", text.get("1.0", "end"))
        self.assertIn("点代入して和を取る", text.get("1.0", "end"))
        self.assertTrue(text.search("選ぶ条件・使い分け：", "1.0", stopindex="end"))
        for tag in ("heading1", "heading", "table_title", "label", "inline", "link"):
            self.assertTrue(text.tag_ranges(tag), tag)
        before = text.get("1.0", "end")
        self.app.toggle_theme()
        self.app.resize_font(1)
        self.assertEqual(text.get("1.0", "end"), before)
        self.assertEqual(text.tag_cget("link", "foreground"), self.app.colors["accent"])
        self.assertEqual(tkfont.Font(font=text.cget("font")).actual("size"), 12)
        self.root.update()
        self.assertFalse(self.errors)

    def test_purpose_navigation_preview_copy_back_and_reload(self):
        path = core.ROOT / "snippets/structures/BIT.py"
        entry = core.Entry("BIT", "File", "structures", "", path.read_text(encoding="utf8"), str(path))
        self.app.entries.append(entry)
        window = tk.Toplevel(self.root)
        window.withdraw()
        with patch("purpose_browser.tk.Toplevel", return_value=window):
            self.app.show_navigator()
        nav = self.app.navigator
        self.root.update()
        self.assertEqual(len(nav.cards), 6)
        self.assertTrue(nav.copy_button.instate(["disabled"]))
        for title in ("配列・集合", "区間を集計する", "和・二乗和・積の和"):
            card = next(card for card in nav.cards if card.cget("text").startswith(title))
            card.invoke()
        card = next(card for card in nav.cards if card.cget("text").startswith("一点を加算"))
        with patch.object(self.app, "_clipboard") as copy:
            card.invoke()
            copy.assert_not_called()
            self.assertIs(nav.entry, entry)
            shown = nav.detail.get("1.0", "end")
            self.assertIn("fenwick_tree", shown)
            self.assertIn("O(log N)", shown)
            self.assertIn("# =>", shown)
            nav.copy_button.invoke()
            copy.assert_called_once_with(entry.code)
            self.assertEqual(self.prefs.recent, [entry.key])
            self.assertTrue(window.winfo_exists())
            self.assertTrue(self.root.winfo_exists())
        with patch.object(self.app, "_clipboard", side_effect=tk.TclError("busy")):
            nav.copy()
        self.assertIn("コピーできません", nav.status.cget("text"))
        before = nav.detail.get("1.0", "end")
        self.app.toggle_theme()
        self.app.resize_font(1)
        self.assertEqual(nav.detail.get("1.0", "end"), before)
        self.assertEqual(card.cget("highlightbackground"), self.app.colors["accent"])
        nav.open_button.invoke()
        self.assertIs(self.app.current, entry)
        self.assertEqual(self.app.tabs.select(), str(self.app.api_page))
        with patch.object(window, "deiconify"):
            self.app.show_navigator()
        self.assertIs(self.app.navigator, nav)
        changed = core.Entry("BIT", "File", "structures", "", entry.code + "\n# reloaded\n", entry.path)
        with patch.object(core, "load_entries", return_value=([changed], [])):
            self.app.reload()
        self.assertIs(nav.entry, changed)
        with patch.object(self.app, "_clipboard") as copy:
            nav.copy()
            copy.assert_called_once_with(changed.code)
        nav.query.set("no_such_purpose_zzzz")
        self.assertEqual(nav.visible, [])
        self.assertTrue(nav.copy_button.instate(["disabled"]))
        nav.back()
        self.assertEqual(nav.path[-1], "和・二乗和・積の和")
        nav.back()
        self.assertEqual(nav.path, ("配列・集合", "区間を集計する"))
        nav.show_all.set(True)
        nav.render()
        self.assertTrue(all(card.purpose is not None for card in nav.cards))
        nav.navigate(())
        nav.query.set("負コスト")
        nav.cards[0].invoke()
        self.assertIsNone(nav.entry)  # 未読込Fileへの誘導はできるがコピーは無効。
        self.assertIn("未読込", nav.detail.get("1.0", "end"))
        with patch.object(core, "load_entries", return_value=([], [])):
            self.app.reload()
        self.assertEqual(nav.query.get(), "負コスト")
        self.assertTrue(nav.copy_button.instate(["disabled"]))
        nav.close()
        self.assertIsNone(self.app.navigator)
        self.root.update()
        self.assertFalse(self.errors)

    def test_usage_and_constructor_docs_are_visible_without_execution(self):
        entry = core.Entry(
            "documented",
            "File",
            "basic",
            "使用例つき",
            '"""短い使い方。\n\n使用例:\n    Demo(3).value  # => 3\n"""\n'
            'raise RuntimeError("must not execute")\n'
            "class Demo:\n"
            "    def __init__(self, value):\n"
            '        """valueは初期値。"""\n'
            "        self.value = value\n"
            "class Child(Demo):\n"
            '    """親と同じ引数。"""\n',
            "documented.py",
        )
        self.app.render_api(entry)
        shown = self.app.api.get("1.0", "end")
        self.assertIn("Demo(3).value  # => 3", shown)
        self.assertIn("valueは初期値", shown)
        self.assertIn("Demo(value)", shown)
        self.assertIn("Child(value)", shown)
        self.assertTrue(self.app.api.tag_ranges("example"))
        self.assertFalse(self.errors)

        for relative, expected in [
            (
                "library/graphs/assignment.py",
                ("cost[i][j]", "N=len(cost)", "O(N²M)"),
            ),
            (
                "library/structures/wavelet_matrix.py",
                ("Xは整数列", "σ=len(set(X))", "O(T log(T+1))"),
            ),
            (
                "library/math/gf2_matrix.py",
                ("rowsは非負整数のlist", "columns", "内部ワード幅"),
            ),
        ]:
            path = core.ROOT / relative
            entry = core.Entry(
                path.stem,
                "File",
                path.parent.name,
                "",
                path.read_text(encoding="utf8"),
                str(path),
            )
            self.app.render_api(entry)
            shown = self.app.api.get("1.0", "end")
            for value in expected:
                self.assertIn(value, shown)
            for tag in (
                "heading", "signature", "label", "complexity", "example", "comment", "inline"
            ):
                self.assertTrue(self.app.api.tag_ranges(tag), (relative, tag))
        # 冪の**やコード内の記号はMarkdownの装飾として取り除かない。
        text = self.app.api
        text.configure(state="normal")
        text.delete("1.0", "end")
        self.app._document(
            text,
            "## 見出し\n**入力**: `values`は整数列。\n"
            "時間O(N log(N+1))。f**k mod x**deg。\n"
            "```python\nif True:\n    value = 2 ** 3  # 計算\n```\n",
        )
        shown = text.get("1.0", "end")
        self.assertIn("f**k mod x**deg", shown)
        self.assertIn("    value = 2 ** 3  # 計算", shown)
        self.assertNotIn("**入力**", shown)
        self.assertNotIn("```", shown)
        for tag in ("strong", "inline", "keyword", "number", "comment"):
            self.assertTrue(text.tag_ranges(tag), tag)
        first, last = text.tag_ranges("complexity")
        self.assertEqual(text.get(first, last), "O(N log(N+1))")
        self.assertFalse(self.errors)


if __name__ == "__main__":
    unittest.main()
