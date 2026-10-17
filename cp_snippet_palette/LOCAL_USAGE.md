# このPCでの使い方

確認日: 2026-10-17。場所は `D:\Kyopro\AtCoder\cp_snippet_palette`。

## まず使う

1. このフォルダの `run_palette.bat` をダブルクリックする。
2. 検索欄に `UnionFind` と入力する。
3. 種別が **File**、名前が **UnionFind** の行を選び、右側のコードを見る。
4. **Enter**を押すとコードをコピーして画面が閉じる。
5. PyCharmの解答ファイルで、`main()`の外側・上の方に**Ctrl+V**で貼り付ける。

貼り付けたクラスは、たとえば次のように使う。

```python
uf = DSU(5)
uf.merge(0, 2)
print(uf.same(0, 2))  # True
print(uf.size(0))     # 2
```

`UnionFind.py`にはACL形式の`DSU`も同梱している。スニペットは提出コードに貼るためのもの。`pip install`や`import snippets`は不要。

複数のライブラリを探すときは**Ctrl+Enter**でコピーし、PyCharmに貼り付けてからパレットへ戻る。**Ctrl+L**で検索語を入れ替えられる。よく使うものは**Ctrl+D**でお気に入りに登録しておく。

## 検索の例

検索はファイル名・クラス/関数名・説明・キーワード・コード本文を対象にする。スペースで区切るとAND条件になる。大文字小文字・全角英数字・識別子のアンダースコアの違いを吸収する。名前やAPI名の一致を優先し、本文に単語が出てくるだけの候補は下に表示する。

| 入力例 | 探すもの |
|---|---|
| `セグ木` / `せぐき` | 通常のsegtreeを先頭に表示 |
| `FenwickTree` | BIT.py内のACL形式のFenwickTree |
| `さいたんろ` | shortest_paths |
| `2sat` | scc内のTwoSAT |
| `fps_inverse` | polynomial内の関数。プレビューも定義へ移動 |
| `区間更新` | lazy_segtreeと、対応するLive Template |
| `@file scc` | Fileに限定して検索 |
| `@live 区間更新` | Liveに限定して検索 |
| `@file セグ木 -compat` | Fileを対象に、compatを含む候補を除外 |
| `"heavy light"` | 語順を含めてフレーズで検索 |
| `geometry 凸包` | 幾何スニペット。凸包を使うなら03_polygon_convexを選ぶ |
| `closest_pair` | 04_closest_pair（関数名はclosest_pair_sq） |
| `SegTree_compat` | update/queryを使う旧SegTree APIの互換版 |
| `SWAG` | aggregate_queue。非可換演算も扱うキュー集約 |
| `区間直線` | li_chao内の座標圧縮版LiChaoTree |
| `ハンガリアン` | assignment。最小費用割当 |
| `連立一次方程式` | linear_algebra。特解と基底を返す |

該当候補がないときだけタイプミスや短い略記を補う。たとえば`segtreee`でもsegtreeを探せる。同点の候補はお気に入り、コピー履歴、Fileの順で優先し、旧API用の`_compat`は通常の候補より後に表示する。

検索欄の下にあるFile／Live、分野、「★ お気に入り」「最近コピー」も組み合わせられる。何も出ない場合は、検索語に加えて絞り込み条件も確認する。「検索・絞り込みをリセット」で一度に戻せる。

このPCでは **Live 90件＋File 71件＝161件**を読み込む。LiveはuserグループのPython用だけ。Fileは従来の17スニペットと54ライブラリファイル（初回抽出51＋追加3）。

## FileとLiveの違い

- **File**: EnterでPythonコードそのものをコピーする。
- **Live**: EnterでPyCharmのテンプレート略語をコピーする。PyCharmでCtrl+Vの後、設定された展開キー（通常Tab）を押す。`$END$`等の変数はPyCharmが処理する。
- **Ctrl+EnterはFile／Live共通で「コピーして続ける」**。従来の「Liveの略語をコピーする」専用操作から変更した。
- プレビューの一部だけを選択してCtrl+Cでコピーすることもできる。ただし、Fileの標準操作は必要なimport・補助定義を含むファイル全体のコピー。

コンテストモードと来歴によるコピー制限は削除した。由来・URLの有無にかかわらずコピーでき、コピー時にURLコメントを自動追加することもない。

## プレビューとAPI・verifyを使う

右側のコードは構文を色分けし、行番号と検索語の位置を表示する。「定義へ」の一覧からクラス・メソッド・関数へ直接移動できる。特定のAPI名で検索したときは、その定義へ自動で移動する。

**F2**で「API・verify」に切り替えると、公開APIの引数、docstring、ACL形式の対応、verify問題の候補を確認できる。APIをクリックするとコードの該当行へ戻る。問題名をクリックするとブラウザが開く。ここに掲載した問題は検証先の候補で、オンラインでのAC記録ではない。

**Ctrl+F**は、選んでいるコードの中を検索する。F3／Shift+F3で次／前へ移動できる。改行を含まない文字列をコード内で選択してからCtrl+Fを押すと、その文字列が検索欄に入る。コード内検索欄のEnterは次の一致へ、Escは検索欄を閉じる操作になる。

コードの文字サイズは「−」「＋」またはCtrl+マウスホイールで調整する。上部の「ライト」「ダーク」で配色を変更できる。一覧とプレビューの境界はドラッグして幅を調整できる。

