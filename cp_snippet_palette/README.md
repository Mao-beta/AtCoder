# CP Snippet Palette

PyCharmの **userグループでPythonコンテキストが有効なLive Templateだけ** と、ローカルのPythonスニペットを検索するツール。標準ライブラリだけで動作する。

文書と現行コードの最終照合：2026-10-17。

| 読みたい内容 | 文書 |
|---|---|
| 起動・検索・コピー・キー操作 | [LOCAL_USAGE.md](LOCAL_USAGE.md) |
| 提出用ライブラリの使い方・API一覧・PyPy/Codon | [LIBRARY_GUIDE.md](LIBRARY_GUIDE.md) |
| ACL形式の引数順・旧APIからの移行 | [ACL_API.md](ACL_API.md) |
| 各ファイルのverify候補・入力変換・検証範囲 | [VERIFY_PROBLEMS.md](VERIFY_PROBLEMS.md) |
| Library Checkerの追加対応・提出ファイルの生成 | [verify/README.md](verify/README.md) |
| 83用途の元コード調査と現在の抽出先 | [LIBRARY_CANDIDATES.md](LIBRARY_CANDIDATES.md) |

## 起動とコピー

このフォルダの `run_palette.bat` をダブルクリックする。既存の `D:\Kyopro\AtCoder\.venv\Scripts\pythonw.exe` で起動する。

検索欄に `セグ木`、`さいたんろ`、`2sat`、`fps_inverse`などを入力し、↑/↓で選んでEnter。クラス・関数名の一致を本文中の一致より優先し、同点ならお気に入り・コピー履歴・Fileを上に表示する。候補がないときは、軽微なタイプミスも補う。

- **File**: ファイルのコードをそのままコピーする。解答のmainより上に貼り付ける。
- **Live**: テンプレートの略語をコピーする。PyCharmで貼り付け、Tabで展開する。

**Enterはコピーして閉じる、Ctrl+Enterはコピーして続ける。** どちらもFileならコード、Liveなら略語をコピーする。検索欄と一覧のどちらにフォーカスがあっても使える。

## 探す・読む・使う

- **絞り込み**：File／Live、分野、お気に入り、最近コピーを組み合わせる。`@file セグ木 -compat`のように検索欄からも指定できる。
- **お気に入りと履歴**：Ctrl+Dで登録・解除。「最近コピー」には直近20件を表示する。
- **コードプレビュー**：構文の色分け、行番号、検索語の強調表示。「定義へ」からクラスや関数へ移動できる。Ctrl+Fでコード内検索。
- **API・verify**：F2で切り替えると、公開API・docstring・ACLとの対応・verify候補を読める。APIをクリックすると定義へ移動し、問題リンクをクリックするとブラウザで開く。
- **表示調整**：ダーク／ライト切り替え、文字サイズ変更、一覧とプレビューの幅調整。ウィンドウの大きさも記憶する。
- **ヘルプ**：F1でショートカット、読み込み状況、関連ガイドを表示する。機能チェックリストもここから開く。

Ctrl+Lで検索欄へ戻る。F5で設定・スニペット・Live Templateを再読み込みする。Escで終了。詳しい手順とキー一覧は[LOCAL_USAGE.md](LOCAL_USAGE.md)を参照。

コンテストモードや来歴によるコピー制限はなく、コードへのURLコメント自動挿入も行わない。

## 読み込み対象

PyCharmの `templates/` と `settingsSync/templates/` を自動探索する。XMLのグループ名がuserで、各テンプレートにPythonまたはPythonのサブコンテキストが有効と明記されているものを読む。HTMLなど他言語のもの、他グループ、Python設定のないものは読み込まない。XMLは変更しない。

同梱の`config.json`には次の読み込み先を設定している。

```json
"snippet_dirs": ["snippets", "library"],
"extra_template_dirs": []
```

相対パスの基準はこのフォルダ。`extra_template_dirs`のXMLにも同じuser/Python条件を適用する。ファイルは読み込みと構文解析だけを行い、検索のために実行しない。

2026-10-17のこのPCでは **Live 90件＋File 71件＝161件**。Fileは従来の17スニペットと54ライブラリファイル（初回抽出51＋追加3）。

ACL形式の呼び出しは[ACL_API.md](ACL_API.md)、問題を使った検証の候補は[VERIFY_PROBLEMS.md](VERIFY_PROBLEMS.md)を参照。全71ファイルに対応する候補133問と、未選定・部分確認の範囲をまとめている。青以上の用途を優先した追加10問題には[提出用ファイルの生成手順](verify/README.md)も用意した。

## 付属ファイル

| 場所 | 内容 |
|---|---|
| `cp_palette.py` | 読み込み・検索・設定保存・CLI |
| `palette_ui.py` | 検索画面・コードプレビュー・API表示 |
| `config.json` | 検索ディレクトリ・日本語キーワード・任意メタデータ |
| `wishlist.json` | 43用途の登録状況チェック。名前の別名も設定可能 |
| `snippets/` | 従来の構造系12・幾何系5ファイル |
| `library/` | 54ファイル。83用途からの抽出51ファイルにSWAG・割当・線形代数を追加 |
| `tests/test_palette.py` | 対象XMLの選別・検索順位・絞り込み・設定保存・一覧出力 |
| `tests/test_palette_ui.py` | 非表示のTkで選択・コピー・再読み込みを確認 |
| `tests/test_library.py` | 抽出ライブラリの代表例・不具合の回帰確認 |
| `tests/test_library_checker.py` | LC向け追加APIと、提出用コードの23サンプル入力検査 |
| `verify/` | 10問題の入出力、提出ファイル生成、公式サンプル入力 |
| `inventory_initial.tsv` | 配布時の一覧。現在の読み込み内容とは異なる |

チェックリストの「未検出」は名前の照合結果であり、未実装の証明ではない。実装があれば`identifiers`に実際のクラス名・関数名を追加できる。

お気に入り、直近20件、テーマ、コードの文字サイズ、ウィンドウサイズは`.palette_state.json`に保存する。このファイルはGitの対象外。検索語・コード本文・クリップボードの内容は保存しない。表示設定を初期化したい場合は、パレットを閉じてからこのファイルを削除する。

## 画面を開かない操作

```powershell
Set-Location D:\Kyopro\AtCoder\cp_snippet_palette
..\.venv\Scripts\python.exe cp_palette.py --check
..\.venv\Scripts\python.exe cp_palette.py --list --query "@file scc"
..\.venv\Scripts\python.exe cp_palette.py --export-inventory inventory_local.tsv
```

実際のエディタ位置でLive Templateを展開できるかはPyCharmが判定する。提出用の新しいコードはFileからコピーする。具体的なPyCharmのショートカット設定は[LOCAL_USAGE.md](LOCAL_USAGE.md)を参照。
