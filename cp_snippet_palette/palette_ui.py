"""Snippet Paletteの画面。tkinterのみ。読み込み・検索はcp_paletteに集約。"""

from __future__ import annotations

import io
import keyword
from pathlib import Path
import re
import subprocess
import sys
import tokenize
import tkinter as tk
from tkinter import ttk
import webbrowser

import cp_palette as core


THEMES = {
    "dark": dict(
        bg="#111820",
        panel="#19232e",
        input="#222f3d",
        text="#e7edf4",
        muted="#a2b3c5",
        accent="#6ce0bd",
        selected="#264e51",
        code="#101923",
        border="#344558",
        hit="#60502b",
        keyword="#b3a5ff",
        string="#9cdbab",
        comment="#849aae",
        number="#efc684",
        error="#ffb1aa",
    ),
    "light": dict(
        bg="#f2f5f8",
        panel="#ffffff",
        input="#ffffff",
        text="#172b3c",
        muted="#536b7d",
        accent="#087d69",
        selected="#d1eee6",
        code="#fbfcfe",
        border="#c6d2dc",
        hit="#ffecad",
        keyword="#6c3b9e",
        string="#267348",
        comment="#667d8d",
        number="#945714",
        error="#b52c27",
    ),
}
SCOPES = {"すべて": "all", "★ お気に入り": "favorites", "最近コピー": "recent"}


