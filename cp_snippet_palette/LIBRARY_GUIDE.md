# 提出用ライブラリの使い方

現行コードとの最終照合：2026-10-17。`library/`は54ファイル。候補83用途から抽出した51ファイルに、Library Checker対応でSWAG・割当・線形代数の3ファイルを追加した。依存する補助コードは同じファイルに含め、元の解答ファイルは変更していない。ACLに対応する同梱スニペットは、Python版ACLと同じ入力形式のAPIを追加・整備した。

[ACL形式のAPIと移行方法](ACL_API.md) ／ [全71ファイルのverify問題一覧](VERIFY_PROBLEMS.md) ／ [LC追加10問題の提出手順](verify/README.md)

## 検索して提出する

`run_palette.bat`を起動し、例えば`graphs SCC`、`座標圧縮`、`fps_inverse`、`区間 和 等差`で検索する。**File**の行を選んでEnter、解答のmainより上に貼り付ける。ローカルのlibraryフォルダをAtCoderにアップロードしたり、提出コードからimportしたりする必要はない。

Ctrl+Enterならコピー後も画面を開いたままにできる。F2で選択中のAPI・verify候補、Ctrl+Dでお気に入り登録、Ctrl+Lで検索欄へ戻る。File／Live・分野・履歴の絞り込みやコード内検索は[操作ガイド](LOCAL_USAGE.md)を参照。

同じファイルに近い用途をまとめたため、一度コピーすればそのファイルの関数を使える。例えば`sequence.py`には座標圧縮・LIS・転倒数がある。複数の解答・旧テンプレートから同名クラスを重ねて貼ることは避ける。

ローカル開発ではリポジトリ直下をプロジェクトルートにして、次のようなimportも可能。

```python
from cp_snippet_palette.library.basic.sequence import compress, lis_length

ids, original = compress([40, 10, 40])  # [1, 0, 1], [10, 40]
print(lis_length([3, 1, 2, 5]))        # 3
```

提出時は上のimport行を、パレットからコピーしたファイルのコードに置き換える。

## 共通の約束

- 頂点・添字・新しい順位APIは0-indexed。区間・長方形は半開区間。入力が1-indexedなら読み込み時に変換する。
- 原則として入力配列を変更しない。構造へのadd/set、最大流・最小費用流の残余グラフ更新などはそのオブジェクトを変更する。
- 数値関数は通常のintを使う。MODやINFを解答側のグローバル変数から暗黙に参照しない。多項式は`FPS_MOD=998244353`固定であり、別の法への書き換えはできない。
- 最短路の`inf`は既定`1<<60`。問題の有限距離の上限より大きい値を渡す。Codonでは加算途中のオーバーフローにも注意する。
- 不正な範囲は原則IndexError、満たせない前提はValueError。高速な既存部品にはassertによる前提検査もある。ホットループ内で全入力の検査を行う設計にはしていない。
- 木専用関数には連結な無向木を渡す。負辺を使えるのはBellman–Ford等、説明で対応が明記されたものに限る。

互換のため残した例外は、既存LCATreeの1-indexed、互換クラスBIT.sum(i)の閉区間（新規コードはFenwickTree.sum(l,r)）、WaveletMatrixの旧quantile/selectの1-indexed、Li Chao Treeの座標定義域[xmin,xmax]。新しいWaveletMatrix.kth_smallest(l,r,k)は0-indexed。AVLの新しいkth/ge/ltを使えば旧upper_boundの紛らわしい意味を避けられる。

## PyPyとCodon

実行確認は**Windows版PyPy 7.3.23 / Python 3.11.15**で行った。uvで`D:\Kyopro\.python\pypy-3.11.15-windows-x86_64-none`に用意している。PyCharm用の既存CPython仮想環境は引き続き検索ツールの起動に使う。

