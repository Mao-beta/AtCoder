# ライブラリ化候補と抽出先（2026-10-17）

83用途を51ファイルに整理し、`library/`へ抽出した。右端のリンクが現在の実装。元ファイル数と元の定義名は調査時点の記録であり、抽出後のAPI名とは異なる場合がある。利用例・変更点・PyPy/Codonの扱いは [LIBRARY_GUIDE.md](LIBRARY_GUIDE.md) を参照。

その後、[Library Checker対応の第1弾](verify/README.md)でSWAG・割当・線形代数の3ファイルを追加し、現在のlibrary/は54ファイル。既存のLi Chao・LowLink・bit_transformsも拡張した。以下の83用途・51抽出先の表は元コード調査の記録として残している。

2026-10-17に抽出先のリンクとファイル数を再照合した。表の「抽出時の確認点」は当時の検討事項を残したもので、未完了タスクの一覧ではない。現在の引数順・制限・検証結果は[ACL_API.md](ACL_API.md)と[LIBRARY_GUIDE.md](LIBRARY_GUIDE.md)を優先する。

解答・既存ライブラリ側のPython 4,574ファイルを再帰的に静的解析した。パレット本体、配布用の重複スニペット、テスト、仮想環境、Git・IDE設定は集計から除外。4,572ファイルを解析でき、トップレベルのクラス・関数定義7,635件（main等を含む）を抽出した。文字列クラス内のSuffix Arrayなどは追加の検索で確認した。

元ファイルの全実装を実行検証したという意味ではない。抽出先については各ファイルの代表例と修正箇所をPyPyで確認した。同じ名前でもAPI・実装・正当性が異なる。『ファイル数』は挙げた名前の定義があるファイルの和集合で、呼び出し回数や独立実装数ではない。リンク先は代表的な抽出元候補。LibraryChecker内にあることだけでAC済みとは断定しない。

## 現在のスニペットとの関係

同梱17ファイルは構造系12・幾何系5。UnionFind、WeightedUnionFind、segtree、SegTree互換版、lazy_segtree、BIT、LCATree、Deque、KindDeque、Heapq、SegmentTreeBeats、make_gridと、Point/Line/Segment/Polygon/Circle/最近点対が利用できる。従来の17ファイルは互換性のため保持し、追加分はlibrary/に置いた。