class PaletteApp:
    def __init__(
        self,
        entries,
        search_dirs=(),
        initial="",
        *,
        root=None,
        preferences=None,
        warnings=None,
    ):
        self.root = root if root is not None else tk.Tk()
        self.preferences = (
            preferences if preferences is not None else core.Preferences()
        )
        self.entries = entries
        self.search_dirs = search_dirs
        self.warnings = list(warnings or [])
        self.pending = None
        self.hits = []
        self.current = None
        self.rendered_key = None
        self.syntax_cache = {}
        self.docs_cache = {}
        self.find_matches = []
        self.find_index = -1
        self.link_number = 0
        self.query_var = tk.StringVar(value=initial)
        self.kind_var = tk.StringVar(value="")
        self.group_var = tk.StringVar(value="すべての分野")
        self.scope_var = tk.StringVar(value="すべて")
        self.find_var = tk.StringVar()
        self.root.title("CP Snippet Palette")
        self.root.geometry(self.preferences.geometry)
        self.root.minsize(960, 620)
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        self.style = ttk.Style(self.root)
        self.style.theme_use("clam")
        self.root.option_add("*Font", ("Yu Gothic UI", 10))
        self._build()
        self.apply_theme()
        self._bindings()
        self._update_groups()
        self.populate()
        self.query.focus_set()
        self.query.selection_range(0, "end")
        if self.preferences.error:
            self.status.configure(text=self.preferences.error)

    def _build(self):
        root = self.root
        root.columnconfigure(0, weight=1)
        root.rowconfigure(2, weight=1)
        header = ttk.Frame(root, padding=(20, 15, 20, 7))
        header.grid(row=0, column=0, sticky="ew")
        ttk.Label(
            header, text="CP", style="Accent.TLabel", font=("Segoe UI", 20, "bold")
        ).pack(side="left", padx=(0, 12))
        ttk.Label(header, text="Snippet Palette", font=("Segoe UI", 18, "bold")).pack(
            side="left"
        )
        ttk.Label(header, text="探す → 確認 → コピー", style="Muted.TLabel").pack(
            side="left", padx=18
        )
        ttk.Button(header, text="ヘルプ  F1", command=self.show_help).pack(side="right")
        self.theme_button = ttk.Button(header, command=self.toggle_theme, width=9)
        self.theme_button.pack(side="right", padx=8)

        search = ttk.Frame(root, padding=(20, 0, 20, 8))
        search.grid(row=1, column=0, sticky="ew")
        search.columnconfigure(0, weight=1)
        self.query = ttk.Entry(
            search, textvariable=self.query_var, font=("Yu Gothic UI", 14)
        )
        self.query.grid(row=0, column=0, sticky="ew", ipady=7)
        ttk.Button(search, text="クリア", command=lambda: self.query_var.set("")).grid(
            row=0, column=1, padx=(8, 0)
        )
        hint = ttk.Frame(search)
        hint.grid(row=1, column=0, columnspan=2, sticky="ew", pady=(5, 7))
        ttk.Label(hint, text="名前・日本語・API名   例：", style="Muted.TLabel").pack(
            side="left"
        )
        for example in ("セグ木", "最短路", "二項係数", "fps_inverse"):
            ttk.Button(
                hint,
                text=example,
                style="Small.TButton",
                command=lambda q=example: self.search_for(q),
            ).pack(side="left", padx=(0, 5))
        filters = ttk.Frame(search)
        filters.grid(row=2, column=0, columnspan=2, sticky="ew")
        for label, value in [
            ("すべて", ""),
            ("コード / File", "File"),
            ("PyCharm / Live", "Live"),
        ]:
            ttk.Radiobutton(
                filters,
                text=label,
                variable=self.kind_var,
                value=value,
                command=self.filter_changed,
                style="Filter.TRadiobutton",
            ).pack(side="left", padx=(0, 4))
        self.group = ttk.Combobox(
            filters, textvariable=self.group_var, state="readonly", width=17
        )
        self.group.pack(side="left", padx=(12, 5))
        self.scope = ttk.Combobox(
            filters,
            textvariable=self.scope_var,
            values=list(SCOPES),
            state="readonly",
            width=13,
        )
        self.scope.pack(side="left")
        self.count = ttk.Label(filters, style="Muted.TLabel")
        self.count.pack(side="right")

        splitter = ttk.Panedwindow(root, orient="horizontal")
        splitter.grid(row=2, column=0, sticky="nsew", padx=20, pady=(0, 8))
        left = ttk.Frame(splitter, width=420)
        right = ttk.Frame(splitter, width=650)
        splitter.add(left, weight=2)
        splitter.add(right, weight=3)
        left.rowconfigure(0, weight=1)
        left.columnconfigure(0, weight=1)
        self.tree = ttk.Treeview(
            left, columns=("kind",), show="tree headings", selectmode="browse"
        )
        self.tree.heading("#0", text="スニペット / 用途")
        self.tree.heading("kind", text="種類")
        self.tree.column("#0", width=345, minwidth=210)
        self.tree.column("kind", width=62, stretch=False)
        self.tree.grid(row=0, column=0, sticky="nsew")
        scroll = ttk.Scrollbar(left, command=self.tree.yview)
        scroll.grid(row=0, column=1, sticky="ns")
        self.tree.configure(yscrollcommand=scroll.set)
        self.empty = ttk.Frame(left, padding=14)
        ttk.Label(
            self.empty,
            text="該当する候補がありません",
            font=("Yu Gothic UI", 12, "bold"),
        ).pack(pady=(0, 8))
        self.empty_text = ttk.Label(self.empty, wraplength=300, justify="left")
        self.empty_text.pack()
        ttk.Button(
            self.empty, text="検索・絞り込みをリセット", command=self.reset
        ).pack(pady=12)

        right.columnconfigure(0, weight=1)
        right.rowconfigure(2, weight=1)
        titlebar = ttk.Frame(right, padding=(12, 3, 0, 4))
        titlebar.grid(row=0, column=0, sticky="ew")
        titlebar.columnconfigure(0, weight=1)
        self.title = ttk.Label(
            titlebar, text="候補を選択", font=("Segoe UI", 16, "bold")
        )
        self.title.grid(row=0, column=0, sticky="w")
        self.favorite = ttk.Button(
            titlebar, text="☆ お気に入り", command=self.toggle_favorite
        )
        self.favorite.grid(row=0, column=1, padx=(8, 0))
        self.detail = ttk.Label(
            right, style="Muted.TLabel", padding=(12, 0, 0, 8), wraplength=600
        )
        self.detail.grid(row=1, column=0, sticky="ew")
        right.bind(
            "<Configure>",
            lambda event: self.detail.configure(wraplength=max(240, event.width - 18)),
        )
        self.tabs = ttk.Notebook(right)
        self.tabs.grid(row=2, column=0, sticky="nsew", padx=(12, 0))
        self.code_page = ttk.Frame(self.tabs)
        self.api_page = ttk.Frame(self.tabs)
        self.tabs.add(self.code_page, text="  コード  ")
        self.tabs.add(self.api_page, text="  API・verify  F2  ")
        self.code_page.columnconfigure(0, weight=1)
        self.code_page.rowconfigure(2, weight=1)
        toolbar = ttk.Frame(self.code_page, padding=(7, 6))
        toolbar.grid(row=0, column=0, sticky="ew")
        toolbar.columnconfigure(1, weight=1)
        ttk.Label(toolbar, text="定義へ").grid(row=0, column=0, padx=(0, 7))
        self.symbol = ttk.Combobox(toolbar, state="readonly")
        self.symbol.grid(row=0, column=1, sticky="ew")
        ttk.Button(toolbar, text="検索 Ctrl+F", command=self.show_find).grid(
            row=0, column=2, padx=(8, 0)
        )
        ttk.Button(
            toolbar, text="−", width=3, command=lambda: self.resize_font(-1)
        ).grid(row=0, column=3, padx=(8, 2))
        ttk.Button(
            toolbar, text="＋", width=3, command=lambda: self.resize_font(1)
        ).grid(row=0, column=4)
        self.find_bar = ttk.Frame(self.code_page, padding=(7, 0, 7, 5))
        self.find_bar.columnconfigure(0, weight=1)
        self.find_entry = ttk.Entry(self.find_bar, textvariable=self.find_var)
        self.find_entry.grid(row=0, column=0, sticky="ew")
        self.find_count = ttk.Label(self.find_bar, width=10, anchor="center")
        self.find_count.grid(row=0, column=1)
        ttk.Button(
            self.find_bar, text="↑", width=3, command=lambda: self.find_next(-1)
        ).grid(row=0, column=2)
        ttk.Button(self.find_bar, text="↓", width=3, command=self.find_next).grid(
            row=0, column=3
        )
        ttk.Button(self.find_bar, text="×", width=3, command=self.hide_find).grid(
            row=0, column=4
        )

        code_frame = ttk.Frame(self.code_page)
        code_frame.grid(row=2, column=0, sticky="nsew")
        code_frame.rowconfigure(0, weight=1)
        code_frame.columnconfigure(1, weight=1)
        self.gutter = tk.Text(
            code_frame,
            width=5,
            wrap="none",
            borderwidth=0,
            padx=7,
            pady=9,
            takefocus=False,
            state="disabled",
            cursor="arrow",
            exportselection=False,
        )
        self.gutter.grid(row=0, column=0, sticky="ns")
        self.preview = tk.Text(
            code_frame,
            wrap="none",
            borderwidth=0,
            padx=10,
            pady=9,
            state="disabled",
            undo=False,
            exportselection=False,
        )
        self.preview.grid(row=0, column=1, sticky="nsew")
        sy = ttk.Scrollbar(code_frame, command=self.preview.yview)
        sy.grid(row=0, column=2, sticky="ns")
        sx = ttk.Scrollbar(code_frame, orient="horizontal", command=self.preview.xview)
        sx.grid(row=1, column=1, sticky="ew")
        self.preview.configure(
            xscrollcommand=sx.set,
            yscrollcommand=lambda first, last: (
                sy.set(first, last),
                self.gutter.yview_moveto(first),
            ),
        )
        self.api_page.columnconfigure(0, weight=1)
        self.api_page.rowconfigure(0, weight=1)
        self.api = tk.Text(
            self.api_page,
            wrap="word",
            padx=14,
            pady=12,
            borderwidth=0,
            state="disabled",
            undo=False,
            exportselection=False,
        )
        self.api.grid(row=0, column=0, sticky="nsew")
        api_scroll = ttk.Scrollbar(self.api_page, command=self.api.yview)
        api_scroll.grid(row=0, column=1, sticky="ns")
        self.api.configure(yscrollcommand=api_scroll.set)

        actions = ttk.Frame(root, padding=(20, 3, 20, 5))
        actions.grid(row=3, column=0, sticky="ew")
        self.copy_button = ttk.Button(
            actions,
            text="コピーして閉じる  Enter",
            style="Primary.TButton",
            command=self.copy_selected,
        )
        self.copy_button.pack(side="left", padx=(0, 8))
        self.keep_button = ttk.Button(
            actions,
            text="コピーして続ける  Ctrl+Enter",
            command=lambda: self.copy_selected(False),
        )
        self.keep_button.pack(side="left")
        ttk.Button(actions, text="再読込  F5", command=self.reload).pack(side="right")
        self.source_button = ttk.Button(
            actions, text="保存場所  F4", command=self.reveal_source
        )
        self.source_button.pack(side="right", padx=8)
        bottom = ttk.Frame(root, padding=(20, 0, 20, 10))
        bottom.grid(row=4, column=0, sticky="ew")
        self.status = ttk.Label(bottom, style="Muted.TLabel")
        self.status.pack(side="left")
        ttk.Label(
            bottom,
            text="↑↓ 選択    Ctrl+L 検索    Ctrl+D ★    Esc 終了",
            style="Muted.TLabel",
        ).pack(side="right")

    def _bindings(self):
        self.query_var.trace_add("write", lambda *_: self.schedule_search())
        self.find_var.trace_add("write", lambda *_: self.find_in_preview())
        self.group.bind("<<ComboboxSelected>>", lambda _: self.populate())
        self.scope.bind("<<ComboboxSelected>>", lambda _: self.populate())
        self.symbol.bind("<<ComboboxSelected>>", self.jump_to_symbol)
        self.tree.bind("<<TreeviewSelect>>", self.select)
        self.tree.bind("<Double-1>", self.double_click)
        self.root.bind("<Return>", lambda _: self.copy_selected())
        self.root.bind("<Control-Return>", lambda _: self.copy_selected(False))
        self.root.bind("<Control-l>", self.focus_search)
        self.root.bind("<Control-f>", lambda _: self.show_find())
        self.root.bind("<Control-d>", lambda _: self.toggle_favorite())
        self.root.bind("<Escape>", lambda _: self.close())
        self.root.bind("<F1>", lambda _: self.show_help())
        self.root.bind("<F2>", lambda _: self.toggle_tab())
        self.root.bind("<F3>", lambda _: self.find_next())
        self.root.bind("<Shift-F3>", lambda _: self.find_next(-1))
        self.root.bind("<F4>", lambda _: self.reveal_source())
        self.root.bind("<F5>", lambda _: self.reload())
        for key, kind in [("1", ""), ("2", "File"), ("3", "Live")]:
            self.root.bind(f"<Alt-Key-{key}>", lambda _, k=kind: self.set_kind(k))
        for widget in (self.query, self.tree):
            for key, delta in [("Down", 1), ("Up", -1), ("Next", 8), ("Prior", -8)]:
                widget.bind(f"<{key}>", lambda _, d=delta: self.move(d))
        self.find_entry.bind("<Return>", lambda _: self.find_next())
        self.find_entry.bind("<Shift-Return>", lambda _: self.find_next(-1))
        self.find_entry.bind("<Escape>", lambda _: self.hide_find())
        self.preview.bind(
            "<Control-MouseWheel>", lambda e: self.resize_font(1 if e.delta > 0 else -1)
        )
        self.gutter.bind(
            "<MouseWheel>",
            lambda e: (
                self.preview.yview_scroll(-int(e.delta / 120) * 3, "units"),
                "break",
            )[1],
        )

    def apply_theme(self):
        c = self.colors = THEMES[self.preferences.theme]
        self.root.configure(bg=c["bg"])
        self.style.configure(
            ".",
            background=c["bg"],
            foreground=c["text"],
            font=("Yu Gothic UI", 10),
            bordercolor=c["border"],
        )
        self.style.configure("TFrame", background=c["bg"])
        self.style.configure("TLabel", background=c["bg"], foreground=c["text"])
        self.style.configure("Muted.TLabel", foreground=c["muted"])
        self.style.configure("Accent.TLabel", foreground=c["accent"])
        self.style.configure(
            "TButton", background=c["panel"], padding=(10, 7), borderwidth=1
        )
        self.style.map(
            "TButton",
            background=[("active", c["selected"])],
            foreground=[("disabled", c["muted"])],
        )
        self.style.configure("Small.TButton", padding=(7, 2), font=("Yu Gothic UI", 9))
        self.style.configure(
            "Primary.TButton",
            background=c["accent"],
            foreground="#102b26",
            font=("Yu Gothic UI", 10, "bold"),
        )
        self.style.map(
            "Primary.TButton",
            background=[("active", c["selected"]), ("disabled", c["panel"])],
            foreground=[("active", c["text"]), ("disabled", c["muted"])],
        )
        if self.preferences.theme == "light":
            self.style.configure("Primary.TButton", foreground="#ffffff")
        self.style.configure(
            "TEntry",
            fieldbackground=c["input"],
            foreground=c["text"],
            insertcolor=c["accent"],
            padding=5,
        )
        self.style.configure(
            "TCombobox",
            fieldbackground=c["input"],
            background=c["panel"],
            foreground=c["text"],
            arrowcolor=c["muted"],
            padding=5,
        )
        self.style.map(
            "TCombobox",
            fieldbackground=[("readonly", c["input"])],
            foreground=[("readonly", c["text"])],
            selectbackground=[("readonly", c["input"])],
            selectforeground=[("readonly", c["text"])],
        )
        self.root.option_add("*TCombobox*Listbox.background", c["panel"])
        self.root.option_add("*TCombobox*Listbox.foreground", c["text"])
        self.root.option_add("*TCombobox*Listbox.selectBackground", c["selected"])
        self.style.configure(
            "Filter.TRadiobutton", background=c["panel"], padding=(9, 6)
        )
        self.style.map(
            "Filter.TRadiobutton",
            background=[("selected", c["selected"]), ("active", c["input"])],
        )
        self.style.configure(
            "Treeview",
            background=c["panel"],
            fieldbackground=c["panel"],
            foreground=c["text"],
            rowheight=53,
            borderwidth=0,
        )
        self.style.map(
            "Treeview",
            background=[("selected", c["selected"])],
            foreground=[("selected", c["text"])],
        )
        self.style.configure(
            "Treeview.Heading",
            background=c["input"],
            foreground=c["muted"],
            padding=(8, 7),
            relief="flat",
        )
        self.style.configure("TNotebook", background=c["bg"], borderwidth=0)
        self.style.configure(
            "TNotebook.Tab",
            background=c["panel"],
            foreground=c["muted"],
            padding=(9, 7),
        )
        self.style.map(
            "TNotebook.Tab",
            background=[("selected", c["code"])],
            foreground=[("selected", c["accent"])],
        )
        self.style.configure(
            "TScrollbar",
            background=c["border"],
            troughcolor=c["bg"],
            arrowcolor=c["muted"],
            borderwidth=0,
        )
        for widget in (self.preview, self.gutter, self.api):
            widget.configure(
                background=c["code"],
                foreground=c["text"],
                insertbackground=c["accent"],
                selectbackground=c["selected"],
                selectforeground=c["text"],
            )
        self.gutter.configure(foreground=c["muted"])
        self.preview.configure(font=("Consolas", self.preferences.font_size))
        self.gutter.configure(font=("Consolas", self.preferences.font_size))
        self.api.configure(font=("Yu Gothic UI", 10))
        for tag in ("keyword", "string", "comment", "number"):
            self.preview.tag_configure(tag, foreground=c[tag])
        self.preview.tag_configure("hit", background=c["hit"])
        self.preview.tag_configure("find", background=c["hit"])
        self.preview.tag_configure(
            "current_find", background=c["accent"], foreground="#102b26"
        )
        self.preview.tag_configure("jump", background=c["selected"])
        self.api.tag_configure(
            "heading",
            foreground=c["accent"],
            font=("Yu Gothic UI", 11, "bold"),
            spacing1=12,
            spacing3=5,
        )
        self.api.tag_configure(
            "signature", foreground=c["accent"], font=("Consolas", 11), spacing1=7
        )
        self.api.tag_configure("muted", foreground=c["muted"])
        self.theme_button.configure(
            text="ライト" if self.preferences.theme == "dark" else "ダーク"
        )
        if self.current:
            self.render_api(self.current)

    def _update_groups(self):
        values = sorted(
            {
                e.group
                for e in self.entries
                if not self.kind_var.get() or e.kind == self.kind_var.get()
            }
        )
        self.group_map = {core.CATEGORIES.get(g, g): g for g in values}
        self.group.configure(values=["すべての分野", *self.group_map])
        if self.group_var.get() not in self.group_map:
            self.group_var.set("すべての分野")

    def filter_changed(self):
        self._update_groups()
        self.populate()

    def set_kind(self, kind):
        self.kind_var.set(kind)
        self.filter_changed()
        return "break"

    def schedule_search(self):
        if self.pending is not None:
            self.root.after_cancel(self.pending)
        self.pending = self.root.after(65, lambda: self.populate(preserve=False))

    def populate(self, preserve=True):
        if self.pending is not None:
            self.root.after_cancel(self.pending)
            self.pending = None
        old = self.current.key if preserve and self.current else None
        self.hits = core.search_entries(
            self.entries,
            self.query_var.get(),
            kind=self.kind_var.get(),
            group=self.group_map.get(self.group_var.get(), ""),
            scope=SCOPES[self.scope_var.get()],
            favorites=self.preferences.favorites,
            recent=self.preferences.recent,
        )
        self.tree.delete(*self.tree.get_children())
        chosen = "0"
        for i, hit in enumerate(self.hits):
            e = hit.entry
            favorite = "★ " if e.key in self.preferences.favorites else ""
            summary = (
                ("旧API · " if e.legacy else "") + e.description.splitlines()[0]
                if e.description
                else e.category
            )
            if len(summary) > 42:
                summary = summary[:41] + "…"
            self.tree.insert(
                "",
                "end",
                iid=str(i),
                text=f"{favorite}{e.name}\n{summary}",
                values=(e.kind,),
            )
            if e.key == old:
                chosen = str(i)
        self.count.configure(text=f"{len(self.hits)} / {len(self.entries)} 件")
        if self.hits:
            self.empty.place_forget()
            self.tree.selection_set(chosen)
            self.tree.focus(chosen)
            self.tree.see(chosen)
            self.select()
        else:
            self.current = None
            self.rendered_key = None
            self.title.configure(text="候補なし")
            self.detail.configure(text="検索語や絞り込みを変更してください")
            for widget in (self.preview, self.gutter, self.api):
                self._text(widget, "")
            self.find_in_preview()
            self.symbol.configure(values=[])
            self.symbol.set("")
            message = (
                "お気に入りは、候補を選んでCtrl+Dで登録できます。"
                if self.scope_var.get() == "★ お気に入り"
                else "検索語を短くするか、分野・File/Liveの絞り込みを解除してください。"
            )
            if self.scope_var.get() == "最近コピー":
                message = "コピーすると、ここに直近20件が表示されます。"
            self.empty_text.configure(text=message)
            self.empty.place(relx=0.5, rely=0.45, anchor="center")
            self.update_actions()
        self.default_status()

    def default_status(self):
        live = sum(e.kind == "Live" for e in self.entries)
        message = f"File {len(self.entries) - live}   Live {live}"
        if self.warnings:
            message += f"   読込警告 {len(self.warnings)}件（F1で確認）"
        self.status.configure(text=message)

    def select(self, _event=None):
        selected = self.tree.selection()
        if not selected or int(selected[0]) >= len(self.hits):
            return
        hit = self.hits[int(selected[0])]
        e = self.current = hit.entry
        self.title.configure(text=e.name)
        action = (
            f"略語「{e.abbreviation}」をコピー → PyCharmでTab"
            if e.kind == "Live"
            else "ファイル全体をコピー → mainより上に貼り付け"
        )
        lines = len(e.code.splitlines())
        self.detail.configure(
            text=f"{e.kind} · {e.category} · {lines:,}行 · {hit.reason or '登録済み'}\n{action}"
        )
        render_key = (e.key, self.query_var.get())
        if self.rendered_key != render_key:
            self._text(self.preview, e.code)
            self._text(self.gutter, "\n".join(map(str, range(1, lines + 1))))
            self.preview.xview_moveto(0)
            self.preview.yview_moveto(0)
            self.symbol.configure(values=[s[0] for s in e.outline])
            self.symbol.set("定義を選択" if e.outline else "")
            self._highlight(e)
            self.render_api(e)
            self.rendered_key = render_key
            if self.find_bar.winfo_manager():
                self.find_in_preview()
        self.update_actions()

    @staticmethod
    def _text(widget, value):
        widget.configure(state="normal")
        widget.delete("1.0", "end")
        widget.insert("1.0", value)
        widget.configure(state="disabled")

    def _highlight(self, entry):
        spans = self.syntax_cache.get(entry.key)
        if spans is None:
            spans = []
            try:
                for token in tokenize.generate_tokens(io.StringIO(entry.code).readline):
                    tag = {
                        tokenize.STRING: "string",
                        tokenize.COMMENT: "comment",
                        tokenize.NUMBER: "number",
                    }.get(token.type)
                    if token.type == tokenize.NAME and keyword.iskeyword(token.string):
                        tag = "keyword"
                    if tag:
                        spans.append((tag, "%d.%d" % token.start, "%d.%d" % token.end))
            except (tokenize.TokenError, IndentationError, SyntaxError):
                pass
            self.syntax_cache[entry.key] = spans
        for tag, start, end in spans:
            self.preview.tag_add(tag, start, end)
        terms, _, _ = core.query_terms(self.query_var.get())
        first = None
        for term in terms:
            index = "1.0"
            for _ in range(500):
                found = self.preview.search(term, index, stopindex="end", nocase=True)
                if not found:
                    break
                end = f"{found}+{len(term)}c"
                self.preview.tag_add("hit", found, end)
                if first is None:
                    first = found
                index = end
        matching = [
            item
            for item in entry.outline
            if any(
                core.compact(t) == core.compact(item[0].split(".")[-1]) for t in terms
            )
        ]
        if matching:
            first = f"{matching[0][2]}.0"
            self.symbol.set(matching[0][0])
        if first:
            self.preview.see(first)

    def _markdown(self, widget, text):
        pattern = re.compile(r"\[([^\]]+)\]\(([^)]+)\)|`([^`]+)`")
        start = 0
        for match in pattern.finditer(text):
            widget.insert("end", text[start : match.start()])
            label, target, code = match.groups()
            if target:
                self.link_number += 1
                tag = f"link_{self.link_number}"
                widget.insert("end", label, tag)
                widget.tag_configure(
                    tag, foreground=self.colors["accent"], underline=True
                )
                widget.tag_bind(
                    tag, "<Button-1>", lambda _, t=target: self.open_link(t)
                )
                widget.tag_bind(
                    tag, "<Enter>", lambda _, w=widget: w.configure(cursor="hand2")
                )
                widget.tag_bind(
                    tag, "<Leave>", lambda _, w=widget: w.configure(cursor="xterm")
                )
            else:
                widget.insert("end", code)
            start = match.end()
        widget.insert("end", text[start:])

    def render_api(self, entry):
        self.api.configure(state="normal")
        self.api.delete("1.0", "end")
        for tag in self.api.tag_names():
            if tag.startswith(("link_", "definition_")):
                self.api.tag_delete(tag)
        self.api.insert("end", entry.description + "\n")
        if entry.kind == "Live":
            self.api.insert(
                "end",
                "userグループ / Python用のLive Template。Enterは略語をコピーします。\n",
                "muted",
            )
        if entry.legacy:
            self.api.insert(
                "end",
                "旧APIの互換用です。新規コードはsegtree.pyのSegTree(op,e,v)を使います。\n",
                "muted",
            )
        if entry.key not in self.docs_cache:
            self.docs_cache[entry.key] = core.documentation(entry)
        sections = self.docs_cache[entry.key]
        for heading, body in sections:
            self.api.insert("end", heading + "\n", "heading")
            self._markdown(self.api, body + "\n")
        if any(title == "verify問題" for title, _ in sections):
            self.api.insert(
                "end", "※検証先の候補です。オンラインAC実績ではありません。\n", "muted"
            )
        self.api.insert("end", "公開API（クリックで定義へ）\n", "heading")
        if not entry.outline:
            self.api.insert(
                "end",
                "定義を抽出できません。コードプレビューを確認してください。\n",
                "muted",
            )
        for i, (_, signature, line, doc) in enumerate(entry.outline):
            tag = f"definition_{i}"
            self.api.insert("end", signature + "\n", ("signature", tag))
            self.api.tag_bind(tag, "<Button-1>", lambda _, n=line: self.goto_line(n))
            self.api.tag_bind(
                tag, "<Enter>", lambda _: self.api.configure(cursor="hand2")
            )
            self.api.tag_bind(
                tag, "<Leave>", lambda _: self.api.configure(cursor="xterm")
            )
            if doc:
                self.api.insert("end", doc.strip() + "\n")
        self.api.insert("end", "関連ドキュメント\n", "heading")
        self._markdown(
            self.api,
            "[ACL形式のAPI](ACL_API.md)　[全verify問題](VERIFY_PROBLEMS.md)　[ライブラリガイド](LIBRARY_GUIDE.md)\n",
        )
        self.api.configure(state="disabled")
        self.api.yview_moveto(0)

    def goto_line(self, line):
        self.tabs.select(self.code_page)
        self.preview.tag_remove("jump", "1.0", "end")
        self.preview.tag_add("jump", f"{line}.0", f"{line}.end")
        self.preview.see(f"{line}.0")
        return "break"

    def jump_to_symbol(self, _event=None):
        if self.current:
            for name, _, line, _ in self.current.outline:
                if name == self.symbol.get():
                    self.goto_line(line)
                    break

    def update_actions(self):
        state = "normal" if self.current else "disabled"
        for button in (
            self.copy_button,
            self.keep_button,
            self.favorite,
            self.source_button,
        ):
            button.configure(state=state)
        if self.current:
            starred = self.current.key in self.preferences.favorites
            self.favorite.configure(text="★ 登録済み" if starred else "☆ お気に入り")
            what = "略語" if self.current.kind == "Live" else "コード"
            self.copy_button.configure(text=f"{what}をコピーして閉じる  Enter")

    def _clipboard(self, text):
        self.root.clipboard_clear()
        self.root.clipboard_append(text)
        self.root.update_idletasks()

    def copy_selected(self, close=True):
        if self.pending is not None:
            self.populate(preserve=False)
        if not self.current:
            return "break"
        entry = self.current
        try:
            mode = "abbrev" if entry.kind == "Live" else "code"
            self._clipboard(core.prepare_code(entry, mode))
        except (tk.TclError, ValueError) as error:
            self.status.configure(text=f"コピーできませんでした: {error}")
            return "break"
        self.preferences.record(entry)
        if close:
            self.close()
        else:
            suffix = f" / {self.preferences.error}" if self.preferences.error else ""
            self.status.configure(text=f"コピーしました：{entry.name}{suffix}")
        return "break"

    def double_click(self, event):
        row = self.tree.identify_row(event.y)
        if row:
            self.tree.selection_set(row)
            self.select()
            return self.copy_selected()
        return "break"

    def toggle_favorite(self):
        if self.pending is not None:
            self.populate(preserve=False)
        if self.current:
            self.preferences.toggle(self.current)
            self.populate()
            if self.preferences.error:
                self.status.configure(text=self.preferences.error)
        return "break"

    def move(self, delta):
        if self.pending is not None:
            self.populate(preserve=False)
        rows = self.tree.get_children()
        if rows:
            selected = self.tree.selection()
            current = rows.index(selected[0]) if selected else 0
            row = rows[max(0, min(len(rows) - 1, current + delta))]
            self.tree.selection_set(row)
            self.tree.focus(row)
            self.tree.see(row)
            self.select()
        return "break"

    def focus_search(self, _event=None):
        self.query.focus_set()
        self.query.selection_range(0, "end")
        return "break"

    def search_for(self, query):
        self.kind_var.set("")
        self.group_var.set("すべての分野")
        self.scope_var.set("すべて")
        self._update_groups()
        self.query_var.set(query)
        self.populate(preserve=False)
        self.focus_search()

    def reset(self):
        self.search_for("")

    def toggle_tab(self):
        self.tabs.select(1 - self.tabs.index(self.tabs.select()))
        return "break"

    def show_find(self):
        self.tabs.select(self.code_page)
        self.find_bar.grid(row=1, column=0, sticky="ew")
        try:
            selection = self.preview.get("sel.first", "sel.last")
            if selection and "\n" not in selection:
                self.find_var.set(selection)
        except tk.TclError:
            pass
        self.find_in_preview()
        self.find_entry.focus_set()
        self.find_entry.selection_range(0, "end")
        return "break"

    def hide_find(self):
        self.find_bar.grid_remove()
        self.preview.tag_remove("find", "1.0", "end")
        self.preview.tag_remove("current_find", "1.0", "end")
        self.query.focus_set()
        return "break"

    def find_in_preview(self):
        term = self.find_var.get()
        self.find_matches = []
        self.find_index = -1
        self.preview.tag_remove("find", "1.0", "end")
        self.preview.tag_remove("current_find", "1.0", "end")
        index = "1.0"
        if term:
            for _ in range(2000):
                found = self.preview.search(term, index, stopindex="end", nocase=True)
                if not found:
                    break
                end = f"{found}+{len(term)}c"
                self.find_matches.append((found, end))
                self.preview.tag_add("find", found, end)
                index = end
        self.find_count.configure(text=f"0 / {len(self.find_matches)}")
        if self.find_matches:
            self.find_next()

    def find_next(self, step=1):
        if not self.find_bar.winfo_manager():
            return self.show_find()
        if self.find_matches:
            self.find_index = (self.find_index + step) % len(self.find_matches)
            start, end = self.find_matches[self.find_index]
            self.preview.tag_remove("current_find", "1.0", "end")
            self.preview.tag_add("current_find", start, end)
            self.preview.tag_raise("current_find")
            self.preview.see(start)
            count = str(len(self.find_matches)) + (
                "+" if len(self.find_matches) == 2000 else ""
            )
            self.find_count.configure(text=f"{self.find_index + 1} / {count}")
        return "break"

    def resize_font(self, delta):
        self.preferences.font_size = max(9, min(20, self.preferences.font_size + delta))
        for widget in (self.preview, self.gutter):
            widget.configure(font=("Consolas", self.preferences.font_size))
        self.preferences.save()
        return "break"

    def toggle_theme(self):
        self.preferences.theme = "light" if self.preferences.theme == "dark" else "dark"
        self.apply_theme()
        self.preferences.save()

    def reload(self):
        warnings = []
        try:
            entries, paths = core.load_entries(warnings=warnings)
        except (OSError, ValueError, TypeError, AttributeError) as error:
            self.status.configure(
                text=f"再読込できません。現在の一覧を保持します: {error}"
            )
            return "break"
        self.entries, self.search_dirs, self.warnings = entries, paths, warnings
        self.syntax_cache.clear()
        self.docs_cache.clear()
        self.rendered_key = None
        self._update_groups()
        self.populate()
        self.status.configure(
            text=f"再読込しました：{len(entries)}件 / 警告{len(warnings)}件"
        )
        return "break"

    def reveal_source(self):
        if not self.current:
            return "break"
        path = Path(self.current.path)
        try:
            if sys.platform == "win32":
                subprocess.Popen(["explorer.exe", "/select,", str(path)])
            else:
                webbrowser.open(path.parent.as_uri())
        except OSError as error:
            self.status.configure(text=f"保存場所を開けません: {error}")
        return "break"

    def open_link(self, target):
        if target.startswith(("https://", "http://")):
            webbrowser.open(target)
        else:
            path = (core.ROOT / target.split("#", 1)[0]).resolve()
            if path.suffix == ".md" and path.is_relative_to(core.ROOT):
                self.show_document(path)
        return "break"

    def text_window(self, title):
        window = tk.Toplevel(self.root)
        window.title(title)
        window.geometry("860x650")
        window.configure(bg=self.colors["bg"])
        window.rowconfigure(0, weight=1)
        window.columnconfigure(0, weight=1)
        text = tk.Text(
            window,
            wrap="word",
            padx=18,
            pady=16,
            font=("Yu Gothic UI", 11),
            bg=self.colors["code"],
            fg=self.colors["text"],
            borderwidth=0,
        )
        text.grid(row=0, column=0, sticky="nsew")
        scroll = ttk.Scrollbar(window, command=text.yview)
        scroll.grid(row=0, column=1, sticky="ns")
        text.configure(yscrollcommand=scroll.set)
        ttk.Button(window, text="閉じる", command=window.destroy).grid(
            row=1, column=0, sticky="e", padx=12, pady=8
        )
        window.bind("<Escape>", lambda _: window.destroy())
        return window, text

    def show_document(self, path):
        try:
            content = Path(path).read_text(encoding="utf8")
        except OSError as error:
            self.status.configure(text=f"説明を開けません: {error}")
            return
        _, text = self.text_window(Path(path).stem)
        text.tag_configure(
            "heading",
            foreground=self.colors["accent"],
            font=("Yu Gothic UI", 13, "bold"),
            spacing1=10,
            spacing3=5,
        )
        text.tag_configure("code", font=("Consolas", 10))
        in_code = False
        for line in content.splitlines():
            if line.startswith("```"):
                in_code = not in_code
                text.insert("end", "\n")
            elif in_code:
                text.insert("end", line + "\n", "code")
            elif line.startswith("#"):
                text.insert("end", line.lstrip("# ") + "\n", "heading")
            elif line.startswith("|"):
                if re.fullmatch(r"[|:\- ]+", line):
                    continue
                cells = [cell.strip() for cell in line.strip("| ").split("|")]
                self._markdown(text, "\n".join(cells).replace("<br>", "\n") + "\n\n")
            else:
                self._markdown(text, line + "\n")
        text.configure(state="disabled")

    def show_help(self):
        window, text = self.text_window("使い方・読み込み状況")
        message = """検索して、↑↓で選び、Enterでコピー。\n\n
File：コード全体をコピーします。解答のmainより上へ貼り付けます。
Live：user/Pythonの略語をコピーします。PyCharmへ貼り付けてTabで展開します。
コードの一部だけが必要なら、プレビューを選択してCtrl+Cを使えます。

Enter                  コピーして閉じる（検索欄・一覧どちらからでも）
Ctrl+Enter             コピーして続ける
Ctrl+L                 検索欄へ戻って全選択
↑ / ↓                  候補を移動
PageUp / PageDown      候補を8件ずつ移動
Ctrl+D                 選択した候補をお気に入りに登録・解除
Alt+1 / Alt+2 / Alt+3   すべて / File / Live
F2                     コードとAPI・verifyを切り替え
Ctrl+F                 コード内検索
F3 / Shift+F3          コード内の次 / 前の一致
F4                     元ファイルの保存場所を開く
F5                     設定・スニペット・テンプレートを再読込
Esc                    終了（コード内検索中は検索欄を閉じる）
Ctrl+マウスホイール     コードの文字サイズを変更

検索はスペース区切りでAND。引用符でフレーズ、-語で除外できます。
例：range sum　 /　@file セグ木 -compat　 /　"heavy light"
大文字小文字・全角英数字・名前の_の差を吸収します。
通常の検索で候補がないときだけ、タイプミス・短い略記を探します。
一致度を優先し、同点ならお気に入り・コピー履歴・Fileを上にします。
旧API専用の_compatは通常の候補より後に表示します。

お気に入り・直近20件・テーマ・文字サイズ・ウィンドウサイズを保存します。
検索語とコードの内容は履歴へ保存しません。

"""
        self._markdown(
            text,
            message
            + "[ACL形式のAPI](ACL_API.md)　[verify問題一覧](VERIFY_PROBLEMS.md)　[操作ガイド](LOCAL_USAGE.md)\n\n",
        )
        text.insert(
            "end",
            "Live Template読込先\n"
            + "\n".join(str(p) for p in self.search_dirs)
            + "\n\n",
        )
        text.insert("end", "表示設定: " + str(self.preferences.path) + "\n")
        if self.warnings:
            text.insert("end", "\n読込警告\n" + "\n\n".join(self.warnings))
        if self.preferences.error:
            text.insert("end", "\n" + self.preferences.error)
        text.configure(state="disabled")
        ttk.Button(window, text="機能チェックリスト", command=self.show_checklist).grid(
            row=1, column=0, sticky="w", padx=12, pady=8
        )
        return "break"

    def show_checklist(self):
        _, text = self.text_window("機能チェックリスト")
        text.insert(
            "end",
            "名前・クラス名による照合です。未検出は未実装の証明ではありません。\n\n",
        )
        for item in core.wishlist_items(self.entries):
            status = "✓" if item["detected"] else "—"
            text.insert(
                "end",
                f"{status} {item['name']}  /  {item.get('category', '')}\n    {item.get('description', '')}\n\n",
            )
        text.configure(state="disabled")

    def close(self):
        if self.pending is not None:
            self.root.after_cancel(self.pending)
            self.pending = None
        width, height = self.root.winfo_width(), self.root.winfo_height()
        if width >= 960 and height >= 620:
            self.preferences.geometry = f"{width}x{height}"
        self.preferences.save()
        self.root.destroy()
        return "break"

    def run(self):
        self.root.mainloop()
