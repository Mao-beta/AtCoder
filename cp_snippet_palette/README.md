# CP Snippet Palette

PyCharmの **userグループでPythonコンテキストが有効なLive Templateだけ** と、ローカルのPythonスニペットを検索するツール。標準ライブラリだけで動作する。

使い方の説明・画面表示の更新：2026-10-19。

| 読みたい内容 | 文書 |
|---|---|
| 起動・検索・コピー・キー操作 | [LOCAL_USAGE.md](LOCAL_USAGE.md) |
| 機能ごとの略語・PyCharmで展開するコード | [Live Template 274件](LIVE_TEMPLATES.md) |
| やりたいことから選ぶ・似た機能の使い分け | [17分野・234用途の逆引き](LIBRARY_GUIDE.md#目的から探す逆引き) |
| 提出用ライブラリの使い方・API一覧・PyPy/Codon | [LIBRARY_GUIDE.md](LIBRARY_GUIDE.md) |
| 発想・不変条件・計算量・適用条件を理解する | [全92ファイルのアルゴリズム解説](ALGORITHMS.md) |
| ABCの頻出パターンに合わせて選ぶ | [ABC向け追加12ファイル](ABC_TOOLKIT.md) |
| セグ木のコールバック定義を省いて使う | [モノイド・遅延更新の派生版33種](SEGTREE_RECIPES.md) |
| ACL形式の引数順・旧APIからの移行 | [ACL_API.md](ACL_API.md) |
| 各ファイルのverify候補・入力変換・検証範囲 | [VERIFY_PROBLEMS.md](VERIFY_PROBLEMS.md) |
| Library Checkerの追加対応・提出ファイルの生成 | [verify/README.md](verify/README.md) |
| 83用途の元コード調査と現在の抽出先 | [LIBRARY_CANDIDATES.md](LIBRARY_CANDIDATES.md) |

## 起動とコピー

このフォルダの `run_palette.bat` をダブルクリックする。既存の `D:\Kyopro\AtCoder\.venv\Scripts\pythonw.exe` で起動する。

検索欄に `セグ木`、`さいたんろ`、`2sat`、`fps_inverse`などを入力し、↑/↓で選んでEnter。クラス・関数名の一致を本文中の一致より優先し、同点ならお気に入り・コピー履歴・Fileを上に表示する。候補がないときは、軽微なタイプミスも補う。

- **File**: ファイルのコードをそのままコピーする。解答のmainより上に貼り付ける。
- **Live**: テンプレートの略語をコピーする。PyCharmで貼り付け、Tabで展開する。

メイン画面は左が検索・絞り込み・候補一覧、右が選択中の解説とコピー。最初は「使い方・解説・API」を表示し、F2かタブでコードへ切り替える。種類の表示と右下の案内で、File全体を貼り付けるか、Liveの略語をTab展開するかを確認できる。コピー結果はボタンの下に表示する。

同梱ライブラリのLiveは機能ごとの略語で、接頭辞は付けない。例えば`compress_sequence`、`lis_length`、`inversion_count`は別々の機能を展開する。関数は個別、クラスはクラス単位で、必要な補助定義も含める。[登録・更新の手順](LOCAL_USAGE.md#live-templateへの登録と更新)を参照。

**検索画面ではEnter・Ctrl+Enter・コピーボタンでコピーし、画面は開いたままになる。** Fileならコード、Liveなら略語をコピーする。キー操作は検索欄と一覧のどちらにフォーカスがあっても使える。終了はEscまたはウィンドウの×で行う。目的ナビのEnterは選択、コピーはボタンまたはCtrl+Enter。

## 探す・読む・使う

- **目的から探す（F6）**：6分類から対象・目的を順に選び、234用途を絞り込む。左で候補を選び、右で条件・APIの入力・計算量・使用例を確認してコピーできる。「戻る」「最初から」、分類内検索、範囲内の全候補表示で比較もできる。従来の逆引き表は「一覧ガイド」から開く。
- **絞り込み**：File／Live、分野、お気に入り、最近コピーを組み合わせる。`@file セグ木 -lazy`のように検索欄からも指定できる。
- **お気に入りと履歴**：Ctrl+Dで登録・解除。「最近コピー」には直近20件を表示する。
- **コードプレビュー**：構文の色分け、行番号、検索語の強調表示。「定義へ」からクラスや関数へ移動できる。Ctrl+Fでコード内検索。
- **使い方・解説・API**：最初に表示するタブ。Fileの使用例、アルゴリズムの解説、目的からの選び方、引数・戻り値・前提条件を読める。機能別Liveは選んだ関数・クラスの入力と使い方を先に表示し、元Fileの使用例へのリンクも付ける。公開APIをクリックするとコードの定義へ移動する。
- **表示調整**：解説は見出しを大きくし、入力ラベル・計算量・API定義・コード例を色と書体で区別する。コード・解説・別窓のガイドは「−」「＋」またはCtrl+マウスホイールで一緒に拡大・縮小できる。ダーク／ライト切り替え、一覧とプレビューの幅調整にも対応。文字サイズとウィンドウの大きさを記憶する。
- **ヘルプ**：F1でショートカット、読み込み状況、関連ガイドを表示する。機能チェックリストもここから開く。

Ctrl+Lで検索欄へ戻る。F5で設定・スニペット・Live Templateを再読み込みする。Escで終了。詳しい手順とキー一覧は[LOCAL_USAGE.md](LOCAL_USAGE.md)を参照。

今回のメイン画面を反映するには、パレットを閉じて`run_palette.bat`から起動し直す。以後、F5で文書・分類・スニペット・登録済みLiveを再読み込みできる。F5は画面プログラムの更新やPyCharmへの登録は行わない。

コンテストモードや来歴によるコピー制限はなく、コードへのURLコメント自動挿入も行わない。

## 読み込み対象

PyCharmの `templates/` と `settingsSync/templates/` を自動探索する。XMLのグループ名がuserで、各テンプレートにPythonまたはPythonのサブコンテキストが有効と明記されているものを読む。HTMLなど他言語のもの、他グループ、Python設定のないものは読み込まない。検索・F5でXMLは変更しない。登録は別の`sync_live_templates.py --apply`で行う。

同梱の`config.json`には次の読み込み先を設定している。

```json
"snippet_dirs": ["snippets", "library"],
"extra_template_dirs": []
```

相対パスの基準はこのフォルダ。`extra_template_dirs`のXMLにも同じuser/Python条件を適用する。ファイルは読み込みと構文解析だけを行い、検索のために実行しない。

2026-10-19に機能別Live 274件を登録済み。このPCでは **Live 364件＋File 92件＝456件**を読み込む。user.xmlの元の94項目のうち4項目はPython対象外のため検索には含めない。Fileは16スニペットと76ライブラリファイル（初回抽出51＋第1弾3＋第2弾8＋派生セグ木集2＋ABC向け12）。

ACL形式の呼び出しは[ACL_API.md](ACL_API.md)、問題を使った検証の候補は[VERIFY_PROBLEMS.md](VERIFY_PROBLEMS.md)を参照。全92ファイルに対応する候補170問と、未選定・部分確認の範囲をまとめている。青以上の用途を優先した対応60問題には[提出用ファイルの生成手順](verify/README.md)も用意した。

全92ファイルの先頭に実行例を掲載し、各公開関数・クラス・メソッドに説明を付けた。パレットでFileを選んでF2を押すか、PyCharmでファイルを開けば読める。使用例は通常のPythonコードで、期待する戻り値を`# => 値`のコメントに記載している。詳細は[使い方の説明の読み方](LIBRARY_GUIDE.md#使い方の説明の読み方)を参照。

入力の説明には、引数の型・並べ方・添字・許される範囲を記載している。計算量は構築と操作を分け、Nなどの記号の意味、時間・空間、最悪・償却・期待の違いを補足した。クラスのメソッドで共通の型・添字・記号は、クラスの説明を参照する。文書更新はF5で反映できる。

頂点・添字・順位は0始まりに統一した。LCATreeは頂点0..N-1、root=0。WaveletMatrixのkth_smallest/kth_largest/selectとFullyIndexableDictionary.selectもk=0が先頭。LinkedListは実ノードID=0から発行し、insert_after(-1,x)で先頭へ挿入する。旧1始まり呼び出しへの自動変換は行わない。F5でスニペットを読み直し、必要なものをコピーし直す。

互換用の旧名も削除した。WeightedUnionFindはmerge/leader/same、LCAはlca、Beatsはchmin/chmax/add/assignとmin/max/sum/prodを使う。戻り値・引数・削除した名前の一覧は[APIの共通規約](ACL_API.md#独自ライブラリの共通規約)を参照。ACL-for-pythonの仕様よりも、公開の添字・頂点番号・順位を0始まりにする方針を優先する。

[アルゴリズム解説](ALGORITHMS.md)はAtCoder青レベルを想定し、基本用語は省いて発想・正しさの要点・計算量・落とし穴をまとめた。F2では選択中のファイルの解説を使用例の直後に表示する。今回の表示追加はパレットを再起動すると反映され、以後の文書更新はF5で読み直せる。

## 付属ファイル

| 場所 | 内容 |
|---|---|
| `cp_palette.py` | 読み込み・検索・設定保存・CLI |
| `palette_ui.py` | 検索画面・コードプレビュー・API表示 |
| `purpose_browser.py` | 段階選択・分類内検索・候補の比較とコピー |
| `purpose_catalog.py` | 逆引き表の分類・目的・条件・APIリンクの読み込み |
| `feature_snippets.py` | 公開関数・クラスと、必要な補助定義の切り出し |
| `sync_live_templates.py` | user/Pythonへの登録プレビュー・バックアップ付き更新・略語一覧の生成 |
| `config.json` | 検索ディレクトリ・日本語キーワード・任意メタデータ |
| `wishlist.json` | 43用途の登録状況チェック。名前の別名も設定可能 |
| `snippets/` | 従来の構造系11・幾何系5ファイル |
| `library/` | 76ファイル。初回抽出51＋第1弾3＋第2弾8＋派生セグ木集2＋ABC向け12 |
| `tests/test_palette.py` | 対象XMLの選別・検索・設定・一覧出力・234用途と全92ファイルの分類対応 |
| `tests/test_palette_ui.py` | 非表示のTkで検索・目的ナビの選択・コピー・再読み込みを確認 |
| `tests/test_live_templates.py` | 機能の単独実行・依存参照・XMLへの登録と既存項目の保全 |
| `tests/test_library.py` | 抽出ライブラリの代表例・不具合の回帰確認 |
| `tests/test_library_checker.py` | LC向け追加APIと、提出用コードの23サンプル入力検査 |
| `tests/test_library_checker_round2.py` | 第2弾50問・91サンプルと追加APIの愚直照合 |
| `tests/test_segtree_recipes.py` | 派生版33種の配列比較・作用則・AtCoder公式サンプル |
| `tests/test_abc_toolkit.py` | ABC向け12ファイルの愚直比較・公式サンプル |
| `verify/` | LC 60問・AtCoder 23問の入出力、提出ファイル生成、公式サンプル入力 |
| `inventory_initial.tsv` | 配布時の一覧。現在の読み込み内容とは異なる |

チェックリストの「未検出」は名前の照合結果であり、未実装の証明ではない。実装があれば`identifiers`に実際のクラス名・関数名を追加できる。

お気に入り、直近20件、テーマ、コード・解説共通の文字サイズ、ウィンドウサイズは`.palette_state.json`に保存する。このファイルはGitの対象外。検索語・コード本文・クリップボードの内容は保存しない。表示設定を初期化したい場合は、パレットを閉じてからこのファイルを削除する。

## 画面を開かない操作

```powershell
Set-Location D:\Kyopro\AtCoder\cp_snippet_palette
..\.venv\Scripts\python.exe cp_palette.py --check
..\.venv\Scripts\python.exe cp_palette.py --list --query "@file scc"
..\.venv\Scripts\python.exe cp_palette.py --export-inventory inventory_local.tsv
```

実際のエディタ位置でLive Templateを展開できるかはPyCharmが判定する。File全体のコピーと、機能別Liveの展開を用途に応じて選ぶ。具体的なPyCharmのショートカット設定は[LOCAL_USAGE.md](LOCAL_USAGE.md)を参照。
