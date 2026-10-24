# 機能別Live Template

同梱92ファイルから公開関数・クラスを切り出した274件。PyCharmのuserグループ、Pythonコンテキストへ登録する。

関数は関数単位、クラスはメソッドを含むクラス単位。必要な補助関数・定数・importは一緒に展開する。元のFileはそのまま残す。略語に接頭辞は付けない。同名の別実装や既存の独自テンプレートとの重複時は、略語の末尾に元ファイル名を添える。

検索画面の「Live · 略語」で絞り、選んだ略語をコピー → PyCharmで貼り付け → Tabで展開する。`lis_length`、`inversion_count`、`range_add_sum`などを直接入力してもよい。展開先は解答のmainより上。

更新は[操作ガイド](LOCAL_USAGE.md#live-templateへの登録と更新)を参照。この一覧は登録スクリプトから生成し、各定義の説明は元Fileと共通。

| 機能 | 略語 | 用途 |
|---|---|---|
| [adjlist](library/graphs/shortest_paths.py) | `adjlist_shortest_paths` | edges=[(u,v),...]から長さnの隣接リストを作る。 |
| [AggregateDeque](library/structures/aggregate_deque.py) | `aggregate_deque` | op(a,b)で左側aの後ろに右側bを連結する。eは左右の単位元。 |
| [AggregateQueue](library/structures/aggregate_queue.py) | `aggregate_queue` | 結合的演算opと左右の単位元eを指定する集約キュー。 |
| [AhoCorasick](library/strings/trie.py) | `aho_corasick` | patternsの全パターンを先に登録し、複数文字列検索器を構築する。 |
| [and_convolution](library/math/bit_transforms.py) | `and_convolution` | c[k]=sum(a[i]*b[j] for i&j==k)を返す。等長・長さ2^mの列を渡す。 |
| [area_min_sliding](library/basic/sliding_window.py) | `area_min_sliding` | 長方形gridの各height×width領域の最小値を二次元listで返す。 |
| [ArithmeticSegmentTree](library/structures/range_arithmetic.py) | `arithmetic_segment_tree` | 初期数列valuesに対する等差数列の区間加算・代入と区間和。 |
| [assign_distinct_in_intervals](library/basic/intervals.py) | `assign_distinct_in_intervals` | 整数の閉区間[l,r]ごとに、互いに異なる整数を1個ずつ割り当てる。 |
| [assignment](library/graphs/assignment.py) | `assignment` | (最小費用, 各行の割当先列)を返す。空なら(0, [])。列番号は0-indexed。 |
| [AVLTree](library/structures/avl_tree.py) | `avl_tree` | 比較可能なキーを昇順に保持する辞書。AVLTree()は空。 |
| [beam_search](library/search/heuristics.py) | `beam_search` | 各深さでscore最大のwidth状態を残す。expand(state)は新しい状態の列。 |
| [bellman_ford](library/graphs/shortest_paths.py) | `bellman_ford` | 有向辺edges=[(u,v,cost),...]と始点sourceから(dist,negative)を返す。O(VE)。 |
| [berlekamp_massey](library/math/linear_recurrence.py) | `berlekamp_massey` | 与えられた先頭項valuesに適合する最短漸化式の係数cを返す。O(N²)。 |
| [bernoulli_number](library/math/polynomial.py) | `bernoulli_number` | B_0..B_nをmod 998244353で返す。生成関数x/(exp(x)-1)。 |
| [bfs_path_count](library/graphs/graph_recipes.py) | `bfs_path_count` | (最短距離list,最短経路数list)。未到達は(-1,0)、始点への空路は1通り。 |
| [BiSegTree](library/graphs/hld.py) | `bi_seg_tree` | 順方向・逆方向の集約を保持する非可換セグメント木。 |
| [BinaryTrie](library/structures/binary_trie.py) | `binary_trie` | 0<=value<2**bitsの整数の多重集合。BinaryTrie(bits=30)は空。 |
| [bipartite_coloring](library/graphs/graph_recipes.py) | `bipartite_coloring` | 無向グラフの(0/1の色list,成分ごとの(色0数,色1数))。奇閉路があればNone。 |
| [bipartite_matching](library/graphs/bipartite_matching.py) | `bipartite_matching_bipartite_matching` | graph[u]に左頂点uと接続する右頂点IDを並べる。左右はそれぞれ0-indexed。 |
| [BitSet](library/structures/bit_set.py) | `bit_set` | sizeビットの固定幅集合。valueの下位sizeビットで初期化（既定0）。 |
| [bostan_mori](library/math/polynomial.py) | `bostan_mori_polynomial` | [x**n] P(x)/Q(x)。O(M(d)log n)、Q[0]!=0。 |
| [bounded_knapsack](library/basic/knapsack_extra.py) | `bounded_knapsack` | items=(重さ,価値,最大個数)の列。容量以下の最大価値。選ばなくてもよい。 |
| [butterfly](library/math/polynomial.py) | `butterfly` | 内部用の順NTT。長さ2^k（1以上2^23以下）のlist Aをその場で変換し、戻り値なし。 |
| [butterfly_inv](library/math/polynomial.py) | `butterfly_inv` | 内部用の逆NTT。長さ2^kのlist Aをその場で変換する。戻り値なし。 |
| [CartesianTree](library/structures/cartesian_tree.py) | `cartesian_tree` | valuesを中順巡回順とする最小ヒープの二分木をO(n)で作る。 |
| [CentroidDecomposition](library/graphs/centroid_decomposition.py) | `centroid_decomposition` | N頂点の無向木の隣接リストG（0-indexed）を重心分解する。 |
| [chinese_postman](library/graphs/exponential.py) | `chinese_postman` | 非負重み無向グラフの全辺を通る最短閉路。O(n³+k²2^k)、kは奇数次数頂点数。 |
| [chromatic_number](library/graphs/exponential.py) | `chromatic_number_exponential` | 独立集合DP＋包除原理。O(n*2^n)回の整数演算、空間O(2^n)。 |
| [Circle](snippets/geometry/05_circle.py) | `circle` | Circle(center,r)で中心Point、半径r>=0の円を作る。 |
| [closest_pair_sq](snippets/geometry/04_closest_pair.py) | `closest_pair_sq` | 点集合の最近点対の距離の二乗。厳密、分割統治 O(N log N)。 |
| [Comb](library/math/combinatorics.py) | `comb` | 0..nまでの階乗・逆階乗を前計算し、組合せを素数modで求める。 |
| [combination_small_k](library/math/combinatorics.py) | `combination_small_k` | O(min(k,n-k))。nが大きい場合向け。min(k,n-k)<primeが必要。 |
| [compress](library/basic/sequence.py) | `compress_sequence` | 比較可能かつhashableな値の列を座標圧縮する。戻り値(ids,original)。 |
| [convex_diameter_sq](library/geometry/convex.py) | `convex_diameter_sq_convex` | convex_hull_pointsのような反時計回り凸包から最遠2点の距離の二乗を返す。 |
| [convex_diameter_sq](snippets/geometry/03_polygon_convex.py) | `convex_diameter_sq_polygon_convex` | 与えられた点集合の最遠点対の距離の二乗。厳密、O(N log N)。 |
| [convex_hull_points](library/geometry/convex.py) | `convex_hull_points` | (x,y)の列から反時計回りの凸包をタプルのlistで返す。O(n log n)。 |
| [ConvexPolygon](library/geometry/convex.py) | `convex_polygon` | points=[(x,y),...]の凸包を構築し、点の内外判定を繰り返す。 |
| [count_avoiding_digits](library/basic/digit_dp.py) | `count_avoiding_digits` | 通常の10進表記に禁止桁を含まない0..boundの整数の数。0の表記は'0'。 |
| [count_digit_occurrences](library/basic/digit_dp.py) | `count_digit_occurrences` | 0..boundを全て書いたときのdigitの出現回数。0は一桁の'0'として数える。 |
| [count_digit_sum_mod](library/basic/digit_dp.py) | `count_digit_sum_mod` | 各桁の和がdivisorの倍数である0..boundの整数の数。既定では0を除く。 |
| [count_distinct_subsequences](library/strings/subsequence.py) | `count_distinct_subsequences` | 文字列・要素列として異なる部分列の数。通常は空列を除く。要素はhash可能。 |
| [count_nonzero_digits](library/basic/digit_dp.py) | `count_nonzero_digits` | 0<=x<=boundで非零桁がちょうどk個の整数の数。0はk=0に含む。 |
| [count_subarrays_distinct_at_most](library/basic/subarray_count.py) | `count_subarrays_distinct_at_most` | 異なる要素が高々k種類の部分配列数。要素はhash可能。k<=0なら0。O(N)期待時間。 |
| [count_subarrays_distinct_exact](library/basic/subarray_count.py) | `count_subarrays_distinct_exact` | 異なる要素がちょうどk種類の部分配列数。k<=0なら0。O(N)期待時間。 |
| [count_subarrays_minmax](library/basic/subarray_count.py) | `count_subarrays_minmax` | 最小値がminimumかつ最大値がmaximumの部分配列数。O(N)時間・O(1)空間。 |
| [count_subarrays_sum](library/basic/subarray_count.py) | `count_subarrays_sum` | 和がtargetの連続部分配列数。負数可、期待O(N)時間・O(N)空間。 |
| [count_subarrays_sum_leq](library/basic/subarray_count.py) | `count_subarrays_sum_leq` | 非負列の和<=limitの部分配列数。0も可。負数入りはValueError。O(N)。 |
| [count_subsequence](library/strings/subsequence.py) | `count_subsequence` | 添字の選び方としてpatternになる部分列の数。同じ文字でも位置が違えば別。 |
| [covered_lengths](library/basic/intervals.py) | `covered_lengths` | result[k]=ちょうどk本に覆われた長さ。k>=1、result[0]は常に0。 |
| [cross3](snippets/geometry/01_point_core.py) | `cross3` | ベクトル AB と AC の外積。反時計回りで正。厳密。 |
| [crt](library/math/number_theory.py) | `crt` | O(k log M)。x≡r_i(mod m_i)。最小非負解と周期。解なしは(0,0)。 |
| [dag_reachability](library/graphs/graph_recipes.py) | `dag_reachability` | DAG上の(u,v)到達判定を入力順のbool listで返す。自分自身へはTrue。 |
| [Deque](snippets/structures/Deque.py) | `deque` | リングバッファによる両端キュー。整数添字でのランダムアクセス O(1)。 |
| [dijkstra](library/graphs/shortest_paths.py) | `dijkstra` | graph[u]=[(v,非負重み),...]と始点sourceを受け取り(dist,parent)を返す。 |
| [discrete_log](library/math/number_theory.py) | `discrete_log` | 最小x>=0でa^x≡b(mod mod)。解なし-1。互いに素でなくても可。O(sqrt(mod))。 |
| [distance](snippets/geometry/01_point_core.py) | `distance` | 二点間のユークリッド距離。float。 |
| [distance_sq](snippets/geometry/01_point_core.py) | `distance_sq` | 二点間のユークリッド距離の二乗。int/Fraction なら厳密。 |
| [divisors](library/math/combinatorics.py) | `divisors_combinatorics` | 正整数nの正の約数を昇順listで返す。n<1はValueError。O(√n)。 |
| [divisors](library/math/factorize64.py) | `divisors_factorize64` | 正整数Nの全約数をlistで返す。順序は未指定。整列にはsorted(divisors(N))。 |
| [Doubling](library/basic/doubling.py) | `doubling` | next_vertex[v]を1回遷移先とする関数グラフ。終端は-1。 |
| [dsu](snippets/structures/UnionFind.py) | `dsu` | dsu(N)。頂点0..N-1の集合を統合する。merge(a,b)は統合後の代表元。 |
| [DynamicFenwickTree](library/structures/dynamic_fenwick.py) | `dynamic_fenwick_tree` | 長さnの全要素0の配列に点加算・区間和。0-indexed、半開区間。 |
| [DynamicFenwickTree2D](library/structures/dynamic_fenwick.py) | `dynamic_fenwick_tree2_d` | height行width列、全要素0の疎な二次元Fenwick Tree。 |
| [DynamicMex](library/structures/dynamic_mex.py) | `dynamic_mex` | DynamicMex(limit, values=())。初期構築O(limit+N)、追加空間O(limit)。 |
| [DynamicSequence](library/structures/dynamic_sequence.py) | `dynamic_sequence` | valuesを初期値とする動的数列。区間和prodと一次変換applyに対応。 |
| [edit_distance](library/strings/matching.py) | `edit_distance_matching` | 挿入・削除・置換のコスト1。O(nm)時間、O(min(n,m))空間。 |
| [edit_distance_bounded](library/strings/subsequence.py) | `edit_distance_bounded` | 挿入・削除・置換が各1の編集距離。距離<=kなら正確な値、超えるとk+1。 |
| [euler_tour](library/graphs/tree.py) | `euler_tour` | 無向木graph（隣接頂点のlist）をrootからDFSし、(order,tin,tout,parent)を返す。 |
| [factorize_trial](library/math/combinatorics.py) | `factorize_trial` | O(sqrt(n))。{素数:指数}。n>=1。大きな整数はfactorize64を使う。 |
| [FenwickMultiset](library/structures/fenwick_multiset.py) | `fenwick_multiset` | FenwickMultiset(universe, values=())。universeは今後追加する全ての値。 |
| [fenwick_tree](snippets/structures/BIT.py) | `fenwick_tree` | Fenwick Tree（区間和）。0-indexed。 |
| [FFT](library/math/polynomial.py) | `fft` | FFT(MOD)。素数MODで係数列を畳み込む。係数は低次から。 |
| [find_cycle](library/graphs/cycle.py) | `find_cycle_cycle` | edges=[(u,v),...]から(vertices,edge_ids)を返す。閉路がなければNone。 |
| [find_prime_factor](library/math/factorize64.py) | `find_prime_factor` | 合成数nの素因数を1つ返すPollard rhoの補助関数。最小素因数とは限らない。 |
| [floor_quotient_ranges](library/math/integer_count.py) | `floor_quotient_ranges` | n//iが一定の半開区間(l,r,商)をiの昇順にyield。1<=i<=n、n>=0。 |
| [floor_sum](library/math/number_theory.py) | `floor_sum` | sum((a*i+b)//m for i in range(n))。a,bは負でもよい。O(log m)。 |
| [floyd_warshall](library/graphs/shortest_paths.py) | `floyd_warshall` | edges=[(u,v,cost),...]から全点対距離の二次元listを返す。O(V³)。 |
| [FPS](library/math/polynomial.py) | `fps` | FPS(L)。998244353での形式的冪級数。係数listはFunc属性、低次から。 |
| [fps_exp](library/math/polynomial.py) | `fps_exp` | exp(a)の先頭size係数をlistで返す。size>=0、size>0ならa[0]==0 mod MOD。 |
| [fps_inverse](library/math/polynomial.py) | `fps_inverse` | 係数列aの1/aをx^size未満で打ち切った長さsizeのlist。 |
| [fps_log](library/math/polynomial.py) | `fps_log` | log(a)の先頭size係数をlistで返す。size>=0、size>0ならa[0]==1 mod MOD。 |
| [fps_power](library/math/polynomial.py) | `fps_power` | a^exponentの先頭size係数をlistで返す。size>=0。0乗は1。 |
| [fps_sqrt](library/math/polynomial.py) | `fps_sqrt` | aの形式平方根を長さsizeの係数listで返す。存在しなければNone。 |
| [FullyIndexableDictionary](library/structures/wavelet_matrix.py) | `fully_indexable_dictionary` | 長さNの静的bit列。初期値は全て0。set(i,bit)を済ませてbuild()を1回呼ぶ。 |
| [FunctionalGraph](library/graphs/functional_graph.py) | `functional_graph` | FunctionalGraph(next_vertex)。cycle_id/entry/depthは各頂点の閉路ID・入口・距離。 |
| [grid_bfs](library/basic/grid_search.py) | `grid_bfs` | 複数始点からの4近傍最短距離をH×Wのlistで返す。未到達・壁は-1。 |
| [grid_components](library/basic/grid_search.py) | `grid_components` | filledのマスの(成分IDの二次元list,成分サイズlist)。対象外ID=-1。 |
| [grid_min_turns](library/basic/grid_search.py) | `grid_min_turns` | 4近傍で移動する際の最小方向転換回数。最初の方向は自由。到達不能は-1。 |
| [grid_shortest_path](library/basic/grid_search.py) | `grid_shortest_path` | 4近傍最短路の座標list（両端を含む）。到達不能ならNone。O(HW)。 |
| [Heapq](snippets/structures/Heapq.py) | `heapq` | heapq を使う削除可能な最小ヒープ（遅延削除方式）。 |
| [HLD](library/graphs/hld.py) | `hld` | n頂点の無向木adjをrootで根付き木にしてHeavy-Light分解する。非再帰O(n)。 |
| [in_grid](library/basic/grid.py) | `in_grid` | 0<=row<heightかつ0<=col<widthならTrue。近傍探索の境界判定に使う。 |
| [interval_union_length](library/basic/intervals.py) | `interval_union_length` | 半開区間の和集合の長さ。重複は一度だけ数える。O(N log N)。 |
| [inv_gcd](library/math/number_theory.py) | `inv_gcd` | (gcd(a,b), x)。b>0、a*x≡gcd(a,b) (mod b)、0<=x<b/gcd(a,b)。 |
| [inv_mod](library/math/number_theory.py) | `inv_mod` | x*y≡1 (mod m)となる逆元y（0<=y<m）を返す。m>0。 |
| [inverse_matrix](library/math/linear_algebra.py) | `inverse_matrix` | 素数mod上の逆行列。特異ならNone、0x0なら[]。 |
| [inverse_matrix_gf2](library/math/gf2_matrix.py) | `inverse_matrix_gf2` | N×N行列の逆行列をbitset行のlistで返す。特異ならNone、0×0なら[]。 |
| [inversion_count](library/basic/sequence.py) | `inversion_count` | O(n log n)。i<jかつa[i]>a[j]の組数。同値は数えない。 |
| [is_probable_prime](library/math/factorize64.py) | `is_probable_prime` | nが素数ならTrue、そうでなければFalse。n<2は偽。 |
| [KDTree](library/geometry/kd_tree.py) | `kd_tree` | 静的な2次元点群points=[(x,y),...]を長方形で検索する。 |
| [KindDeque](snippets/structures/KindDeque.py) | `kind_deque` | 要素の出現数と異なる値の種類数を O(1) で追跡する deque。 |
| [kmeans](library/search/numeric.py) | `kmeans` | 同じ次元の数値ベクトル列pointsをk群に分け、(labels,centers)を返す。 |
| [kmp_search](library/strings/matching.py) | `kmp_search` | text内のpatternの全一致開始位置を昇順listで返す。重なりも含む。 |
| [knapsack_01](library/basic/subset_dp.py) | `knapsack_01` | items=[(非負整数の重さ,価値),...]から各品物を高々1個選ぶ。 |
| [knapsack_by_value](library/basic/knapsack_extra.py) | `knapsack_by_value` | items=(重さ,価値)の列、各1個。容量以下の最大価値を返す。重さ・価値とも非負整数。 |
| [knapsack_unbounded](library/basic/knapsack_extra.py) | `knapsack_unbounded` | items=(正の整数の重さ,価値)。各品物を何個でも使い、容量以下の価値を最大化。 |
| [largest_rectangle_in_grid](library/basic/sliding_window.py) | `largest_rectangle_in_grid_sliding_window` | 真の要素だけでできた最大長方形の面積を整数で返す。O(HW)。 |
| [largest_rectangle_in_histogram](library/basic/sliding_window.py) | `largest_rectangle_in_histogram_sliding_window` | 非負の高さ。幅1の棒を並べたヒストグラムの最大面積。 |
| [lazy_segtree](snippets/structures/lazy_segtree.py) | `lazy_segtree` | 遅延評価セグメント木。0-indexed / 半開区間 [l,r)。 |
| [LCATree](snippets/structures/LCATree.py) | `lca_tree` | 二分累乗法で LCA を求める木。頂点番号は0-indexed。 |
| [lcm](library/math/factorize64.py) | `lcm` | 非負整数x,yの最小公倍数。片方が0なら0。O(log min(x,y))。 |
| [lcs_length](library/strings/matching.py) | `lcs_length` | 最長共通部分列の長さ。O(nm)時間、O(min(n,m))空間。 |
| [lcs_restore](library/strings/subsequence.py) | `lcs_restore` | 最長共通部分列を1つ復元。両方strならstr、それ以外はlist。O(NM)時間・空間。 |
| [LiChaoInt](library/structures/li_chao.py) | `li_chao_int` | 非再帰・動的 Li Chao 木（整数クエリ専用）。 |
| [LiChaoTree](library/structures/li_chao.py) | `li_chao_tree` | 問い合わせ座標xsを先に登録するLi Chao木。重複・順不同可。 |
| [Line](snippets/geometry/02_line_segment.py) | `line` | 異なるPoint p,qから定義する無限直線。Line(p,q)。同じ2点はValueError。 |
| [linear_congruence](library/math/integer_count.py) | `linear_congruence` | a*x≡b (mod mod)の全解を(x0,周期)で返す。解なしNone、mod>0。 |
| [linear_equations](library/math/linear_algebra.py) | `linear_equations` | Ax=bの(一つの解, 同次解の基底リスト)。解なしNone。 |
| [linear_equations_gf2](library/math/bit_transforms.py) | `linear_equations_gf2` | GF(2)のAx=bを解き、(特解bitset, 同次解の基底bitsetのリスト)を返す。 |
| [linear_recurrence](library/math/linear_recurrence.py) | `linear_recurrence` | a[n]を返す。initialは先頭k項、coefficientsは長さk。nは0-indexed。 |
| [linear_recurrence_ntt](library/math/polynomial.py) | `linear_recurrence_ntt` | k次漸化式のa[n]をBostan–Moriで返す。O(M(k)log n)、法998244353固定。 |
| [LinkedList](library/structures/linked_list.py) | `linked_list` | 空の双方向連結リスト。ノードIDによる挿入・削除はO(1)。 |
| [lis_indices](library/basic/sequence.py) | `lis_indices` | 最長増加部分列の元配列上の添字リストを返す（値の列ではない）。 |
| [lis_length](library/basic/sequence.py) | `lis_length` | 最長増加部分列の長さ。strict=Falseなら非減少列。空なら0。 |
| [longest_common_substring](library/strings/suffix_array.py) | `longest_common_substring` | 文字列s,tの最長共通部分文字列を区間(a,b,c,d)で返す。 |
| [LowLink](library/graphs/lowlink.py) | `low_link` | n頂点の無向グラフedges=[(u,v),...]を解析する。0-indexed、非連結・多重辺可。 |
| [make_grid](snippets/structures/make_grid.py) | `make_grid` | h×w の整数二次元配列を生成する。O(hw)。各行は独立。 |
| [manacher](library/strings/matching.py) | `manacher` | (odd,even)の2配列を返す。odd[i]は中心iを含む半径、even[i]はi-1/i間の半径。 |
| [manhattan_distance](snippets/geometry/01_point_core.py) | `manhattan_distance` | 二点間のマンハッタン距離。int/Fraction なら厳密。 |
| [matrix_det](library/math/linear_algebra.py) | `matrix_det` | 正方行列の行列式 mod 素数。0x0行列の行列式は1。 |
| [matrix_multiply](library/basic/matrix.py) | `matrix_multiply` | a(n×k), b(k×m)の積を新しい二次元listで返す。形が合わないとValueError。 |
| [matrix_power](library/basic/matrix.py) | `matrix_power` | 正方行列aの非負整数exponent乗。0乗は単位行列。 |
| [matrix_product_gf2](library/math/gf2_matrix.py) | `matrix_product_gf2` | N×MのaとM×Kのbの積を返す。columns=Kを明示する。 |
| [matrix_rank](library/math/linear_algebra.py) | `matrix_rank` | 素数mod上の階数。行数または列数が0なら0。 |
| [matrix_rank_gf2](library/math/gf2_matrix.py) | `matrix_rank_gf2` | rowsのGF(2)上の階数。columnsは列数。空行列は0。 |
| [max_plus_multiply](library/basic/matrix.py) | `max_plus_multiply` | c[i][j]=max_t(a[i][t]+b[t][j])を返す。a(n×k),b(k×m)。 |
| [max_plus_power](library/basic/matrix.py) | `max_plus_power` | max-plus積で正方行列aをexponent回掛ける。exponent>=0。 |
| [MaxQueue](library/structures/max_queue.py) | `max_queue` | キーごとに1つの数値を保持し最大値を取得する。MaxQueue()は空。 |
| [maximum_independent_set](library/graphs/exponential.py) | `maximum_independent_set_exponential` | 分枝探索、最悪O(2^n)。無向・自己ループなし。解の頂点リストを返す。 |
| [mcf_graph](library/graphs/min_cost_flow.py) | `mcf_graph` | n頂点の有向グラフに非負整数容量・非負整数費用の辺を追加する。 |
| [merge_intervals](library/basic/intervals.py) | `merge_intervals` | 半開区間を併合し、昇順で互いに離れた区間listを返す。隣接区間も併合。 |
| [mf_graph](library/graphs/max_flow.py) | `mf_graph` | n頂点の有向グラフ（0-indexed）に非負整数容量を追加して最大流を求める。 |
| [minimum_spanning_forest](library/graphs/mst.py) | `minimum_spanning_forest` | n頂点・無向辺edges=[(u,v,cost),...]の最小全域森。0-indexed。 |
| [mo_order](library/structures/mo.py) | `mo_order` | 長さnの配列に対するqueries=[(l,r),...]をMo順に処理するためのクエリID列。 |
| [mo_solve](library/structures/mo.py) | `mo_solve` | 半開区間queries=[(l,r),...]の答えを入力順のlistで返す。 |
| [mobius_sieve](library/math/integer_count.py) | `mobius_sieve` | メビウス関数mu[0..limit]。mu[0]=0、mu[1]=1。平方因子あり0、異なるk素因子なら(-1)^k。 |
| [ModContext](library/math/scalar.py) | `mod_context` | with ModContext(mod): で法を指定する。shakayami/ACL-for-pythonの対象外。 |
| [Modint](library/math/scalar.py) | `modint` | with ModContext(mod)内でModint(v)を構築する。vは整数、既定0。 |
| [multi_source_bfs](library/graphs/graph_recipes.py) | `multi_source_bfs` | (dist,parent)を返す。各始点の距離0、未到達dist=-1、始点/未到達parent=-1。 |
| [negamax](library/search/heuristics.py) | `negamax` | 交互着手・零和ゲームで(手番側の評価値,最善手)を返す。深さ制限付きαβ探索。 |
| [normal_cdf](library/search/numeric.py) | `normal_cdf` | 平均mean、標準偏差sigma>0の正規分布でP(X<=x)をfloatで返す。 |
| [OfflineFenwick2D](library/structures/fenwick_2d.py) | `offline_fenwick2_d` | points=[(x,y),...]は全更新先。重複可。初期値は全点0。 |
| [on_segment](snippets/geometry/01_point_core.py) | `on_segment` | 点 q が閉線分 [p, r] 上か。共線性も確認する（退化線分も可）。 |
| [orientation](snippets/geometry/01_point_core.py) | `orientation` | p->q->r の向き。反時計回り +1、時計回り -1、一直線 0。 |
| [partition_function](library/math/polynomial.py) | `partition_function` | 0..nの整数分割数を剰余のlistで返す。順序を区別しない正整数への分割。 |
| [path_prod](library/graphs/hld.py) | `path_prod` | hldのpos順で構築したsegを使い、uからvへ進む順で値を集約する。O(log² n)。 |
| [PersistentQueue](library/structures/persistent_queue.py) | `persistent_queue` | 版番号で操作するキュー。append/popleftは新しい版を作り、元の版を保持する。 |
| [Point](snippets/geometry/01_point_core.py) | `point` | 2次元の点・ベクトル。Point(x,y)で作る。座標はint/Fraction/float。 |
| [point_plane_distance](library/geometry/plane_distance.py) | `point_plane_distance` | point,a,b,cは(x,y,z)。a,b,cを通る無限平面とpointの最短距離(float)。 |
| [Polygon](snippets/geometry/03_polygon_convex.py) | `polygon` | Pointの列verticesを周上順に渡す多角形。通常は単純多角形を想定する。 |
| [polynomial_divmod](library/math/polynomial.py) | `polynomial_divmod` | 多項式aをbで割った(商list,余りlist)。低次から、法998244353。 |
| [polynomial_gcd](library/math/polynomial.py) | `polynomial_gcd` | モニックGCD。入力を変更しない。gcd(0,0)=[]。 |
| [polynomial_interpolation](library/math/polynomial.py) | `polynomial_interpolation` | 相異なるXと同長のYからf(X[i])=Y[i]を満たす次数<len(X)のFPSを返す。 |
| [polynomial_inverse](library/math/polynomial.py) | `polynomial_inverse` | aの多項式modulusによる逆元を係数listで返す。存在しなければNone。 |
| [postorder_from_preorder_inorder](library/graphs/tree.py) | `postorder_from_preorder_inorder` | 要素は重複しない。O(n)。前順・中順から後順を復元。 |
| [pow_mod](library/math/number_theory.py) | `pow_mod` | ACL形式。x**n mod m。n>=0、m>=1。 |
| [prefix_function](library/strings/matching.py) | `prefix_function` | KMPの失敗関数。O(m)。pi[i]=真の接頭辞かつ接尾辞の最長長。 |
| [prefix_sum_2d](library/basic/prefix_sum_2d.py) | `prefix_sum_2d` | 長方形grid(H×W)から(H+1)×(W+1)の累積和を返す。 |
| [prime_fact](library/math/factorize64.py) | `prime_fact` | 1<=n<2**64を素因数分解しCounter({素数:指数})を返す。1なら空のCounter。 |
| [primes_up_to](library/math/combinatorics.py) | `primes_up_to` | 2以上n以下の素数を昇順listで返す。n>=0、O(n log log n)時間・O(n)空間。 |
| [PrioritySumStructure](library/structures/priority_sum.py) | `priority_sum_structure` | 数値の多重集合のうち、小さい方からmin(k,要素数)個の和を管理する。 |
| [project_point](snippets/geometry/02_line_segment.py) | `project_point` | 無限直線 line への垂線の足。int/Fraction 入力なら厳密な Point。 |
| [range_add_gcd](library/structures/lazy_segtree_actions.py) | `range_add_gcd` | range_add_gcd(V)。整数列への区間加算と区間GCD。apply(l,r,delta)。 |
| [range_add_max](library/structures/lazy_segtree_actions.py) | `range_add_max` | range_add_max(V)。apply(l,r,delta)で加算、prodは最大値、空は-inf。 |
| [range_add_min](library/structures/lazy_segtree_actions.py) | `range_add_min` | range_add_min(V)。apply(l,r,delta)で加算、prodは最小値、空はinf。 |
| [range_add_min_count](library/structures/lazy_segtree_actions.py) | `range_add_min_count` | range_add_min_count(V)。apply(l,r,delta)で加算、prodは(最小値,その個数)。 |
| [range_add_sum](library/structures/lazy_segtree_actions.py) | `range_add_sum` | range_add_sum(V)。apply(l,r,delta)で区間加算。prodは和、空は0。 |
| [range_affine_composite](library/structures/segtree_monoids.py) | `range_affine_composite` | range_affine_composite(V,mod=998244353)。V[i]=(a,b)はa*x+b。 |
| [range_affine_minmax](library/structures/lazy_segtree_actions.py) | `range_affine_minmax` | range_affine_minmax(V)。apply(l,r,(a,b))でx←a*x+b。負のaにも対応。 |
| [range_affine_sum](library/structures/lazy_segtree_actions.py) | `range_affine_sum` | range_affine_sum(V,mod=998244353)。apply(l,r,(a,b))でx←a*x+b。 |
| [range_affine_sum_squares](library/structures/lazy_segtree_actions.py) | `range_affine_sum_squares` | range_affine_sum_squares(V,mod=998244353)。apply(l,r,(a,b))でx←a*x+b。 |
| [range_and](library/structures/segtree_monoids.py) | `range_and` | range_and(V)。非負整数の点代入・区間AND。空は-1（全ビット1の単位元）。 |
| [range_assign_max_subarray](library/structures/lazy_segtree_actions.py) | `range_assign_max_subarray` | range_assign_max_subarray(V,allow_empty=True)。区間代入と最大部分配列和。 |
| [range_assign_sum](library/structures/lazy_segtree_actions.py) | `range_assign_sum` | range_assign_sum(V)。apply(l,r,value)で区間代入。prodは和、空は0。 |
| [range_binary_runs](library/structures/lazy_segtree_actions.py) | `range_binary_runs` | range_binary_runs(V)。0/1列の反転・代入と最長連続0/1。文字列も可。 |
| [range_brackets](library/structures/segtree_monoids.py) | `range_brackets` | range_brackets(V)。Vは'('と')'の文字列または列。set(p,'(')で点更新。 |
| [range_clamp_minmax](library/structures/lazy_segtree_actions.py) | `range_clamp_minmax` | range_clamp_minmax(V)。apply(l,r,(lo,hi))で全要素を[lo,hi]へ切り詰める。 |
| [range_count_distinct](library/structures/offline_queries.py) | `range_count_distinct` | valuesの各[l,r)に含まれる異なる値の数をqueriesと同じ順のlistで返す。 |
| [range_digit_assign](library/structures/lazy_segtree_actions.py) | `range_digit_assign` | range_digit_assign(V,mod=998244353,base=10)。数字列の区間代入と数値化。 |
| [range_flip_brackets](library/structures/lazy_segtree_actions.py) | `range_flip_brackets` | range_flip_brackets(V)。括弧列の'('と')'を区間で交換する。 |
| [range_flip_inversions](library/structures/lazy_segtree_actions.py) | `range_flip_inversions` | range_flip_inversions(V)。0/1列の区間反転と転倒数。文字列'010'も渡せる。 |
| [range_gcd](library/structures/segtree_monoids.py) | `range_gcd` | range_gcd(V)。整数の点代入・区間GCD。prodは非負、空は0。 |
| [range_index_affine_sum](library/structures/lazy_segtree_actions.py) | `range_index_affine_sum` | range_index_affine_sum(V,mod=0)。apply(l,r,(a,b,c))でA[i]←a*A[i]+b*i+c。 |
| [range_matrix_product](library/structures/segtree_monoids.py) | `range_matrix_product` | range_matrix_product(V,mod=998244353)。2×2行列を(a00,a01,a10,a11)で渡す。 |
| [range_max](library/structures/segtree_monoids.py) | `range_max` | range_max(V)。点代入・区間最大値。空は-float('inf')。 |
| [range_max_count](library/structures/segtree_monoids.py) | `range_max_count` | range_max_count(V)。prodは(最大値,その個数)、空は(-inf,0)。set/getは数値。 |
| [range_max_subarray](library/structures/segtree_monoids.py) | `range_max_subarray` | range_max_subarray(V,allow_empty=True)。最大部分配列和の点更新。 |
| [range_min](library/structures/segtree_monoids.py) | `range_min` | range_min(V)。点代入・区間最小値。空はfloat('inf')。 |
| [range_min_count](library/structures/segtree_monoids.py) | `range_min_count` | range_min_count(V)。prodは(最小値,その個数)、空は(inf,0)。set/getは数値。 |
| [range_or](library/structures/segtree_monoids.py) | `range_or` | range_or(V)。非負整数の点代入・区間OR。空は0。 |
| [range_pair_add_product](library/structures/lazy_segtree_actions.py) | `range_pair_add_product` | range_pair_add_product(V,mod=998244353)。V=[(A[i],B[i]),...]。 |
| [range_sum](library/structures/segtree_monoids.py) | `range_sum` | range_sum(V)。点代入・区間和。prodは数値、空は0。和の境界探索は非負列で使う。 |
| [range_top2](library/structures/segtree_monoids.py) | `range_top2` | range_top2(V)。異なる上位2値と個数を(v1,c1,v2,c2)で返す。 |
| [range_xor](library/structures/segtree_monoids.py) | `range_xor` | range_xor(V)。非負整数の点代入・区間XOR。空は0。 |
| [range_xor_basis](library/structures/segtree_monoids.py) | `range_xor_basis` | range_xor_basis(V,bits=60)。0<=V[i]<2**bits。区間の部分集合XORの線形基底。 |
| [raw](library/math/scalar.py) | `raw` | 現在のModContextの法で、代表値vを持つModintを返す。 |
| [rectangle_sum](library/basic/prefix_sum_2d.py) | `rectangle_sum` | prefix_sum_2dの戻り値から[top,bottom)×[left,right)の和をO(1)で返す。 |
| [rectangle_union_area](library/geometry/rectangle_union.py) | `rectangle_union_area` | rectangles=[(left,bottom,right,top),...]の和集合の面積を返す。 |
| [reflect_point](snippets/geometry/02_line_segment.py) | `reflect_point` | 無限直線 line に関する点 p の鏡映。int/Fraction 入力なら厳密。 |
| [rerooting](library/graphs/rerooting.py) | `rerooting` | 無向木の隣接リストgraphに対し、各頂点を根にしたDP値のlistを返す。 |
| [restore_path](library/graphs/shortest_paths.py) | `restore_path` | 到達不能なら[]。source自身への経路は[source]。 |
| [RollbackDSU](library/structures/rollback_dsu.py) | `rollback_dsu` | n個の単集合から始める。mergeはACLと同じく併合後の代表を返す。 |
| [RollingHash](library/strings/rolling_hash.py) | `rolling_hash` | 文字列または整数列valuesの静的な二重Rolling Hash。構築O(n)、queryはO(1)。 |
| [RollingHashSegTree](library/strings/rolling_hash.py) | `rolling_hash_seg_tree` | 文字列または整数列valuesへの一点更新付き二重Rolling Hash。 |
| [rotate90](library/basic/grid.py) | `rotate90` | 長方形gridを時計回りに90度回転したlist[list]を返す。O(HW)、入力は変更しない。 |
| [run_length_decode](library/basic/sequence.py) | `run_length_decode` | (値,非負の個数)の列を通常のlistへ復元する。O(復元長)。 |
| [run_length_encode](library/basic/sequence.py) | `run_length_encode` | O(n)。[(値, 連続数), ...]。空入力は[]。 |
| [scc](library/graphs/scc.py) | `scc` | scc(N,edges)で各成分の頂点listをトポロジカル順に返す。O(N+M)。 |
| [scc_dag](library/graphs/scc.py) | `scc_dag` | 独自拡張: SCCを縮約したDAGの隣接リスト。自己辺・多重辺を除く。 |
| [scc_ids](library/graphs/scc.py) | `scc_ids` | 独自拡張: 頂点ごとの成分番号。異なる成分への辺u→vではids[u]<ids[v]。 |
| [schedule_intervals](library/basic/intervals.py) | `schedule_intervals` | 重ならない半開区間を最多選択し、元の添字を実施順に返す。l<rが必要。 |
| [Segment](snippets/geometry/02_line_segment.py) | `segment` | Point p,qを両端とする閉線分Segment(p,q)。p==qの退化線分も許す。 |
| [SegmentTreeBeats](snippets/structures/SegmentTreeBeats.py) | `segment_tree_beats` | Segment Tree Beats。0-indexed / 半開区間 [l,r)。 |
| [segtree](snippets/structures/segtree.py) | `segtree` | 一般のセグメント木。0-indexed / 半開区間 [l,r)。 |
| [semigroup_segtree](library/structures/segtree_monoids.py) | `semigroup_segtree` | semigroup_segtree(V,OP)。単位元を用意しにくい結合的演算をそのまま渡す。 |
| [sliding_min](library/basic/sliding_window.py) | `sliding_min` | valuesの連続width要素ごとの最小値を左端順に返す。O(n)。 |
| [SlopeTrick](library/structures/slope_trick.py) | `slope_trick` | f(x)=0から始まる区分線形凸関数を保持する。 |
| [smallest_prime_factors](library/math/combinatorics.py) | `smallest_prime_factors` | 0..nの最小素因数を長さn+1のlistで返す。n>=0。 |
| [smallest_subsequence](library/strings/subsequence.py) | `smallest_subsequence` | 長さkの辞書順最小部分列。str入力ならstr、それ以外はlist。0<=k<=N。 |
| [solve_gf2](library/math/bit_transforms.py) | `solve_gf2` | Ax=b。rowsは各行の係数bitset。戻り値(rank, 一つの解bitset)。矛盾があればNone。 |
| [SortedMultiset](library/structures/sorted_set.py) | `sorted_multiset` | 比較可能な値の順序付き多重集合。重複を保持する。 |
| [SortedSet](library/structures/sorted_set.py) | `sorted_set` | 比較可能な値の順序付き集合。初期値・追加値の重複を除く。 |
| [split_and_list](library/basic/subset_dp.py) | `split_and_list_subset_dp` | valuesを中央で二分し、それぞれの部分集合和の昇順リスト(left,right)を返す。 |
| [SqrtDecomposition](library/structures/sqrt_decomposition.py) | `sqrt_decomposition` | 初期数列valuesに区間加算・区間和を行う平方分割。 |
| [sqrt_mod](library/math/number_theory.py) | `sqrt_mod` | Tonelli–Shanks。primeは素数。小さい方の平方根、存在しなければ-1。 |
| [steiner_tree](library/graphs/exponential.py) | `steiner_tree` | 非負重み無向グラフ。O(3^t*n+2^t*(n+m)log n)、空間O(2^t*n)。 |
| [stirling_first](library/math/polynomial.py) | `stirling_first` | 符号付き第一種Stirling数s(n,k)をk=0..nのlistで返す。 |
| [stirling_second](library/math/polynomial.py) | `stirling_second` | 第二種Stirling数S(n,k)をk=0..nのlistで返す。 |
| [String](library/strings/suffix_array.py) | `string` | String(s)。文字列・整数列のSA/LCP/Zを求める。入力は変更しない。 |
| [subsequence_positions](library/strings/subsequence.py) | `subsequence_positions` | patternが部分列なら最も左を選ぶ添字list、そうでなければNone。空patternは[]。 |
| [subset_sum](library/math/polynomial.py) | `subset_sum` | 非負整数列Aから各要素を高々一度選ぶ部分集合和の個数を剰余で返す。 |
| [subset_sum_bits](library/basic/subset_dp.py) | `subset_sum_bits` | PyPy用。戻り値のbit kが1なら和kを作れる。0<=k<=limit。 |
| [subset_sum_restore](library/basic/knapsack_extra.py) | `subset_sum_restore` | 各要素を高々1回選び和targetにする元の添字list。無理ならNone、target=0なら[]。 |
| [subset_sums](library/basic/subset_dp.py) | `subset_sums` | O(2^n)。空集合を含む全ての部分集合和。重複を保持する。 |
| [subset_sums_by_size](library/basic/subset_dp.py) | `subset_sums_by_size` | result[k]: k要素を選ぶ部分集合和のリスト。 |
| [subset_zeta](library/math/bit_transforms.py) | `subset_zeta` | values[mask]を部分集合上で合計したlistを返す。長さは2^k。 |
| [sum_floor_quotients](library/math/integer_count.py) | `sum_floor_quotients` | sum(n//i for i in range(1,n+1))。O(sqrt(n))時間・O(1)空間。 |
| [sum_subarray_max](library/basic/subarray_count.py) | `sum_subarray_max` | 全ての非空連続部分配列の最大値の総和。負数・重複可、O(N)時間・空間。 |
| [sum_subarray_min](library/basic/subarray_count.py) | `sum_subarray_min` | 全ての非空連続部分配列の最小値の総和。単調スタック、O(N)時間・空間。 |
| [to_index](library/basic/grid.py) | `to_index` | 0-indexedの(row,col)をrow*width+colに平坦化する。widthは列数。範囲検査なし。 |
| [to_position](library/basic/grid.py) | `to_position` | 平坦化した非負indexを(row,col)へ戻す。width>0。divmod(index,width)を返す。 |
| [topological_sort](library/graphs/shortest_paths.py) | `topological_sort_shortest_paths` | 有向隣接リストgraph[u]=[v,...]のトポロジカル順（頂点のlist）。O(V+E)。 |
| [totient](library/math/factorize64.py) | `totient` | 1..NでNと互いに素な整数の個数。1<=N<2**64、totient(1)=1。 |
| [totient_sieve](library/math/integer_count.py) | `totient_sieve` | phi[0..limit]。phi[n]は1..nでnと互いに素の個数。phi[0]=0、phi[1]=1。 |
| [transpose](library/basic/grid.py) | `transpose` | 長方形grid（行の列）の転置を新しいlist[list]で返す。O(HW)。空なら[]。 |
| [tree_centers](library/graphs/tree.py) | `tree_centers` | 重みなし無向木の中心頂点のlist（1個か2個）。空なら[]。 |
| [tree_diameter](library/graphs/tree.py) | `tree_diameter` | 重みなし無向木。O(n)。直径の長さと、その経路を返す。 |
| [Trie](library/strings/trie.py) | `trie` | 文字列（またはhashableな要素の列）を重複付きで登録する空のTrie。 |
| [tsp_cycle](library/graphs/exponential.py) | `tsp_cycle` | O(n²2^n)時間・O(n2^n)空間。全頂点を一度ずつ通りstartへ戻る最小コスト。 |
| [tsp_nearest_neighbor](library/search/heuristics.py) | `tsp_nearest_neighbor` | O(n²)の近傍法。distanceは完全な距離行列。巡回順（始点を末尾にも含む）。 |
| [tsp_two_opt](library/search/heuristics.py) | `tsp_two_opt` | 対称なn×n費用行列distance、長さn+1の閉じた巡回順tour、非負整数passesを入力する。改善した新しい頂点順listを返し、元のtourは変えない。 |
| [two_choice_sum](library/basic/knapsack_extra.py) | `two_choice_sum` | 各(a,b)から必ず1つ選び和targetにする。選択を0/1のlistで返し、無理ならNone。 |
| [two_sat](library/graphs/scc.py) | `two_sat_scc` | two_sat(n,clause)で解のboolリストを返す。充足不能ならNone。O(n+節数)。 |
| [walsh_hadamard](library/math/bit_transforms.py) | `walsh_hadamard` | 長さ2^kのXOR変換（FWHT）。入力非破壊、時間O(n log n)、空間O(n)。 |
| [WaveletMatrix](library/structures/wavelet_matrix.py) | `wavelet_matrix` | 静的な整数列Xから区間順位・頻度を検索する。負数・重複も座標圧縮して扱う。 |
| [weighted_adjlist](library/graphs/shortest_paths.py) | `weighted_adjlist` | edges=[(u,v,weight),...]からgraph[u]=[(v,weight),...]を作る。 |
| [weighted_tree_diameter](library/graphs/tree.py) | `weighted_tree_diameter` | 非負重みの無向木graph[u]=[(v,weight),...]の(直径長,頂点経路)を返す。 |
| [WeightedUnionFind](snippets/structures/WeightedUnionFind.py) | `weighted_union_find` | ポテンシャル差を管理する Union-Find（加法群、0-indexed）。 |
| [xor_basis](library/math/bit_transforms.py) | `xor_basis` | 非負整数のXOR基底を最上位bitの降順で返す。O(n*bit幅)。 |
| [xor_convolution](library/math/bit_transforms.py) | `xor_convolution` | c[k]=sum(a[i]*b[j] for i^j==k) mod mod。等長・長さ2^k、奇数mod。 |
| [XorDSU](library/structures/xor_dsu.py) | `xor_dsu` | XorDSU(n)。leader/same/merge/size/groupsとXOR用のdiff/potentialを用意。 |
| [xor_maximum](library/math/bit_transforms.py) | `xor_maximum` | xor_basisで作った基底から任意個を選び、initialとXORした値を最大化する。 |
| [xor_minimax](library/math/bit_transforms.py) | `xor_minimax` | min_x max(a^x)。非負整数列。O(n*bit幅)、再帰深さはbit幅。 |
| [zero_one_bfs](library/graphs/shortest_paths.py) | `zero_one_bfs` | graph[u]=[(v,重み),...]で全重みが0か1の場合の距離list。未到達はinf。 |
