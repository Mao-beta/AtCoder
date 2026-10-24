# Library Checkerへの対応

更新：2026-10-18。第2弾として50問を追加し、提出用コードを生成できる問題は合計60問になった。AtCoder青以上を目安に、永続化・オフライン処理・区間更新・木の経路・多項式計算を優先した。色は用途を選ぶ目安で、問題の公式難度区分ではない。

[公式一覧](https://github.com/yosupo06/library-checker-problems/blob/1814c4e5205517e368bb57a8d1127eb961cfeaae/categories.toml)の235問題のうち、ここでいう「対応済み」は入出力アダプター・1ファイル生成・公式サンプルのローカル検査まで用意した60問を指す。オンラインACの記録ではない。[ライブラリ別のverify候補](../VERIFY_PROBLEMS.md)には、提出アダプターがまだない問題も含む。

## 第2弾：今回追加した50問

新規ファイルは8個。RollbackDSU、PersistentQueue、AggregateDeque、DynamicSequence、OfflineFenwick2D、静的区間種類数、閉路復元、GF(2)行列を追加した。既存のHLD・LowLink・木・文字列・多項式・bit変換も拡張し、二部マッチングを非再帰Hopcroft–Karpへ更新した。残りの対応は、既存APIに提出用の入出力を接続したもの。

使い方は各ファイル先頭の通常のPythonコードと`# => 戻り値`、各APIのdocstringにある。検索パレットではFileを選んでF2で読める。

セグ木の派生版追加に伴い、range_affine_range_sum・range_affine_point_get・point_set_range_composite・staticrmqの4アダプターは設定済みのクラスを使う形に簡略化した。LCの対応数は60問のまま。別枠でセグ木の[AtCoder6問・12サンプル](../SEGTREE_RECIPES.md#verifyに使う問題)と、[ABC向け17問・47サンプル](../ABC_TOOLKIT.md#問題で確認する)を用意し、`build.py --atcoder 問題ID`で提出用コードを生成できる。

### データ構造・オフライン処理

| 問題ID | 使用するファイル | 使い方・条件 |
|---|---|---|
| [persistent_unionfind](https://judge.yosupo.jp/problem/persistent_unionfind) | [rollback_dsu](../library/structures/rollback_dsu.py) | RollbackDSU。版の木をオフラインDFSし、merge/undoで連結性を復元する。オンライン永続dsuではない。 |
| [persistent_queue](https://judge.yosupo.jp/problem/persistent_queue) | [persistent_queue](../library/structures/persistent_queue.py) | PersistentQueue。版0が空。appendは新しい版、popleftは(新しい版,値)。過去の版を保持。 |
| [deque_operate_all_composite](https://judge.yosupo.jp/problem/deque_operate_all_composite) | [aggregate_deque](../library/structures/aggregate_deque.py) | AggregateDeque。op(f,g)=g∘f、前後の追加・削除は償却O(1)回のop。 |
| [range_affine_range_sum](https://judge.yosupo.jp/problem/range_affine_range_sum) | [lazy_segtree_actions](../library/structures/lazy_segtree_actions.py) | range_affine_sum(A)。apply(l,r,(a,b))とprod(l,r)。和は数値で返る。 |
| [range_affine_point_get](https://judge.yosupo.jp/problem/range_affine_point_get) | [lazy_segtree_actions](../library/structures/lazy_segtree_actions.py) | range_affine_sum(A)。apply(l,r,(a,b))とget(i)。要素は数値で返る。 |
| [range_chmin_chmax_add_range_sum](https://judge.yosupo.jp/problem/range_chmin_chmax_add_range_sum) | [SegmentTreeBeats](../snippets/structures/SegmentTreeBeats.py) | SegmentTreeBeats。chmin/chmax/add/sum。 |
| [point_set_range_composite](https://judge.yosupo.jp/problem/point_set_range_composite) | [segtree_monoids](../library/structures/segtree_monoids.py) | range_affine_composite(V)。先に左、次に右の一次関数を適用する非可換集約。 |
| [line_add_get_min](https://judge.yosupo.jp/problem/line_add_get_min) | [li_chao](../library/structures/li_chao.py) | LiChaoTree(xs)。全ての問い合わせ座標を先に登録し、直線を追加。 |
| [range_kth_smallest](https://judge.yosupo.jp/problem/range_kth_smallest) | [wavelet_matrix](../library/structures/wavelet_matrix.py) | WaveletMatrix.kth_smallest(l,r,k)。kは0-indexed。 |
| [static_range_frequency](https://judge.yosupo.jp/problem/static_range_frequency) | [wavelet_matrix](../library/structures/wavelet_matrix.py) | WaveletMatrix.count(l,r,x)。値xの出現数。空列・空区間に対応。 |
| [static_range_count_distinct](https://judge.yosupo.jp/problem/static_range_count_distinct) | [offline_queries](../library/structures/offline_queries.py) | range_count_distinct(a,queries)。右端順の処理とFenwick木、結果は入力順。 |
| [point_add_rectangle_sum](https://judge.yosupo.jp/problem/point_add_rectangle_sum) | [fenwick_2d](../library/structures/fenwick_2d.py) | OfflineFenwick2D。全更新座標を事前登録。点加算・半開長方形和O(log² N)。 |
| [dynamic_sequence_range_affine_range_sum](https://judge.yosupo.jp/problem/dynamic_sequence_range_affine_range_sum) | [dynamic_sequence](../library/structures/dynamic_sequence.py) | DynamicSequence。挿入・削除・反転・一次変換・和は期待O(log N)。法998244353。 |
| [range_reverse_range_sum](https://judge.yosupo.jp/problem/range_reverse_range_sum) | [dynamic_sequence](../library/structures/dynamic_sequence.py) | DynamicSequence(mod=0)。区間反転と整数の区間和。 |
| [set_xor_min](https://judge.yosupo.jp/problem/set_xor_min) | [binary_trie](../library/structures/binary_trie.py) | BinaryTrie.min_xor(x)。挿入前のcountで集合として重複を防ぐ。 |
| [staticrmq](https://judge.yosupo.jp/problem/staticrmq) | [segtree_monoids](../library/structures/segtree_monoids.py) | range_min(A)。半開区間の最小値。 |

### グラフ・木

| 問題ID | 使用するファイル | 使い方・条件 |
|---|---|---|
| [cycle_detection](https://judge.yosupo.jp/problem/cycle_detection) | [cycle](../library/graphs/cycle.py) | find_cycle(n,edges)。頂点列と入力辺ID列を復元。非再帰O(N+M)。 |
| [cycle_detection_undirected](https://judge.yosupo.jp/problem/cycle_detection_undirected) | [cycle](../library/graphs/cycle.py) | find_cycle(...,directed=False)。自己ループ・多重辺も閉路として扱う。 |
| [jump_on_tree](https://judge.yosupo.jp/problem/jump_on_tree) | [hld](../library/graphs/hld.py) | HLD.jump(u,v,k)。uからvへの経路でk辺先。経路外なら-1。O(log N)。 |
| [tree_diameter](https://judge.yosupo.jp/problem/tree_diameter) | [tree](../library/graphs/tree.py) | weighted_tree_diameter。非負重みの木から(距離,頂点経路)を返す。 |
| [two_edge_connected_components](https://judge.yosupo.jp/problem/two_edge_connected_components) | [lowlink](../library/graphs/lowlink.py) | LowLink.two_edge_connected_components。橋を除いた連結成分。各頂点は1成分。 |
| [lca](https://judge.yosupo.jp/problem/lca) | [LCATree](../snippets/structures/LCATree.py) | LCATree.lca(u,v)。親配列から無向辺リストを作る。頂点0..N-1、root=0。 |
| [vertex_set_path_composite](https://judge.yosupo.jp/problem/vertex_set_path_composite) | [hld](../library/graphs/hld.py) | HLD＋BiSegTree＋path_prod。u→vの向きを保って一次関数を合成。 |
| [vertex_add_path_sum](https://judge.yosupo.jp/problem/vertex_add_path_sum) | [hld](../library/graphs/hld.py) | HLD＋BiSegTree。頂点値の一点加算と両端を含む経路和。 |
| [vertex_add_subtree_sum](https://judge.yosupo.jp/problem/vertex_add_subtree_sum) | [hld](../library/graphs/hld.py) / [BIT](../snippets/structures/BIT.py) | HLD.subtree_range＋fenwick_tree.sum。部分木には根の頂点自身も含む。 |
| [bipartitematching](https://judge.yosupo.jp/problem/bipartitematching) | [bipartite_matching](../library/graphs/bipartite_matching.py) | 非再帰Hopcroft–Karpへ更新。O((V+E)√V)、左右の相手配列を返す。 |
| [shortest_path](https://judge.yosupo.jp/problem/shortest_path) | [shortest_paths](../library/graphs/shortest_paths.py) | dijkstra＋restore_path。非負の有向辺、到達不可は-1。 |
| [scc](https://judge.yosupo.jp/problem/scc) | [scc](../library/graphs/scc.py) | scc(N,edges)。成分をトポロジカル順で出力。 |
| [two_sat](https://judge.yosupo.jp/problem/two_sat) | [scc](../library/graphs/scc.py) | two_sat。DIMACSの符号付き1-indexed変数を変換し、割当を出力。 |
| [minimum_spanning_tree](https://judge.yosupo.jp/problem/minimum_spanning_tree) | [mst](../library/graphs/mst.py) | minimum_spanning_forest。Kruskal法、採用辺IDを復元。 |

### 多項式・漸化式・畳み込み

| 問題ID | 使用するファイル | 使い方・条件 |
|---|---|---|
| [multipoint_evaluation](https://judge.yosupo.jp/problem/multipoint_evaluation) | [polynomial](../library/math/polynomial.py) | FPS.multipoint_evaluation(points)。係数は低次から。 |
| [polynomial_interpolation](https://judge.yosupo.jp/problem/polynomial_interpolation) | [polynomial](../library/math/polynomial.py) | polynomial_interpolation(xs,ys)。xsは法上で相異なる。戻り値.Funcが係数列。 |
| [polynomial_taylor_shift](https://judge.yosupo.jp/problem/polynomial_taylor_shift) | [polynomial](../library/math/polynomial.py) | FPS.taylor_shift(c)。f(x+c)の係数を返す。 |
| [division_of_polynomials](https://judge.yosupo.jp/problem/division_of_polynomials) | [polynomial](../library/math/polynomial.py) | polynomial_divmod(a,b)→(商,余り)。末尾0を除き、零多項式は[]。 |
| [convolution_mod](https://judge.yosupo.jp/problem/convolution_mod) | [polynomial](../library/math/polynomial.py) | FFT(998244353).convolution(a,b)。shakayami/ACL-for-pythonのFFT形式。 |
| [bitwise_and_convolution](https://judge.yosupo.jp/problem/bitwise_and_convolution) | [bit_transforms](../library/math/bit_transforms.py) | and_convolution(a,b)。等長2^k、ANDで添字を合成。O(k 2^k)。 |
| [kth_term_of_linearly_recurrent_sequence](https://judge.yosupo.jp/problem/kth_term_of_linearly_recurrent_sequence) | [polynomial](../library/math/polynomial.py) | linear_recurrence_ntt。Bostan–MoriでO(M(d)log k)。係数c[j]はa[t-j-1]に掛かる。 |
| [find_linear_recurrence](https://judge.yosupo.jp/problem/find_linear_recurrence) | [linear_recurrence](../library/math/linear_recurrence.py) | berlekamp_massey。最短の漸化式を推定、O(N²)。係数の順序は上と同じ。 |
| [pow_of_formal_power_series](https://judge.yosupo.jp/problem/pow_of_formal_power_series) | [polynomial](../library/math/polynomial.py) | fps_power(a,exponent,size)。sizeは係数数、0乗は1。 |
| [sqrt_of_formal_power_series](https://judge.yosupo.jp/problem/sqrt_of_formal_power_series) | [polynomial](../library/math/polynomial.py) | fps_sqrt(a,size)。平方根がなければNone。根は非一意なので二乗して検査。 |
| [inv_of_formal_power_series](https://judge.yosupo.jp/problem/inv_of_formal_power_series) | [polynomial](../library/math/polynomial.py) | fps_inverse(a,size)。a[0]≠0。 |
| [log_of_formal_power_series](https://judge.yosupo.jp/problem/log_of_formal_power_series) | [polynomial](../library/math/polynomial.py) | fps_log(a,size)。a[0]=1。 |
| [exp_of_formal_power_series](https://judge.yosupo.jp/problem/exp_of_formal_power_series) | [polynomial](../library/math/polynomial.py) | fps_exp(a,size)。a[0]=0。 |
| [inv_of_polynomials](https://judge.yosupo.jp/problem/inv_of_polynomials) | [polynomial](../library/math/polynomial.py) | polynomial_inverse(a,g)。逆元なしNone、非零定数を法とした場合は[]。 |

### 文字列・GF(2)・幾何

| 問題ID | 使用するファイル | 使い方・条件 |
|---|---|---|
| [longest_common_substring](https://judge.yosupo.jp/problem/longest_common_substring) | [suffix_array](../library/strings/suffix_array.py) | longest_common_substring(s,t)→(a,b,c,d)。s[a:b]=t[c:d]が最長。 |
| [enumerate_palindromes](https://judge.yosupo.jp/problem/enumerate_palindromes) | [matching](../library/strings/matching.py) | manacher(s)。奇数・偶数半径から、文字上と文字間の回文長を交互に出力。 |
| [inverse_matrix_mod_2](https://judge.yosupo.jp/problem/inverse_matrix_mod_2) | [gf2_matrix](../library/math/gf2_matrix.py) | inverse_matrix_gf2(rows)。bit jが列j。特異ならNone。任意精度整数を使う。 |
| [matrix_rank_mod_2](https://judge.yosupo.jp/problem/matrix_rank_mod_2) | [gf2_matrix](../library/math/gf2_matrix.py) | matrix_rank_gf2(rows,columns)。0行・0列を含む矩形行列に対応。 |
| [matrix_product_mod_2](https://judge.yosupo.jp/problem/matrix_product_mod_2) | [gf2_matrix](../library/math/gf2_matrix.py) | matrix_product_gf2(a,b,columns)。8列ずつXOR表を作って行列積を計算。 |
| [area_of_union_of_rectangles](https://judge.yosupo.jp/problem/area_of_union_of_rectangles) | [rectangle_union](../library/geometry/rectangle_union.py) | rectangle_union_area。座標順は(left,bottom,right,top)、面積を整数で返す。 |

## 第1弾：対応済みの10問

| 問題 | 使用するAPI | 主な用途・条件 |
|---|---|---|
| [Queue Operate All Composite](https://judge.yosupo.jp/problem/queue_operate_all_composite) | [AggregateQueue(op,e)](../library/structures/aggregate_queue.py) | SWAG。非可換な関数合成を含む、キュー全体の集約。追加・先頭削除は償却O(1)回のop。 |
| [Segment Add Get Min](https://judge.yosupo.jp/problem/segment_add_get_min) | [LiChaoTree(xs).add_segment(l,r,a,b)](../library/structures/li_chao.py) | 区間内だけ有効な直線、最小化DP。座標は事前登録、区間は[l,r)。追加O(log²n)、問い合わせO(log n)。 |
| [Biconnected Components](https://judge.yosupo.jp/problem/biconnected_components) | [LowLink.biconnected_components / block_cut_tree](../library/graphs/lowlink.py) | 関節点をまたぐ経路・連結性の問題。孤立点・多重辺対応、非再帰O(V+E)。 |
| [Assignment Problem](https://judge.yosupo.jp/problem/assignment) | [assignment(cost)](../library/graphs/assignment.py) | Hungarian法。負費用可、行数n≤列数m、O(n²m)。最適費用と割当先を返す。 |
| [Determinant of Matrix](https://judge.yosupo.jp/problem/matrix_det) | [matrix_det(a,mod)](../library/math/linear_algebra.py) | 素数mod上の行列式、O(n³)。合成数modには対応しない。 |
| [Rank of Matrix](https://judge.yosupo.jp/problem/matrix_rank) | [matrix_rank(a,mod)](../library/math/linear_algebra.py) | 矩形行列・0行/0列対応。O(nm min(n,m))。 |
| [Inverse Matrix](https://judge.yosupo.jp/problem/inverse_matrix) | [inverse_matrix(a,mod)](../library/math/linear_algebra.py) | 逆行列。特異ならNone。O(n³)。 |
| [System of Linear Equations](https://judge.yosupo.jp/problem/system_of_linear_equations) | [linear_equations(a,b,mod)](../library/math/linear_algebra.py) | 特解と同次解の基底を返す。解なしNone。自由変数・不定系も扱う。 |
| [System of Linear Equations (Mod 2)](https://judge.yosupo.jp/problem/system_of_linear_equations_mod_2) | [linear_equations_gf2(rows,rhs,variables)](../library/math/bit_transforms.py) | XOR制約。行・解・基底を整数bitsetで表す。特解だけでよければsolve_gf2が(rank,特解)を返す。両APIとも解なしはNone。 |
| [Bitwise Xor Convolution](https://judge.yosupo.jp/problem/bitwise_xor_convolution) | [xor_convolution(a,b,mod)](../library/math/bit_transforms.py) | XORで添字を合成する数え上げ。FWHT、O(n log n)。同じ長さ2^k、奇数mod。 |

## 提出用の1ファイルを作る

リポジトリ直下で実行する。検索パレットからは今までどおり、必要なライブラリだけをコピーできる。

```powershell
Set-Location D:\Kyopro\AtCoder
# 対応している問題ID
.\.venv\Scripts\python.exe cp_snippet_palette\verify\build.py --list
# ライブラリと入出力をまとめる
.\.venv\Scripts\python.exe cp_snippet_palette\verify\build.py segment_add_get_min
```

生成先は`cp_snippet_palette/verify/build/segment_add_get_min.py`。このファイル全体をLibrary Checkerに提出する。生成物にはローカルライブラリのimportを残さず、標準ライブラリだけで動作する。再生成すると同名の生成物を更新するため、問題固有の入出力を直す場合は`library_checker/`側を編集する。`build/`はGitの対象外。

ローカル実行は次の形式。入力ファイル名は自分のものに置き換える。

```powershell
Get-Content .\input.txt | & D:\Kyopro\.python\pypy-3.11.15-windows-x86_64-none\pypy3.exe -B cp_snippet_palette\verify\build\segment_add_get_min.py
```

アダプター自体も、リポジトリ直下から`python -m cp_snippet_palette.verify.library_checker.segment_add_get_min`の形式で実行できる。提出にはbuildでまとめたファイルを使う。

## 確認済みの範囲

- 2026-10-18のAPI整理後、影響するLC 13問17サンプルをPyPyで確認し、提出コードを再生成した。新APIの使用例は17ファイル70件、関連するライブラリ・LC・検索の47テストはCPythonで確認。以下は追加時点の確認記録。
- Windows版PyPy 7.3.23 / Python 3.11.15で、既存34テスト、第1弾7テスト、第2弾6テストを確認。
- 60問・公式サンプル入力114件を、生成した提出コードの独立プロセスで検査。今回の追加分は50問・91件。愚直計算と照合し、閉路・マッチング・SCC・木の直径・逆行列・多項式平方根などの非一意な出力は条件を検査した。
- 新規構造の版分岐、巻き戻し、両端操作、動的数列の挿入・削除・反転・一次変換、長方形和を小規模ランダム入力で照合。Hopcroft–Karpは総当たり最大マッチング、AND畳み込みは二重ループと比較した。
- 第2弾の規模確認：永続キュー50万追加、動的数列50万要素＋2千回の反転・一次変換・和、二次元Fenwick木10万点追加、50万頂点の有向閉路、左右10万頂点の長い増加路を持つ二部マッチング、GF(2) 512×512行列、65536×65536のNTT畳み込み。FPSのlog/exp・逆数・平方根は2048係数で恒等式を確認し、多項式除算・評価・補間・逆元はNTTを通るサイズでも確認した。
- 第1弾では割当500×500、逆行列500×500、XOR畳み込み2^20要素、GF(2)方程式4096×4096、二重連結成分50万頂点のパス、区間直線N=Q=20万の代表入力も確認済み。
- 公式ジェネレーターの全テスト・オンライン提出・AC判定は未実施。代表入力は全ての最悪ケースの時間・メモリ制限を保証しない。特に動的数列や大きなFPSは操作内容により負荷が変わる。Codonコンパイルも未確認。GF(2) bitsetと永続キューのarray利用はPyPyを前提にしている。

```powershell
& D:\Kyopro\.python\pypy-3.11.15-windows-x86_64-none\pypy3.exe -B cp_snippet_palette\tests\test_library.py -v
& D:\Kyopro\.python\pypy-3.11.15-windows-x86_64-none\pypy3.exe -B cp_snippet_palette\tests\test_library_checker.py -v
& D:\Kyopro\.python\pypy-3.11.15-windows-x86_64-none\pypy3.exe -B cp_snippet_palette\tests\test_library_checker_round2.py -v
```

サンプル入力の出典・リビジョンは[samples/README.md](samples/README.md)に記載。テスト実行時にネット接続や追加パッケージは不要。

## 次の追加候補

- [Dynamic Graph Vertex Add Component Sum](https://judge.yosupo.jp/problem/dynamic_graph_vertex_add_component_sum)：Rollback dsuに成分集約と辺の生存区間処理を組み合わせる。
- [Subset Convolution](https://judge.yosupo.jp/problem/subset_convolution)、[Convolution (Mod 1000000007)](https://judge.yosupo.jp/problem/convolution_mod_1000000007)：集合冪級数と別の法の畳み込み。
- [Directed MST](https://judge.yosupo.jp/problem/directedmst)、[Minimum Cost b-flow](https://judge.yosupo.jp/problem/min_cost_b_flow)：有向最小全域木と需要付き最小費用流。
- [Frequency Table of Tree Distance](https://judge.yosupo.jp/problem/frequency_table_of_tree_distance)：重心分解と畳み込みによる木の距離集計。
- [Closest Pair](https://judge.yosupo.jp/problem/closest_pair)、[Minimum Steiner Tree](https://judge.yosupo.jp/problem/minimum_steiner_tree)：既存の値のみのAPIに点ID・辺の復元を追加する。

## ABC向けの追加

[ABC向けガイド](../ABC_TOOLKIT.md)の17問を追加し、AtCoderのアダプターは合計23問・公式サンプル59件。ABC19問・ABL1問・practice2の1問・EDPC1問・典型90の1問を含む。LCは60問のまま。`build.py --atcoder --list`で一覧、`build.py --atcoder abc330_e`で提出ファイルを生成する。
