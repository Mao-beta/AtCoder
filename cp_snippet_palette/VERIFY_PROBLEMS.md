# ライブラリ別verify問題一覧

確認日：2026-10-17。提出用の全71ファイル（library 54、snippets 17）を対象に、AtCoder公式問題文とLibrary Checkerの公式問題リポジトリから選んだ。問題数は重複を除いて133問。

**問題の推薦表であり、オンラインジャッジでのAC実績表ではない。** 今回は問題の内容・出力形式とAPIを照合した。提出、全ケースの実行、最大制約での速度確認は行っていない。APIの統一内容は[ACL_API.md](ACL_API.md)、一般の使い方は[LIBRARY_GUIDE.md](LIBRARY_GUIDE.md)を参照。

パレットではF2の「API・verify」に選択中のファイルの行を表示する。FPSなどの関数ごとの追加問題は、この文書の「同梱機能の追加問題」を参照する。画面内の「全verify問題」からこの文書を開ける。

青以上の用途を優先した追加対応では、下表のうち10問題に提出用の1ファイル生成と公式サンプル入力の検査を用意した。対応済みの問題・コマンド・今後の候補は[Library Checker対応状況](verify/README.md)を参照。オンラインAC済みという意味ではない。

- **直接**：主処理をそのAPIで実装できる。入出力の読み書きと番号変換は必要。
- **応用／補助**：そのAPIを使うが、問題固有の変換や別の処理も必要。
- **部分確認**：APIの一部、または小さいケースだけを検査できる。現APIのまま全制約でACできる候補とはしない。
- **未選定**：適切な基本問題を今回確認できなかった。無関係な問題を無理に対応させず、ローカル確認内容を記した。

