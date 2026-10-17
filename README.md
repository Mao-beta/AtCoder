# AtCoder
AtCoderで解けた問題のコードをあげてく

## スニペット検索・提出用ライブラリ

[CP Snippet Palette](cp_snippet_palette/README.md)で、userグループのPython用Live Templateと同梱ライブラリを検索できる。

- [起動・検索・コピーの操作](cp_snippet_palette/LOCAL_USAGE.md)
- [ライブラリの使い方・API一覧](cp_snippet_palette/LIBRARY_GUIDE.md)
- [ACL形式の呼び出しと旧APIからの移行](cp_snippet_palette/ACL_API.md)
- [AtCoder・Library Checkerのverify候補](cp_snippet_palette/VERIFY_PROBLEMS.md)
- [Library Checkerの追加対応・提出用コードの生成](cp_snippet_palette/verify/README.md)
- [ローカルPython環境](ATCODER-ENVIRONMENT.md)

直下の`_cp_structures_guide.md`は旧統合版、`_codex_refactor_instructions.md`は過去の再編計画。現在の提出用コードには上記ガイドを使う。

## ファイルの作成・整理

コンテスト前は、リポジトリ直下で `_make_contest_files.py` を実行してファイルを作る。
終了後の整理には `_folder_move.py` を使う。作業ディレクトリによらず、このスクリプトがあるリポジトリを対象にする。

```powershell
# 移動予定を確認する（ファイルは変更しない）
.\.venv\Scripts\python.exe _folder_move.py
# 実際に整理する
.\.venv\Scripts\python.exe _folder_move.py --apply
# 直下の作業中ファイルを残し、保存済みのファイルだけを整理する
.\.venv\Scripts\python.exe _folder_move.py --archives-only --apply
```

- ABC・ARC・AGC: `ABC/ABC479/ABC479A.py` のように種類と回で分類する。
- PAST: フォルダ名・ファイル名とも回番号を3桁にする。例: `PAST/PAST004/PAST004A.py`。
- ADT: `ADT/20231018/ADT_20231018_2A.py` のように開催日で分類する。
- yukicoder: `yuki/02xx/yuki_0247.py` のように百番単位で分類する。同じ番号の `.txt` も一緒に置く。
- EDPC・典型90問: 既存の `EDPC/`・`tenkei90/` を使う。

同名ファイルがある場合は、既存ファイルを上書きせず、移動する側を `_alt2.py`、`_alt3.py` のように命名する。
入力データなど命名規則に当てはまらないファイルはそのまま残し、移動で空になったフォルダだけ取り除く。
旧 `folder_constructor.py`・`yuki/_organize_files.py` の代わりに、この整理ツールを使う。

## 別解の残し方

別解も同じコンテストフォルダに置き、問題名の後ろに方式を付ける。
たとえば `ARC092C.py` と `ARC092C_dinic.py`、`ABC168E_fraction.py` と `ABC168E_counter.py`。
`_draft` は作業途中、`_bruteforce` は愚直解など、用途が明確な場合だけその名前を付ける。
方式や用途が分からない場合は `_alt2` のまま保持し、後で分かったときに改名する。
ファイル名だけを根拠に正解・不正解や新旧を判定せず、コードの内容は整理時に変更しない。

## 整理ツールの確認

```powershell
.\.venv\Scripts\python.exe -B -m unittest discover -s tests -v
```