AtCoder公式の言語テスト環境にはPyPy 3.11-v7.3.20、Codon 0.19.3が掲載されている。手元のPyPyとはパッチ版とOSが異なり、AtCoderへの提出・AC判定は今回行っていない。[AtCoder公式の実行環境](https://atcoder.jp/contests/language-test-202505/rules)

Codonは通常のintが64bitで、CPython/PyPyと完全に同じ処理系ではない。このPCにはCodon/WSL環境がないため、**全ファイルともCodonのコンパイル確認は未実施**。次の区分は移植時の判断材料であり、動作保証のラベルではない。[Codon公式FAQ](https://docs.exaloop.io/start/faq/)

| 扱い | 対象・注意 |
|---|---|
| 共通化しやすい処理 | 配列主体の累積和、行列、ダブリング、最短路など。列・辞書の型を揃え、中間の乗算も64bitに収める。 |
| PyPy用として使う処理 | 任意精度bitset、subset_sum_bits、大きなGF(2)行列、彩色数の包除原理、64bit整数のPollard rho/Miller–Rabin。通常intのままCodonへ移すと結果が変わり得る。 |
| 個別の移植確認が必要 | Generic/NamedTupleを使う既存構造、Optionalを含む戻り値、コールバック型、Fraction、ModInt、FPSの演算子オーバーロード、SA-ISの内部関数。まずPyPyで使う。 |
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

## 用途に応じた選択

- 単純な順位付き集合にはSortedSet/SortedMultiset、キーと値の辞書にはAVLTree。二重ヒープで足りる下位k個の和にはPrioritySumStructure。
- 静的な区間k番目にはWaveletMatrix。整数値の挿入削除と最小XORにはBinaryTrie。ビット幅は入力上限に合わせる。
- 最小費用流は元の辺費用が非負のケース専用。flow/slopeは1オブジェクト1回で、再呼び出しは例外。最大流MFGraphとは契約が異なる。
- 二部マッチングは非再帰の増加路法O(L*E)。非常に大きいケースでは最大流等と比較する。探索系のTSP/Steiner/独立集合は指数時間なので、関数冒頭の計算量を確認する。
- 数論のCombは素数modかつ前計算n<mod。大きなn・小さなkにはcombination_small_k。64bitの大きな素因数分解にはfactorize64。
- 多項式はlistを受け取るfps_inverse/log/exp/power/sqrtを基本にする。size=係数数、NTT長上限は2^23。旧FormalPowerSeriesのdeg引数は「最大次数」で1ずれる。補間の戻り値はFormalPowerSeriesなので`.poly`で係数を取り出す。
- 正確な有理数にはFractionを採用した。独自MyFractionを二重管理しない。CHTは傾き/問い合わせの単調性を要求しないLiChaoIntに統合。
- 区間限定の直線を追加する場合は、問い合わせ座標を先に登録するLiChaoTree(xs)を使う。add_segment(l,r,a,b)は[l,r)、有効な直線がないquery(x)はNone。LiChaoIntの閉区間定義域・空なら例外という旧仕様とは区別する。
- キュー全体の集約はAggregateQueue(op,e)。非可換な関数合成ではop(f,g)=g∘fとし、先頭から順に適用する。汎用モノイドを対象とし、逆元は不要。
- 密な最小費用割当はassignment(cost)。行数≤列数、負費用可。疎な容量・流量付き問題はMCFGraphを使い、費用の前提も確認する。
- 行列式・階数・逆行列・連立方程式はlinear_algebraの素数mod版。linear_equationsは(特解, 同次解の基底)かNone、GF(2)版linear_equations_gf2は整数bitsetを返す。任意の合成数modへはそのまま使えない。
- 頂点二重連結成分はLowLink.biconnected_components()。block_cut_tree()では元頂点0..n-1と成分頂点n..n+k-1の所属関係を森にする。橋を除く「辺二重連結成分」とは異なる。
- XOR畳み込みはxor_convolution(a,b,mod)。長さは同じ2^kで、modは1より大きい奇数。整数の通常の積の畳み込みにはconvolutionを使う。
- ビームサーチ・ゲーム木は、状態生成・評価・同一状態のキーを呼び出し側で指定する。k-meansは近似であり、最適性や全クラスタが非空になる保証はない。

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
| 巨大値でLi Chaoの有限INFが答えになる | 実際の直線値で初期化。空なら例外 |
| キー再追加時の削除ヒープの誤判定 | MaxQueueを世代番号で管理 |
| FPSの0乗・次数・GCDのtuple更新/負添字等 | 境界条件、半GCDのシフト、0逆元、入力非破壊を修正 |
| 部分和計数の0重み・上限外重み | 0重みは2倍、上限を超える重みは無視 |
| 問題固有の入力・定数・クラス依存 | 同じファイルへ必要部分だけ含め、引数と戻り値を明示 |

## 検証

オンラインverify候補は[VERIFY_PROBLEMS.md](VERIFY_PROBLEMS.md)に整理した。各行に入力変換・出力・検証できない機能を記載している。

全54ファイルの単独読み込み、代表的な入出力・上記の不具合・ACL形式の呼び出しを対象にした既存34テストと、LC向けの追加7テストをPyPyで実行した。全入力に対する正当性や全問題での時間制限内実行を保証するものではない。保存済みサンプルを使うためテスト実行時のネットワークや外部ライブラリは不要。

2026-10-17時点の確認結果は次のとおり。変更対象ごとに実行した結果を記載する。

| 対象 | テスト数・結果 |
|---|---|
| 提出用ライブラリ `test_library.py` | 34テスト。LC追加後にPyPyで再実行して成功。CPythonはライブラリ・ACL対応時の実行記録。 |
| LC追加対応 `test_library_checker.py` | 7テスト。PyPyで成功。内部で10問題・公式サンプル入力23件の提出コードも独立したプロセスで検査。 |
| 検索・設定・読み込み `test_palette.py` | 5テスト。検索画面更新後にCPythonで成功。 |
| 非表示GUI `test_palette_ui.py` | 2テスト。検索画面更新後にCPythonで成功。コピー文字列・再読み込み・失敗時の処理を確認。 |

現在のテスト構成は合計48件。GUIテストではクリップボード部分を置き換えており、実際のPyCharmへの貼り付けは行っていない。LC追加後は実データ161件で非表示GUIの初期化と、拡張した6モジュールの検索・API・verify表示も確認した。

LC追加分は制約上限に相当する代表入力も実行した。対象・確認範囲は[verify/README.md](verify/README.md#確認済みの範囲)を参照。公式テスト全件の実行、オンラインAC、Codonコンパイルは未確認。

別系統の従来構造テストは、PyPyで12ファイル・11群・1,637,651項目が成功した記録を保持している。ACL対応時は変更した構造系4群・221,997項目を再実行した。全入力の網羅確認やオンラインACを示すものではない。

```powershell
Set-Location D:\Kyopro\AtCoder\cp_snippet_palette
& D:\Kyopro\.python\pypy-3.11.15-windows-x86_64-none\pypy3.exe -B tests\test_library.py -v
& D:\Kyopro\.python\pypy-3.11.15-windows-x86_64-none\pypy3.exe -B tests\test_library_checker.py -v
..\.venv\Scripts\python.exe -B -m unittest discover -s tests -v
```

## ファイル別API

各ファイルの先頭に計算量・入力条件・提出時の注意を記載。検索語には下表の関数名をそのまま使える。

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
| [graphs/bipartite_matching.py](library/graphs/bipartite_matching.py) | `bipartite_matching` |
| [graphs/assignment.py](library/graphs/assignment.py) | `assignment` |
| [graphs/centroid_decomposition.py](library/graphs/centroid_decomposition.py) | `CentroidDecomposition` |
| [graphs/exponential.py](library/graphs/exponential.py) | `tsp_cycle`, `steiner_tree`, `chinese_postman`, `maximum_independent_set`, `chromatic_number` |
| [graphs/hld.py](library/graphs/hld.py) | `BiSegTree`, `HLD`, `path_fold_noncomm` |
| [graphs/lowlink.py](library/graphs/lowlink.py) | `LowLink` |
| [graphs/max_flow.py](library/graphs/max_flow.py) | `MFGraph` |
| [graphs/min_cost_flow.py](library/graphs/min_cost_flow.py) | `MCFGraph` |
| [graphs/mst.py](library/graphs/mst.py) | `minimum_spanning_forest` |
| [graphs/rerooting.py](library/graphs/rerooting.py) | `rerooting` |
| [graphs/scc.py](library/graphs/scc.py) | `SCCGraph`, `SCC`（旧名）, `TwoSAT` |
| [graphs/shortest_paths.py](library/graphs/shortest_paths.py) | `adjlist`, `weighted_adjlist`, `dijkstra`, `restore_path`, `zero_one_bfs`, `bellman_ford`, `floyd_warshall`, `topological_sort` |
| [graphs/tree.py](library/graphs/tree.py) | `euler_tour`, `tree_diameter`, `tree_centers`, `postorder_from_preorder_inorder` |
| [math/bit_transforms.py](library/math/bit_transforms.py) | `subset_zeta`, `xor_basis`, `xor_maximum`, `xor_minimax`, `solve_gf2`, `linear_equations_gf2`, `walsh_hadamard`, `xor_convolution` |
| [math/combinatorics.py](library/math/combinatorics.py) | `Comb`, `combination_small_k`, `smallest_prime_factors`, `primes_up_to`, `factorize_trial`, `divisors` |
| [math/factorize64.py](library/math/factorize64.py) | `is_prime`, `find_prime_factor`, `factorize` |
| [math/linear_recurrence.py](library/math/linear_recurrence.py) | `berlekamp_massey`, `linear_recurrence` |
| [math/linear_algebra.py](library/math/linear_algebra.py) | `matrix_det`, `matrix_rank`, `inverse_matrix`, `linear_equations` |
| [math/number_theory.py](library/math/number_theory.py) | `pow_mod`, `inv_gcd`, `inv_mod`, `crt`, `floor_sum`, `discrete_log`, `sqrt_mod` |
| [math/polynomial.py](library/math/polynomial.py) | `butterfly`, `butterfly_inv`, `convolution`, `autocorrelation`, `FormalPowerSeries`, `poly_coef`, `subset_sum`, `partition_function`, `bernoulli_number`, `stirling_first`, `stirling_second`, `polynomial_interpolation`, `Mat2`, `poly_gcd`, `poly_inv`, `fps_inverse`, `fps_log`, `fps_exp`, `fps_power`, `fps_sqrt`, `bostan_mori`, `polynomial_gcd`, `polynomial_inverse` |
| [math/scalar.py](library/math/scalar.py) | `ModContext`, `Modint`, `raw`, `ModInt`（旧形式） |
| [search/heuristics.py](library/search/heuristics.py) | `beam_search`, `negamax`, `tsp_nearest_neighbor`, `tsp_two_opt` |
| [search/numeric.py](library/search/numeric.py) | `normal_cdf`, `kmeans` |
| [strings/matching.py](library/strings/matching.py) | `prefix_function`, `kmp_search`, `manacher`, `edit_distance`, `lcs_length` |
| [strings/rolling_hash.py](library/strings/rolling_hash.py) | `RollingHash`, `RollingHashSegTree` |
| [strings/suffix_array.py](library/strings/suffix_array.py) | `suffix_array`, `lcp_array`, `z_algorithm` |
| [strings/trie.py](library/strings/trie.py) | `Trie`, `AhoCorasick` |
| [structures/avl_tree.py](library/structures/avl_tree.py) | `AVLTree` |
| [structures/aggregate_queue.py](library/structures/aggregate_queue.py) | `AggregateQueue` |
| [structures/binary_trie.py](library/structures/binary_trie.py) | `BinaryTrie` |
| [structures/bit_set.py](library/structures/bit_set.py) | `BitSet` |
| [structures/cartesian_tree.py](library/structures/cartesian_tree.py) | `CartesianTree` |
| [structures/dynamic_fenwick.py](library/structures/dynamic_fenwick.py) | `DynamicFenwickTree`, `DynamicFenwickTree2D` |
| [structures/li_chao.py](library/structures/li_chao.py) | `LiChaoTree`, `LiChaoInt` |
| [structures/linked_list.py](library/structures/linked_list.py) | `LinkedList` |
| [structures/max_queue.py](library/structures/max_queue.py) | `MaxQueue` |
| [structures/mo.py](library/structures/mo.py) | `mo_order`, `mo_solve` |
| [structures/priority_sum.py](library/structures/priority_sum.py) | `PrioritySumStructure` |
| [structures/range_arithmetic.py](library/structures/range_arithmetic.py) | `ArithmeticSegmentTree` |
| [structures/slope_trick.py](library/structures/slope_trick.py) | `SlopeTrick` |
| [structures/sorted_set.py](library/structures/sorted_set.py) | `SortedSet`, `SortedMultiset` |
| [structures/sqrt_decomposition.py](library/structures/sqrt_decomposition.py) | `SqrtDecomposition` |
| [structures/wavelet_matrix.py](library/structures/wavelet_matrix.py) | `FullyIndexableDictionary`, `WaveletMatrix` |
