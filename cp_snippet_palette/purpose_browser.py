"""目的 → 対象・条件 → APIを選ぶ、ローカル文書に基づくナビゲーター。"""

from pathlib import Path
import re
import tkinter as tk
from tkinter import ttk

import cp_palette as core
from purpose_catalog import load_purposes


ROOT_ORDER = ("配列・集合", "グラフ・木", "文字列", "整数・数式", "グリッド・幾何", "DP・探索")
ROOT_HINTS = {
    "配列・集合": "区間の集計、順位、連続区間、キュー",
    "グラフ・木": "最短路、連結性、木の経路、フロー",
    "文字列": "一致、回文、部分列、編集距離",
    "整数・数式": "数論、組合せ、行列、多項式",
    "グリッド・幾何": "迷路、長方形、点群、交差判定",
    "DP・探索": "ナップサック、桁DP、最適化、探索",
}


class PurposeBrowser:
    def __init__(self, app):
        self.app = app
        self.path = ()
        self.purposes = []
        self.selected = None
        self.entry = None
        self.cards = []
        self.window = tk.Toplevel(app.root)
        self.window.title("目的から探す — Snippet Palette")
        self.window.geometry("1120x780")
        self.window.minsize(960, 620)
        self.window.protocol("WM_DELETE_WINDOW", self.close)
        self.query = tk.StringVar(self.window)
        self.show_all = tk.BooleanVar(self.window, False)
        self.window.columnconfigure(0, weight=1)
        self.window.rowconfigure(2, weight=1)

        header = ttk.Frame(self.window, padding=(24, 20, 24, 12))
        header.grid(row=0, column=0, sticky="ew")
        ttk.Label(header, text="目的から探す", font=("Yu Gothic UI", 21, "bold")).pack(side="left")
        self.summary = ttk.Label(header, style="Muted.TLabel")
        self.summary.pack(side="left", padx=16)
        ttk.Button(header, text="一覧ガイド", command=lambda: app.open_link(
            "LIBRARY_GUIDE.md#目的から探す逆引き")).pack(side="right")
        ttk.Button(header, text="配色", command=app.toggle_theme).pack(side="right", padx=8)

        nav = ttk.Frame(self.window, padding=(24, 0, 24, 12))
        nav.grid(row=1, column=0, sticky="ew")
        nav.columnconfigure(2, weight=1)
        self.back_button = ttk.Button(nav, text="← 戻る", command=self.back)
        self.back_button.grid(row=0, column=0, padx=(0, 8))
        ttk.Button(nav, text="最初から", command=lambda: self.navigate(())).grid(row=0, column=1)
        self.breadcrumb = ttk.Label(nav, style="Muted.TLabel", wraplength=700)
        self.breadcrumb.grid(row=0, column=2, sticky="w", padx=(16, 0))
        nav.bind("<Configure>", lambda e: self.breadcrumb.configure(wraplength=max(200, e.width - 240)))

        body = ttk.Panedwindow(self.window, orient="horizontal")
        body.grid(row=2, column=0, sticky="nsew", padx=24)
        left = ttk.Frame(body, width=440, padding=(0, 0, 16, 0))
        right = ttk.Frame(body, width=560)
        body.add(left, weight=4)
        body.add(right, weight=5)
        left.columnconfigure(0, weight=1)
        left.rowconfigure(4, weight=1)
        self.prompt = ttk.Label(left, font=("Yu Gothic UI", 13, "bold"))
        self.prompt.grid(row=0, column=0, sticky="w", pady=(0, 12))
        ttk.Label(left, text="この範囲から検索（目的・条件・API）", style="Muted.TLabel").grid(row=1, column=0, sticky="w")
        search = ttk.Frame(left)
        search.grid(row=2, column=0, sticky="ew", pady=(4, 8))
        search.columnconfigure(0, weight=1)
        self.search = ttk.Entry(search, textvariable=self.query)
        self.search.grid(row=0, column=0, sticky="ew")
        ttk.Button(search, text="クリア", command=lambda: self.query.set("")).grid(row=0, column=1, padx=(8, 0))
        self.all_button = ttk.Checkbutton(left, text="この範囲の候補をすべて表示", variable=self.show_all, command=self.render)
        self.all_button.grid(row=3, column=0, sticky="w", pady=(0, 12))

        choices = ttk.Frame(left)
        choices.grid(row=4, column=0, sticky="nsew")
        choices.rowconfigure(0, weight=1)
        choices.columnconfigure(0, weight=1)
        self.canvas = tk.Canvas(choices, highlightthickness=0, borderwidth=0)
        self.canvas.grid(row=0, column=0, sticky="nsew")
        scroll = ttk.Scrollbar(choices, command=self.canvas.yview)
        scroll.grid(row=0, column=1, sticky="ns", padx=(4, 0))
        self.canvas.configure(yscrollcommand=scroll.set)
        self.list_frame = tk.Frame(self.canvas)
        self.list_id = self.canvas.create_window(0, 0, window=self.list_frame, anchor="nw")
        self.canvas.bind("<Configure>", self._resize_cards)
        self.list_frame.bind("<Configure>", lambda _: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.canvas.bind("<MouseWheel>", self._wheel)

        right.columnconfigure(0, weight=1)
        right.rowconfigure(1, weight=1)
        ttk.Label(right, text="候補の使い方", font=("Yu Gothic UI", 13, "bold")).grid(row=0, column=0, sticky="w", pady=(0, 12))
        preview = ttk.Frame(right)
        preview.grid(row=1, column=0, sticky="nsew")
        preview.columnconfigure(0, weight=1)
        preview.rowconfigure(0, weight=1)
        self.detail = tk.Text(preview, wrap="word", padx=20, pady=12, borderwidth=0, width=40, height=10)
        self.detail.grid(row=0, column=0, sticky="nsew")
        scrollbar = ttk.Scrollbar(preview, command=self.detail.yview)
        scrollbar.grid(row=0, column=1, sticky="ns")
        self.detail.configure(yscrollcommand=scrollbar.set)
        app.document_views.append(self.detail)
        actions = ttk.Frame(right, padding=(0, 12, 0, 0))
        actions.grid(row=2, column=0, sticky="ew")
        self.copy_button = ttk.Button(actions, text="コードをコピー", style="Primary.TButton", command=self.copy)
        self.copy_button.pack(side="right")
        self.open_button = ttk.Button(actions, text="詳しい解説・API", command=self.open_entry)
        self.open_button.pack(side="right", padx=8)
        ttk.Button(actions, text="A−", width=3, command=lambda: app.resize_font(-1)).pack(side="left")
        ttk.Button(actions, text="A＋", width=3, command=lambda: app.resize_font(1)).pack(side="left", padx=4)

        footer = ttk.Frame(self.window, padding=(24, 12, 24, 16))
        footer.grid(row=3, column=0, sticky="ew")
        footer.columnconfigure(0, weight=1)
        self.status = ttk.Label(footer, style="Muted.TLabel", wraplength=760)
        self.status.grid(row=0, column=0, sticky="w")
        ttk.Button(footer, text="閉じる", command=self.close).grid(row=0, column=1, padx=(16, 0))

        self.window.bind("<Escape>", lambda _: self.close())
        self.window.bind("<Alt-Left>", lambda _: self.back())
        self.window.bind("<Control-l>", lambda _: self.focus_search())
        self.window.bind("<Control-Return>", lambda _: self.copy())
        self.window.bind("<F5>", lambda _: app.reload())
        # Enterはフォーカスしたボタンだけを操作。候補の選択ではコピーしない。
        self.window.bind("<Return>", self._activate)
        self.query.trace_add("write", lambda *_: self.render())
        self.apply_theme()
        self.reload()
        self.search.focus_set()

    def _activate(self, event):
        if isinstance(event.widget, (tk.Button, ttk.Button, ttk.Checkbutton)):
            event.widget.invoke()
        return "break"

    def focus_search(self):
        self.search.focus_set()
        self.search.selection_range(0, "end")
        return "break"

    def close(self):
        self.window.destroy()
        self.app.navigator = None
        return "break"

    def reload(self):
        try:
            self.purposes = load_purposes()
        except (OSError, ValueError, IndexError) as error:
            self.purposes = []
            self.render()
            self.status.configure(text=f"逆引きを読み込めません: {error}")
            return
        if not any(p.path[:len(self.path)] == self.path for p in self.purposes):
            self.path = ()
        selected = self.selected
        self.render()
        if selected:
            current = next((p for p in self.visible
                            if (p.target, p.api, p.goal) == (selected.target, selected.api, selected.goal)), None)
            if current:
                self.select(current)

    def navigate(self, path):
        self.path = tuple(path)
        self.show_all.set(False)
        self.query.set("")  # traceで描画する。
        self.canvas.yview_moveto(0)
        if self.cards:
            self.cards[0].focus_set()

    def back(self):
        if self.query.get() or self.show_all.get():
            self.navigate(self.path)
        elif self.path:
            self.navigate(self.path[:-1])
        return "break"

    def render(self):
        self.selected = self.entry = None
        for card in self.list_frame.winfo_children():
            card.destroy()
        self.cards = []
        scoped = [p for p in self.purposes if p.path[:len(self.path)] == self.path]
        self.visible = [p for p in scoped if p.matches(self.query.get())]
        self.summary.configure(text=f"{len({p.path[0] for p in self.purposes})}分類 · {len(self.purposes)}用途")
        self.breadcrumb.configure(text="すべて" + ("  /  " + "  /  ".join(self.path) if self.path else ""))
        filtered = bool(self.query.get().strip()) or self.show_all.get()
        self.back_button.configure(state="normal" if self.path or filtered else "disabled")
        children = list(dict.fromkeys(p.path[len(self.path)] for p in scoped if len(p.path) > len(self.path)))
        if not self.path:
            children.sort(key=lambda name: ROOT_ORDER.index(name) if name in ROOT_ORDER else len(ROOT_ORDER))
        if children and not filtered:
            self.prompt.configure(text="1  対象を選ぶ" if not self.path else f"{len(self.path) + 1}  目的を選ぶ")
            for name in children:
                path = (*self.path, name)
                members = [p for p in scoped if p.path[:len(path)] == path]
                hint = ROOT_HINTS.get(name) or " / ".join(dict.fromkeys(p.path[len(path)] for p in members if len(p.path) > len(path)))
                self._card(f"{name}   ›\n{hint + '  ·  ' if hint else ''}{len(members)}用途", lambda path=path: self.navigate(path))
            # 分類の深さが混在していても、この階層に属する用途を落とさない。
            results = [p for p in scoped if p.path == self.path]
        else:
            self.prompt.configure(text=f"条件に合う候補を選ぶ  ·  {len(self.visible)}用途")
            results = self.visible
        for purpose in results:
            self._card(f"{purpose.goal}\n{purpose.api}", lambda p=purpose: self.select(p), purpose)
        self.canvas.yview_moveto(0)
        self.status.configure(text="Tabで移動 / Enterで選択 / Alt+←で戻る / Ctrl+Enterでコピー")
        self.detail.configure(state="normal")
        self.detail.delete("1.0", "end")
        if not self.visible:
            self.detail.insert("end", "一致する候補がありません\n", "heading")
            self.detail.insert("end", "検索語を短くするか、クリア・戻るで範囲を広げてください。\n")
        else:
            self.detail.insert("end", "目的と条件から選ぶ\n", "heading")
            self.detail.insert("end", "左の項目を順に選ぶと、使える関数・クラスを絞り込めます。\n\n")
            self.detail.insert("end", "選び方\n", "subheading")
            self.detail.insert("end", "• 対象 → 目的 → 候補の順に選ぶ\n• 候補を押して、入力・計算量・使用例を確認\n• コードをコピーして解答へ貼り付ける\n\n")
            self.detail.insert("end", "条件が決まっていない場合\n", "subheading")
            self.detail.insert("end", "「この範囲の候補をすべて表示」で比較できます。検索は現在の分類内が対象です。\n")
        self.detail.configure(state="disabled")
        self._actions()

    def _card(self, text, command, purpose=None):
        card = tk.Button(self.list_frame, text=text, command=command, anchor="w", justify="left",
                         padx=16, pady=12, relief="flat", borderwidth=0,
                         highlightthickness=2, takefocus=True, cursor="hand2")
        card.purpose = purpose
        card.pack(fill="x", pady=(0, 8), padx=2)
        self.cards.append(card)
        self._style_card(card)
        card.configure(wraplength=max(180, self.canvas.winfo_width() - 48))
        card.bind("<Enter>", lambda _: card.configure(background=self.app.colors["selected"]))
        card.bind("<Leave>", lambda _: self._style_card(card))
        card.bind("<FocusIn>", lambda _: self._see_card(card))
        card.bind("<MouseWheel>", self._wheel)

    def _see_card(self, card):
        self.canvas.update_idletasks()
        height = max(1, self.list_frame.winfo_height())
        top, bottom = self.canvas.yview()
        y, end = card.winfo_y(), card.winfo_y() + card.winfo_height()
        if y < top * height:
            self.canvas.yview_moveto(y / height)
        elif end > bottom * height:
            self.canvas.yview_moveto((end - self.canvas.winfo_height()) / height)

    def _wheel(self, event):
        self.canvas.yview_scroll(-int(event.delta / 120) * 3, "units")
        return "break"

    def _resize_cards(self, event):
        self.canvas.itemconfigure(self.list_id, width=event.width)
        for card in self.cards:
            card.configure(wraplength=max(180, event.width - 48))

    def _style_card(self, card):
        c = self.app.colors
        selected = card.purpose is not None and card.purpose == self.selected
        card.configure(background=c["selected"] if selected else c["panel"], foreground=c["text"],
                       activebackground=c["selected"], activeforeground=c["text"],
                       highlightbackground=c["accent"] if selected else c["border"],
                       highlightcolor=c["accent"], font=("Yu Gothic UI", self.app.preferences.font_size))

    def apply_theme(self):
        self.window.configure(bg=self.app.colors["bg"])
        self.canvas.configure(bg=self.app.colors["bg"])
        self.list_frame.configure(bg=self.app.colors["bg"])
        self.app._style_document(self.detail)
        for card in self.cards:
            self._style_card(card)

    def select(self, purpose):
        self.selected = purpose
        target = (core.ROOT / purpose.target).resolve()
        self.entry = next((e for e in self.app.entries if e.kind == "File" and Path(e.path).resolve() == target), None)
        for card in self.cards:
            self._style_card(card)
        self.detail.configure(state="normal")
        self.detail.delete("1.0", "end")
        self.detail.insert("end", purpose.goal + "\n", "heading")
        self.detail.insert("end", purpose.api + "\n", "signature")
        self.detail.insert("end", "選ぶ条件・使い分け\n", "subheading")
        self.app._document(self.detail, purpose.condition)
        self.detail.insert("end", "\n" + purpose.target + "\n", "muted")
        if self.entry:
            names = set(re.findall(r"[A-Za-z_]\w*", purpose.api))
            for name, signature, _, doc in self.entry.outline:
                if name in names or name.split(".")[-1] in names:
                    self.detail.insert("end", signature + "\n", "signature")
                    if doc:
                        self.app._document(self.detail, doc, docstring=True)
            if self.entry.module_doc:
                self.detail.insert("end", "ファイルの使い方・実行例\n", "heading")
                self.app._document(self.detail, self.entry.module_doc, docstring=True)
            self.status.configure(text=f"コピー対象: {Path(purpose.target).name} 全体（補助定義を含む）")
        else:
            self.detail.insert("end", "\nこのFileは未読込です。設定のsnippet_dirsを確認してF5で再読み込みしてください。\n", "muted")
            self.status.configure(text="対象Fileが未読込のため、コピーできません。")
        self.detail.configure(state="disabled")
        self.detail.yview_moveto(0)
        self._actions()

    def _actions(self):
        state = "normal" if self.entry else "disabled"
        self.copy_button.configure(state=state)
        self.open_button.configure(state=state)

    def copy(self):
        if self.entry:
            self.app.copy_entry(self.entry)
            self.status.configure(text=self.app.status.cget("text"))
        return "break"

    def open_entry(self):
        if self.entry:
            self.app.open_link(self.selected.target)
        return "break"