`_cp_structures.py`は旧APIの統合版、`cp_snippet_palette/snippets/`は検索・貼り付け用。リポジトリ直下にも旧`snippets/`があるが、現在のパレット設定はそちらを読まない。検索対象はパレット内の`snippets/`と`library/`。新しい自作スニペットは[操作ガイド](LOCAL_USAGE.md#スニペットの追加)に従ってパレット内の`snippets/`へ置き、同じ実装を両方へ登録しない。

座標圧縮・累積和・Comb・SCCなどから使い始められる。FPSなど依存の大きいものは同じファイルに補助コードを含めた。

旧 `_codex_refactor_instructions.md` では行列演算や2次元累積和を未実装扱いしているが、調査時点でどちらも `_test.py` に実装があった。現在はそれぞれ`library/basic/matrix.py`と`library/basic/prefix_sum_2d.py`へ抽出済み。

## まず追加しやすい基本部品

| 用途 | クラス・関数 | ファイル数 | 元ファイルの候補 | 抽出時の確認点 | 抽出先（現在のAPI） |
|---|---|---:|---|---|---|
| 隣接リスト | `adjlist`, `make_adjlist_d`, `make_adjlist_nond`, `adjlist_nond_1to0` | 182 | [_test.py:60](<D:/Kyopro/AtCoder/_test.py:60>) / [LibraryChecker/vertex_add_path_sum.py:112](<D:/Kyopro/AtCoder/LibraryChecker/vertex_add_path_sum.py:112>) | 有向/無向、0/1始まり、重み付きの引数を整理する。 | [graphs/shortest_paths](library/graphs/shortest_paths.py) |
| 座標圧縮 | `compress` | 82 | [_test.py:43](<D:/Kyopro/AtCoder/_test.py:43>) / [_inversion_num.py:22](<D:/Kyopro/AtCoder/_inversion_num.py:22>) | 圧縮結果と復元表の返り値を揃える。 | [basic/sequence](library/basic/sequence.py) |
| 2次元累積和・長方形和 | `cum_2D`, `area_sum` | 28 | [_test.py:480](<D:/Kyopro/AtCoder/_test.py:480>) / [ABC/ABC005/ABC005D.py:22](<D:/Kyopro/AtCoder/ABC/ABC005/ABC005D.py:22>) | すでに実装あり。半開区間とパディングの約束を明記する。 | [basic/prefix_sum_2d](library/basic/prefix_sum_2d.py) |
| 行列積・行列累乗 | `mul_matrix`, `pow_matrix` | 19 | [_test.py:437](<D:/Kyopro/AtCoder/_test.py:437>) / [LibraryChecker/matrix_product.py:24](<D:/Kyopro/AtCoder/LibraryChecker/matrix_product.py:24>) | すでに実装あり。MODと演算の差し替え方を明示する。 | [basic/matrix](library/basic/matrix.py) |
| 転倒数 | `inversion_num` | 16 | [_inversion_num.py:62](<D:/Kyopro/AtCoder/_inversion_num.py:62>) / [ABC/ABC261/ABC261F.py:62](<D:/Kyopro/AtCoder/ABC/ABC261/ABC261F.py:62>) | BIT・compressも同梱する。 | [basic/sequence](library/basic/sequence.py) |
| 最長増加部分列 | `LIS` | 10 | [_test.py:263](<D:/Kyopro/AtCoder/_test.py:263>) / [ABC/ABC006/ABC006D.py:28](<D:/Kyopro/AtCoder/ABC/ABC006/ABC006D.py:28>) | 狭義/広義の違い、長さ/復元の返り値を決める。 | [basic/sequence](library/basic/sequence.py) |
| ダブリング | `Doubling` | 11 | [_test.py:120](<D:/Kyopro/AtCoder/_test.py:120>) / [ABC/ABC013/ABC013D.py:27](<D:/Kyopro/AtCoder/ABC/ABC013/ABC013D.py:27>) | 遷移先がない頂点とステップ数の上限を明記する。 | [basic/doubling](library/basic/doubling.py) |
| ランレングス圧縮 | `runLengthEncode`, `runLengthDecode`, `runLengthEncodeToString` | 57 | [_Strings.py:194](<D:/Kyopro/AtCoder/_Strings.py:194>) / [ABC/ABC019/ABC019B.py:27](<D:/Kyopro/AtCoder/ABC/ABC019/ABC019B.py:27>) | 文字列専用と一般列用の契約を整理する。 | [basic/sequence](library/basic/sequence.py) |
| グリッド変換・範囲判定 | `i2hw`, `hw2i`, `in_grid`, `transpose`, `rotate90` | 3 | [_test.py:209](<D:/Kyopro/AtCoder/_test.py:209>) / [ABC/ABC237/ABC237B.py:22](<D:/Kyopro/AtCoder/ABC/ABC237/ABC237B.py:22>) | H/Wなどのグローバル値を引数にする。 | [basic/grid](library/basic/grid.py) |
| スライド最小値 | `sliding_min`, `area_min_sliding` | 1 | [ADT/20231207/ADT_20231207_2I.py:55](<D:/Kyopro/AtCoder/ADT/20231207/ADT_20231207_2I.py:55>) | 1次元と2次元を分けて登録する。 | [basic/sliding_window](library/basic/sliding_window.py) |
| 最大長方形 | `largest_rectangle_in_histogram`, `largest_rectangle_in_grid` | 3 | [AOJ/DPL_3_B.py:23](<D:/Kyopro/AtCoder/AOJ/DPL_3_B.py:23>) / [ABC/ABC311/ABC311F.py:144](<D:/Kyopro/AtCoder/ABC/ABC311/ABC311F.py:144>) | ヒストグラムとグリッドの2段階で使う。 | [basic/sliding_window](library/basic/sliding_window.py) |
| 半分全列挙 | `split_and_list`, `split_and_list_by_size` | 7 | [_test.py:237](<D:/Kyopro/AtCoder/_test.py:237>) / [ABC/ABC032/ABC032D.py:14](<D:/Kyopro/AtCoder/ABC/ABC032/ABC032D.py:14>) | 集合の生成と問題固有の評価を分ける。 | [basic/subset_dp](library/basic/subset_dp.py) |
| ナップサック・部分和 | `Knapsack`, `subset_sum_dp` | 3 | [_test.py:97](<D:/Kyopro/AtCoder/_test.py:97>) / [algorithm_math/030.py:27](<D:/Kyopro/AtCoder/algorithm_math/030.py:27>) | 重さ軸/価値軸、復元の要否を別スニペットにする。 | [basic/subset_dp](library/basic/subset_dp.py) |

## データ構造・区間クエリ

| 用途 | クラス・関数 | ファイル数 | 元ファイルの候補 | 抽出時の確認点 | 抽出先（現在のAPI） |
|---|---|---:|---|---|---|
| 順序付き集合・多重集合 | `SortedSet`, `SortedMultiset` | 55 | [_Sorted_Set.py:32](<D:/Kyopro/AtCoder/_Sorted_Set.py:32>) / [LibraryChecker/LC_predecessor_problem.py:29](<D:/Kyopro/AtCoder/LibraryChecker/LC_predecessor_problem.py:29>) | 同じ実装のコピーが多い。出典とAPIを揃えて一本を選ぶ。 | [structures/sorted_set](library/structures/sorted_set.py) |
| 整数トライ | `BinaryTrie` | 6 | [_Binary_Trie.py:22](<D:/Kyopro/AtCoder/_Binary_Trie.py:22>) / [LibraryChecker/set_xor_min.py:28](<D:/Kyopro/AtCoder/LibraryChecker/set_xor_min.py:28>) | ビット幅、重複、XOR操作、空集合を確認する。 | [structures/binary_trie](library/structures/binary_trie.py) |
| Wavelet Matrix | `WaveletMatrix`, `FullyIndexableDictionary` | 1 | [_WaveletMatrix.py:24](<D:/Kyopro/AtCoder/_WaveletMatrix.py:24>) | 補助構造と一緒に切り出す。値域・rank/selectの境界を検証する。 | [structures/wavelet_matrix](library/structures/wavelet_matrix.py) |
| ビット集合 | `BitSet`, `Bitset`, `GridBit` | 6 | [_BitSet.py:25](<D:/Kyopro/AtCoder/_BitSet.py:25>) / [LibraryChecker/matrix_product_mod_2.py:26](<D:/Kyopro/AtCoder/LibraryChecker/matrix_product_mod_2.py:26>) | Python整数で足りる用途と固定長構造が必要な用途を区別する。 | [structures/bit_set](library/structures/bit_set.py) |
| Mo法 | `Mo` | 3 | [_Mo.py:27](<D:/Kyopro/AtCoder/_Mo.py:27>) / [ABC/ABC242/ABC242G.py:29](<D:/Kyopro/AtCoder/ABC/ABC242/ABC242G.py:29>) | add/deleteと答え取得を問題に応じて渡せる形にする。 | [structures/mo](library/structures/mo.py) |
| 上位/下位k個の和 | `PrioritySumStructure` | 3 | [ABC/ABC306/ABC306E.py:98](<D:/Kyopro/AtCoder/ABC/ABC306/ABC306E.py:98>) / [ABC/ABC281/ABC281E_hq.py:98](<D:/Kyopro/AtCoder/ABC/ABC281/ABC281E_hq.py:98>) | ヒープ・削除処理とセットで切り出す。 | [structures/priority_sum](library/structures/priority_sum.py) |
| CHT・Li Chao Tree | `ConvexHullTrick`, `LineCHT`, `LiChaoInt` | 4 | [_Convex_Hull_Trick.py:27](<D:/Kyopro/AtCoder/_Convex_Hull_Trick.py:27>) / [ABC/ABC289/ABC289G.py:25](<D:/Kyopro/AtCoder/ABC/ABC289/ABC289G.py:25>) | 座標範囲、最小/最大、整数条件を整理する。 | [structures/li_chao](library/structures/li_chao.py) |
| Slope Trick | `SlopeTrick` | 2 | [ABC/ABC127/ABC127F.py:98](<D:/Kyopro/AtCoder/ABC/ABC127/ABC127F.py:98>) / [ABC/ABC365/ABC365F.py:99](<D:/Kyopro/AtCoder/ABC/ABC365/ABC365F.py:99>) | 凸関数の更新の意味とヒープのオフセットを文書化する。 | [structures/slope_trick](library/structures/slope_trick.py) |
| Cartesian Tree | `CartesianTree` | 1 | [NDPC_F.py:26](<D:/Kyopro/AtCoder/NDPC_F.py:26>) | 等値要素の優先順位と返す親子配列を確認する。 | [structures/cartesian_tree](library/structures/cartesian_tree.py) |
| 動的Fenwick Tree・2次元版 | `DynamicFenwickTree`, `DynamicFenwickTree2D` | 1 | [ABC/ABC324/ABC324G.py:107](<D:/Kyopro/AtCoder/ABC/ABC324/ABC324G.py:107>) | 辞書実装のメモリ量、値域、座標圧縮との使い分けを確認する。 | [structures/dynamic_fenwick](library/structures/dynamic_fenwick.py) |
| 等差数列更新セグ木 | `LazySegmentTreeArithmetic` | 1 | [ABC/ABC371/ABC371F.py:69](<D:/Kyopro/AtCoder/ABC/ABC371/ABC371F.py:69>) | 通常lazy_segtreeとの役割の違いを整理する。 | [structures/range_arithmetic](library/structures/range_arithmetic.py) |
| 平方分割 | `SqrtDecomposition`, `Bucket` | 2 | [PAST/PAST003/PAST003N.py:23](<D:/Kyopro/AtCoder/PAST/PAST003/PAST003N.py:23>) / [PAST/PAST014/PAST014O.py:23](<D:/Kyopro/AtCoder/PAST/PAST014/PAST014O.py:23>) | バケット内の更新と集約が問題に依存していないか確認する。 | [structures/sqrt_decomposition](library/structures/sqrt_decomposition.py) |
| 連結リスト | `LinkedList` | 1 | [tessoku-book/C17.py:33](<D:/Kyopro/AtCoder/tessoku-book/C17.py:33>) | sentinel・削除済みノード・要素識別の契約を明記する。 | [structures/linked_list](library/structures/linked_list.py) |
| AVL木・平衡木 | `AVLTree`, `BalancingPivotTree` | 4 | [_AVL_Tree.py:36](<D:/Kyopro/AtCoder/_AVL_Tree.py:36>) / [_Balancing_Tree.py:22](<D:/Kyopro/AtCoder/_Balancing_Tree.py:22>) | SortedSetで足りる場合は追加を急がず、比較・境界テストを優先する。 | [structures/avl_tree](library/structures/avl_tree.py) |
| 最大値取得と削除 | `GetMax_and_Delete` | 1 | [_GetMax_and_Delete.py:18](<D:/Kyopro/AtCoder/_GetMax_and_Delete.py:18>) | Heapq/SortedMultisetと用途が重ならないか確認する。 | [structures/max_queue](library/structures/max_queue.py) |

## グラフ・木

| 用途 | クラス・関数 | ファイル数 | 元ファイルの候補 | 抽出時の確認点 | 抽出先（現在のAPI） |
|---|---|---:|---|---|---|
| Dijkstra | `Dijkstra`, `__Dijkstra` | 55 | [_Graph_Algorithm.py:118](<D:/Kyopro/AtCoder/_Graph_Algorithm.py:118>) / [ABC/ABC035/ABC035D.py:16](<D:/Kyopro/AtCoder/ABC/ABC035/ABC035D.py:16>) | 辺追加、戻り値、到達不能値を統一する。 | [graphs/shortest_paths](library/graphs/shortest_paths.py) |
| Bellman–Ford | `BellmanFord` | 4 | [_Graph_Algorithm.py:251](<D:/Kyopro/AtCoder/_Graph_Algorithm.py:251>) / [ABC/ABC137/ABC137E.py:25](<D:/Kyopro/AtCoder/ABC/ABC137/ABC137E.py:25>) | 負閉路の検出と影響頂点の扱いを明記する。 | [graphs/shortest_paths](library/graphs/shortest_paths.py) |
| トポロジカルソート | `topological_sort` | 16 | [_Graph_Algorithm.py:57](<D:/Kyopro/AtCoder/_Graph_Algorithm.py:57>) / [ABC/ABC135/ABC135F.py:67](<D:/Kyopro/AtCoder/ABC/ABC135/ABC135F.py:67>) | 閉路がある場合の返り値を決める。 | [graphs/shortest_paths](library/graphs/shortest_paths.py) |
| 強連結成分分解 | `SCC`, `scc`, `construct`, `StronglyConnectedComponents` | 14 | [_SCC.py:16](<D:/Kyopro/AtCoder/_SCC.py:16>) / [ABC/ABC245/ABC245F.py:31](<D:/Kyopro/AtCoder/ABC/ABC245/ABC245F.py:31>) | 成分番号の順序と縮約グラフを説明する。 | [graphs/scc](library/graphs/scc.py) |
| 2-SAT | `two_sat` | 5 | [_ACL_two_sat.py:18](<D:/Kyopro/AtCoder/_ACL_two_sat.py:18>) / [ABC/ABC210/ABC210F.py:16](<D:/Kyopro/AtCoder/ABC/ABC210/ABC210F.py:16>) | リテラルの真偽と充足割当の取り出し方を揃える。 | [graphs/scc](library/graphs/scc.py) |
| LowLink | `LowLink` | 3 | [_Low_Link.py:25](<D:/Kyopro/AtCoder/_Low_Link.py:25>) / [ABC/ABC334/ABC334G.py:24](<D:/Kyopro/AtCoder/ABC/ABC334/ABC334G.py:24>) | 多重辺と非連結グラフを確認する。 | [graphs/lowlink](library/graphs/lowlink.py) |
| 全方位木DP | `Rerooting` | 2 | [_Rerooting.py:25](<D:/Kyopro/AtCoder/_Rerooting.py:25>) / [EDPC/EDPC_V.py:26](<D:/Kyopro/AtCoder/EDPC/EDPC_V.py:26>) | merge/op/単位元と辺情報の渡し方を整理する。 | [graphs/rerooting](library/graphs/rerooting.py) |
| HLD・非可換な経路集約 | `HeavyLightDecomposition`, `HLD`, `BiSegTree`, `path_fold_noncomm` | 6 | [LibraryChecker/vertex_set_path_composite.py:29](<D:/Kyopro/AtCoder/LibraryChecker/vertex_set_path_composite.py:29>) / [LibraryChecker/vertex_add_path_sum.py:23](<D:/Kyopro/AtCoder/LibraryChecker/vertex_add_path_sum.py:23>) | 頂点/辺クエリと経路の向きを区別する。LibraryChecker側が抽出候補。 | [graphs/hld](library/graphs/hld.py) |
| 重心分解 | `CentroidDecomposition` | 1 | [ABC/ABC291/ABC291H.py:51](<D:/Kyopro/AtCoder/ABC/ABC291/ABC291H.py:51>) | 問題固有の出力を外し、分解木と階層を返す。 | [graphs/centroid_decomposition](library/graphs/centroid_decomposition.py) |
| Euler Tour | `EulerTour`, `euler_tour` | 2 | [_test.py:171](<D:/Kyopro/AtCoder/_test.py:171>) / [_Graph_Algorithm.py:16](<D:/Kyopro/AtCoder/_Graph_Algorithm.py:16>) | 入時刻/出時刻と部分木区間を定義する。 | [graphs/tree](library/graphs/tree.py) |
| 木の直径・中心 | `diameter`, `get_tree_center_info` | 6 | [PAST/PAST020/PAST020L.py:24](<D:/Kyopro/AtCoder/PAST/PAST020/PAST020L.py:24>) / [_Graph_Algorithm.py:88](<D:/Kyopro/AtCoder/_Graph_Algorithm.py:88>) | 重みの有無と中心が1点/2点のケースを確認する。 | [graphs/tree](library/graphs/tree.py) |
| 最小全域木 | `MST`, `Kruskal` | 9 | [ARC/ARC076/ARC076D.py:64](<D:/Kyopro/AtCoder/ARC/ARC076/ARC076D.py:64>) / [ABC/ABC282/ABC282E.py:89](<D:/Kyopro/AtCoder/ABC/ABC282/ABC282E.py:89>) | UnionFindを同梱し、非連結時の振る舞いを明記する。 | [graphs/mst](library/graphs/mst.py) |
| 最大流 | `MFGraph`, `Dinic`, `mf_graph` | 27 | [_Graph_Algorithm.py:345](<D:/Kyopro/AtCoder/_Graph_Algorithm.py:345>) / [ABC/ABC010/ABC010D_maxflow.py:16](<D:/Kyopro/AtCoder/ABC/ABC010/ABC010D_maxflow.py:16>) | 辺オブジェクト・残余辺・復元も含めて切り出す。 | [graphs/max_flow](library/graphs/max_flow.py) |
| 最小費用流 | `MCFGraph`, `MinCostFlow` | 10 | [_Graph_Algorithm.py:579](<D:/Kyopro/AtCoder/_Graph_Algorithm.py:579>) / [ABC/ABC247/ABC247G.py:29](<D:/Kyopro/AtCoder/ABC/ABC247/ABC247G.py:29>) | 負費用、ポテンシャル、実行可能流量を確認する。 | [graphs/min_cost_flow](library/graphs/min_cost_flow.py) |
| 二部マッチング | `bipartite_matching` | 1 | [tessoku-book/A69.py:167](<D:/Kyopro/AtCoder/tessoku-book/A69.py:167>) | 流量実装への依存と左右の頂点番号を整理する。 | [graphs/bipartite_matching](library/graphs/bipartite_matching.py) |
| 巡回セールスマンDP | `TSP`, `Salesman` | 7 | [AOJ/DPL_2_A.py:23](<D:/Kyopro/AtCoder/AOJ/DPL_2_A.py:23>) / [_Graph_Algorithm.py:705](<D:/Kyopro/AtCoder/_Graph_Algorithm.py:705>) | 始点、帰還、距離行列、Nの上限を明記する。 | [graphs/exponential](library/graphs/exponential.py) |
| 最小Steiner木 | `min_steiner_tree` | 1 | [yuki/01xx/yuki_0114.py:23](<D:/Kyopro/AtCoder/yuki/01xx/yuki_0114.py:23>) | 端点集合のサイズに対する計算量を説明する。 | [graphs/exponential](library/graphs/exponential.py) |
| 中国人郵便配達問題 | `chinese_postman_problem` | 1 | [AOJ/DPL_2_B.py:23](<D:/Kyopro/AtCoder/AOJ/DPL_2_B.py:23>) | グラフの前提と最短路計算への依存を整理する。 | [graphs/exponential](library/graphs/exponential.py) |
| 木の巡回列復元 | `reconstruct_post_from_pre_and_in` | 1 | [_Graph_Algorithm.py:733](<D:/Kyopro/AtCoder/_Graph_Algorithm.py:733>) | 頂点値の一意性と再帰深さを確認する。 | [graphs/tree](library/graphs/tree.py) |
| 最大独立集合・彩色数 | `maximum_independent_set`, `chromatic_number` | 2 | [code_thanks_festival_2017_g.py:23](<D:/Kyopro/AtCoder/code_thanks_festival_2017_g.py:23>) / [ARC/ARC171/ARC171D.py:42](<D:/Kyopro/AtCoder/ARC/ARC171/ARC171D.py:42>) | 指数時間の適用範囲を明記し、小さいN向けに分ける。 | [graphs/exponential](library/graphs/exponential.py) |

## 文字列

| 用途 | クラス・関数 | ファイル数 | 元ファイルの候補 | 抽出時の確認点 | 抽出先（現在のAPI） |
|---|---|---:|---|---|---|
| Suffix Array・LCP・Z | `string`, `z_algo` | 14 | [_Strings.py:23](<D:/Kyopro/AtCoder/_Strings.py:23>) / [_test.py:649](<D:/Kyopro/AtCoder/_test.py:649>) | stringクラスのsa_is/suffix_array/lcp_array/z_algorithmも対象。クラスメソッドとしての呼び方を整理する。 | [strings/suffix_array](library/strings/suffix_array.py) |
| KMP | `make_kmp_table`, `kmp` | 4 | [_Strings.py:245](<D:/Kyopro/AtCoder/_Strings.py:245>) / [ABC/ABC135/ABC135F.py:27](<D:/Kyopro/AtCoder/ABC/ABC135/ABC135F.py:27>) | 空文字列と一致位置の返り値を確認する。 | [strings/matching](library/strings/matching.py) |
| Rolling Hash | `RollingHash`, `RollingHashSingle`, `make_hash`, `sub_hash`, `rabin_karp` | 8 | [_Strings.py:290](<D:/Kyopro/AtCoder/_Strings.py:290>) / [ABC/ABC284/ABC284F_RH.py:27](<D:/Kyopro/AtCoder/ABC/ABC284/ABC284F_RH.py:27>) | 基数・法・乱数・衝突の前提を明記する。 | [strings/rolling_hash](library/strings/rolling_hash.py) |
| 更新可能Rolling Hash | `segtree_rollinghash` | 1 | [ABC/ABC331/ABC331F.py:23](<D:/Kyopro/AtCoder/ABC/ABC331/ABC331F.py:23>) | 通常セグ木とハッシュの結合規則をまとめる。 | [strings/rolling_hash](library/strings/rolling_hash.py) |
| Trie | `Trie`, `TrieNode` | 6 | [ABC/ABC377/ABC377G.py:40](<D:/Kyopro/AtCoder/ABC/ABC377/ABC377G.py:40>) / [ABC/ABC362/ABC362G.py:14](<D:/Kyopro/AtCoder/ABC/ABC362/ABC362G.py:14>) | カウンタ等の問題固有情報を必要最小限にする。 | [strings/trie](library/strings/trie.py) |
| Aho–Corasick | `AhoCorasick`, `build_automaton`, `search_text` | 2 | [ABC/ABC362/ABC362G.py:21](<D:/Kyopro/AtCoder/ABC/ABC362/ABC362G.py:21>) / [yuki/04xx/yuki_0430.py:96](<D:/Kyopro/AtCoder/yuki/04xx/yuki_0430.py:96>) | 同一ファイル内の再定義やTrieへの依存を確認してから抽出する。 | [strings/trie](library/strings/trie.py) |
| Manacher | `manacher` | 3 | [_Strings.py:375](<D:/Kyopro/AtCoder/_Strings.py:375>) / [ABC/ABC398/ABC398F.py:24](<D:/Kyopro/AtCoder/ABC/ABC398/ABC398F.py:24>) | 奇数長のみの実装と偶数長対応を区別する。 | [strings/matching](library/strings/matching.py) |
| 編集距離・LCS | `edit_distance`, `LCS` | 4 | [_Strings.py:227](<D:/Kyopro/AtCoder/_Strings.py:227>) / [tessoku-book/B20.py:22](<D:/Kyopro/AtCoder/tessoku-book/B20.py:22>) | メモリ量と復元の有無を説明する。 | [strings/matching](library/strings/matching.py) |

## 整数・組合せ・多項式

| 用途 | クラス・関数 | ファイル数 | 元ファイルの候補 | 抽出時の確認点 | 抽出先（現在のAPI） |
|---|---|---:|---|---|---|
| 二項係数 | `Comb`, `HugeComb`, `cmb`, `Combinations` | 96 | [_Fractions.py:108](<D:/Kyopro/AtCoder/_Fractions.py:108>) / [ABC/ABC003/ABC003D.py:15](<D:/Kyopro/AtCoder/ABC/ABC003/ABC003D.py:15>) | 素数mod、nの範囲、前計算量で実装を選ぶ。 | [math/combinatorics](library/math/combinatorics.py) |
| 篩・素因数分解・約数 | `Eratosthenes`, `make_prime_table`, `prime_fact`, `prime_factorize`, `divisors` | 91 | [_Fractions.py:183](<D:/Kyopro/AtCoder/_Fractions.py:183>) / [ABC/ABC020/ABC020D.py:24](<D:/Kyopro/AtCoder/ABC/ABC020/ABC020D.py:24>) | SPF・試し割りの用途と返り値を統一する。 | [math/combinatorics](library/math/combinatorics.py) |
| Miller–Rabin・Pollard rho系 | `is_prime`, `find_prime_factor`, `factorize` | 11 | [LibraryChecker/LC_factorize.py:29](<D:/Kyopro/AtCoder/LibraryChecker/LC_factorize.py:29>) / [ABC/ABC284/ABC284D.py:33](<D:/Kyopro/AtCoder/ABC/ABC284/ABC284D.py:33>) | 対応する整数範囲・乱数・実装差を確認する。 | [math/factorize64](library/math/factorize64.py) |
| 逆元・CRT・floor_sum | `inv_gcd`, `inv_mod`, `crt`, `floor_sum` | 14 | [_ACL_math.py:15](<D:/Kyopro/AtCoder/_ACL_math.py:15>) / [LibraryChecker/LC_Composition_of_FPS.py:59](<D:/Kyopro/AtCoder/LibraryChecker/LC_Composition_of_FPS.py:59>) | 解なし、負値、modの制約を確認する。 | [math/number_theory](library/math/number_theory.py) |
| 離散対数 | `mod_log` | 2 | [ABC/ABC270/ABC270G.py:23](<D:/Kyopro/AtCoder/ABC/ABC270/ABC270G.py:23>) / [ARC/ARC042/ARC042D.py:24](<D:/Kyopro/AtCoder/ARC/ARC042/ARC042D.py:24>) | 互いに素でないケース、解なしの扱いを確認する。 | [math/number_theory](library/math/number_theory.py) |
| mod平方根 | `sqrt_mod` | 5 | [LibraryChecker/LC_Mutipoint_Evaluation.py:76](<D:/Kyopro/AtCoder/LibraryChecker/LC_Mutipoint_Evaluation.py:76>) / [LibraryChecker/LC_Composition_of_FPS.py:23](<D:/Kyopro/AtCoder/LibraryChecker/LC_Composition_of_FPS.py:23>) | 素数modを前提とするか確認する。 | [math/number_theory](library/math/number_theory.py) |
| ModInt・有理数 | `ModInt`, `MyFraction` | 5 | [_Fractions.py:15](<D:/Kyopro/AtCoder/_Fractions.py:15>) / [_test.py:590](<D:/Kyopro/AtCoder/_test.py:590>) | 速度と演算互換性を確認し、fractions.Fractionとも使い分ける。 | [math/scalar](library/math/scalar.py) |
| ゼータ・メビウス変換 | `zeta`, `mobius`, `subset_zeta_transform`, `subset_mobius_transform` | 3 | [PAST/PAST012/PAST012O.py:23](<D:/Kyopro/AtCoder/PAST/PAST012/PAST012O.py:23>) / [_Fractions.py:81](<D:/Kyopro/AtCoder/_Fractions.py:81>) | 部分集合/上位集合、入力の破壊有無を揃える。 | [math/bit_transforms](library/math/bit_transforms.py) |
| GF(2)の掃き出し | `binary_gauss_jordan` | 1 | [yuki/00xx/yuki_0074.py:23](<D:/Kyopro/AtCoder/yuki/00xx/yuki_0074.py:23>) | ランク・解・矛盾判定とビット表現を整理する。 | [math/bit_transforms](library/math/bit_transforms.py) |
| XORの最小化・minimax | `xor_minimization`, `xor_minimax` | 2 | [ADT/20240926/ADT_20240926_2I.py:60](<D:/Kyopro/AtCoder/ADT/20240926/ADT_20240926_2I.py:60>) / [yuki/01xx/yuki_0130.py:60](<D:/Kyopro/AtCoder/yuki/01xx/yuki_0130.py:60>) | 基底構築やbit trieとの役割を読み分ける。 | [math/bit_transforms](library/math/bit_transforms.py) |
| NTT・畳み込み | `ntt`, `intt`, `multiply`, `FFT`, `convolution` | 27 | [FPS24A.py:195](<D:/Kyopro/AtCoder/FPS24A.py:195>) / [LibraryChecker/LC_Composition_of_FPS.py:137](<D:/Kyopro/AtCoder/LibraryChecker/LC_Composition_of_FPS.py:137>) | 法・原始根・長さ制限と補助関数をまとめる。 | [math/polynomial](library/math/polynomial.py) |
| 形式的冪級数 | `FPS`, `FormalPowerSeries` | 26 | [LibraryChecker/LC_Inv_of_FPS.py:198](<D:/Kyopro/AtCoder/LibraryChecker/LC_Inv_of_FPS.py:198>) / [LibraryChecker/LC_Composition_of_FPS.py:198](<D:/Kyopro/AtCoder/LibraryChecker/LC_Composition_of_FPS.py:198>) | NTT/逆元等への依存が大きい。先に基本演算を選ぶ。 | [math/polynomial](library/math/polynomial.py) |
| Bostan–Mori・母関数係数 | `bostan_mori`, `_bostan_mori`, `coef_of_generating_function` | 4 | [_Convolution.py:261](<D:/Kyopro/AtCoder/_Convolution.py:261>) / [_FFT_comvolve.py:58](<D:/Kyopro/AtCoder/_FFT_comvolve.py:58>) | 畳み込み実装とmodを揃える。 | [math/polynomial](library/math/polynomial.py) |
| 線形漸化式の推定と第n項 | `berlekamp_massey`, `linear_recurrence` | 1 | [LibraryChecker/LC_Mutipoint_Evaluation.py:425](<D:/Kyopro/AtCoder/LibraryChecker/LC_Mutipoint_Evaluation.py:425>) | 係数の向きとmodの制約を確認する。 | [math/linear_recurrence](library/math/linear_recurrence.py) |
| 多項式補間 | `polynomial_interpolation`, `polynominal_interpolation`, `lagrangian_interpolation` | 6 | [LibraryChecker/LC_Mutipoint_Evaluation.py:406](<D:/Kyopro/AtCoder/LibraryChecker/LC_Mutipoint_Evaluation.py:406>) / [LibraryChecker/LC_Composition_of_FPS.py:583](<D:/Kyopro/AtCoder/LibraryChecker/LC_Composition_of_FPS.py:583>) | 名前の綴りと点の条件を統一する。 | [math/polynomial](library/math/polynomial.py) |
| 多項式GCD・逆元 | `poly_gcd`, `poly_inv` | 4 | [LibraryChecker/LC_Inv_of_Polynomials.py:699](<D:/Kyopro/AtCoder/LibraryChecker/LC_Inv_of_Polynomials.py:699>) / [LibraryChecker/LC_Composition_of_FPS.py:699](<D:/Kyopro/AtCoder/LibraryChecker/LC_Composition_of_FPS.py:699>) | FPSと行列補助クラスも含めて依存を切り出す。 | [math/polynomial](library/math/polynomial.py) |
| 分割数・特殊数列 | `partition_function`, `partition_number`, `bernoulli_number`, `stirling_first`, `stirling_second` | 5 | [LibraryChecker/LC_Composition_of_FPS.py:532](<D:/Kyopro/AtCoder/LibraryChecker/LC_Composition_of_FPS.py:532>) / [LibraryChecker/LC_Inv_of_FPS.py:532](<D:/Kyopro/AtCoder/LibraryChecker/LC_Inv_of_FPS.py:532>) | 用途ごとに小分けし、重い依存を必要な場合だけ付ける。 | [math/polynomial](library/math/polynomial.py) |
| Max-plus行列 | `sparse_matrix_max_multiply`, `matrix_max_power` | 1 | [ABC/ABC358/ABC358G.py:23](<D:/Kyopro/AtCoder/ABC/ABC358/ABC358G.py:23>) | 通常の行列積と別名にして、到達不能の単位元を明記する。 | [basic/matrix](library/basic/matrix.py) |

## 幾何・探索・応用

| 用途 | クラス・関数 | ファイル数 | 元ファイルの候補 | 抽出時の確認点 | 抽出先（現在のAPI） |
|---|---|---:|---|---|---|
| 凸包・回転キャリパー | `convex`, `ConvexHull`, `RotatingCalipers` | 5 | [yuki/00xx/yuki_0096.py:77](<D:/Kyopro/AtCoder/yuki/00xx/yuki_0096.py:77>) / [ABC/ABC022/ABC022D.py:22](<D:/Kyopro/AtCoder/ABC/ABC022/ABC022D.py:22>) | 新しい幾何スニペットとの重複を確認し、片方を選ぶ。 | [geometry/convex](library/geometry/convex.py) |
| 凸多角形の内外判定 | `inside_convex_polygon` | 1 | [ABC/ABC296/ABC296G.py:34](<D:/Kyopro/AtCoder/ABC/ABC296/ABC296G.py:34>) | 頂点順序・境界点・前処理条件を確認する。 | [geometry/convex](library/geometry/convex.py) |
| KD-tree | `kDTree`, `KDTree` | 1 | [AOJ/DSL_2_C.py:29](<D:/Kyopro/AtCoder/AOJ/DSL_2_C.py:29>) | 同じファイルに複数実装があるため代表を決める。 | [geometry/kd_tree](library/geometry/kd_tree.py) |
| 長方形の和集合面積 | `AreaOfUnionOfRectangles` | 1 | [ABC/ABC449/ABC449F.py:202](<D:/Kyopro/AtCoder/ABC/ABC449/ABC449F.py:202>) | 座標圧縮と区間木を依存込みで切り出す。 | [geometry/rectangle_union](library/geometry/rectangle_union.py) |
| 3次元の平面と点の距離 | `dist_P_from_plane_of_3points` | 1 | [yuki/01xx/yuki_0132.py:28](<D:/Kyopro/AtCoder/yuki/01xx/yuki_0132.py:28>) | 3点が一直線の場合と誤差を確認する。 | [geometry/plane_distance](library/geometry/plane_distance.py) |
| ビームサーチ | `BeamSearch` | 1 | [AHC042/main.py:145](<D:/Kyopro/AtCoder/AHC042/main.py:145>) | 探索骨格の候補。状態・評価・遷移を問題から分離する作業が必要。 | [search/heuristics](library/search/heuristics.py) |
| TSP近似・局所探索 | `tsp_approximation_return_to_start` | 1 | [AHC027/main2.py:135](<D:/Kyopro/AtCoder/AHC027/main2.py:135>) | 終了条件・乱数・距離計算を外部指定にする。 | [search/heuristics](library/search/heuristics.py) |
| ゲーム木探索 | `NegamaxStrategy`, `NegamaxAlphaBetaStrategy` | 1 | [Othello/main.py:250](<D:/Kyopro/AtCoder/Othello/main.py:250>) | 評価関数・合法手・盤面の依存が強いため優先度は低め。 | [search/heuristics](library/search/heuristics.py) |
| k-means・正規分布CDF | `kmeans`, `normal_cdf` | 2 | [AHC039/main.py:27](<D:/Kyopro/AtCoder/AHC039/main.py:27>) / [AHC022/main.py:117](<D:/Kyopro/AtCoder/AHC022/main.py:117>) | 数値精度、依存ライブラリ、乱数を確認する。標準ライブラリで済む箇所もある。 | [search/numeric](library/search/numeric.py) |

## まだ候補を特定できていないもの

Rollback UnionFind、Sparse Table、Disjoint Sparse Table、Hilbert順序、永続データ構造、Treap/Eertreeは、今回の定義名・関連名検索では切り出し元を特定できなかった。別名やmain内部にインライン実装されている可能性は残る。0-1 BFS・Warshall–Floydは今回graphs/shortest_paths.pyに追加した。

パレットの『未検出』は現在登録されたフォルダとXMLについての名前照合にすぎない。今回抽出したWaveletMatrix・LowLink・Mo等も既定の検索対象に追加済み。

## 整理時の方針

- 解答ファイルをそのまま検索対象に登録するとmainや入出力までコピーされる。候補を確認し、必要な定義・import・定数を自己完結したファイルにしてから追加する。
- MOD、INF、N、隣接リスト、再帰設定などのグローバル依存を確認する。入力を読むトップレベル処理やmainはスニペットに含めない。
- 新しいデータ構造は原則0-indexed・半開区間で説明する。既存LCATreeは1-indexed、BIT.sum(i)はiを含むので、互換APIを黙って変えない。
- 抽出した1機能について小さい実例と関連する既存テストで確認し、過去解答全体の書き換えは行わない。
- 幾何5ファイルは必要なPoint等を各ファイル内に同梱している。複数を貼る場合は定義の重複に注意する。

## 解析できなかったファイル

- [第二回全国統一予選C.py](<D:/Kyopro/AtCoder/第二回全国統一予選C.py>): `expected an indented block after 'for' statement on line 26 (第二回全国統一予選C.py, line 28)`。今回の作業では変更していない。
- [ABC/ABC432/ABC432G.py](<D:/Kyopro/AtCoder/ABC/ABC432/ABC432G.py>): `expected an indented block after 'if' statement on line 71 (ABC432G.py, line 73)`。今回の作業では変更していない。

上の一覧は83用途群。各候補を代表する実装を51ファイルに統合し、パレットに登録した。同じ用途の別実装すべてを移植したわけではない。CHTはLi Chao Tree、独自有理数は標準Fraction、探索クラスは問題依存を外した関数を採用している。
