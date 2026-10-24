# 提出用ライブラリの使い方

使い方の説明の更新：2026-10-19。`library/`は76ファイル。候補83用途から抽出した51ファイルに、第1弾で3ファイル、第2弾で8ファイル、派生セグ木集を2ファイル、ABC向け部品を12ファイル追加した。Library Checkerの提出アダプターは合計60問。依存する補助コードは同じファイルに含め、元の解答ファイルは変更していない。ACL対応APIはshakayami/ACL-for-pythonの名前・引数順・戻り値に統一した。

[目的から探す逆引き](LIBRARY_GUIDE.md#目的から探す逆引き) ／ [ABCの頻出パターン](ABC_TOOLKIT.md) ／ [セグ木派生版33種](SEGTREE_RECIPES.md) ／ [ACL形式のAPIと移行方法](ACL_API.md) ／ [全92ファイルのverify問題一覧](VERIFY_PROBLEMS.md) ／ [LC対応60問題の提出手順](verify/README.md)

## 検索して提出する

`run_palette.bat`を起動し、例えば`graphs SCC`、`座標圧縮`、`fps_inverse`、`区間 和 等差`で検索する。**File**の行を選んでEnter、解答のmainより上に貼り付ける。ローカルのlibraryフォルダをAtCoderにアップロードしたり、提出コードからimportしたりする必要はない。

検索欄・候補一覧でのEnter、Ctrl+Enter、コピーボタンは、いずれもコピー後に画面を開いたままにする。右側は最初に使い方を表示し、F2でコードと切り替える。Ctrl+Dでお気に入り登録、Ctrl+Lで検索欄へ戻る。File／Live・分野・履歴の絞り込みやコード内検索は[操作ガイド](LOCAL_USAGE.md)を参照。

同じファイルに近い用途をまとめたため、一度コピーすればそのファイルの関数を使える。例えば`sequence.py`には座標圧縮・LIS・転倒数がある。複数の解答・旧テンプレートから同名クラスを重ねて貼ることは避ける。

機能だけを展開したいときは[機能別Live Template 274件](LIVE_TEMPLATES.md)を使う。`compress_sequence`、`lis_length`、`inversion_count`のように公開関数・クラスごとに分割し、必要な補助定義を同梱する。元Fileの実装を更新したら、[登録スクリプト](LOCAL_USAGE.md#live-templateへの登録と更新)でLive側も更新する。

ローカル開発ではリポジトリ直下をプロジェクトルートにして、次のようなimportも可能。

```python
from cp_snippet_palette.library.basic.sequence import compress, lis_length

ids, original = compress([40, 10, 40])  # [1, 0, 1], [10, 40]
print(lis_length([3, 1, 2, 5]))        # 3
```

提出時は上のimport行を、パレットからコピーしたファイルのコードに置き換える。

## 使い方の説明の読み方

全92ファイル（library 76＋snippets 16）の先頭に、入力と期待する出力を示した実行例を掲載した。各公開関数・クラス・メソッドのdocstringには、用途・引数・戻り値・境界条件を記載している。PyCharmでもソース内の同じ説明を読める。

入力の型と形もdocstringで確認する。例えば、重み付き隣接リストは`graph[u] = [(v, cost), ...]`、辺リストは`edges = [(u, v, cost), ...]`、GF(2)行列は「整数のbit jが列j」という形式で示す。計算量のN・M・σなどは、入力の長さ・辺数・異なる値数のどれを指すかを明記した。構築と操作、最悪・償却・期待時間を区別し、多倍長整数やコールバックのコストも必要な箇所に記載している。メソッド共通の型・添字の範囲・記号はクラスの説明へまとめている。

[全92ファイルのアルゴリズム解説](ALGORITHMS.md)には、発想・不変条件・正しさの要点・計算量・適用条件をまとめた。青レベルを前提に基本用語は省き、派生版は共通の仕組みと差分を説明している。F2では使用例、選択ファイルの解説、逆引き・verify、公開APIの順に読める。解説文は`ALGORITHMS.md`へ集約しており、提出用コードのコピーには含まれない。

例えば`Doubling`なら、次の例から「遷移先の列で構築し、jumpで問い合わせる」「終端に着くと-1」と分かる。

```python
db = Doubling([1, 2, -1], max_steps=10)
db.jump(0, 2), db.jump(0, 3)  # => (2, -1)
```

使用例は通常のPythonコードで、期待する戻り値を`# => 値`のコメントに記載している。画面に結果を出したい場合は、その式を`print(...)`で囲む。全ファイルに必要なimport・補助クラスを含んでいるので、File全体をコピーしてから例の呼び出し部分を使う。

コールバックが必要な処理には定義一式を載せた。`lazy_segtree.py`は区間加算・区間和と更新の合成順、`hld.py`は頂点値・辺値の格納位置、`rerooting.py`は最大距離・距離和、`mo.py`は状態の追加・削除、`aggregate_queue.py`は非可換な一次関数合成を扱う。

## 共通の約束

- 頂点・添字・順位APIはすべて0-indexed。区間・長方形は半開区間。入力が1-indexedなら読み込み時に変換する。
- 原則として入力配列を変更しない。構造へのadd/set、最大流・最小費用流の残余グラフ更新などはそのオブジェクトを変更する。
- 数値関数は通常のintを使う。MODやINFを解答側のグローバル変数から暗黙に参照しない。FPS・多項式補助関数は998244353固定。畳み込みだけはFFT(MOD)で素数の法を指定する。
- 最短路の`inf`は既定`1<<60`。問題の有限距離の上限より大きい値を渡す。Codonでは加算途中のオーバーフローにも注意する。
- 不正な範囲は原則IndexError、満たせない前提はValueError。高速な既存部品にはassertによる前提検査もある。ホットループ内で全入力の検査を行う設計にはしていない。
- 木専用関数には連結な無向木を渡す。負辺を使えるのはBellman–Ford等、説明で対応が明記されたものに限る。

LCATreeは頂点0..N-1、既定の根は0。WaveletMatrixのkth_smallest/kth_largest/selectと、FullyIndexableDictionary.selectはすべて順位0から数える。LinkedListの実ノードIDは0から発行し、先頭前の番兵は-1。旧来の1-indexed呼び出しには対応しない。

LiChaoIntの整数定義域も[xmin,xmax)の半開区間。直線がなければLiChaoTreeと同じくNone。AVLはkth/ge/ltを使い、存在しないキーの添字アクセスはKeyError、get(key,default)はdefaultを返す。

## PyPyとCodon

実行確認は**Windows版PyPy 7.3.23 / Python 3.11.15**で行った。uvで`D:\Kyopro\.python\pypy-3.11.15-windows-x86_64-none`に用意している。PyCharm用の既存CPython仮想環境は引き続き検索ツールの起動に使う。

AtCoder公式の言語テスト環境にはPyPy 3.11-v7.3.20、Codon 0.19.3が掲載されている。手元のPyPyとはパッチ版とOSが異なり、AtCoderへの提出・AC判定は今回行っていない。[AtCoder公式の実行環境](https://atcoder.jp/contests/language-test-202505/rules)

Codonは通常のintが64bitで、CPython/PyPyと完全に同じ処理系ではない。このPCにはCodon/WSL環境がないため、**全ファイルともCodonのコンパイル確認は未実施**。次の区分は移植時の判断材料であり、動作保証のラベルではない。[Codon公式FAQ](https://docs.exaloop.io/start/faq/)

| 扱い | 対象・注意 |
|---|---|
| 共通化しやすい処理 | 配列主体の累積和、行列、ダブリング、最短路など。列・辞書の型を揃え、中間の乗算も64bitに収める。 |
| PyPy用として使う処理 | 任意精度bitset、subset_sum_bits、大きなGF(2)行列、彩色数の包除原理、64bit整数のPollard rho/Miller–Rabin。通常intのままCodonへ移すと結果が変わり得る。 |
| 個別の移植確認が必要 | Generic/NamedTupleを使う既存構造、Optionalを含む戻り値、コールバック型、Fraction、Modint、FPSの演算子オーバーロード、SA-ISの内部関数。まずPyPyで使う。 |
| 二重Rolling Hash | 約10^9の法を2つ使用。約2^61の法を掛け合わせる実装を避けた。衝突の可能性は残る。 |

DFS系はSCC・HLD・LowLink・重心分解・最大流などで非再帰を採用。再帰を残した範囲更新/KD-treeは深さO(log n)、ゲーム木は指定depth、XOR minimaxはbit幅に比例する。再帰上限やpypyjit設定を読み込み時に変更しない。

## 使い方の例

```python
# prefix_sum_2d.pyを貼る
p = prefix_sum_2d([[1, 2, 3], [4, 5, 6]])
print(rectangle_sum(p, 0, 1, 2, 3))  # 16

# shortest_paths.pyを貼る
g = weighted_adjlist(3, [(0, 1, 2), (1, 2, 3)], directed=True)
dist, parent = dijkstra(g, 0)
print(dist[2], restore_path(parent, 0, 2))  # 5 [0, 1, 2]

# range_arithmetic.pyを貼る
seg = ArithmeticSegmentTree([0] * 5)
seg.add(1, 4, first=2, step=3)  # [0, 2, 5, 8, 0]
print(seg.sum(0, 5))           # 15

# polynomial.pyを貼る。sizeは係数の個数。
print(fps_inverse([1, -1], 5))  # [1, 1, 1, 1, 1]
```

## 目的から探す逆引き

表は17分野・234用途で、同梱の全92ファイルを網羅する。GUIでは同じ234用途を「配列・集合」「グラフ・木」「文字列」「整数・数式」「グリッド・幾何」「DP・探索」の6分類から段階的に絞り込む。[操作手順](LOCAL_USAGE.md#名前が分からないときは目的から探す)を参照。

まず「更新があるか」「位置や順序も変わるか」「クエリを先読みできるか」で絞り、表のAPI・ファイルを選ぶ。リンク先のファイル先頭には、そのまま試せる使用例がある。パレットでは「目的から探す」（F6）で6分類から対象・目的・条件を順に選べる。この節は目的ナビの「一覧ガイド」から開く。APIのリンクを押すと、そのFileを選択して使い方を表示する。

検索欄には表の「検索語」を入力する。名前を思い出せなくても、例えば`一点加算 区間和`、`過去のキュー 分岐`、`負辺 最短路`で探せる。Fileだけに絞るなら先頭に`@file`を付ける。F2には選択中のファイルに対応する逆引き行も表示する。

Nは要素・頂点数、Qはクエリ数。原則0-indexed・半開区間。ここでの案内は実装済みAPIの選択基準であり、Codonでの動作保証ではない。任意精度整数を使う機能はPyPyを前提にする。

[区間の集計と更新](LIBRARY_GUIDE.md#区間の集計と更新) / [セグ木の設定済み派生版](LIBRARY_GUIDE.md#セグ木の設定済み派生版) / [集合と順序統計](LIBRARY_GUIDE.md#集合と順序統計) / [キューと過去の状態](LIBRARY_GUIDE.md#キューと過去の状態) / [二次元とグリッド](LIBRARY_GUIDE.md#二次元とグリッド) / [連結性と制約](LIBRARY_GUIDE.md#連結性と制約) / [距離と経路](LIBRARY_GUIDE.md#距離と経路) / [木の経路と部分木](LIBRARY_GUIDE.md#木の経路と部分木) / [マッチングとフロー](LIBRARY_GUIDE.md#マッチングとフロー) / [文字列](LIBRARY_GUIDE.md#文字列) / [数論と組合せ](LIBRARY_GUIDE.md#数論と組合せ) / [多項式と線形漸化式](LIBRARY_GUIDE.md#多項式と線形漸化式) / [行列とXOR](LIBRARY_GUIDE.md#行列とXOR) / [数列と部分集合DP](LIBRARY_GUIDE.md#数列と部分集合DP) / [幾何](LIBRARY_GUIDE.md#幾何) / [最適化と小規模探索](LIBRARY_GUIDE.md#最適化と小規模探索) / [ABCの頻出パターン](LIBRARY_GUIDE.md#ABCの頻出パターン)

最初の分岐だけをまとめると、次のとおり。

- 配列の和：更新なしは累積和、一点加算はfenwick_tree、区間更新はlazy_segtree、挿入・削除・順序反転はDynamicSequence。
- 二次元の和：密な静的格子は二次元累積和、更新座標を登録できる点群はOfflineFenwick2D、座標が後から分かる場合はDynamicFenwickTree2D。
- 順位：更新のない配列区間はWaveletMatrix、集合全体の追加・削除はSortedMultiset、整数のXORはBinaryTrie。
- 連結性：追加のみはdsu、操作の取り消しはRollbackDSU、有向の相互到達はscc。
- 木：部分木を配列化するならEuler Tour、経路の値を集約するならHLD、全頂点を根にしたDPならrerooting。
- 割当：費用なしの最大個数は二部マッチング、費用行列から全行を割り当てるならassignment、容量と費用を持つ輸送はmcf_graph。


### 区間の集計と更新

| やりたいこと | API・ファイル | 選ぶ条件・使い分け | 検索語 |
|---|---|---|---|
| <!-- navigator: 配列・集合 > 区間を集計する > 和・二乗和・積の和 --> 一点を加算して区間の合計を知りたい | [fenwick_tree.add / sum](snippets/structures/BIT.py) | 長さが固定の配列。点加算・区間和O(log N)。区間をまとめて更新するなら次のlazy_segtree。 | `一点加算 区間和` |
| <!-- navigator: 配列・集合 > 区間を集計する > 演算を自分で定義する --> 一点を書き換えて区間の最小値・最大値・GCDを知りたい | [segtree.set / prod](snippets/structures/segtree.py) | 結合則と単位元を指定。和も扱えるが、単純な点加算・和ならfenwick_treeが軽い。 | `一点更新 区間最小` |
| <!-- navigator: 配列・集合 > 区間を集計する > 演算を自分で定義する --> 条件を満たす最長の区間端を探したい | [segtree.max_right / min_left](snippets/structures/segtree.py) | 区間を伸ばすと条件が真→偽に変わり、単位元で真になること。和の閾値なら要素非負が必要。 | `区間 境界探索` |
| <!-- navigator: 配列・集合 > 区間を集計する > 演算を自分で定義する --> 区間をまとめて加算・代入・一次変換したい | [lazy_segtree.apply / prod](snippets/structures/lazy_segtree.py) | 要素位置は固定。集約・更新・更新の合成を定義できる場合。区間和には要素数も持たせる。 | `区間更新 区間和` |
| <!-- navigator: 配列・集合 > 区間を集計する > 最小値・最大値・順位 --> 区間内の各値を上限・下限で切り詰めたい | [SegmentTreeBeats.chmin / chmax / sum](snippets/structures/SegmentTreeBeats.py) | chmin・chmax・加算・代入と和。普通のlazy_segtreeで最小・最大と和だけを持つ方式では足りない。 | `区間 chmin chmax` |
| <!-- navigator: 配列・集合 > 区間を集計する > 添字に応じて更新する --> 2,5,8のような等差数列を区間に加えたい | [ArithmeticSegmentTree.add / assign / sum](library/structures/range_arithmetic.py) | firstは区間左端に加える値、stepは隣同士の差。代入も可能。各操作O(log N)。 | `等差数列 区間加算` |
| <!-- navigator: 配列・集合 > 順序を変える・キューを扱う > 挿入・削除・反転する --> 配列の途中に挿入・削除しながら区間を集計したい | [DynamicSequence.insert / erase / prod](library/structures/dynamic_sequence.py) | Implicit Treap。位置がずれる数列に使う。各操作は期待O(log N)、mod=0なら整数の和。 | `途中挿入 区間和` |
| <!-- navigator: 配列・集合 > 順序を変える・キューを扱う > 挿入・削除・反転する --> 区間を反転しながら一次変換・区間和を処理したい | [DynamicSequence.reverse / apply / prod](library/structures/dynamic_sequence.py) | reverse(l,r)は要素の並びを逆転。apply(l,r,a,b)は各値をa*x+bへ変換。添字は0始まり。 | `区間反転 区間和` |
| <!-- navigator: 配列・集合 > 区間を集計する > 個数・種類数・k番目 --> 更新のない区間でk番目に小さい値を知りたい | [WaveletMatrix.kth_smallest](library/structures/wavelet_matrix.py) | 構築後の点更新は不可。kは0始まり。同じ配列への多数のクエリ向け。 | `更新なし 区間k番目` |
| <!-- navigator: 配列・集合 > 区間を集計する > 個数・種類数・k番目 --> 区間内の特定の値の個数やx未満の個数を知りたい | [WaveletMatrix.count / count_less](library/structures/wavelet_matrix.py) | 静的配列用。長さσの値域を圧縮し、基本クエリO(log σ)。 | `区間 出現数` |
| <!-- navigator: 配列・集合 > 区間を集計する > 個数・種類数・k番目 --> 区間内に何種類の値があるか知りたい | [range_count_distinct](library/structures/offline_queries.py) | 配列の更新なし、全クエリを先に渡せる場合。答えは入力順。O((N+Q)log N)。 | `区間 種類数` |
| <!-- navigator: 配列・集合 > 区間を集計する > 個数・種類数・k番目 --> 区間の要素を1つ足す・外す処理なら書ける | [mo_solve / mo_order](library/structures/mo.py) | 更新なしのオフラインクエリ。種類数だけならrange_count_distinct。左右で処理が異なる場合はmo_order。 | `区間 オフライン Mo` |
| <!-- navigator: 配列・集合 > 区間を集計する > 最小値・最大値・順位 --> 一定幅の窓の最小値を全部求めたい | [sliding_min](library/basic/sliding_window.py) | 静的配列を1回走査、O(N)。任意区間を繰り返し問い合わせる場合はsegtree等。 | `固定幅 窓 最小値` |
| <!-- navigator: 配列・集合 > 区間を集計する > 和・二乗和・積の和 --> 平方分割で区間加算と区間和を扱いたい | [SqrtDecomposition.add / sum](library/structures/sqrt_decomposition.py) | 単純なバケット実装が欲しい場合。各操作O(√N)。多数の更新にはlazy_segtreeも検討。 | `平方分割 区間和` |
| <!-- navigator: 配列・集合 > 区間を集計する > 和・二乗和・積の和 --> 巨大な添字範囲の一部だけ更新したい | [DynamicFenwickTree](library/structures/dynamic_fenwick.py) | 添字の上限nは既知、実際に更新する座標は未確定でもよい。必要なノードだけ辞書へ保存。 | `疎な配列 点加算` |
| <!-- navigator: 配列・集合 > 区間を集計する > 最小値・最大値・順位 --> 配列を最小値を根とする木に分解したい | [CartesianTree](library/structures/cartesian_tree.py) | 元の順序を保った最小Cartesian Tree。O(N)でroot/parent/left/rightを得る。RMQそのもののAPIではない。 | `最小値 CartesianTree` |

### セグ木の設定済み派生版

演算・単位元・遅延更新の定義を省いて使える33種類。[設計と使用例の一覧](SEGTREE_RECIPES.md)も参照。set/getには元の要素を渡し、prodの戻り値は各行のとおり。

| やりたいこと | 使うもの | 選ぶ条件・使い分け | 検索語 |
|---|---|---|---|
| <!-- navigator: 配列・集合 > 区間を集計する > 和・二乗和・積の和 --> 点代入して和を取る | [range_sum(V)](library/structures/segtree_monoids.py) | 和。空は0。 | `点代入して和を取る` |
| <!-- navigator: 配列・集合 > 区間を集計する > 最小値・最大値・順位 --> 点代入して最小値を取る | [range_min(V)](library/structures/segtree_monoids.py) | 最小値。空はinf。 | `点代入して最小値を取る` |
| <!-- navigator: 配列・集合 > 区間を集計する > 最小値・最大値・順位 --> 点代入して最大値を取る | [range_max(V)](library/structures/segtree_monoids.py) | 最大値。空は-inf。 | `点代入して最大値を取る` |
| <!-- navigator: 配列・集合 > 区間を集計する > GCD・ビット演算 --> 点代入してGCDを取る | [range_gcd(V)](library/structures/segtree_monoids.py) | 非負GCD。空は0。 | `点代入してGCDを取る` |
| <!-- navigator: 配列・集合 > 区間を集計する > GCD・ビット演算 --> 点代入してXORを取る | [range_xor(V)](library/structures/segtree_monoids.py) | XOR。空は0。 | `点代入してXORを取る` |
| <!-- navigator: 配列・集合 > 区間を集計する > GCD・ビット演算 --> 点代入してORを取る | [range_or(V)](library/structures/segtree_monoids.py) | OR。空は0。 | `点代入してORを取る` |
| <!-- navigator: 配列・集合 > 区間を集計する > GCD・ビット演算 --> 点代入してANDを取る | [range_and(V)](library/structures/segtree_monoids.py) | AND。空は-1。 | `点代入してANDを取る` |
| <!-- navigator: 配列・集合 > 区間を集計する > 最小値・最大値・順位 --> 最小値が何個あるか数える | [range_min_count(V)](library/structures/segtree_monoids.py) | (最小値,個数)。空は(inf,0)。 | `最小値が何個あるか数える` |
| <!-- navigator: 配列・集合 > 区間を集計する > 最小値・最大値・順位 --> 最大値が何個あるか数える | [range_max_count(V)](library/structures/segtree_monoids.py) | (最大値,個数)。空は(-inf,0)。 | `最大値が何個あるか数える` |
| <!-- navigator: 配列・集合 > 区間を集計する > 最小値・最大値・順位 --> 2番目に大きい値・個数を取る | [range_top2(V)](library/structures/segtree_monoids.py) | (最大値,個数,異なる第2位,個数)。欠けた値はNone、個数0。 | `第2位 個数` |
| <!-- navigator: 配列・集合 > 区間を集計する > 和・二乗和・積の和 --> 最大部分配列和を取る | [range_max_subarray(V,allow_empty=True)](library/structures/segtree_monoids.py) | (sum,prefix,suffix,best)。空は(0,0,0,0)。Falseなら最大値3つが-inf。 | `最大部分配列和を取る` |
| <!-- navigator: 配列・集合 > 区間を集計する > 括弧・0と1・数字列 --> 括弧の点変更・交換と区間判定 | [range_brackets(V)](library/structures/segtree_monoids.py) | (balance,min_prefix,max_prefix)。空は(0,0,0)。 | `括弧の点変更・交換と区間判定` |
| <!-- navigator: 配列・集合 > 区間を集計する > 関数・行列を合成する --> 一次関数を左から順に合成する | [range_affine_composite(V,mod=998244353)](library/structures/segtree_monoids.py) | (a,b)。空は恒等関数(1,0)。 | `一次関数を左から順に合成する` |
| <!-- navigator: 配列・集合 > 区間を集計する > 関数・行列を合成する --> 2×2行列の積を取る | [range_matrix_product(V,mod=998244353)](library/structures/segtree_monoids.py) | (a00,a01,a10,a11)。空は単位行列。 | `2×2行列の積を取る` |
| <!-- navigator: 配列・集合 > 区間を集計する > GCD・ビット演算 --> 区間から選ぶ部分集合XORを最大化する | [range_xor_basis(V,bits=60)](library/structures/segtree_monoids.py) | 正規化した線形基底tuple。空は()。 | `部分集合XOR 基底` |
| <!-- navigator: 配列・集合 > 区間を集計する > 演算を自分で定義する --> 単位元を作りにくい結合的演算を使う | [semigroup_segtree(V,OP)](library/structures/segtree_monoids.py) | OPの集約値。空はNone。 | `半群 単位元` |
| <!-- navigator: 配列・集合 > 区間を集計する > 和・二乗和・積の和 --> 区間加算・区間和 | [range_add_sum(V)](library/structures/lazy_segtree_actions.py) | f=加算量。prodは和、空0。 | `区間加算・区間和` |
| <!-- navigator: 配列・集合 > 区間を集計する > 和・二乗和・積の和 --> 区間代入・区間和 | [range_assign_sum(V)](library/structures/lazy_segtree_actions.py) | f=代入値。prodは和、空0。 | `区間代入・区間和` |
| <!-- navigator: 配列・集合 > 区間を集計する > 和・二乗和・積の和 --> 加算・乗算・代入を混ぜて区間和 | [range_affine_sum(V,mod=998244353)](library/structures/lazy_segtree_actions.py) | f=(a,b)でx←a*x+b。prodは和、空0。 | `加算・乗算・代入を混ぜて区間和` |
| <!-- navigator: 配列・集合 > 区間を集計する > 最小値・最大値・順位 --> 区間加算・最小値 | [range_add_min(V)](library/structures/lazy_segtree_actions.py) | f=加算量。prodは最小値、空inf。 | `区間加算・最小値` |
| <!-- navigator: 配列・集合 > 区間を集計する > 最小値・最大値・順位 --> 区間加算・最大値 | [range_add_max(V)](library/structures/lazy_segtree_actions.py) | f=加算量。prodは最大値、空-inf。 | `区間加算・最大値` |
| <!-- navigator: 配列・集合 > 区間を集計する > 最小値・最大値・順位 --> 区間加算・最小値の個数 | [range_add_min_count(V)](library/structures/lazy_segtree_actions.py) | f=加算量。prodは(最小値,個数)、空(inf,0)。 | `区間加算・最小値の個数` |
| <!-- navigator: 配列・集合 > 区間を集計する > 最小値・最大値・順位 --> 負の倍率を含む一次変換とmin/max | [range_affine_minmax(V)](library/structures/lazy_segtree_actions.py) | f=(a,b)。prodは(min,max)、空(inf,-inf)。 | `負の倍率を含む一次変換とmin/max` |
| <!-- navigator: 配列・集合 > 区間を集計する > 最小値・最大値・順位 --> chmin・chmax・代入とmin/max | [range_clamp_minmax(V)](library/structures/lazy_segtree_actions.py) | f=(lo,hi)、lo<=hi。prodは(min,max)、空(inf,-inf)。 | `chmin・chmax・代入とmin/max` |
| <!-- navigator: 配列・集合 > 区間を集計する > 括弧・0と1・数字列 --> 0/1反転・転倒数 | [range_flip_inversions(V)](library/structures/lazy_segtree_actions.py) | f=Trueで反転。prodは(zeros,ones,inversions)、空(0,0,0)。 | `ビット反転 転倒数` |
| <!-- navigator: 配列・集合 > 区間を集計する > 括弧・0と1・数字列 --> 0/1反転・代入・最長連続長 | [range_binary_runs(V)](library/structures/lazy_segtree_actions.py) | f=(to0,to1)。prodは(n,p0,s0,b0,p1,s1,b1)、空は全て0。 | `連続ビット 反転` |
| <!-- navigator: 配列・集合 > 区間を集計する > 括弧・0と1・数字列 --> 括弧を区間で交換して正当性を判定 | [range_flip_brackets(V)](library/structures/lazy_segtree_actions.py) | f=Trueで'('と')'を交換。prodは(balance,min_prefix,max_prefix)。空(0,0,0)。 | `括弧を区間で交換して正当性を判定` |
| <!-- navigator: 配列・集合 > 区間を集計する > 和・二乗和・積の和 --> 一次変換・和と二乗和 | [range_affine_sum_squares(V,mod=998244353)](library/structures/lazy_segtree_actions.py) | f=(a,b)。prodは(sum,sum_square)、空(0,0)。 | `二乗和 区間更新` |
| <!-- navigator: 配列・集合 > 区間を集計する > 和・二乗和・積の和 --> 2列へ加算して積の総和 | [range_pair_add_product(V,mod=998244353)](library/structures/lazy_segtree_actions.py) | Vは(A[i],B[i])の列。f=(da,db)。prodは(sumA,sumB,sumAB)、空(0,0,0)。 | `二列 積の和` |
| <!-- navigator: 配列・集合 > 区間を集計する > 添字に応じて更新する --> 添字に比例する加算・代入と区間和 | [range_index_affine_sum(V,mod=0)](library/structures/lazy_segtree_actions.py) | f=(a,b,c)でA[i]←a*A[i]+b*i+c。prodは和、空0。 | `添字 一次変換` |
| <!-- navigator: 配列・集合 > 区間を集計する > 括弧・0と1・数字列 --> 数字列を区間代入して数値化 | [range_digit_assign(V,mod=998244353,base=10)](library/structures/lazy_segtree_actions.py) | f=数字。prodはその区間を読んだ数値mod mod、空0。 | `数字列 区間代入` |
| <!-- navigator: 配列・集合 > 区間を集計する > 和・二乗和・積の和 --> 区間代入・最大部分配列和 | [range_assign_max_subarray(V,allow_empty=True)](library/structures/lazy_segtree_actions.py) | f=代入値。prodは(sum,prefix,suffix,best)。空の扱いは通常版と同じ。 | `区間代入・最大部分配列和` |
| <!-- navigator: 配列・集合 > 区間を集計する > GCD・ビット演算 --> 区間加算・GCD | [range_add_gcd(V)](library/structures/lazy_segtree_actions.py) | f=加算量。prodは非負GCD、空0。set/getは符号付き整数。 | `区間加算 GCD` |

### 集合と順序統計

| やりたいこと | API・ファイル | 選ぶ条件・使い分け | 検索語 |
|---|---|---|---|
| <!-- navigator: 配列・集合 > 値の集合を管理する > 順位・前後の値・辞書 --> 値の追加・削除と前後の値の検索をしたい | [SortedSet.add / discard / lt / ge](library/structures/sorted_set.py) | 重複しない順序付き集合。s[k]は小さい順0始まり。更新・順位操作O(√N)。 | `順序付き集合 前後` |
| <!-- navigator: 配列・集合 > 値の集合を管理する > 順位・前後の値・辞書 --> 重複を残して順位や中央値を求めたい | [SortedMultiset](library/structures/sorted_set.py) | 重複を保持する。s[k]、bisect_left(x)、bisect_right(x)で順位を扱う。中央値ならs[(len(s)-1)//2]等。 | `多重集合 中央値` |
| <!-- navigator: 配列・集合 > 値の集合を管理する > 順位・前後の値・辞書 --> キー順に探索できる辞書が欲しい | [AVLTree](library/structures/avl_tree.py) | key→value。kth(k)は値でなくキー。更新・探索O(log N)。重複キーは上書き。 | `順序付き辞書` |
| <!-- navigator: 配列・集合 > 値の集合を管理する > 小さい順の和・絶対値の和 --> 小さい方からk個の合計を更新したい | [PrioritySumStructure.add / discard / query](library/structures/priority_sum.py) | 数値の多重集合。queryはO(1)、add/discardは償却O(log N)。set_kのコストは移動する要素数による。 | `小さいk個 合計` |
| <!-- navigator: 配列・集合 > 値の集合を管理する > 小さい順の和・絶対値の和 --> 大きい方からk個の合計を更新したい | [PrioritySumStructure](library/structures/priority_sum.py) | 値を符号反転して登録し、query結果も符号反転する。全体の順位検索はSortedMultisetを使う。 | `大きいk個 合計` |
| <!-- navigator: 配列・集合 > 値の集合を管理する > XOR・bit集合 --> 整数集合の中からxとのXORが最小の要素を探したい | [BinaryTrie.min_xor](library/structures/binary_trie.py) | 返すのは要素そのものではなく最小XOR値。元の要素は結果^x。重複可、各操作O(bits)。 | `XOR 最小` |
| <!-- navigator: 配列・集合 > 値の集合を管理する > 順位・前後の値・辞書 --> 整数の追加・削除とk番目・x未満の個数を扱いたい | [BinaryTrie.kth / count_less](library/structures/binary_trie.py) | 0以上2**bits未満の整数専用。kは0始まり。集合として使うなら重複登録を避ける。 | `整数集合 順位` |
| <!-- navigator: 配列・集合 > 値の集合を管理する > 最大値・最小値を取り出す --> 任意の値を削除できる最小ヒープが欲しい | [Heapq.push / discard / top / pop](snippets/structures/Heapq.py) | discard(x)は同じ値を1個削除。遅延削除なので内部配列を直接読まない。単純なpush/popだけならheapq。 | `削除可能 最小ヒープ` |
| <!-- navigator: 配列・集合 > 値の集合を管理する > 最大値・最小値を取り出す --> IDごとの値を更新して最大を取りたい | [MaxQueue.set / discard / top](library/structures/max_queue.py) | キーごとに1個の値を保持。同じキーのsetは上書き。最大側を扱うID付きキュー。 | `ID更新 最大値` |
| <!-- navigator: 配列・集合 > 値の集合を管理する > XOR・bit集合 --> 0/1集合をbit単位で保持・シフトしたい | [BitSet.set / count / shifted / indices](library/structures/bit_set.py) | 固定ビット幅。多倍長整数を使うため大きな幅はPyPy向け。 | `ビット集合 シフト` |

### キューと過去の状態

| やりたいこと | API・ファイル | 選ぶ条件・使い分け | 検索語 |
|---|---|---|---|
| <!-- navigator: 配列・集合 > 順序を変える・キューを扱う > 両端操作と全体の集計 --> 両端操作に加えて添字アクセスもしたい | [Deque](snippets/structures/Deque.py) | リングバッファ。整数添字のアクセスO(1)。添字アクセス不要なら標準collections.dequeでよい。 | `両端キュー 添字` |
| <!-- navigator: 配列・集合 > 順序を変える・キューを扱う > 両端操作と全体の集計 --> 窓の中の値の種類数を保ちたい | [KindDeque](snippets/structures/KindDeque.py) | 両端の追加・削除と出現数を追跡。固定した配列への多数の区間種類数はoffline_queries。 | `キュー 種類数` |
| <!-- navigator: 配列・集合 > 順序を変える・キューを扱う > 両端操作と全体の集計 --> キュー全体のGCD・最小値・関数合成を保ちたい | [AggregateQueue.append / popleft / prod](library/structures/aggregate_queue.py) | 末尾追加・先頭削除だけ。結合的なopと単位元eが必要、逆元は不要。操作は償却O(1)回のop。 | `キュー 全体集約` |
| <!-- navigator: 配列・集合 > 順序を変える・キューを扱う > 両端操作と全体の集計 --> 両端を追加・削除しながら全体を集約したい | [AggregateDeque](library/structures/aggregate_deque.py) | appendleft/append/popleft/pop/prod。関数合成のような非可換演算にも対応。 | `両端 集約` |
| <!-- navigator: 配列・集合 > 過去の状態へ戻る・分岐する --> 過去のキューから分岐して操作したい | [PersistentQueue.append / popleft](library/structures/persistent_queue.py) | 版0が空。append(version,x)は新しい版番号、popleft(version)は(版番号,削除値)。古い版も残る。 | `過去のキュー 分岐` |
| <!-- navigator: グラフ・木 > 過去の連結状態へ戻る --> 連結操作をDFSの帰りに取り消したい | [RollbackDSU.snapshot / rollback / undo](library/structures/rollback_dsu.py) | 経路圧縮なし。snapshotは履歴長。オンラインで任意の過去版を自由に参照する永続dsuとは異なる。 | `連結 巻き戻し` |
| <!-- navigator: グラフ・木 > 過去の連結状態へ戻る --> 版ごとに分岐するUnion-Findの問い合わせを処理したい | [RollbackDSU](library/structures/rollback_dsu.py) | 版の木を作ってDFSできる場合。LC persistent_unionfindのアダプターが例。 | `版 分岐 UnionFind` |
| <!-- navigator: 配列・集合 > 順序を変える・キューを扱う > 挿入・削除・反転する --> ノードIDを指定して隣へ挿入・削除したい | [LinkedList.insert_after / erase](library/structures/linked_list.py) | 実ノードIDは0始まり。追加時のIDを保存して使う。insert_after(-1,x)は先頭挿入。位置iの探索は速くない。 | `ID指定 挿入削除` |

### 二次元とグリッド

| やりたいこと | API・ファイル | 選ぶ条件・使い分け | 検索語 |
|---|---|---|---|
| <!-- navigator: グリッド・幾何 > 長方形の中を集計する --> 更新のない格子で長方形の合計を知りたい | [prefix_sum_2d / rectangle_sum](library/basic/prefix_sum_2d.py) | 前計算O(HW)、各和O(1)。引数は(top,left,bottom,right)、右下を含まない。 | `更新なし 長方形和` |
| <!-- navigator: グリッド・幾何 > 長方形の中を集計する --> 全ての更新座標が分かる点群で長方形和を知りたい | [OfflineFenwick2D.add / sum](library/structures/fenwick_2d.py) | 先に全更新座標を登録。境界座標は未登録でよい。sum(left,bottom,right,top)、各操作O(log² N)。 | `事前登録 長方形和` |
| <!-- navigator: グリッド・幾何 > 長方形の中を集計する --> 更新座標がまだ分からない疎な格子を集計したい | [DynamicFenwickTree2D](library/structures/dynamic_fenwick.py) | 高さ・幅は先に指定。座標は(row,col)、必要な辞書ノードだけ確保。1回O(log H log W)。 | `オンライン 二次元和` |
| <!-- navigator: グリッド・幾何 > 長方形の中を集計する --> 長方形の中にある点のIDを列挙したい | [KDTree.query](library/geometry/kd_tree.py) | 静的点群用。返す点数に比例したコストもかかる。重みの和だけならFenwick2D等。 | `長方形 点列挙` |
| <!-- navigator: グリッド・幾何 > 長方形の中を集計する --> 格子上の全てのh×w領域の最小値を求めたい | [area_min_sliding](library/basic/sliding_window.py) | 長方形のスライド最小値。格子は更新しない。 | `二次元 スライド最小` |
| <!-- navigator: グリッド・幾何 > 長方形の中を集計する --> 障害物のない最大長方形を求めたい | [largest_rectangle_in_grid](library/basic/sliding_window.py) | 真のセルだけからなる長方形の最大面積。0/1の意味を変換して渡す。O(HW)。 | `格子 最大長方形` |
| <!-- navigator: グリッド・幾何 > 盤面を作る・回転する --> 行列の転置・90度回転・添字の平坦化をしたい | [transpose / rotate90 / to_index / to_position](library/basic/grid.py) | rotate90は時計回り。幅widthは列数。新しい格子を返し入力を変えない。 | `格子 回転 転置` |
| <!-- navigator: グリッド・幾何 > 盤面を作る・回転する --> 各行が独立した整数グリッドを作りたい | [make_grid](snippets/structures/make_grid.py) | h×wの整数配列。1行の変更が別の行へ波及しない。 | `グリッド 初期化` |

### 連結性と制約

| やりたいこと | API・ファイル | 選ぶ条件・使い分け | 検索語 |
|---|---|---|---|
| <!-- navigator: グラフ・木 > 連結性・到達可能性を調べる --> 辺を追加して連結かどうかを知りたい | [dsu.merge / same / size / groups](snippets/structures/UnionFind.py) | 追加のみ。ACL形式でmergeは代表頂点を返す。削除・巻き戻しはRollbackDSUと別の処理が必要。 | `連結判定 辺追加` |
| <!-- navigator: グラフ・木 > 値の制約・矛盾を扱う --> 二つの頂点の値の差と矛盾を管理したい | [WeightedUnionFind.merge / diff](snippets/structures/WeightedUnionFind.py) | ポテンシャル差の制約。merge(a,b,w)はpotential[b]-potential[a]=wを設定して代表元を返す。矛盾はValueError。普通の最短路ではない。 | `差分制約 矛盾` |
| <!-- navigator: グラフ・木 > 連結性・到達可能性を調べる --> 有向グラフの相互到達可能な頂点をまとめたい | [scc(N,edges)](library/graphs/scc.py) | 強連結成分。成分順はトポロジカル順。無向の連結判定だけならdsu。 | `相互到達 強連結` |
| <!-- navigator: グラフ・木 > 値の制約・矛盾を扱う --> 二択の条件を同時に満たす割当を求めたい | [two_sat(n,clause)](library/graphs/scc.py) | 1節が2リテラルのOR。clauseの各(i,f,j,g)は(x_i=f) OR (x_j=g)。解なしはNone。 | `二択 条件充足` |
| <!-- navigator: グラフ・木 > 順序・閉路・橋を調べる --> 依存関係を満たす実行順を求めたい | [topological_sort](library/graphs/shortest_paths.py) | 有向グラフ。DAGなら全頂点の順序、閉路があればValueError。 | `依存関係 順序` |
| <!-- navigator: グラフ・木 > 順序・閉路・橋を調べる --> 閉路を実際の頂点・辺の列として取り出したい | [find_cycle](library/graphs/cycle.py) | directed=True/Falseで有向・無向。戻り値(vertices,edge_ids)、閉路なしNone。 | `閉路 復元` |
| <!-- navigator: グラフ・木 > 順序・閉路・橋を調べる --> 切ると分断される辺や頂点を知りたい | [LowLink.bridges / articulation](library/graphs/lowlink.py) | 無向グラフ。bridgesは入力辺ID、articulationは頂点集合。多重辺にも対応。 | `橋 関節点` |
| <!-- navigator: グラフ・木 > 順序・閉路・橋を調べる --> 橋を除いた成分に分解したい | [LowLink.two_edge_connected_components](library/graphs/lowlink.py) | 辺二重連結成分。各頂点はちょうど1成分。橋を成分間の辺とすれば森になる。 | `橋 成分分解` |
| <!-- navigator: グラフ・木 > 順序・閉路・橋を調べる --> 関節点を介する成分のつながりを木にしたい | [LowLink.biconnected_components / block_cut_tree](library/graphs/lowlink.py) | 頂点二重連結成分。関節点は複数成分に属する。block_cut_treeは元頂点と成分頂点の所属関係。 | `関節点 成分 木` |

### 距離と経路

| やりたいこと | API・ファイル | 選ぶ条件・使い分け | 検索語 |
|---|---|---|---|
| <!-- navigator: グラフ・木 > 最短距離・経路を求める --> 非負コストの最短路と経路を求めたい | [dijkstra / restore_path](library/graphs/shortest_paths.py) | 重み付き隣接リストgraph[u]=[(v,cost),...]。dijkstraは(dist,parent)。負辺不可。 | `非負 最短路 復元` |
| <!-- navigator: グラフ・木 > 最短距離・経路を求める --> 重みが0か1だけの最短距離を求めたい | [zero_one_bfs](library/graphs/shortest_paths.py) | 0-1 BFS、O(V+E)。距離配列を返す。全辺1なら標準dequeによるBFSでもよい。 | `0-1 最短距離` |
| <!-- navigator: グラフ・木 > 最短距離・経路を求める --> 負コストの辺を含む最短路を求めたい | [bellman_ford](library/graphs/shortest_paths.py) | 辺リストを渡す。O(VE)なので規模に注意。(dist,negative)で負閉路の影響を区別。 | `負辺 最短路` |
| <!-- navigator: グラフ・木 > 最短距離・経路を求める --> 全頂点の組の距離を求めたい | [floyd_warshall](library/graphs/shortest_paths.py) | O(V³)、距離表O(V²)。頂点数が小さい場合。疎な大グラフは各始点からDijkstra等。 | `全点対 距離` |
| <!-- navigator: グラフ・木 > マッチング・輸送・全体の接続 --> 最小の総辺コストで全頂点をつなぎたい | [minimum_spanning_forest](library/graphs/mst.py) | Kruskal法。重み・採用辺ID・成分数を返す。非連結なら森。最短路木とは目的が異なる。 | `全頂点 接続 最小コスト` |
| <!-- navigator: グラフ・木 > 同じ遷移を繰り返す --> 各頂点から遷移をK回繰り返した先を知りたい | [Doubling.jump](library/basic/doubling.py) | 1頂点につき遷移先が1つの関数グラフ。max_stepsに最大Kを指定。終端は-1。 | `K回 遷移` |

### 木の経路と部分木

| やりたいこと | API・ファイル | 選ぶ条件・使い分け | 検索語 |
|---|---|---|---|
| <!-- navigator: グラフ・木 > 木を扱う > LCA・距離・経路上の頂点 --> 最小共通祖先や木上の距離を求めたい | [HLD.lca / distance](library/graphs/hld.py) | 0-indexedの無向木。distは辺数。値の更新・経路集約にも拡張するならHLDを選ぶ。 | `木 LCA 距離` |
| <!-- navigator: グラフ・木 > 木を扱う > LCA・距離・経路上の頂点 --> 木の経路上でk辺先の頂点を知りたい | [HLD.jump / kth_ancestor](library/graphs/hld.py) | jump(u,v,k)はu→v上、kth_ancestor(u,k)は根方向。範囲外は-1。 | `木 経路 k番目` |
| <!-- navigator: グラフ・木 > 木を扱う > 経路・部分木を集計する --> 木の頂点値を更新して経路の和・合成を求めたい | [HLD / BiSegTree / path_prod](library/graphs/hld.py) | HLD.pos順へ値を並べる。非可換の関数合成でもu→vの順を保持する。 | `木 経路集約` |
| <!-- navigator: グラフ・木 > 木を扱う > 経路・部分木を集計する --> 木の辺の値を経路上で集計したい | [HLD.reorder_by_pos_from_edge_values / path_prod](library/graphs/hld.py) | 辺値を子のposへ置く。根の値を単位元にし、path_prod(...,edge=True)。 | `木 辺の集約` |
| <!-- navigator: グラフ・木 > 木を扱う > 経路・部分木を集計する --> 部分木を連続した配列区間にしたい | [euler_tour](library/graphs/tree.py) | order,tin,tout,parentを返す。部分木は[tin[v],tout[v])。区間の更新・和はfenwick_tree等と組み合わせる。 | `部分木 配列区間` |
| <!-- navigator: グラフ・木 > 木を扱う > 経路・部分木を集計する --> HLD構築済みの木で部分木の範囲を知りたい | [HLD.subtree_range](library/graphs/hld.py) | pos上の(l,r)を返す。頂点自身を含む。別途Euler Tourを作らず同じ配列を使える。 | `HLD 部分木` |
| <!-- navigator: グラフ・木 > 木を扱う > 直径・中心・走査の復元 --> 木の最も離れた2頂点と経路を求めたい | [tree_diameter / weighted_tree_diameter](library/graphs/tree.py) | 前者は重みなし、後者は非負重みの隣接リスト。戻り値は(長さ,頂点経路)。 | `木 直径 経路` |
| <!-- navigator: グラフ・木 > 木を扱う > 直径・中心・走査の復元 --> 最も遠い頂点までの距離を最小にする木の頂点を知りたい | [tree_centers](library/graphs/tree.py) | 重みなし木の中心を1個または2個返す。部分木サイズを均等にする重心とは異なる。 | `木 中心` |
| <!-- navigator: グラフ・木 > 木を扱う > 全方位DP・重心分解 --> 全頂点をそれぞれ根としたDPを計算したい | [rerooting](library/graphs/rerooting.py) | merge、identity、辺をまたぐliftを指定。非再帰O(N)。単位元とコールバック例はファイル先頭。 | `全頂点 根 木DP` |
| <!-- navigator: グラフ・木 > 木を扱う > 全方位DP・重心分解 --> 木を重心で分割して距離クエリの土台を作りたい | [CentroidDecomposition](library/graphs/centroid_decomposition.py) | 重心分解木を構築する部品。距離頻度や動的最寄り頂点の答えは呼び出し側で追加する。 | `重心分解 距離` |
| <!-- navigator: グラフ・木 > 木を扱う > 直径・中心・走査の復元 --> 前順・中順の走査から後順を復元したい | [postorder_from_preorder_inorder](library/graphs/tree.py) | 頂点ラベルは重複なし。返すのは後順列。左右の子配列の復元APIではない。 | `走査順 復元` |
| <!-- navigator: グラフ・木 > 木を扱う > LCA・距離・経路上の頂点 --> ダブリングでLCA・祖先・木上の経路を求めたい | [LCATree](snippets/structures/LCATree.py) | 頂点0..N-1、root=0。辺リストから構築。値の更新・経路集約も必要ならHLDを選ぶ。 | `0-indexed LCA ダブリング` |

### マッチングとフロー

| やりたいこと | API・ファイル | 選ぶ条件・使い分け | 検索語 |
|---|---|---|---|
| <!-- navigator: グラフ・木 > マッチング・輸送・全体の接続 --> 二つのグループをできるだけ多く一対一で結びたい | [bipartite_matching](library/graphs/bipartite_matching.py) | 二部グラフの最大マッチング。左右の相手配列、未対応-1。費用がなければまずこれ。 | `一対一 最大個数` |
| <!-- navigator: グラフ・木 > マッチング・輸送・全体の接続 --> 各行を別々の列へ割り当てて費用を最小にしたい | [assignment](library/graphs/assignment.py) | 費用行列、行数≤列数。負費用可。全行を割り当てるHungarian法、O(n²m)。 | `割当 費用最小` |
| <!-- navigator: グラフ・木 > マッチング・輸送・全体の接続 --> 容量制約の中で最大量を流したい | [mf_graph.add_edge / flow / min_cut](library/graphs/max_flow.py) | 最大流・最小カット。容量は非負。辺ごとの流量を復元するAPIもある。 | `容量 最大流 最小カット` |
| <!-- navigator: グラフ・木 > マッチング・輸送・全体の接続 --> 容量と単価を持つ輸送の最小費用を求めたい | [mcf_graph.add_edge / flow / slope](library/graphs/min_cost_flow.py) | 元の辺費用は非負。flow/slopeは同じ個体で合計1回。負費用やb-flowはそのまま扱えない。 | `輸送 容量 費用` |

### 文字列

| やりたいこと | API・ファイル | 選ぶ条件・使い分け | 検索語 |
|---|---|---|---|
| <!-- navigator: 文字列 > パターン・接頭辞を探す --> 一つのパターンの出現位置を全て知りたい | [kmp_search](library/strings/matching.py) | KMP、O(N+M)。重なりも数える。空パターンは文字間の全位置。 | `パターン 出現位置` |
| <!-- navigator: 文字列 > パターン・接頭辞を探す --> 接頭辞と接尾辞の一致長を知りたい | [prefix_function](library/strings/matching.py) | KMPの失敗関数。pi[i]はその接頭辞の真の接頭辞・接尾辞の最長一致長。 | `接頭辞 接尾辞 一致` |
| <!-- navigator: 文字列 > パターン・接頭辞を探す --> 全ての接尾辞について先頭との一致長を求めたい | [String.z_algorithm](library/strings/suffix_array.py) | Z配列をO(N)で返す。文字列と整数列に対応。 | `先頭との一致長` |
| <!-- navigator: 文字列 > 部分文字列を比較・分類する --> 接尾辞を辞書順に並べたい | [String.suffix_array / lcp_array](library/strings/suffix_array.py) | SAは開始位置の順列、LCPはSA順で隣り合う接尾辞の共通接頭辞長。 | `接尾辞 辞書順` |
| <!-- navigator: 文字列 > 部分文字列を比較・分類する --> 異なる部分文字列の種類数を求めたい | [String.suffix_array / lcp_array](library/strings/suffix_array.py) | 長さNならN*(N+1)//2-sum(lcp)。文字列は更新しない。 | `異なる部分文字列` |
| <!-- navigator: 文字列 > 部分文字列を比較・分類する --> 二つの文字列に共通する最長の連続部分を求めたい | [longest_common_substring](library/strings/suffix_array.py) | 戻り値(a,b,c,d)でs[a:b]==t[c:d]。飛び飛びに選ぶLCSとは異なる。 | `最長共通部分文字列` |
| <!-- navigator: 文字列 > 回文を調べる --> 文字列の各中心の最長回文を求めたい | [manacher](library/strings/matching.py) | 奇数・偶数半径をO(N)で返す。奇数長は2*odd[i]-1、偶数長は2*even[i]。 | `回文 全中心` |
| <!-- navigator: 文字列 > 部分文字列を比較・分類する --> 部分文字列の一致を何度も調べたい | [RollingHash](library/strings/rolling_hash.py) | 二重ハッシュ。静的文字列向け。衝突があり得るので厳密一致が必要ならSA/LCP等を検討。 | `部分文字列 一致 ハッシュ` |
| <!-- navigator: 文字列 > 部分文字列を比較・分類する --> 文字を更新しながら部分文字列を比較したい | [RollingHashSegTree](library/strings/rolling_hash.py) | 一点更新付きハッシュ。回文判定には順方向・逆方向の2本を使う。衝突の可能性は残る。 | `文字更新 ハッシュ` |
| <!-- navigator: 文字列 > パターン・接頭辞を探す --> 登録した単語の完全一致数や接頭辞一致数を知りたい | [Trie.add / count / count_prefix](library/strings/trie.py) | 重複登録可、削除不可。整数のXOR検索にはBinaryTrieを使う。 | `単語 接頭辞 個数` |
| <!-- navigator: 文字列 > パターン・接頭辞を探す --> 多数のパターンの出現回数をまとめて数えたい | [AhoCorasick.count](library/strings/trie.py) | パターン群を先に登録し、テキストを渡す。出現位置一覧ではなく各パターンの回数を返す。 | `複数パターン 出現回数` |
| <!-- navigator: 文字列 > 編集距離・最長共通部分列 --> 挿入・削除・置換の最小回数を求めたい | [edit_distance](library/strings/matching.py) | 編集距離、各コスト1。文字列だけでなく列にも使える。O(NM)。 | `編集距離` |
| <!-- navigator: 文字列 > 編集距離・最長共通部分列 --> 飛び飛びに選べる最長共通部分列の長さが欲しい | [lcs_length](library/strings/matching.py) | LCSの長さ。部分列自体の復元は未対応。最長共通部分文字列と区別する。 | `最長共通部分列` |

### 数論と組合せ

| やりたいこと | API・ファイル | 選ぶ条件・使い分け | 検索語 |
|---|---|---|---|
| <!-- navigator: 整数・数式 > 組合せ・整数分割を数える --> 組合せnCkを何度も計算したい | [Comb](library/math/combinatorics.py) | 素数mod、前計算上限n<mod。階乗・逆階乗を使う。合成数mod用ではない。 | `組合せ 前計算` |
| <!-- navigator: 整数・数式 > 組合せ・整数分割を数える --> nが大きくkだけ小さい組合せを計算したい | [combination_small_k](library/math/combinatorics.py) | O(min(k,n-k))、min(k,n-k)<primeが必要。nまで前計算しない。 | `巨大n 小さいk` |
| <!-- navigator: 整数・数式 > 素数・約数・素因数を求める --> 小さな整数を大量に素因数分解したい | [smallest_prime_factors](library/math/combinatorics.py) | 最大値まで最小素因数表を作り、割り算を繰り返す。表のサイズ分のメモリが必要。 | `大量 素因数分解` |
| <!-- navigator: 整数・数式 > 素数・約数・素因数を求める --> 上限以下の素数を列挙したい | [primes_up_to](library/math/combinatorics.py) | 篩、O(N log log N)時間・O(N)空間。大きな1個の素数判定はfactorize64.is_probable_prime。 | `素数 一覧` |
| <!-- navigator: 整数・数式 > 素数・約数・素因数を求める --> 小さな数の約数・素因数を知りたい | [divisors / factorize_trial](library/math/combinatorics.py) | どちらもO(√N)。大きな64bit整数を試し割りしない。 | `約数 試し割り` |
| <!-- navigator: 整数・数式 > 素数・約数・素因数を求める --> 大きな64bit整数の素数判定・素因数分解をしたい | [is_probable_prime / prime_fact](library/math/factorize64.py) | 符号なし64bit範囲。多倍長の積を使うPyPy向け。Codonの通常intにそのまま移さない。 | `64bit 素因数分解` |
| <!-- navigator: 整数・数式 > 余り・合同式・mod演算 --> 合同式の逆元や最大公約数付き逆元が欲しい | [inv_mod / inv_gcd](library/math/number_theory.py) | inv_modは互いに素のとき。inv_gcdは(gcd,x)。素数modだけに限定されない。 | `合同式 逆元` |
| <!-- navigator: 整数・数式 > 余り・合同式・mod演算 --> 複数の余り条件を同時に満たす整数を求めたい | [crt](library/math/number_theory.py) | 法は正。互いに素でなくても可。最小非負解と周期、解なし(0,0)。 | `余り条件 中国剰余` |
| <!-- navigator: 整数・数式 > 切り捨て・商の総和を求める --> 一次式を割って切り捨てた値の総和を高速に求めたい | [floor_sum](library/math/number_theory.py) | sum((a*i+b)//mod for i in range(n))。a,bは負でも可、O(log mod)。 | `床関数 総和` |
| <!-- navigator: 整数・数式 > 余り・合同式・mod演算 --> aの何乗がbになるかmod上で求めたい | [discrete_log](library/math/number_theory.py) | 最小の非負指数、解なし-1。互いに素でなくても可。O(√mod)で大きな法は重い。 | `離散対数 指数` |
| <!-- navigator: 整数・数式 > 余り・合同式・mod演算 --> 素数mod上で平方根を求めたい | [sqrt_mod](library/math/number_theory.py) | 素数を指定。小さい方の根、存在しなければ-1。整数の平方根とは別。 | `mod 平方根` |
| <!-- navigator: 整数・数式 > 余り・合同式・mod演算 --> 剰余を取る数の四則演算を書きやすくしたい | [ModContext / Modint](library/math/scalar.py) | with ModContext(mod)内で構築。除算には逆元が必要。高速性優先の内側ループは通常intも検討。 | `剰余 四則演算` |

### 多項式と線形漸化式

| やりたいこと | API・ファイル | 選ぶ条件・使い分け | 検索語 |
|---|---|---|---|
| <!-- navigator: 整数・数式 > 多項式・母関数を扱う > 積・逆数・log・exp・累乗 --> 和がkになる組を全てのkについて数えたい | [FFT.convolution](library/math/polynomial.py) | 頻度配列a,bの畳み込み。FFT(998244353).convolution(a,b)、係数は低次から。整数の正確な総数ではなく剰余。 | `和の分布 畳み込み` |
| <!-- navigator: 整数・数式 > 多項式・母関数を扱う > 積・逆数・log・exp・累乗 --> 多項式を掛けたい | [FFT.convolution / FPS](library/math/polynomial.py) | FFTは素数の法と対応NTT長を指定。FPSの法は998244353固定。 | `多項式 積` |
| <!-- navigator: 整数・数式 > 多項式・母関数を扱う > 積・逆数・log・exp・累乗 --> 形式的冪級数の逆数を求めたい | [fps_inverse](library/math/polynomial.py) | a[0]≠0。sizeは係数数で、x**size未満を返す。 | `級数 逆数` |
| <!-- navigator: 整数・数式 > 多項式・母関数を扱う > 積・逆数・log・exp・累乗 --> 形式的冪級数のlog・expを求めたい | [fps_log / fps_exp](library/math/polynomial.py) | logは定数項1、expは定数項0。法998244353固定。 | `級数 対数 指数` |
| <!-- navigator: 整数・数式 > 多項式・母関数を扱う > 積・逆数・log・exp・累乗 --> 形式的冪級数を累乗・平方根にしたい | [fps_power / fps_sqrt](library/math/polynomial.py) | 平方根がなければNone。sizeは係数数。負の指数には定数項非零が必要。 | `級数 累乗 平方根` |
| <!-- navigator: 整数・数式 > 多項式・母関数を扱う > 除算・GCD・評価・補間 --> 多項式を割った商と余りを求めたい | [polynomial_divmod](library/math/polynomial.py) | 戻り値(商list,余りlist)。零多項式は[]、末尾0を取り除く。 | `多項式 商 余り` |
| <!-- navigator: 整数・数式 > 多項式・母関数を扱う > 除算・GCD・評価・補間 --> 多項式のGCDや別の多項式を法とする逆元が欲しい | [polynomial_gcd / polynomial_inverse](library/math/polynomial.py) | GCDはモニック。逆元なしNone、非零定数を法とした場合は[]。FPSの逆数とは別。 | `多項式 GCD 逆元` |
| <!-- navigator: 整数・数式 > 多項式・母関数を扱う > 除算・GCD・評価・補間 --> 多項式を多数の点で評価したい | [FPS.multipoint_evaluation](library/math/polynomial.py) | 同じ多項式fについてf(x_i)を一括計算。戻り値は入力点順のlist。 | `多点評価` |
| <!-- navigator: 整数・数式 > 多項式・母関数を扱う > 除算・GCD・評価・補間 --> 点の値から多項式を復元したい | [polynomial_interpolation](library/math/polynomial.py) | x座標は法上で相異なる。戻り値はFPS、係数は.Funcで取得。 | `多項式 補間` |
| <!-- navigator: 整数・数式 > 多項式・母関数を扱う > 除算・GCD・評価・補間 --> f(x+c)の係数へ平行移動したい | [FPS.taylor_shift](library/math/polynomial.py) | xへcを足すTaylor Shift。係数自体をcだけずらす操作ではない。 | `Taylor Shift 平行移動` |
| <!-- navigator: 整数・数式 > 漸化式・遷移の遠い項を求める --> 数列の先頭から線形漸化式を推定したい | [berlekamp_massey](library/math/linear_recurrence.py) | O(N²)。最短の係数列。未知のd次漸化式の推定には通常2d項以上を用意する。 | `漸化式 推定` |
| <!-- navigator: 整数・数式 > 漸化式・遷移の遠い項を求める --> 次数が小さい線形漸化式の遠い項を求めたい | [linear_recurrence](library/math/linear_recurrence.py) | O(d² log K)、素数modを指定可。係数c[j]はa[t-j-1]に掛かる。 | `漸化式 小さい次数` |
| <!-- navigator: 整数・数式 > 漸化式・遷移の遠い項を求める --> 次数が大きい線形漸化式の遠い項を求めたい | [linear_recurrence_ntt](library/math/polynomial.py) | Bostan–Mori、O(M(d)log K)。998244353固定。先頭d項と長さdの係数を渡す。 | `漸化式 高速 第K項` |
| <!-- navigator: 整数・数式 > 漸化式・遷移の遠い項を求める --> 有理型母関数の遠い係数を求めたい | [bostan_mori](library/math/polynomial.py) | P(x)/Q(x)の[x**n]。引数順は分子・分母・n、Q[0]≠0。 | `母関数 係数取得` |
| <!-- navigator: 整数・数式 > 組合せ・整数分割を数える --> 部分集合和の作り方を全ての和について数えたい | [subset_sum](library/math/polynomial.py) | 非負の重み。各要素を高々1回選び、和0..limitの個数をmodで返す。可能かどうかだけならbitset。 | `部分和 個数 母関数` |
| <!-- navigator: 整数・数式 > 組合せ・整数分割を数える --> 整数分割数やStirling数を計算したい | [partition_function / stirling_first / stirling_second / bernoulli_number](library/math/polynomial.py) | 全て998244353での係数列。第一種Stirling数は符号付き。Bernoulli数はB1=-1/2。 | `分割数 Stirling Bernoulli` |

### 行列とXOR

| やりたいこと | API・ファイル | 選ぶ条件・使い分け | 検索語 |
|---|---|---|---|
| <!-- navigator: 整数・数式 > 漸化式・遷移の遠い項を求める --> 行列を掛ける・累乗して遷移をまとめたい | [matrix_multiply / matrix_power](library/basic/matrix.py) | 二次元list。mod=0は整数、正なら剰余。一般の正方行列累乗はO(N³ log K)。 | `行列 累乗` |
| <!-- navigator: 整数・数式 > 漸化式・遷移の遠い項を求める --> ちょうどK回の遷移で利益を最大化したい | [max_plus_multiply / max_plus_power](library/basic/matrix.py) | 通常の和・積をmax・加算へ置き換える。到達不能の番兵と値の範囲に注意。 | `最大利益 行列` |
| <!-- navigator: 整数・数式 > 行列・連立方程式を解く --> 素数mod上の行列式・階数・逆行列を求めたい | [matrix_det / matrix_rank / inverse_matrix](library/math/linear_algebra.py) | 正方行列の逆行列はO(N³)、特異ならNone。任意の合成数mod用ではない。 | `素数mod 行列式` |
| <!-- navigator: 整数・数式 > 行列・連立方程式を解く --> 一次方程式の特解と自由度を求めたい | [linear_equations](library/math/linear_algebra.py) | 素数mod上。戻り値(特解,同次解の基底)、解なしNone。実数の連立方程式とは別。 | `連立方程式 特解 基底` |
| <!-- navigator: 整数・数式 > 行列・連立方程式を解く --> XOR制約の解と自由変数を求めたい | [linear_equations_gf2](library/math/bit_transforms.py) | 行・特解・基底を整数bitsetで表す。bit jが変数j。任意精度整数を使うPyPy向け。 | `XOR 方程式 基底` |
| <!-- navigator: 整数・数式 > 行列・連立方程式を解く --> 0/1行列の階数・逆行列・積を求めたい | [matrix_rank_gf2 / inverse_matrix_gf2 / matrix_product_gf2](library/math/gf2_matrix.py) | 加算をXORとするGF(2)上の行列。bit jが列j。0/1の通常の整数行列積とは異なる。 | `GF2 行列積 逆行列` |
| <!-- navigator: 整数・数式 > XOR・部分集合の演算 --> 何個か選んでXORした値を最大化したい | [xor_basis / xor_maximum](library/math/bit_transforms.py) | 非負整数のXOR基底を作る。1個の要素とxとの最小XORならBinaryTrie。 | `部分集合 XOR最大` |
| <!-- navigator: 整数・数式 > XOR・部分集合の演算 --> 全要素へ同じxをXORして最大値を最小にしたい | [xor_minimax](library/math/bit_transforms.py) | min_x max(a_i^x)を返す。通常のXOR最大化とは目的が異なる。 | `XOR minimax` |
| <!-- navigator: 整数・数式 > XOR・部分集合の演算 --> XOR・ANDで合成した値の分布を求めたい | [xor_convolution / and_convolution](library/math/bit_transforms.py) | 両配列は同じ長さ2^k。通常の添字和の畳み込みとは別。XOR版は奇数mod。 | `XOR AND 畳み込み` |
| <!-- navigator: 整数・数式 > XOR・部分集合の演算 --> 各集合の全ての部分集合の値を足したい | [subset_zeta](library/math/bit_transforms.py) | 長さ2^k。inverse=Trueでメビウス逆変換。Subset Convolutionそのものは未同梱。 | `部分集合 ゼータ変換` |

### 数列と部分集合DP

| やりたいこと | API・ファイル | 選ぶ条件・使い分け | 検索語 |
|---|---|---|---|
| <!-- navigator: 配列・集合 > 配列を変換・整列する --> 値を順序を保った小さな整数へ変換したい | [compress](library/basic/sequence.py) | 戻り値(ids,original)。元の値はoriginal[ids[i]]。大小関係を保つ。 | `値 座標圧縮` |
| <!-- navigator: 配列・集合 > 配列を変換・整列する --> 最長増加部分列の長さや実際の位置を求めたい | [lis_length / lis_indices](library/basic/sequence.py) | strict=Falseなら非減少。lis_indicesは値ではなく元配列の添字を返す。 | `LIS 復元` |
| <!-- navigator: 配列・集合 > 配列を変換・整列する --> 隣接交換で整列する最小回数を知りたい | [inversion_count](library/basic/sequence.py) | i<jかつa[i]>a[j]の組数。等しい値は転倒に数えない。O(N log N)。 | `隣接交換 転倒数` |
| <!-- navigator: 配列・集合 > 配列を変換・整列する --> 連続する同じ値をまとめたい | [run_length_encode / run_length_decode](library/basic/sequence.py) | [(値,連続数),...]へ変換。文字列以外の列にも使える。 | `連続 同じ値 圧縮` |
| <!-- navigator: 配列・集合 > 区間を集計する > 最小値・最大値・順位 --> 棒グラフの中の最大長方形を求めたい | [largest_rectangle_in_histogram](library/basic/sliding_window.py) | 非負の高さ、棒の幅は1。O(N)。 | `ヒストグラム 最大長方形` |
| <!-- navigator: DP・探索 > 部分集合和・ナップサック --> 要素数が少なく値の総和が大きい部分集合和を扱いたい | [split_and_list / subset_sums](library/basic/subset_dp.py) | 半分全列挙。両半分の和を返すので、目標値への二分探索等は呼び出し側で行う。 | `部分和 半分全列挙` |
| <!-- navigator: DP・探索 > 部分集合和・ナップサック --> ちょうどk個を選ぶ部分集合和を列挙したい | [subset_sums_by_size](library/basic/subset_dp.py) | result[k]がk個選んだ和の列。指数時間なので小さい要素数向け。 | `部分和 個数指定` |
| <!-- navigator: DP・探索 > 部分集合和・ナップサック --> 容量が小さい0/1ナップサックを解きたい | [knapsack_01](library/basic/subset_dp.py) | 品物は(非負整数の重さ,価値)。各品物を高々1個使う。 | `ナップサック 0/1` |
| <!-- navigator: DP・探索 > 部分集合和・ナップサック --> 作れる和だけを高速に判定したい | [subset_sum_bits](library/basic/subset_dp.py) | 戻り値のbit sが1なら和sを作れる。非負の重み、limitまで。個数は数えない。PyPy向け。 | `部分和 到達可能` |

### 幾何

| やりたいこと | API・ファイル | 選ぶ条件・使い分け | 検索語 |
|---|---|---|---|
| <!-- navigator: グリッド・幾何 > 点群・凸包・多角形 --> 整数座標の凸包や凸多角形の内外判定が欲しい | [convex_hull_points / ConvexPolygon.locate](library/geometry/convex.py) | 点は(x,y)タプル。locateは外-1・辺上0・内1。containsは境界込みのbool、contains_strictは内部だけのbool。Point版Polygonと同じ。 | `整数凸包 内外判定` |
| <!-- navigator: グリッド・幾何 > 点群・凸包・多角形 --> 凸包上の最遠点間距離を求めたい | [convex_diameter_sq](library/geometry/convex.py) | 反時計回りの凸包を渡す。距離の二乗を返す。点群からなら先にconvex_hull_points。 | `凸包 最遠点` |
| <!-- navigator: グリッド・幾何 > 点群・凸包・多角形 --> 点・ベクトルの内積・外積・向きを計算したい | [Point.dot / cross / orientation](snippets/geometry/01_point_core.py) | Pointを使う場合の基本部品。後続の幾何スニペットにも同梱されている。 | `ベクトル 内積 外積` |
| <!-- navigator: グリッド・幾何 > 直線・線分・円の交差と距離 --> 直線・線分の交差や距離を求めたい | [Line / Segment](snippets/geometry/02_line_segment.py) | Pointで構築。線分交点はNone/Point/Segment。重なる線分や退化線分も区別する。 | `線分 交点 距離` |
| <!-- navigator: グリッド・幾何 > 点群・凸包・多角形 --> 一般の多角形の面積・内外・切断を扱いたい | [Polygon](snippets/geometry/03_polygon_convex.py) | 周上順のPoint列。locateは内1・境界0・外-1。convex_cutは凸多角形の切断に使う。 | `多角形 面積 切断` |
| <!-- navigator: グリッド・幾何 > 点群・凸包・多角形 --> 点群の一番近い2点の距離を求めたい | [closest_pair_sq](snippets/geometry/04_closest_pair.py) | Pointの列。O(N log N)、距離の二乗だけを返す。点IDの復元は未対応、2点未満None。 | `最近点対 距離` |
| <!-- navigator: グリッド・幾何 > 直線・線分・円の交差と距離 --> 円と直線・円同士の交差を求めたい | [Circle.line_intersections / circle_intersections](snippets/geometry/05_circle.py) | Point中心と半径。交点座標はfloat。同一円はcircle_intersectionsがNoneを返す。 | `円 交点` |
| <!-- navigator: グリッド・幾何 > 直線・線分・円の交差と距離 --> 線分が円周または円盤に触れるか知りたい | [Circle.intersects_segment / intersects_disk_segment](snippets/geometry/05_circle.py) | 前者は円周との交差、後者は内部込みの円盤との交差。線分が円の中だけにある場合に差が出る。 | `円盤 線分` |
| <!-- navigator: グリッド・幾何 > 長方形の重なりの面積 --> 長方形の重なりを一度だけ数えた面積が欲しい | [rectangle_union_area](library/geometry/rectangle_union.py) | 矩形は(left,bottom,right,top)。軸平行、O(N log N)。重み付き矩形和とは別。 | `長方形 和集合 面積` |
| <!-- navigator: グリッド・幾何 > 直線・線分・円の交差と距離 --> 3次元の点から平面までの距離を知りたい | [point_plane_distance](library/geometry/plane_distance.py) | 点と平面を定める3点を(x,y,z)で渡す。平面側3点が共線ならValueError。 | `3次元 平面 距離` |

### 最適化と小規模探索

| やりたいこと | API・ファイル | 選ぶ条件・使い分け | 検索語 |
|---|---|---|---|
| <!-- navigator: DP・探索 > DPを高速化する --> DPのmin(a_j*x+b_j)を高速に計算したい | [LiChaoTree / LiChaoInt](library/structures/li_chao.py) | 問い合わせ座標が先に分かるならLiChaoTree(xs)。未知の整数座標ならLiChaoInt(xmin,xmax)。直線追加・問い合わせの単調性は不要。 | `直線 最小化DP` |
| <!-- navigator: DP・探索 > DPを高速化する --> 区間内だけ有効な直線を追加したい | [LiChaoTree.add_segment](library/structures/li_chao.py) | 問い合わせ座標を先に登録。[l,r)だけ有効、追加O(log² N)。LiChaoIntにはこのAPIはない。 | `区間限定 直線` |
| <!-- navigator: DP・探索 > DPを高速化する --> 絶対値の和で表される凸なDPを管理したい | [SlopeTrick.add_abs / shift / prefix_min](library/structures/slope_trick.py) | 区分線形凸関数。minimumは最小値、argminは最小点の範囲。evaluateは多数の問い合わせ向きではない。 | `絶対値 凸DP` |
| <!-- navigator: DP・探索 > 小さなグラフを厳密に解く --> 小さなグラフの巡回セールスマンを厳密に解きたい | [tsp_cycle](library/graphs/exponential.py) | O(N²2^N)。全頂点を1回ずつ通り始点へ戻る最小費用。大きなNには使わない。 | `TSP 厳密` |
| <!-- navigator: DP・探索 > 小さなグラフを厳密に解く --> 指定した少数の頂点を最小費用でつなぎたい | [steiner_tree](library/graphs/exponential.py) | 非負重みの無向グラフ。端点数に対して指数時間。戻り値は費用のみ、辺の復元は未対応。 | `Steiner木 費用` |
| <!-- navigator: DP・探索 > 小さなグラフを厳密に解く --> 無向グラフの全辺を通る最短巡回が欲しい | [chinese_postman](library/graphs/exponential.py) | 非負重み。奇数次数頂点数に対して指数時間。返すのは費用。 | `全辺 巡回 郵便配達` |
| <!-- navigator: DP・探索 > 小さなグラフを厳密に解く --> 小さなグラフの最大独立集合や彩色数を求めたい | [maximum_independent_set / chromatic_number](library/graphs/exponential.py) | どちらも指数時間。前者は頂点リスト、後者は色数を返す。 | `独立集合 彩色` |
| <!-- navigator: DP・探索 > 近似解・ゲーム探索を行う --> 多数の候補から良さそうな状態を残して探索したい | [beam_search](library/search/heuristics.py) | expand・score・keyを指定。各深さでwidth状態を残す。最適解の保証はない。 | `ビームサーチ` |
| <!-- navigator: DP・探索 > 近似解・ゲーム探索を行う --> 交互手番の零和ゲームで次の手を選びたい | [negamax](library/search/heuristics.py) | 深さ制限付きαβ探索。評価は現在の手番側の視点。状態遷移と評価は自分で定義する。 | `ゲーム αβ` |
| <!-- navigator: DP・探索 > 近似解・ゲーム探索を行う --> 巡回路の近似解を作って改善したい | [tsp_nearest_neighbor / tsp_two_opt](library/search/heuristics.py) | 近傍法で初期解、対称距離なら2-opt。始点を末尾にも含む巡回順。厳密解ではない。 | `TSP 近似 2-opt` |
| <!-- navigator: DP・探索 > 点群の分類・確率を計算する --> 点群をいくつかの集団に分けたい | [kmeans](library/search/numeric.py) | 数値ベクトルをk群へ分ける近似手法。返り値(labels,centers)。最適性や全群非空は保証しない。 | `クラスタ 分類` |
| <!-- navigator: DP・探索 > 点群の分類・確率を計算する --> 正規分布の累積確率を計算したい | [normal_cdf](library/search/numeric.py) | sigmaは標準偏差。floatでP(X<=x)を返す。 | `正規分布 確率` |

### ABCの頻出パターン

[使用例とABCのverify問題](ABC_TOOLKIT.md)も参照。

| やりたいこと | API・ファイル | 選ぶ条件・使い分け | 検索語 |
|---|---|---|---|
| <!-- navigator: グラフ・木 > 同じ遷移を繰り返す --> 同じ遷移を10^18回以上繰り返す | [FunctionalGraph.jump](library/graphs/functional_graph.py) | 次の頂点が必ず1個。閉路部分を剰余で飛ばす。終端-1は既存Doubling。 | `functional graph 巨大回数 遷移` |
| <!-- navigator: グラフ・木 > 同じ遷移を繰り返す --> 一方向の遷移で目的地へ何回で着くか | [FunctionalGraph.distance](library/graphs/functional_graph.py) | 到達不能-1。単なる無向連結性とは異なる。 | `functional graph 到達距離` |
| <!-- navigator: グラフ・木 > 同じ遷移を繰り返す --> 各頂点から到達できる頂点数を数える | [FunctionalGraph.reachable_count](library/graphs/functional_graph.py) | 木部分の長さ＋閉路長。自己到達を含む。分解O(N)、各取得O(1)。 | `functional graph 到達数` |
| <!-- navigator: グラフ・木 > 最短距離・経路を求める --> 複数の始点から最寄りの距離を求める | [multi_source_bfs](library/graphs/graph_recipes.py) | 重みなし隣接リスト。distとparentを返す。 | `複数始点 BFS 最寄り` |
| <!-- navigator: グラフ・木 > 最短距離・経路を求める --> 最短経路が何通りあるか数える | [bfs_path_count](library/graphs/graph_recipes.py) | 重みなし。未到達0通り、平行辺は別経路。mod=0で厳密整数。 | `最短路 通り数` |
| <!-- navigator: グラフ・木 > 連結性・到達可能性を調べる --> 二部グラフの色と成分ごとの人数が欲しい | [bipartite_coloring](library/graphs/graph_recipes.py) | 無向辺を両方向へ登録。奇閉路はNone。 | `二部グラフ 色 成分人数` |
| <!-- navigator: グラフ・木 > 連結性・到達可能性を調べる --> DAGの大量の到達判定をまとめる | [dag_reachability](library/graphs/graph_recipes.py) | クエリ先読み。block_size件のbitsetを伝播。閉路はValueError。PyPy向け。 | `DAG 到達判定 一括` |
| <!-- navigator: グラフ・木 > 値の制約・矛盾を扱う --> A[u] XOR A[v]=wを追加して矛盾を検出する | [XorDSU.merge / is_consistent](library/structures/xor_dsu.py) | mergeは代表元を返し、矛盾はValueError。追加を拒否する用途はis_consistent。 | `XOR 制約 矛盾` |
| <!-- navigator: グラフ・木 > 値の制約・矛盾を扱う --> 連結済みの2変数のXORを取得する | [XorDSU.diff](library/structures/xor_dsu.py) | 未連結はValueError。整数の差ならWeightedUnionFind。 | `XOR 差分 DSU` |
| <!-- navigator: グラフ・木 > 値の制約・矛盾を扱う --> XOR制約を満たす整数列の総和を最小化する | [XorDSU.minimum_sum_values](library/structures/xor_dsu.py) | 成分ごと・bitごとに1の少ない向きを選ぶ。O(NB)。 | `XOR 制約 最小和` |
| <!-- navigator: 配列・集合 > 値の集合を管理する > 順位・前後の値・辞書 --> 要素を増減しながら順位・中央値を求める | [FenwickMultiset.kth / bisect_left / bisect_right](library/structures/fenwick_multiset.py) | 全ての更新値をuniverseへ事前登録。kは0-indexed。重複可。 | `動的 順位 中央値` |
| <!-- navigator: 配列・集合 > 値の集合を管理する > 小さい順の和・絶対値の和 --> 小さい順または大きい順にk個取った和を求める | [FenwickMultiset.sum_smallest / sum_largest](library/structures/fenwick_multiset.py) | kは取得のたび変更可。更新・取得O(log σ)。スライド窓にも使える。 | `小さい順 k個 和` |
| <!-- navigator: 配列・集合 > 値の集合を管理する > 小さい順の和・絶対値の和 --> 増減する集合との絶対値の和を求める | [FenwickMultiset.sum_abs](library/structures/fenwick_multiset.py) | sum(abs(x-value))。valueは未登録でもよい。O(log σ)。 | `動的 絶対値 和` |
| <!-- navigator: 配列・集合 > 値の集合を管理する > mexを求める --> 配列の書き換え後のmexを求める | [DynamicMex](library/structures/dynamic_mex.py) | 最大要素数Nならlimit=N。古い値をdiscard、新しい値をadd。範囲を全て埋めるとNone。 | `動的 mex 更新` |
| <!-- navigator: 配列・集合 > 区間の被覆・予定を扱う --> 重なる区間をまとめる | [merge_intervals](library/basic/intervals.py) | 半開区間。隣接も併合し、空区間を無視。O(N log N)。 | `区間 併合` |
| <!-- navigator: 配列・集合 > 区間の被覆・予定を扱う --> 重複を除いた被覆の長さを求める | [interval_union_length](library/basic/intervals.py) | 半開区間の和集合。整数・実数座標。O(N log N)。 | `区間 被覆長` |
| <!-- navigator: 配列・集合 > 区間の被覆・予定を扱う --> ちょうどk本の区間に覆われる長さを数える | [covered_lengths](library/basic/intervals.py) | イベントを座標順に走査。result[0]は未被覆長ではなく0。 | `区間 重複数 長さ` |
| <!-- navigator: 配列・集合 > 区間の被覆・予定を扱う --> 重ならない予定を最多選択する | [schedule_intervals](library/basic/intervals.py) | 正の長さの半開区間、重みなし。選んだ元の添字を返す。 | `区間 スケジューリング 復元` |
| <!-- navigator: 配列・集合 > 区間の被覆・予定を扱う --> 各範囲内から異なる整数を1つずつ選ぶ | [assign_distinct_in_intervals](library/basic/intervals.py) | この関数だけ整数の閉区間[l,r]。割当list、無理ならNone。 | `区間 異なる整数 割当` |
| <!-- navigator: 配列・集合 > 条件を満たす連続区間を数える --> 和がちょうどKの連続区間を数える | [count_subarrays_sum](library/basic/subarray_count.py) | 負数あり可。累積和の頻度でO(N)期待時間。 | `和がKの区間数` |
| <!-- navigator: 配列・集合 > 条件を満たす連続区間を数える --> 和がK以下の連続区間を数える | [count_subarrays_sum_leq](library/basic/subarray_count.py) | 非負列限定。K以上は全区間数からK-1以下を引く。 | `非負 部分配列 和 以下` |
| <!-- navigator: 配列・集合 > 条件を満たす連続区間を数える --> 高々・ちょうどK種類を含む連続区間を数える | [count_subarrays_distinct_at_most / count_subarrays_distinct_exact](library/basic/subarray_count.py) | 正式名はcount_subarrays_distinct_at_most / count_subarrays_distinct_exact。空区間を除く。 | `部分配列 種類数 ちょうど` |
| <!-- navigator: 配列・集合 > 条件を満たす連続区間を数える --> 最小値と最大値が指定値の区間を数える | [count_subarrays_minmax](library/basic/subarray_count.py) | 範囲外の最後の位置・min/maxの最後の位置から数える。O(N)。 | `部分配列 最小値 最大値 個数` |
| <!-- navigator: 配列・集合 > 条件を満たす連続区間を数える --> 全ての連続区間の最小値・最大値を足す | [sum_subarray_min / sum_subarray_max](library/basic/subarray_count.py) | 単調スタック。負数・同値可、O(N)。 | `全区間 最小値 総和` |
| <!-- navigator: DP・探索 > 桁の条件を満たす整数を数える --> 非零の桁がちょうどK個ある整数を数える | [count_nonzero_digits](library/basic/digit_dp.py) | 上限は10進文字列でも可。0はk=0に含める。O(LK)。 | `桁DP 非零桁 個数` |
| <!-- navigator: DP・探索 > 桁の条件を満たす整数を数える --> 各桁の和がDの倍数になる整数を数える | [count_digit_sum_mod](library/basic/digit_dp.py) | 既定では0を除く。上限を含む。O(LD*10)。 | `桁DP 桁和 倍数` |
| <!-- navigator: DP・探索 > 桁の条件を満たす整数を数える --> 禁止した数字を含まない整数を数える | [count_avoiding_digits](library/basic/digit_dp.py) | 先頭の0は除外。整数0は文字0として判定。補集合で禁止数字を含む数も数えられる。 | `桁DP 禁止数字` |
| <!-- navigator: DP・探索 > 桁の条件を満たす整数を数える --> 0から上限までに特定の数字が何回出るか | [count_digit_occurrences](library/basic/digit_dp.py) | 先頭の補助的な0を数えず、整数0は一桁として数える。O(L)。 | `桁DP 数字 出現回数` |
| <!-- navigator: DP・探索 > 部分集合和・ナップサック --> 重さが巨大な0/1ナップサックを解く | [knapsack_by_value](library/basic/knapsack_extra.py) | 価値総和Vが小さい場合。重量・価値とも非負整数。O(NV)。 | `ナップサック 価値DP` |
| <!-- navigator: DP・探索 > 部分集合和・ナップサック --> 各種類に個数制限があるナップサックを解く | [bounded_knapsack](library/basic/knapsack_extra.py) | (重さ,価値,個数)。単調dequeでO(NW)。重量0も対応。 | `ナップサック 個数制限` |
| <!-- navigator: DP・探索 > 部分集合和・ナップサック --> 各品物を何個でも使うナップサックを解く | [knapsack_unbounded](library/basic/knapsack_extra.py) | 重さは正、O(NW)。価値は負でもよい。 | `ナップサック 無制限` |
| <!-- navigator: DP・探索 > 部分集合和・ナップサック --> 目標和を作る部分集合を復元する | [subset_sum_restore](library/basic/knapsack_extra.py) | 非負列。元の添字list、無理ならNone。bitsetを使うPyPy向け。 | `部分和 復元` |
| <!-- navigator: DP・探索 > 部分集合和・ナップサック --> 各ペアから必ず1つ選び目標和を作る | [two_choice_sum](library/basic/knapsack_extra.py) | 非負ペア。0/1の選択list、無理ならNone。bitset履歴を保持。 | `二択 和 復元` |
| <!-- navigator: 文字列 > 部分列を選ぶ・数える --> ある文字列が部分列か判定して位置を返す | [subsequence_positions](library/strings/subsequence.py) | 最も左を選ぶ添字list、不可ならNone。O(N+M)。 | `部分列 位置 復元` |
| <!-- navigator: 文字列 > 部分列を選ぶ・数える --> 長さKの辞書順最小部分列を作る | [smallest_subsequence](library/strings/subsequence.py) | 文字列・比較可能な列。単調スタックでO(N)。 | `部分列 辞書順 最小` |
| <!-- navigator: 文字列 > 部分列を選ぶ・数える --> 指定文字列になる部分列の選び方を数える | [count_subsequence](library/strings/subsequence.py) | 同じ文字でも位置が違えば別。O(NM)。空patternは1。 | `部分列 選び方 通り数` |
| <!-- navigator: 文字列 > 部分列を選ぶ・数える --> 異なる部分列が何種類あるか数える | [count_distinct_subsequences](library/strings/subsequence.py) | 内容が同じなら同一として数える。既定は空を除く。O(N)期待時間。 | `部分列 異なる 種類数` |
| <!-- navigator: 文字列 > 編集距離・最長共通部分列 --> 最長共通部分列そのものを復元する | [lcs_restore](library/strings/subsequence.py) | O(NM)時間・空間。長さだけなら既存lcs_length。 | `LCS 復元` |
| <!-- navigator: 文字列 > 編集距離・最長共通部分列 --> K回以内の編集で文字列を一致させられるか | [edit_distance_bounded](library/strings/subsequence.py) | 挿入・削除・置換は各1。距離>KならK+1、帯状DPでO((K+1)min(N,M))。 | `編集距離 K以内` |
| <!-- navigator: グリッド・幾何 > 迷路の距離・経路・連結成分 --> 壁のある盤面で複数始点からの距離を求める | [grid_bfs](library/basic/grid_search.py) | 座標(row,column)、4近傍。未到達・壁は-1。 | `グリッド 複数始点 BFS` |
| <!-- navigator: グリッド・幾何 > 迷路の距離・経路・連結成分 --> 迷路の最短経路を復元する | [grid_shortest_path](library/basic/grid_search.py) | 始点・終点を含む座標list。到達不能None。 | `迷路 最短経路 復元` |
| <!-- navigator: グリッド・幾何 > 迷路の距離・経路・連結成分 --> 4方向・8方向につながるマスを分類する | [grid_components](library/basic/grid_search.py) | filledで対象文字を指定。成分ID配列とサイズ列。 | `グリッド 8近傍 連結成分` |
| <!-- navigator: グリッド・幾何 > 迷路の距離・経路・連結成分 --> 迷路で曲がる回数を最小化する | [grid_min_turns](library/basic/grid_search.py) | 方向を状態に追加した0-1 BFS。最初の方向は自由、到達不能-1。 | `迷路 方向転換 最小` |
| <!-- navigator: 整数・数式 > 切り捨て・商の総和を求める --> Nを1からNで割った商をまとめて足す | [floor_quotient_ranges / sum_floor_quotients](library/math/integer_count.py) | 分母が変わるN//i。商が同じ範囲を半開区間で列挙。O(sqrt N)。 | `整数除算 商 区間 総和` |
| <!-- navigator: 整数・数式 > 余り・合同式・mod演算 --> a*x≡bの最小非負解と周期を求める | [linear_congruence](library/math/integer_count.py) | (解,周期)、解なしNone。aとmodが互いに素でなくてもよい。 | `一次合同式 解 周期` |
| <!-- navigator: 整数・数式 > 素数・約数・素因数を求める --> φ・μを上限まで一括で計算する | [totient_sieve / mobius_sieve](library/math/integer_count.py) | 互いに素の計数・約数での包除。0番は0、1番は1。 | `トーシェント メビウス 一括` |

### 同梱品で足りる範囲と別途必要な処理

- 単純なキューは`collections.deque`、最小ヒープは`heapq`、出現数は`collections.Counter`、静的な整列済み列の二分探索は`bisect`を使える。一次元の静的区間和は累積和で足りる。
- 正確な有理数は標準の`fractions.Fraction`、整数平方根は`math.isqrt`。`sqrt_mod`とは用途が異なる。
- 辺削除を伴うオンライン動的連結性、動的な木のlink/cut、更新付き区間k番目、一般の永続セグ木は専用実装を同梱していない。RollbackDSUやWaveletMatrixだけで直接処理できるとは限らない。
- 負費用をそのまま渡す最小費用流、合成数modでの一般の行列式、任意modの高速畳み込み、Subset Convolutionも現APIの対象外。
- 最近点対の点ID、Steiner木の辺復元は追加実装が必要。LCSの文字列復元はsubsequence.pyのlcs_restoreで対応する。既存APIが返す値だけで提出条件を満たすか確認する。
- 幾何は`(x,y)`タプルを使う`library/geometry/convex.py`と、`Point`を使う`snippets/geometry/`を区別する。Point版の各ファイルは自己完結しているので、必要な機能を含む1ファイルを選ぶ。同名クラスを重ねて貼らない。


## 主な修正

| 元実装の問題 | 今回の処理 |
|---|---|
| LISの固定INF、Doublingの終端-1/上限 | 番兵を使わないLISと復元、終端を保持し上限超過を検出 |
| BinaryTrieが非常に大きな配列を事前確保 | 必要なノードだけ追加。順位を0-indexedに整理しmin_xorを追加 |
| Waveletのbit消去がOR、範囲外select | ANDで消去、存在数を確認、空区間和と0-indexed順位APIを追加 |
| LowLinkが親頂点を丸ごと無視 | 親の辺IDだけ除外し多重辺に対応 |
| 全方位木DPの単位元が1に固定 | 引数の単位元を使い、隣接順序を保つprefix/suffix集約へ |
| Mo・等差数列セグ木が未完成 | MoのコールバックAPI、等差数列の区間加算/代入/和を実装 |
| Suffix Arrayの整数列比較にbit演算 | 論理比較に修正しUnicode・空列に対応 |
| 巨大値でLi Chaoの有限INFが答えになる | 実際の直線値で初期化。有効な直線がなければNone |
| キー再追加時の削除ヒープの誤判定 | MaxQueueを世代番号で管理 |
| FPSの0乗・次数・GCDのtuple更新/負添字等 | 境界条件、半GCDのシフト、0逆元、入力非破壊を修正 |
| 部分和計数の0重み・上限外重み | 0重みは2倍、上限を超える重みは無視 |
| 問題固有の入力・定数・クラス依存 | 同じファイルへ必要部分だけ含め、引数と戻り値を明示 |

## 検証

オンラインverify候補は[VERIFY_PROBLEMS.md](VERIFY_PROBLEMS.md)に整理した。各行に入力変換・出力・検証できない機能を記載している。

2026-10-18のAPI整理では17ファイルを更新。関連するライブラリ・LC・検索の47テストをCPythonで確認し、影響するLC 13問17サンプルと、17ファイルの使用例70件をPyPyで確認した。最後の引数名・境界指定の調整後には、該当する4テストもPyPyで確認した。以下の全体規模・過去の確認記録とは区別する。

2026-10-18の第2弾では、既存34テストとLC第1弾7テスト、第2弾6テストをPyPyで確認した。第2弾は50問・公式サンプル91件を含み、合計60問・114件の入出力を検査する。必要なサンプルは保存済みで、実行時にネット接続や追加パッケージは不要。

| 対象 | テスト数・結果 |
|---|---|
| ABC向け追加 `test_abc_toolkit.py` | 13テスト。12ファイルの使用例・愚直比較・17問47サンプル。PyPyで成功。 |
| 提出用ライブラリ `test_library.py` | 現在35テスト。今回のAPI整理後はCPythonで成功。過去の34テストはPyPyでも確認済み。 |
| セグ木派生版 `test_segtree_recipes.py` | 7テスト。33種類の設計・使用例・配列比較・結合則/作用則・AtCoder6問12サンプル。 |
| LC第1弾 `test_library_checker.py` | 7テスト。10問・公式入力23件を含む。 |
| LC第2弾 `test_library_checker_round2.py` | 6テスト。50問・公式入力91件、版分岐・動的数列・長方形和・グラフ・多項式等の愚直照合。 |
| 検索・設定・読み込み `test_palette.py` | 6テスト。目的ナビ追加後にCPythonで確認。234用途の分類と全92ファイルへのリンクも検査。 |
| 非表示GUI `test_palette_ui.py` | 5テスト。目的ナビ追加後にCPythonで確認。段階選択・比較・コピー・再読み込み、逆引きの見出し移動・File選択も検査。クリップボードはテスト用に置き換える。 |
| 機能別Live `test_live_templates.py` | 2テスト。274機能の単独読み込み・依存参照・代表例と、既存XMLを保持した登録を確認。 |
| 使用例 | ACL API統一時に変更した11ファイルの51例をPyPyで確認。派生版33種の例は専用テストで確認。以前の71ファイル383例・追加15ファイル64例は過去の確認記録。全て通常のPythonコード＋戻り値コメント。 |

unittestの登録数は合計81件。メイン画面・機能別Live Template追加では検索・GUI・登録の関連13件を実行した。目的ナビ追加では検索・GUIの関連11件を実行した。ABC向け追加では専用13テストと関連する既存の検索・GUI・単体読み込みを確認。派生セグ木の追加では専用7テストと、影響する既存のLC・検索・GUI検証を実行した。ACL API統一の際にはライブラリ・LCアダプター・検索・GUIの既存テストを再確認した。指定先の86個の呼び出し形式（引数名・順序・既定値）と代表操作も照合した。使用例はdoctest形式ではなく、PyCharmで読みやすい通常のコードとして掲載している。確認対象の規模と、公式全テスト・オンラインAC・Codonコンパイルが未確認である点は[verify/README.md](verify/README.md#確認済みの範囲)を参照。

別系統の従来構造テストは、PyPyで12ファイル・11群・1,637,651項目が成功した記録を保持している。これらは旧APIでの過去の実行記録であり、現行APIの確認結果は上の表を参照する。全入力の網羅確認やオンラインACを示すものではない。

```powershell
Set-Location D:\Kyopro\AtCoder\cp_snippet_palette
& D:\Kyopro\.python\pypy-3.11.15-windows-x86_64-none\pypy3.exe -B tests\test_library.py -v
& D:\Kyopro\.python\pypy-3.11.15-windows-x86_64-none\pypy3.exe -B tests\test_library_checker.py -v
& D:\Kyopro\.python\pypy-3.11.15-windows-x86_64-none\pypy3.exe -B tests\test_library_checker_round2.py -v
..\.venv\Scripts\python.exe -B -m unittest discover -s tests -v
```

## ファイル別API

各ファイルの先頭に使用例、各定義に引数・戻り値・前提条件を記載。検索語には下表の関数名をそのまま使える。同梱16スニペットも同じ説明形式で、[全92ファイルの一覧](VERIFY_PROBLEMS.md)から開ける。

| 分野 / ファイル | 主な公開クラス・関数 |
|---|---|
| [basic/doubling.py](library/basic/doubling.py) | `Doubling` |
| [basic/grid.py](library/basic/grid.py) | `to_index`, `to_position`, `in_grid`, `transpose`, `rotate90` |
| [basic/matrix.py](library/basic/matrix.py) | `matrix_multiply`, `matrix_power`, `max_plus_multiply`, `max_plus_power` |
| [basic/prefix_sum_2d.py](library/basic/prefix_sum_2d.py) | `prefix_sum_2d`, `rectangle_sum` |
| [basic/sequence.py](library/basic/sequence.py) | `compress`, `lis_indices`, `lis_length`, `inversion_count`, `run_length_encode`, `run_length_decode` |
| [basic/sliding_window.py](library/basic/sliding_window.py) | `sliding_min`, `area_min_sliding`, `largest_rectangle_in_histogram`, `largest_rectangle_in_grid` |
| [basic/subset_dp.py](library/basic/subset_dp.py) | `subset_sums`, `split_and_list`, `subset_sums_by_size`, `knapsack_01`, `subset_sum_bits` |
| [geometry/convex.py](library/geometry/convex.py) | `convex_hull_points`, `convex_diameter_sq`, `ConvexPolygon` |
| [geometry/kd_tree.py](library/geometry/kd_tree.py) | `KDTree` |
| [geometry/plane_distance.py](library/geometry/plane_distance.py) | `point_plane_distance` |
| [geometry/rectangle_union.py](library/geometry/rectangle_union.py) | `rectangle_union_area` |
| [graphs/assignment.py](library/graphs/assignment.py) | `assignment` |
| [graphs/bipartite_matching.py](library/graphs/bipartite_matching.py) | `bipartite_matching` |
| [graphs/centroid_decomposition.py](library/graphs/centroid_decomposition.py) | `CentroidDecomposition` |
| [graphs/cycle.py](library/graphs/cycle.py) | `find_cycle` |
| [graphs/exponential.py](library/graphs/exponential.py) | `tsp_cycle`, `steiner_tree`, `chinese_postman`, `maximum_independent_set`, `chromatic_number` |
| [graphs/hld.py](library/graphs/hld.py) | `BiSegTree`, `HLD`, `path_prod` |
| [graphs/lowlink.py](library/graphs/lowlink.py) | `LowLink` |
| [graphs/max_flow.py](library/graphs/max_flow.py) | `mf_graph` |
| [graphs/min_cost_flow.py](library/graphs/min_cost_flow.py) | `mcf_graph` |
| [graphs/mst.py](library/graphs/mst.py) | `minimum_spanning_forest` |
| [graphs/rerooting.py](library/graphs/rerooting.py) | `rerooting` |
| [graphs/scc.py](library/graphs/scc.py) | `scc_ids`, `scc`, `scc_dag`, `two_sat` |
| [graphs/shortest_paths.py](library/graphs/shortest_paths.py) | `adjlist`, `weighted_adjlist`, `dijkstra`, `restore_path`, `zero_one_bfs`, `bellman_ford`, `floyd_warshall`, `topological_sort` |
| [graphs/tree.py](library/graphs/tree.py) | `euler_tour`, `tree_diameter`, `tree_centers`, `weighted_tree_diameter`, `postorder_from_preorder_inorder` |
| [math/bit_transforms.py](library/math/bit_transforms.py) | `and_convolution`, `subset_zeta`, `xor_basis`, `xor_maximum`, `xor_minimax`, `solve_gf2`, `linear_equations_gf2`, `walsh_hadamard`, `xor_convolution` |
| [math/combinatorics.py](library/math/combinatorics.py) | `Comb`, `combination_small_k`, `smallest_prime_factors`, `primes_up_to`, `factorize_trial`, `divisors` |
| [math/factorize64.py](library/math/factorize64.py) | `is_probable_prime`, `find_prime_factor`, `prime_fact`, `divisors`, `totient`, `lcm` |
| [math/gf2_matrix.py](library/math/gf2_matrix.py) | `matrix_rank_gf2`, `inverse_matrix_gf2`, `matrix_product_gf2` |
| [math/linear_algebra.py](library/math/linear_algebra.py) | `matrix_det`, `matrix_rank`, `inverse_matrix`, `linear_equations` |
| [math/linear_recurrence.py](library/math/linear_recurrence.py) | `berlekamp_massey`, `linear_recurrence` |
| [math/number_theory.py](library/math/number_theory.py) | `pow_mod`, `inv_gcd`, `inv_mod`, `crt`, `floor_sum`, `discrete_log`, `sqrt_mod` |
| [math/polynomial.py](library/math/polynomial.py) | `butterfly`, `butterfly_inv`, `subset_sum`, `partition_function`, `bernoulli_number`, `stirling_first`, `stirling_second`, `fps_inverse`, `fps_log`, `fps_exp`, `fps_power`, `fps_sqrt`, `bostan_mori`, `polynomial_gcd`, `polynomial_inverse`, `polynomial_divmod`, `linear_recurrence_ntt`, `FFT`, `FPS`, `polynomial_interpolation` |
| [math/scalar.py](library/math/scalar.py) | `ModContext`, `Modint`, `raw` |
| [search/heuristics.py](library/search/heuristics.py) | `beam_search`, `negamax`, `tsp_nearest_neighbor`, `tsp_two_opt` |
| [search/numeric.py](library/search/numeric.py) | `normal_cdf`, `kmeans` |
| [strings/matching.py](library/strings/matching.py) | `prefix_function`, `kmp_search`, `manacher`, `edit_distance`, `lcs_length` |
| [strings/rolling_hash.py](library/strings/rolling_hash.py) | `RollingHash`, `RollingHashSegTree` |
| [strings/suffix_array.py](library/strings/suffix_array.py) | `longest_common_substring`, `String` |
| [strings/trie.py](library/strings/trie.py) | `Trie`, `AhoCorasick` |
| [structures/aggregate_deque.py](library/structures/aggregate_deque.py) | `AggregateDeque` |
| [structures/aggregate_queue.py](library/structures/aggregate_queue.py) | `AggregateQueue` |
| [structures/avl_tree.py](library/structures/avl_tree.py) | `AVLTree` |
| [structures/binary_trie.py](library/structures/binary_trie.py) | `BinaryTrie` |
| [structures/bit_set.py](library/structures/bit_set.py) | `BitSet` |
| [structures/cartesian_tree.py](library/structures/cartesian_tree.py) | `CartesianTree` |
| [structures/dynamic_fenwick.py](library/structures/dynamic_fenwick.py) | `DynamicFenwickTree`, `DynamicFenwickTree2D` |
| [structures/dynamic_sequence.py](library/structures/dynamic_sequence.py) | `DynamicSequence` |
| [structures/fenwick_2d.py](library/structures/fenwick_2d.py) | `OfflineFenwick2D` |
| [structures/li_chao.py](library/structures/li_chao.py) | `LiChaoTree`, `LiChaoInt` |
| [structures/linked_list.py](library/structures/linked_list.py) | `LinkedList` |
| [structures/max_queue.py](library/structures/max_queue.py) | `MaxQueue` |
| [structures/mo.py](library/structures/mo.py) | `mo_order`, `mo_solve` |
| [structures/offline_queries.py](library/structures/offline_queries.py) | `range_count_distinct` |
| [structures/persistent_queue.py](library/structures/persistent_queue.py) | `PersistentQueue` |
| [structures/priority_sum.py](library/structures/priority_sum.py) | `PrioritySumStructure` |
| [structures/range_arithmetic.py](library/structures/range_arithmetic.py) | `ArithmeticSegmentTree` |
| [structures/rollback_dsu.py](library/structures/rollback_dsu.py) | `RollbackDSU` |
| [structures/slope_trick.py](library/structures/slope_trick.py) | `SlopeTrick` |
| [structures/sorted_set.py](library/structures/sorted_set.py) | `SortedSet`, `SortedMultiset` |
| [structures/sqrt_decomposition.py](library/structures/sqrt_decomposition.py) | `SqrtDecomposition` |
| [structures/wavelet_matrix.py](library/structures/wavelet_matrix.py) | `FullyIndexableDictionary`, `WaveletMatrix` |
| [structures/segtree_monoids.py](library/structures/segtree_monoids.py) | `range_sum`, `range_min`, `range_max`, `range_gcd`, `range_xor`, `range_or`, `range_and`, `range_min_count`, `range_max_count`, `range_top2`, `range_max_subarray`, `range_brackets`, `range_affine_composite`, `range_matrix_product`, `range_xor_basis`, `semigroup_segtree` |
| [structures/lazy_segtree_actions.py](library/structures/lazy_segtree_actions.py) | `range_add_sum`, `range_assign_sum`, `range_affine_sum`, `range_add_min`, `range_add_max`, `range_add_min_count`, `range_affine_minmax`, `range_clamp_minmax`, `range_flip_inversions`, `range_binary_runs`, `range_flip_brackets`, `range_affine_sum_squares`, `range_pair_add_product`, `range_index_affine_sum`, `range_digit_assign`, `range_assign_max_subarray`, `range_add_gcd` |
| [functional_graph](library/graphs/functional_graph.py) | `FunctionalGraph` |
| [graph_recipes](library/graphs/graph_recipes.py) | `multi_source_bfs`, `bfs_path_count`, `bipartite_coloring`, `dag_reachability` |
| [xor_dsu](library/structures/xor_dsu.py) | `XorDSU` |
| [fenwick_multiset](library/structures/fenwick_multiset.py) | `FenwickMultiset` |
| [dynamic_mex](library/structures/dynamic_mex.py) | `DynamicMex` |
| [intervals](library/basic/intervals.py) | `merge_intervals`, `interval_union_length`, `covered_lengths`, `schedule_intervals`, `assign_distinct_in_intervals` |
| [subarray_count](library/basic/subarray_count.py) | `count_subarrays_sum`, `count_subarrays_sum_leq`, `count_subarrays_distinct_at_most`, `count_subarrays_distinct_exact`, `count_subarrays_minmax`, `sum_subarray_min`, `sum_subarray_max` |
| [digit_dp](library/basic/digit_dp.py) | `count_nonzero_digits`, `count_digit_sum_mod`, `count_avoiding_digits`, `count_digit_occurrences` |
| [knapsack_extra](library/basic/knapsack_extra.py) | `knapsack_by_value`, `bounded_knapsack`, `knapsack_unbounded`, `subset_sum_restore`, `two_choice_sum` |
| [subsequence](library/strings/subsequence.py) | `subsequence_positions`, `smallest_subsequence`, `count_subsequence`, `count_distinct_subsequences`, `lcs_restore`, `edit_distance_bounded` |
| [grid_search](library/basic/grid_search.py) | `grid_bfs`, `grid_shortest_path`, `grid_components`, `grid_min_turns` |
| [integer_count](library/math/integer_count.py) | `floor_quotient_ranges`, `sum_floor_quotients`, `linear_congruence`, `totient_sieve`, `mobius_sieve` |