まずはpractice2 A/B/G/J/K、LCのSuffix Array・Z Algorithm・Convolutionから始めると、番号や半開区間の変換が少ない。非可換な演算や境界探索は別問題・ローカル例を足して確認する。[AtCoder Library Practice Contest](https://atcoder.jp/contests/practice2/tasks)

## ACLの定番問題

| API | 最初の1問 | 次に確認する内容 |
|---|---|---|
| DSU | [practice2 A Disjoint Set Union](https://atcoder.jp/contests/practice2/tasks/practice2_a) | mergeの戻り値、size/groupsはローカルでも確認 |
| FenwickTree | [practice2 B Fenwick Tree](https://atcoder.jp/contests/practice2/tasks/practice2_b) | 空区間・負の加算 |
| SegTree | [practice2 J Segment Tree](https://atcoder.jp/contests/practice2/tasks/practice2_j) | [Point Set Range Composite](https://judge.yosupo.jp/problem/point_set_range_composite)で順序依存の集約 |
| LazySegTree | [practice2 K Range Affine Range Sum](https://atcoder.jp/contests/practice2/tasks/practice2_k) | [practice2 L Lazy Segment Tree](https://atcoder.jp/contests/practice2/tasks/practice2_l)で反転と転倒数 |
| SCCGraph / TwoSAT | [practice2 G SCC](https://atcoder.jp/contests/practice2/tasks/practice2_g) / [2 Sat](https://judge.yosupo.jp/problem/two_sat) | 成分順・充足不能・空グラフ |
| MFGraph / MCFGraph | [practice2 D Maxflow](https://atcoder.jp/contests/practice2/tasks/practice2_d) / [practice2 E MinCostFlow](https://atcoder.jp/contests/practice2/tasks/practice2_e) | 流量からの復元・非負費用への変換 |
| floor_sum / convolution | [practice2 C Floor Sum](https://atcoder.jp/contests/practice2/tasks/practice2_c) / [practice2 F Convolution](https://atcoder.jp/contests/practice2/tasks/practice2_f) | mod、空列、負入力をAPIの契約内で確認 |
| suffix_array / lcp_array / z_algorithm | [Suffix Array](https://judge.yosupo.jp/problem/suffixarray) / [practice2 I Number of Substrings](https://atcoder.jp/contests/practice2/tasks/practice2_i) / [Z Algorithm](https://judge.yosupo.jp/problem/zalgorithm) | 整数列とupper指定はローカルで補う |

## 基本処理

| ファイル | 問題 | 検証範囲・合わせ方 |
|---|---|---|
| [basic/doubling.py](library/basic/doubling.py) | [ABC167 D Teleporter](https://atcoder.jp/contests/abc167/tasks/abc167_d) | 直接：K回遷移。町番号を0-indexedにし、max_steps=K。終端-1は別途ローカル確認。 |
| [basic/grid.py](library/basic/grid.py) | [ABC218 C Shapes](https://atcoder.jp/contests/abc218/tasks/abc218_c) | 応用：rotate90と座標集合の平行移動を使う。transpose・添字変換は補助機能。 |
| [basic/matrix.py](library/basic/matrix.py) | [Matrix Product](https://judge.yosupo.jp/problem/matrix_product)<br>[Pow of Matrix](https://judge.yosupo.jp/problem/pow_of_matrix) | 直接：行列積・累乗。mod=998244353。max_plus系はこの2問の対象外。 |
| [basic/prefix_sum_2d.py](library/basic/prefix_sum_2d.py) | [ABC005 D おいしいたこ焼きの焼き方](https://atcoder.jp/contests/abc005/tasks/abc005_4) | 応用：全長方形を列挙し、rectangle_sumで面積別最大値を求める。境界は半開区間。 |
| [basic/sequence.py](library/basic/sequence.py) | [Longest Increasing Subsequence](https://judge.yosupo.jp/problem/longest_increasing_subsequence)<br>[ABC213 C Reorder Cards](https://atcoder.jp/contests/abc213/tasks/abc213_c)<br>[ABC259 C XX to XXX](https://atcoder.jp/contests/abc259/tasks/abc259_c) | LISは直接：値ではなく復元した添字を出力。座標圧縮はABC213 C、RLEはABC259 C。転倒数は次表に補足。 |
| [basic/sliding_window.py](library/basic/sliding_window.py) | [ABC189 C Mandarin Orange](https://atcoder.jp/contests/abc189/tasks/abc189_c)<br>[ABC228 F Stamp Game](https://atcoder.jp/contests/abc228/tasks/abc228_f) | ヒストグラム最大長方形はABC189 Cで直接確認。ABC228 Fは2D累積和と、符号反転したarea_min_slidingの応用。2D最大長方形はローカル確認を補う。 |
| [basic/subset_dp.py](library/basic/subset_dp.py) | [DP D Knapsack 1](https://atcoder.jp/contests/dp/tasks/dp_d)<br>[ABC184 F Programming Contest](https://atcoder.jp/contests/abc184/tasks/abc184_f)<br>[典型90 051 Typical Shop](https://atcoder.jp/contests/typical90/tasks/typical90_ay)<br>[ABC204 D Cooking](https://atcoder.jp/contests/abc204/tasks/abc204_d) | 0/1ナップサック、半分全列挙、個数別部分和、bitset部分和の順。itemsは(重さ,価値)。ABC204 Dは全体和と到達可能和から2台の完了時間を最小化。 |

## データ構造（抽出ライブラリ）

| ファイル | 問題 | 検証範囲・合わせ方 |
|---|---|---|
| [structures/aggregate_queue.py](library/structures/aggregate_queue.py) | [Queue Operate All Composite](https://judge.yosupo.jp/problem/queue_operate_all_composite) | 直接：AggregateQueue(op,(1,0))。op(f,g)はg∘f、append/popleft/prodを使う。空のprodは恒等写像。提出アダプターあり。 |
| [structures/avl_tree.py](library/structures/avl_tree.py) | [Ordered Set](https://judge.yosupo.jp/problem/ordered_set)<br>[Associative Array](https://judge.yosupo.jp/problem/associative_array) | 辞書は直接。Ordered Setはkth(k-1)へ変換し、rank（x以下の個数）クエリはkth上の二分探索などを補う。rankは現APIにないためそのままでは全操作に対応しない。 |
| [structures/binary_trie.py](library/structures/binary_trie.py) | [Set Xor-Min](https://judge.yosupo.jp/problem/set_xor_min) | 直接：min_xor(x)。この問題は集合なので重複挿入をcountで防ぐ。多重集合の仕様と区別。 |
| [structures/bit_set.py](library/structures/bit_set.py) | [ABC258 G Triangle](https://atcoder.jp/contests/abc258/tasks/abc258_g) | 応用：行ごとのbitsetのANDとpopcountで三角形数を数える。ANDはbits同士の整数演算を使う。shiftedは対象外。 |
| [structures/cartesian_tree.py](library/structures/cartesian_tree.py) | [Cartesian Tree](https://judge.yosupo.jp/problem/cartesian_tree) | 直接：parent配列。内部の根の親-1を、問題指定の根自身の番号に直す。 |
| [structures/dynamic_fenwick.py](library/structures/dynamic_fenwick.py) | [Point Add Range Sum](https://judge.yosupo.jp/problem/point_add_range_sum)<br>[Point Add Rectangle Sum](https://judge.yosupo.jp/problem/point_add_rectangle_sum) | 直接：1D／2Dの点加算・半開区間和。2Dではx/yとrow/columnの順を固定。辞書版は大入力でメモリ・時間の実測が必要。 |
| [structures/li_chao.py](library/structures/li_chao.py) | [Line Add Get Min](https://judge.yosupo.jp/problem/line_add_get_min)<br>[Segment Add Get Min](https://judge.yosupo.jp/problem/segment_add_get_min) | 直接：LiChaoIntは全域の直線。追加したLiChaoTree(xs)は全域と半開区間add_segment(l,r,a,b)に対応。座標を事前登録し、有効な直線がないqueryのNoneをINFINITYに変換。区間版の提出アダプターあり。 |
| [structures/linked_list.py](library/structures/linked_list.py) | [ABC344 E Insert or Erase](https://atcoder.jp/contests/abc344/tasks/abc344_e) | 応用：値→ノードIDの辞書を別に持ち、insert_after/erase。値と内部ノードIDを混同しない。 |
| [structures/max_queue.py](library/structures/max_queue.py) | [ABC170 E Smart Infants](https://atcoder.jp/contests/abc170/tasks/abc170_e) | 応用：各園の最大値をキーごとに更新し、その最小値を取る。MaxQueueは最大値なので値の符号を反転。園内の多重集合は別途必要。 |
| [structures/mo.py](library/structures/mo.py) | [Static Range Count Distinct](https://judge.yosupo.jp/problem/static_range_count_distinct) | 直接：add/removeで頻度と種類数を更新し、answerで種類数を返す。mo_order単体では答えを計算しない。 |
| [structures/priority_sum.py](library/structures/priority_sum.py) | [ABC306 E Best Performances](https://atcoder.jp/contests/abc306/tasks/abc306_e) | 応用：上位K個の和。下位k個用なので値を負にしてqueryの符号を戻す。重複・K=0も確認。 |
| [structures/range_arithmetic.py](library/structures/range_arithmetic.py) | [Point Add Range Sum](https://judge.yosupo.jp/problem/point_add_range_sum) | 部分確認：長さ1のaddとsum。等差数列の区間add/assignを直接検査する基本問題は今回未選定。step≠0、重なる代入・加算は既存ローカルテストで確認。 |
| [structures/slope_trick.py](library/structures/slope_trick.py) | [ABC127 F Absolute Minima](https://atcoder.jp/contests/abc127/tasks/abc127_f) | 応用：add_abs(a)、add_constant(b)、argminと最小値。shift・prefix_min・suffix_minはこの問題では確認できない。 |
| [structures/sorted_set.py](library/structures/sorted_set.py) | [Ordered Set](https://judge.yosupo.jp/problem/ordered_set)<br>[ABC241 D Sequence Query](https://atcoder.jp/contests/abc241/tasks/abc241_d) | SortedSetはLCで直接、SortedMultisetはABC241 Dで重複と順位を確認。LCの順位とローカルの0-indexed順位を変換。 |
| [structures/sqrt_decomposition.py](library/structures/sqrt_decomposition.py) | [Point Add Range Sum](https://judge.yosupo.jp/problem/point_add_range_sum) | 部分確認：add(p,p+1,x)とsum(l,r)。長い区間への加算とバケット境界は既存ローカルテストで補う。 |
| [structures/wavelet_matrix.py](library/structures/wavelet_matrix.py) | [Range Kth Smallest](https://judge.yosupo.jp/problem/range_kth_smallest)<br>[Static Range Frequency](https://judge.yosupo.jp/problem/static_range_frequency) | 直接：kth_smallest(l,r,k)はLCと同じ0-indexed。頻度はrange_rankを利用。旧quantile/selectは1-indexedなので使い分ける。 |

## グラフ・木

| ファイル | 問題 | 検証範囲・合わせ方 |
|---|---|---|
| [graphs/assignment.py](library/graphs/assignment.py) | [Assignment Problem](https://judge.yosupo.jp/problem/assignment) | 直接：assignment(cost)の最適費用と割当列を出力。負費用可。長方形n≤mは独自拡張で、LCは正方行列。提出アダプターあり。 |
| [graphs/bipartite_matching.py](library/graphs/bipartite_matching.py) | [Matching on Bipartite Graph](https://judge.yosupo.jp/problem/bipartitematching) | 直接：左右のマッチ配列からサイズと辺を出力。O(L*E)なので最大制約での速度は別途確認。 |
| [graphs/centroid_decomposition.py](library/graphs/centroid_decomposition.py) | [ABC291 Ex Balanced Tree](https://atcoder.jp/contests/abc291/tasks/abc291_h) | 直接：重心分解木の親配列。根は-1、他は1-indexedに戻す。基本操作そのものだがABC Exであり難度は高い。 |
| [graphs/exponential.py](library/graphs/exponential.py) | [ABC180 E Traveling Salesman among Aerial Cities](https://atcoder.jp/contests/abc180/tasks/abc180_e)<br>[Minimum Steiner Tree](https://judge.yosupo.jp/problem/minimum_steiner_tree)<br>[Maximum Independent Set](https://judge.yosupo.jp/problem/maximum_independent_set)<br>[Chromatic Number](https://judge.yosupo.jp/problem/chromatic_number) | TSPは距離行列を作る応用、最大独立集合・彩色数は直接。Steiner問題は辺集合も出力するため費用のみの現APIは部分確認。Chinese Postmanは今回未選定。全て指数時間。 |
| [graphs/hld.py](library/graphs/hld.py) | [Vertex Add Path Sum](https://judge.yosupo.jp/problem/vertex_add_path_sum)<br>[Vertex Set Path Composite](https://judge.yosupo.jp/problem/vertex_set_path_composite) | 応用：HLD順の配列を構築しセグ木に載せる。非可換な関数合成はBiSegTreeとpath_fold_noncommで向きも確認。 |
| [graphs/lowlink.py](library/graphs/lowlink.py) | [Two-Edge-Connected Components](https://judge.yosupo.jp/problem/two_edge_connected_components)<br>[ABC075 C Bridge](https://atcoder.jp/contests/abc075/tasks/abc075_c)<br>[Biconnected Components](https://judge.yosupo.jp/problem/biconnected_components) | 橋を除く成分分解は追加DFS、ABC075 Cは橋の個数。頂点二重連結成分は追加したbiconnected_components()で直接出力。孤立点・多重辺に対応し、提出アダプターあり。block_cut_tree()は別途ローカル確認。 |
| [graphs/max_flow.py](library/graphs/max_flow.py) | [practice2 D Maxflow](https://atcoder.jp/contests/practice2/tasks/practice2_d)<br>[Matching on Bipartite Graph](https://judge.yosupo.jp/problem/bipartitematching) | 応用：source→左→右→sink、容量1。flowに加えedgesからマッチを復元。min_cut/change_edgeは別途ローカル確認。 |
| [graphs/min_cost_flow.py](library/graphs/min_cost_flow.py) | [practice2 E MinCostFlow](https://atcoder.jp/contests/practice2/tasks/practice2_e) | 応用：利得をC-aの非負コストに変換し、選択数を含めて利得を復元。負費用の辺をそのまま入れない。flowとslopeは同じ個体で併用しない。 |
| [graphs/mst.py](library/graphs/mst.py) | [Minimum Spanning Tree](https://judge.yosupo.jp/problem/minimum_spanning_tree) | 直接：コスト・採用辺IDを出力。入力が連結なため、非連結のminimum_spanning_forestはローカルで補う。 |
| [graphs/rerooting.py](library/graphs/rerooting.py) | [DP V Subtree](https://atcoder.jp/contests/dp/tasks/dp_v) | 応用：merge=積 mod M、identity=1、lift=(x+1) mod M。全頂点分の答えを確認。Mが素数とは限らない。 |
| [graphs/scc.py](library/graphs/scc.py) | [practice2 G SCC](https://atcoder.jp/contests/practice2/tasks/practice2_g)<br>[2 Sat](https://judge.yosupo.jp/problem/two_sat) | 直接：SCCGraph.scc()の成分順、TwoSAT.satisfiable()/answer()。DIMACS形式の±変数番号を(abs(x)-1,x>0)にする。 |
| [graphs/shortest_paths.py](library/graphs/shortest_paths.py) | [Shortest Path](https://judge.yosupo.jp/problem/shortest_path)<br>[ABC176 D Wizard in Maze](https://atcoder.jp/contests/abc176/tasks/abc176_d)<br>[ABC061 D Score Attack](https://atcoder.jp/contests/abc061/tasks/abc061_d)<br>[ABC012 D バスと避けられない運命](https://atcoder.jp/contests/abc012/tasks/abc012_4)<br>[DP G Longest Path](https://atcoder.jp/contests/dp/tasks/dp_g) | 順にDijkstra+経路復元、0-1 BFS、Bellman–Ford、Floyd–Warshall、トポロジカル順の応用。Floydでは各頂点の最大距離を最小化、DP Gでは得られた順序上で最長路DPを行う。ABC061 Dは符号反転と、終点へ到達できる頂点への制限が必要。 |
| [graphs/tree.py](library/graphs/tree.py) | [典型90 003 Longest Circular Road](https://atcoder.jp/contests/typical90/tasks/typical90_c)<br>[Vertex Add Subtree Sum](https://judge.yosupo.jp/problem/vertex_add_subtree_sum)<br>[ABC255 F Pre-order and In-order](https://atcoder.jp/contests/abc255/tasks/abc255_f) | 重みなし直径+1を典型90 003へ出力。LC Tree Diameterは重み付きなので現APIの直接verifyにはしない。部分木和はEuler TourとFenwickTreeを組み合わせる。ABC255 Fは走査順からの復元の応用で、子配列と入力妥当性検査の追加が必要。tree_centersは直径パスからローカル確認。 |

## 文字列

| ファイル | 問題 | 検証範囲・合わせ方 |
|---|---|---|
| [strings/matching.py](library/strings/matching.py) | [Enumerate Palindromes](https://judge.yosupo.jp/problem/enumerate_palindromes)<br>[ABC185 E Sequence Matching](https://atcoder.jp/contests/abc185/tasks/abc185_e)<br>[DP F LCS](https://atcoder.jp/contests/dp/tasks/dp_f) | Manacherは直接（奇数/偶数半径をLCの2n-1個の長さに変換）。編集距離は直接。DP FはLCS文字列の復元が必要でlcs_length単体では未完。KMP/prefix_functionは重なり・空パターンのローカル確認を補う。 |
| [strings/rolling_hash.py](library/strings/rolling_hash.py) | [ABC141 E Who Says a Pun?](https://atcoder.jp/contests/abc141/tasks/abc141_e)<br>[ABC331 F Palindrome Query](https://atcoder.jp/contests/abc331/tasks/abc331_f) | 応用：静的な部分文字列比較／更新付き回文判定。後者は順方向と逆方向の2本を持つ。ハッシュ衝突を検出し尽くせる検証ではない。 |
| [strings/suffix_array.py](library/strings/suffix_array.py) | [Suffix Array](https://judge.yosupo.jp/problem/suffixarray)<br>[practice2 I Number of Substrings](https://atcoder.jp/contests/practice2/tasks/practice2_i)<br>[Z Algorithm](https://judge.yosupo.jp/problem/zalgorithm) | 直接：SA、異なる部分文字列数=n(n+1)/2-sum(lcp)、Z配列。upper指定の整数列はローカル確認を追加。 |
| [strings/trie.py](library/strings/trie.py) | [ABC353 E Yet Another Sigma Problem](https://atcoder.jp/contests/abc353/tasks/abc353_e)<br>[ABC362 G Count Substring Query](https://atcoder.jp/contests/abc362/tasks/abc362_g) | Trieの応用：各接頭辞の既存個数を加算してから挿入。AhoCorasick.countはABC362 Gで直接確認。LC aho_corasickはオートマトン構造の出力問題で、このcount APIの直接verifyにはしない。 |

## 数論・代数

| ファイル | 問題 | 検証範囲・合わせ方 |
|---|---|---|
| [math/bit_transforms.py](library/math/bit_transforms.py) | [Rank of Matrix (Mod 2)](https://judge.yosupo.jp/problem/matrix_rank_mod_2)<br>[ABC141 F Xor Sum 3](https://atcoder.jp/contests/abc141/tasks/abc141_f)<br>[ABC281 F Xor Minimization](https://atcoder.jp/contests/abc281/tasks/abc281_f)<br>[Bitwise And Convolution](https://judge.yosupo.jp/problem/bitwise_and_convolution)<br>[System of Linear Equations (Mod 2)](https://judge.yosupo.jp/problem/system_of_linear_equations_mod_2)<br>[Bitwise Xor Convolution](https://judge.yosupo.jp/problem/bitwise_xor_convolution) | rankはsolve_gf2のrhs=0。linear_equations_gf2は特解と基底まで返し、文字列の左から変数0になるようbit順を変換する。xor_convolutionはFWHTによる直接対応。この2問は提出アダプターあり。AND畳み込みはsubset_zetaの添字反転・積・逆変換を組み合わせる。 |
| [math/combinatorics.py](library/math/combinatorics.py) | [ABC034 C 経路](https://atcoder.jp/contests/abc034/tasks/abc034_c)<br>[ABC084 D 2017-like Number](https://atcoder.jp/contests/abc084/tasks/abc084_d)<br>[ABC180 C Cream puff](https://atcoder.jp/contests/abc180/tasks/abc180_c)<br>[Binomial Coefficient (Prime Mod)](https://judge.yosupo.jp/problem/binomial_coefficient_prime_mod) | 二項係数・篩と累積和・約数の基本問題。LCでもn<modが保証されるため最大nまで前計算して使えるが、大きい前計算のメモリ・時間は別確認。permutation/homogeneousはローカルで補う。 |
| [math/factorize64.py](library/math/factorize64.py) | [Primality Test](https://judge.yosupo.jp/problem/primality_test)<br>[Factorize](https://judge.yosupo.jp/problem/factorize) | 直接：素数判定／素因数分解。factorizeの辞書を重複度分展開して昇順出力。試し割り版は同じ問題の小入力比較用。 |
| [math/linear_recurrence.py](library/math/linear_recurrence.py) | [Find Linear Recurrence](https://judge.yosupo.jp/problem/find_linear_recurrence)<br>[Kth term of Linearly Recurrent Sequence](https://judge.yosupo.jp/problem/kth_term_of_linearly_recurrent_sequence) | 直接：BM係数と第k項。係数は直前の項からの順。linear_recurrenceはO(d² log k)なのでLC大入力のTLEに注意。高速版はpolynomialのBostan–Moriを使う。 |
| [math/linear_algebra.py](library/math/linear_algebra.py) | [Determinant of Matrix](https://judge.yosupo.jp/problem/matrix_det)<br>[Rank of Matrix](https://judge.yosupo.jp/problem/matrix_rank)<br>[Inverse Matrix](https://judge.yosupo.jp/problem/inverse_matrix)<br>[System of Linear Equations](https://judge.yosupo.jp/problem/system_of_linear_equations) | 直接：素数mod=998244353。逆行列・方程式のNoneは-1。方程式では基底の本数が解空間の次元。0行/0列のrankにも対応。4問とも提出アダプターあり。合成数modの行列式は未対応。 |
| [math/number_theory.py](library/math/number_theory.py) | [practice2 C Floor Sum](https://atcoder.jp/contests/practice2/tasks/practice2_c)<br>[ABC193 E Oversleeping](https://atcoder.jp/contests/abc193/tasks/abc193_e)<br>[ABC186 E Throne](https://atcoder.jp/contests/abc186/tasks/abc186_e)<br>[Discrete Logarithm](https://judge.yosupo.jp/problem/discrete_logarithm_mod)<br>[Sqrt Mod](https://judge.yosupo.jp/problem/sqrt_mod) | floor_sumは直接、CRTと逆元はABCの応用、離散対数・平方根は直接。pow_modとinv_gcdは補助関数としてローカル境界確認。 |
| [math/polynomial.py](library/math/polynomial.py) | [practice2 F Convolution](https://atcoder.jp/contests/practice2/tasks/practice2_f)<br>[Convolution](https://judge.yosupo.jp/problem/convolution_mod) | convolution(998244353,a,b)で直接確認。FPSなど同梱する他機能は下の専用表に分ける。 |
| [math/scalar.py](library/math/scalar.py) | [ABC156 D Bouquet](https://atcoder.jp/contests/abc156/tasks/abc156_d)<br>[ABC168 E ∙ (Bullet)](https://atcoder.jp/contests/abc168/tasks/abc168_e) | ModintはABC156 Dで冪・四則・逆元を組み合わせる応用。ABC168 Eはベクトル正規化にFractionを使う補助例（垂直・零ベクトルは分岐）。modint専用のジャッジではない。 |

## 幾何・探索

| ファイル | 問題 | 検証範囲・合わせ方 |
|---|---|---|
| [geometry/convex.py](library/geometry/convex.py) | [Static Convex Hull](https://judge.yosupo.jp/problem/static_convex_hull)<br>[Furthest Pair of Points](https://judge.yosupo.jp/problem/furthest_pair)<br>[ABC296 G Polygon and Points](https://atcoder.jp/contests/abc296/tasks/abc296_g) | 凸包は直接。最遠点対は現APIが距離のみなので点IDの復元が必要。凸多角形内判定はABC296 Gで直接：0/1/2をOUT/ON/INに変換。 |
| [geometry/kd_tree.py](library/geometry/kd_tree.py) | [Rectangle Sum](https://judge.yosupo.jp/problem/rectangle_sum) | 応用：queryで返ったIDの重みを足す。列挙数に比例するため全制約の高速な矩形和verifyには不適。小ケースで境界と点の列挙を確認する用途。 |
| [geometry/plane_distance.py](library/geometry/plane_distance.py) | 未選定 | 未選定：3点が定める3D平面と点の距離に合うAtCoder基本問題／LC問題を今回確認できなかった。z=0平面、斜面、3点共線の例外をローカルで確認。 |
| [geometry/rectangle_union.py](library/geometry/rectangle_union.py) | [Area of Union of Rectangles](https://judge.yosupo.jp/problem/area_of_union_of_rectangles) | 直接：半開長方形(left,bottom,right,top)の和集合面積。重なり・接触・同じxのイベントを確認。 |
| [search/heuristics.py](library/search/heuristics.py) | [鉄則本 A46 Heuristic 1](https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_at) | TSPの近似解作成の用途例。nearest_neighbor→two_optを使い、出発点へ戻る出力を補う。スコア評価であり最適性のverifyではない。beam_search/negamaxの状態遷移は別途ローカル確認。 |
| [search/numeric.py](library/search/numeric.py) | 未選定 | 未選定：normal_cdfとkmeansには今回適切なAtCoder基本問題／LCの正誤ジャッジを見つけられなかった。CDFの対称性・既知値、k-meansの分離した点群を固定seedで確認。最適クラスタの保証はしない。 |

## 従来の構造スニペット（12ファイル）

| ファイル | 問題 | 検証範囲・合わせ方 |
|---|---|---|
| [structures/make_grid.py](snippets/structures/make_grid.py) | [ABC075 B Minesweeper](https://atcoder.jp/contests/abc075/tasks/abc075_b) | 補助：盤面の作成と隣接マス処理。配列の行が共有されないことはローカルで確認。 |
| [structures/KindDeque.py](snippets/structures/KindDeque.py) | [ABC210 C Colorful Candies](https://atcoder.jp/contests/abc210/tasks/abc210_c) | 応用：長さKの窓をappend/popleftしkindプロパティで種類数。rotateは対象外。 |
| [structures/UnionFind.py](snippets/structures/UnionFind.py) | [practice2 A Disjoint Set Union](https://atcoder.jp/contests/practice2/tasks/practice2_a) | 直接：DSU.merge/same。groups/size/leaderはローカルでも確認。UnionFindは旧名の別名。 |
| [structures/WeightedUnionFind.py](snippets/structures/WeightedUnionFind.py) | [ABC087 D People on a Line](https://atcoder.jp/contests/abc087/tasks/arc090_b) | 応用：w=weight[y]-weight[x]でunite(x,y,w)。矛盾の判定を行う。ACLの通常DSUと違う構造なので重み引数を保持。 |
| [structures/segtree.py](snippets/structures/segtree.py) | [practice2 J Segment Tree](https://atcoder.jp/contests/practice2/tasks/practice2_j)<br>[Point Set Range Composite](https://judge.yosupo.jp/problem/point_set_range_composite) | 直接：set/prod/max_right。非可換の合成はLCで確認。AtCoder側の1-indexed・閉区間を変換。 |
| [structures/SegTree_compat.py](snippets/structures/SegTree_compat.py) | [practice2 J Segment Tree](https://atcoder.jp/contests/practice2/tasks/practice2_j) | 旧API用：SegTree(v,op,e)、update/query。新規コードはsegtree.pyのSegTree(op,e,v)を使う。この2ファイルを同時に貼らない。 |
| [structures/lazy_segtree.py](snippets/structures/lazy_segtree.py) | [practice2 K Range Affine Range Sum](https://atcoder.jp/contests/practice2/tasks/practice2_k)<br>[practice2 L Lazy Segment Tree](https://atcoder.jp/contests/practice2/tasks/practice2_l) | 直接：アフィン更新・区間和／0,1反転・転倒数。後者は非可換集約も確認できる。1点applyや境界探索はローカルで補う。 |
| [structures/BIT.py](snippets/structures/BIT.py) | [practice2 B Fenwick Tree](https://atcoder.jp/contests/practice2/tasks/practice2_b) | 直接：FenwickTree.add/sum(l,r)。初期値はaddで入れるか配列拡張コンストラクタを使う。旧BIT.sum(i)とは区別。 |
| [structures/LCATree.py](snippets/structures/LCATree.py) | [Lowest Common Ancestor](https://judge.yosupo.jp/problem/lca)<br>[Jump on Tree](https://judge.yosupo.jp/problem/jump_on_tree) | 直接：ただしこのクラスは1-indexed。入出力を±1変換し、jumpが-1ならそのまま出力。 |
| [structures/Deque.py](snippets/structures/Deque.py) | [Deque](https://judge.yosupo.jp/problem/deque) | 直接：両端追加削除・添字アクセス。永続性はないためpersistent_queueは対応問題にしない。 |
| [structures/Heapq.py](snippets/structures/Heapq.py) | [ABC212 D Querying Multiset](https://atcoder.jp/contests/abc212/tasks/abc212_d) | 応用：全要素加算を外側のoffsetで処理し、push/top/pop。eraseと同じ値の再追加はローカルで補う。 |
| [structures/SegmentTreeBeats.py](snippets/structures/SegmentTreeBeats.py) | [Range Chmin Chmax Add Range Sum](https://judge.yosupo.jp/problem/range_chmin_chmax_add_range_sum) | 直接：半開区間のchmin/chmax/add/sum。全操作を混在させる定番verify。 |

## 従来の幾何スニペット（5ファイル）

| ファイル | 問題 | 検証範囲・合わせ方 |
|---|---|---|
| [geometry/01_point_core.py](snippets/geometry/01_point_core.py) | [ABC197 D Opposite](https://atcoder.jp/contests/abc197/tasks/abc197_d)<br>[ABC266 C Convex Quadrilateral](https://atcoder.jp/contests/abc266/tasks/abc266_c) | 回転／外積・向き判定の応用。内積、距離、共線はローカル例も併用する。 |
| [geometry/02_line_segment.py](snippets/geometry/02_line_segment.py) | [ABC016 D 一刀両断](https://atcoder.jp/contests/abc016/tasks/abc016_4) | 応用：切断線分と多角形の各辺の交差数。平行・共線・端点接触など問題の制約外になるケースはローカルで補う。 |
| [geometry/03_polygon_convex.py](snippets/geometry/03_polygon_convex.py) | [Static Convex Hull](https://judge.yosupo.jp/problem/static_convex_hull)<br>[ABC296 G Polygon and Points](https://atcoder.jp/contests/abc296/tasks/abc296_g) | 凸包／内外判定。LCの出力順と共線点の扱いに合わせる。非凸多角形の内外判定は別途確認。 |
| [geometry/04_closest_pair.py](snippets/geometry/04_closest_pair.py) | [Closest Pair of Points](https://judge.yosupo.jp/problem/closest_pair) | 部分確認：closest_pair_sqは距離の二乗のみを返す。LCが要求する点IDの対を出すには復元の追加が必要。距離だけで提出しても通らない。 |
| [geometry/05_circle.py](snippets/geometry/05_circle.py) | [ABC259 D Circumferences](https://atcoder.jp/contests/abc259/tasks/abc259_d) | 応用：on_circleとintersects_circleで連結グラフを作る。交点座標の数値精度は対象外。 |

## 同梱機能の追加問題

| 関数 | 問題 | 検証範囲・合わせ方 |
|---|---|---|
| `sequence.inversion_count` | [ABC190 F Shift and Inversions](https://atcoder.jp/contests/abc190/tasks/abc190_f) | 応用：初回をinversion_countで求め、先頭aを末尾へ動かすごとにN-1-2*aを加算。一般の区間転倒数クエリへの対応とは区別。 |
| `polynomial.fps_inverse` | [Inv of Formal Power Series](https://judge.yosupo.jp/problem/inv_of_formal_power_series) | 直接：size=N、定数項は非零。 |
| `polynomial.fps_log` | [Log of Formal Power Series](https://judge.yosupo.jp/problem/log_of_formal_power_series) | 直接：size=N、定数項は1。 |
| `polynomial.fps_exp` | [Exp of Formal Power Series](https://judge.yosupo.jp/problem/exp_of_formal_power_series) | 直接：size=N、定数項は0。 |
| `polynomial.fps_power` | [Pow of Formal Power Series](https://judge.yosupo.jp/problem/pow_of_formal_power_series) | 直接：指数とsize=N。0乗・先頭の零係数を含む。 |
| `polynomial.fps_sqrt` | [Sqrt of Formal Power Series](https://judge.yosupo.jp/problem/sqrt_of_formal_power_series) | 直接：size=N。解なしNoneを-1に変換。平方根はどちらの符号でも条件を満たせばよい。 |
| `polynomial.bostan_mori / poly_coef` | [Kth term of Linearly Recurrent Sequence](https://judge.yosupo.jp/problem/kth_term_of_linearly_recurrent_sequence) | 応用：Q=[1,-c0,-c1,...]、P=(初期列*Q)の先頭d係数。第k係数を取得。 |
| `polynomial.polynomial_interpolation` | [Polynomial Interpolation](https://judge.yosupo.jp/problem/polynomial_interpolation) | 直接：相異なるxとy。戻り値.polyをN係数に零埋めする。 |
| `polynomial.polynomial_inverse` | [Inv of Polynomials](https://judge.yosupo.jp/problem/inv_of_polynomials) | 直接：法多項式を第2引数に渡す。失敗時の返り値は下の注意参照。 |
| `polynomial.polynomial_gcd` | [Inv of Polynomials](https://judge.yosupo.jp/problem/inv_of_polynomials) | 部分確認：逆元の存在条件gcd=1を介して使う。一般の多項式GCDを単独で検証する問題としては扱わない。 |
| `polynomial.subset_sum` | [#p Subset Sum](https://judge.yosupo.jp/problem/sharp_p_subset_sum) | 直接：重み列と上限を渡し、問題が求める次数1..Tだけ出力。0重みの独自拡張はローカル確認。 |
| `polynomial.partition_function` | [Partition Function](https://judge.yosupo.jp/problem/partition_function) | 直接：p(0)..p(N)。戻り値の型を確認して係数を出す。 |
| `polynomial.bernoulli_number` | [Bernoulli Number](https://judge.yosupo.jp/problem/bernoulli_number) | 直接：B0..BN。B1の符号規約を問題と合わせる。 |
| `polynomial.stirling_first` | [Stirling Number of the First Kind](https://judge.yosupo.jp/problem/stirling_number_of_the_first_kind) | 直接：符号付き／符号なしの規約を下の注意で確認する。 |
| `polynomial.stirling_second` | [Stirling Number of the Second Kind](https://judge.yosupo.jp/problem/stirling_number_of_the_second_kind) | 直接：S(N,0)..S(N,N)。 |

## 出力形式と取りこぼしの注意

- 多項式はすべてmod 998244353。fps_*のsizeは係数数、旧FormalPowerSeriesのdegは最大次数。LCの長さNに合わせるならsize=N。
- polynomial_inverseは解なしNoneを-1に変換。解が[]なら零多項式として長さ0を出す。partition_function、bernoulli_number、stirling_first/secondは係数リストを返す。
- stirling_firstは符号付きでLCと同じ。bernoulli_numberのB1は-1/2。符号を変える必要はない。
- Manacherは位置iの奇数長を2*odd[i]-1、iとi+1の間の偶数長を2*even[i+1]とし、交互に並べる。
- LC Static Convex Hullは重複点と辺の途中の共線点を除き、反時計回り。始点の回転は任意。
- ACLのDSU/SCCは成分内の順序まで照合しない。TwoSATやマッチングは複数の正解があり得るので、サンプルと文字列が違うだけで失敗と判断しない。
- Mo、二部マッチング、行列、素数列挙、KD-tree、線形漸化式などは、アルゴリズムの計算量と各問題の最大制約を確認する。Python/PyPyでのTLEを正当性の失敗と混同しない。Codonは全ファイル未コンパイル。
- 正規CDF・k-means・ビームサーチなどは、一般の正誤ジャッジ1問で品質や最適性まで確かめることはできない。幾何の退化ケース、負閉路、空集合、独自拡張も既存ローカルテストと併用する。

Library Checkerのタイトル・入力・出力は[公式problemリポジトリ](https://github.com/yosupo06/library-checker-problems)の各info.toml/task.mdを確認した。表のリンクは提出先の問題ページ。AtCoderは各リンク先の公式問題文を確認した。

## ローカル確認

ACL形式のコンストラクタ、半開区間、遅延更新の合成順、TwoSAT、upper付きSuffix Array、ModContext、modを先頭に取る畳み込みを既存テストへ追加した。実行結果とコマンドは[ライブラリガイドの検証](LIBRARY_GUIDE.md#検証)を参照。