## キー操作

| キー | 操作 |
|---|---|
| Enter | 選んだ候補をコピーして閉じる |
| Ctrl+Enter | コピーして開いたままにする |
| ↑ / ↓ | 検索欄・一覧から候補を移動 |
| PageUp / PageDown | 検索欄・一覧から8件ずつ移動 |
| Ctrl+L | 検索欄へ戻り、検索語を全選択 |
| Ctrl+D | お気に入りに登録・解除 |
| Alt+1 / Alt+2 / Alt+3 | すべて / File / Liveに切り替え |
| F2 | コードとAPI・verifyを切り替え |
| Ctrl+F | コード内検索を開く |
| F3 / Shift+F3 | コード内の次 / 前の一致 |
| F4 | 元ファイルをエクスプローラーで選択 |
| F5 | 設定・コード・Live Templateを再読み込み |
| F1 | 操作ヘルプ・読み込み状況・機能チェックリスト |
| Esc | 終了。コード内検索欄では検索欄を閉じる |

一覧の候補をダブルクリックしてもコピーして閉じられる。

お気に入り、最近コピーした20件、配色、コードの文字サイズ、ウィンドウサイズは`.palette_state.json`に保存する。検索語とコード本文は保存しない。このファイルはGitの対象外で、閉じた状態で削除すれば表示設定と履歴を初期化できる。

## PyCharmからショートカットで起動する

Settings → Tools → External Tools → ＋ に次を登録する。

| 項目 | 設定値 |
|---|---|
| Name | CP Snippet Palette |
| Program | `D:\Kyopro\AtCoder\.venv\Scripts\pythonw.exe` |
| Arguments | `"D:\Kyopro\AtCoder\cp_snippet_palette\cp_palette.py"` |
| Working directory | `D:\Kyopro\AtCoder\cp_snippet_palette` |

Settings → Keymap → External Tools → CP Snippet Paletteから、空いているキーを割り当てる。たとえばCtrl+Alt+Shift+L。IDEの設定変更は今回行っていない。

起動時の検索語も指定できる。

```powershell
.\run_palette.bat --query "@file セグ木"
```

## スニペットの追加

自己完結した`.py`をこのフォルダの`snippets/`以下に置き、F5で再読み込みする。たとえば`snippets/graphs/SCC.py`。必要なimport・補助定義も同じファイルに含め、入力を読むmain処理は含めない。

`config.json`の`keywords`に、ファイル名の拡張子を除いた名前をキーとして日本語の検索語を足せる。任意の`descriptions`にも同じキーで一覧の説明文を設定できる。

```json
"SCC": ["強連結成分", "縮約グラフ"]
```

`snippet_dirs`の相対パスはパレットのあるフォルダが基準。現在は`["snippets", "library"]`。リポジトリ直下の別の`snippets/`や解答ファイル全体は検索しない。[抽出済みライブラリの使い方](LIBRARY_GUIDE.md)と[候補との対応表](LIBRARY_CANDIDATES.md)を参照。

幾何5ファイルは各々に必要なPoint等を含む。複数ファイルを貼ると同じ定義が重複する場合がある。最新のAPIは[ACL_API.md](ACL_API.md)と各ファイルのdocstringを参照。新規コードはSegTree(op,e,v)、LazySegTree(op,e,mapping,composition,id_,v)、FenwickTree.sum(l,r)を使う。LCATreeは頂点が1-indexed、互換クラスBIT.sum(i)はiを含む。直下の`_cp_structures_guide.md`は旧APIの説明。

## 画面を開かない確認

PowerShellで次を実行する。

```powershell
Set-Location D:\Kyopro\AtCoder\cp_snippet_palette
..\.venv\Scripts\python.exe cp_palette.py --check
..\.venv\Scripts\python.exe cp_palette.py --list --query "structures UnionFind"
..\.venv\Scripts\python.exe cp_palette.py --export-inventory inventory_local.tsv
..\.venv\Scripts\python.exe -B -m unittest discover -s tests -v
```

一覧の出力先はパレットフォルダ内。`inventory_initial.tsv`は元の配布時の一覧であり、このPCのLive Templateを含む最新一覧ではない。

## 動作確認の範囲

検索ツールの関連7テストが成功。user/Pythonだけの読み込み、検索順位・別名・タイプミス・絞り込み、設定の保存、APIの抽出、検索直後のコピー対象、候補がない場合、再読み込み、コピー失敗時の処理を確認した。GUIのテストはウィンドウを非表示にして実行し、クリップボード部分を置き換えてコピー文字列を確認している。

Library Checker向けの追加後、実データ161件で非表示GUIの初期化と、今回拡張した6モジュールの検索・API・verify表示を確認した。目視確認、実際のクリップボード書き換え、PyCharmへの貼り付け操作は行っていない。

提出用ライブラリ自体のAPI・PyPyでの検証・Codonに関する注意は[LIBRARY_GUIDE.md](LIBRARY_GUIDE.md)、verify問題の候補と入力の変換方法は[VERIFY_PROBLEMS.md](VERIFY_PROBLEMS.md)を参照。Live TemplateのXMLは変更していない。

Library Checkerの追加10問題は[verify/README.md](verify/README.md)の手順で、入出力を含む提出用の1ファイルを生成できる。
