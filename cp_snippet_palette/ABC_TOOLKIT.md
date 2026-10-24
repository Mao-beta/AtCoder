# ABCで使い回すための追加ライブラリ

2026-10-18に12ファイルを追加した。ABCのD〜Gで繰り返し使うグラフ・多重集合・mex・区間計数・桁DP・復元を中心にしている。各Fileは自己完結しており、パレットで検索してEnterでコピーし、解答のmainより上に貼る。コピー後も画面は開いたまま。

## 入力を見たら何を選ぶか

各アルゴリズムの仕組みと計算量は[アルゴリズム解説](ALGORITHMS.md)に掲載した。パレットでもFileを選び、F2の「アルゴリズムの解説」で読める。

- 「各頂点の次が1つ」「10^18回繰り返す」ならfunctional_graph。
- 「更新しながら小さい順k個」「中央値」ならfenwick_multiset。更新値を事前登録できるかを確認する。
- 「書き換えるたびmex」ならdynamic_mex。配列長Nならlimit=Nでよい。
- 「連続区間を何通り」ならsubarray_count。負数がある場合は和の尺取り法を使わない。
- 「上限Nが10進数で与えられる」ならdigit_dp。0を数えるか、先頭0をどう扱うかを確認する。
- 「選び方も出力」ならknapsack_extraやsubsequenceの復元関数。
- 「方向を変える回数」ならgrid_min_turns。移動距離を最小にする通常BFSとは目的が異なる。

一般の重み付き最短路、LCA/HLD、フロー、LIS、文字列マッチング、組合せ、畳み込みは既存の[目的別ガイド](LIBRARY_GUIDE.md#目的から探す逆引き)へ。区間更新の指定が多いときは[セグ木派生版33種](SEGTREE_RECIPES.md)も使える。

## 目的別の呼び出し方

添字は0始まり。区間は半開区間を基本とし、整数の異なる割当だけ閉区間を渡す。mod=0対応の関数は整数で正確に数えられる。各ファイル先頭に実行例と期待値、各関数・クラスに前提条件・返り値・計算量を記載した。Codonコンパイルは未確認で、bitsetと巨大整数を使うものはPyPyを基準にしている。

| やりたいこと | API・ファイル | 選ぶ条件・使い分け | 検索語 |
|---|---|---|---|
| 同じ遷移を10^18回以上繰り返す | [FunctionalGraph.jump](library/graphs/functional_graph.py) | 次の頂点が必ず1個。閉路部分を剰余で飛ばす。終端-1は既存Doubling。 | `functional graph 巨大回数 遷移` |
| 一方向の遷移で目的地へ何回で着くか | [FunctionalGraph.distance](library/graphs/functional_graph.py) | 到達不能-1。単なる無向連結性とは異なる。 | `functional graph 到達距離` |
| 各頂点から到達できる頂点数を数える | [FunctionalGraph.reachable_count](library/graphs/functional_graph.py) | 木部分の長さ＋閉路長。自己到達を含む。分解O(N)、各取得O(1)。 | `functional graph 到達数` |
| 複数の始点から最寄りの距離を求める | [multi_source_bfs](library/graphs/graph_recipes.py) | 重みなし隣接リスト。distとparentを返す。 | `複数始点 BFS 最寄り` |
| 最短経路が何通りあるか数える | [bfs_path_count](library/graphs/graph_recipes.py) | 重みなし。未到達0通り、平行辺は別経路。mod=0で厳密整数。 | `最短路 通り数` |
| 二部グラフの色と成分ごとの人数が欲しい | [bipartite_coloring](library/graphs/graph_recipes.py) | 無向辺を両方向へ登録。奇閉路はNone。 | `二部グラフ 色 成分人数` |
| DAGの大量の到達判定をまとめる | [dag_reachability](library/graphs/graph_recipes.py) | クエリ先読み。block_size件のbitsetを伝播。閉路はValueError。PyPy向け。 | `DAG 到達判定 一括` |
| A[u] XOR A[v]=wを追加して矛盾を検出する | [XorDSU.merge / is_consistent](library/structures/xor_dsu.py) | mergeは代表元を返し、矛盾はValueError。追加を拒否する用途はis_consistent。 | `XOR 制約 矛盾` |
| 連結済みの2変数のXORを取得する | [XorDSU.diff](library/structures/xor_dsu.py) | 未連結はValueError。整数の差ならWeightedUnionFind。 | `XOR 差分 DSU` |
| XOR制約を満たす整数列の総和を最小化する | [XorDSU.minimum_sum_values](library/structures/xor_dsu.py) | 成分ごと・bitごとに1の少ない向きを選ぶ。O(NB)。 | `XOR 制約 最小和` |
| 要素を増減しながら順位・中央値を求める | [FenwickMultiset.kth / bisect_left / bisect_right](library/structures/fenwick_multiset.py) | 全ての更新値をuniverseへ事前登録。kは0-indexed。重複可。 | `動的 順位 中央値` |
| 小さい順または大きい順にk個取った和を求める | [FenwickMultiset.sum_smallest / sum_largest](library/structures/fenwick_multiset.py) | kは取得のたび変更可。更新・取得O(log σ)。スライド窓にも使える。 | `小さい順 k個 和` |
| 増減する集合との絶対値の和を求める | [FenwickMultiset.sum_abs](library/structures/fenwick_multiset.py) | sum(abs(x-value))。valueは未登録でもよい。O(log σ)。 | `動的 絶対値 和` |
| 配列の書き換え後のmexを求める | [DynamicMex](library/structures/dynamic_mex.py) | 最大要素数Nならlimit=N。古い値をdiscard、新しい値をadd。範囲を全て埋めるとNone。 | `動的 mex 更新` |
| 重なる区間をまとめる | [merge_intervals](library/basic/intervals.py) | 半開区間。隣接も併合し、空区間を無視。O(N log N)。 | `区間 併合` |
| 重複を除いた被覆の長さを求める | [interval_union_length](library/basic/intervals.py) | 半開区間の和集合。整数・実数座標。O(N log N)。 | `区間 被覆長` |
| ちょうどk本の区間に覆われる長さを数える | [covered_lengths](library/basic/intervals.py) | イベントを座標順に走査。result[0]は未被覆長ではなく0。 | `区間 重複数 長さ` |
| 重ならない予定を最多選択する | [schedule_intervals](library/basic/intervals.py) | 正の長さの半開区間、重みなし。選んだ元の添字を返す。 | `区間 スケジューリング 復元` |
| 各範囲内から異なる整数を1つずつ選ぶ | [assign_distinct_in_intervals](library/basic/intervals.py) | この関数だけ整数の閉区間[l,r]。割当list、無理ならNone。 | `区間 異なる整数 割当` |
| 和がちょうどKの連続区間を数える | [count_subarrays_sum](library/basic/subarray_count.py) | 負数あり可。累積和の頻度でO(N)期待時間。 | `和がKの区間数` |
| 和がK以下の連続区間を数える | [count_subarrays_sum_leq](library/basic/subarray_count.py) | 非負列限定。K以上は全区間数からK-1以下を引く。 | `非負 部分配列 和 以下` |
| 高々・ちょうどK種類を含む連続区間を数える | [count_subarrays_distinct_at_most / count_subarrays_distinct_exact](library/basic/subarray_count.py) | 正式名はcount_subarrays_distinct_at_most / count_subarrays_distinct_exact。空区間を除く。 | `部分配列 種類数 ちょうど` |
| 最小値と最大値が指定値の区間を数える | [count_subarrays_minmax](library/basic/subarray_count.py) | 範囲外の最後の位置・min/maxの最後の位置から数える。O(N)。 | `部分配列 最小値 最大値 個数` |
| 全ての連続区間の最小値・最大値を足す | [sum_subarray_min / sum_subarray_max](library/basic/subarray_count.py) | 単調スタック。負数・同値可、O(N)。 | `全区間 最小値 総和` |
| 非零の桁がちょうどK個ある整数を数える | [count_nonzero_digits](library/basic/digit_dp.py) | 上限は10進文字列でも可。0はk=0に含める。O(LK)。 | `桁DP 非零桁 個数` |
| 各桁の和がDの倍数になる整数を数える | [count_digit_sum_mod](library/basic/digit_dp.py) | 既定では0を除く。上限を含む。O(LD*10)。 | `桁DP 桁和 倍数` |
| 禁止した数字を含まない整数を数える | [count_avoiding_digits](library/basic/digit_dp.py) | 先頭の0は除外。整数0は文字0として判定。補集合で禁止数字を含む数も数えられる。 | `桁DP 禁止数字` |
| 0から上限までに特定の数字が何回出るか | [count_digit_occurrences](library/basic/digit_dp.py) | 先頭の補助的な0を数えず、整数0は一桁として数える。O(L)。 | `桁DP 数字 出現回数` |
| 重さが巨大な0/1ナップサックを解く | [knapsack_by_value](library/basic/knapsack_extra.py) | 価値総和Vが小さい場合。重量・価値とも非負整数。O(NV)。 | `ナップサック 価値DP` |
| 各種類に個数制限があるナップサックを解く | [bounded_knapsack](library/basic/knapsack_extra.py) | (重さ,価値,個数)。単調dequeでO(NW)。重量0も対応。 | `ナップサック 個数制限` |
| 各品物を何個でも使うナップサックを解く | [knapsack_unbounded](library/basic/knapsack_extra.py) | 重さは正、O(NW)。価値は負でもよい。 | `ナップサック 無制限` |
| 目標和を作る部分集合を復元する | [subset_sum_restore](library/basic/knapsack_extra.py) | 非負列。元の添字list、無理ならNone。bitsetを使うPyPy向け。 | `部分和 復元` |
| 各ペアから必ず1つ選び目標和を作る | [two_choice_sum](library/basic/knapsack_extra.py) | 非負ペア。0/1の選択list、無理ならNone。bitset履歴を保持。 | `二択 和 復元` |
| ある文字列が部分列か判定して位置を返す | [subsequence_positions](library/strings/subsequence.py) | 最も左を選ぶ添字list、不可ならNone。O(N+M)。 | `部分列 位置 復元` |
| 長さKの辞書順最小部分列を作る | [smallest_subsequence](library/strings/subsequence.py) | 文字列・比較可能な列。単調スタックでO(N)。 | `部分列 辞書順 最小` |
| 指定文字列になる部分列の選び方を数える | [count_subsequence](library/strings/subsequence.py) | 同じ文字でも位置が違えば別。O(NM)。空patternは1。 | `部分列 選び方 通り数` |
| 異なる部分列が何種類あるか数える | [count_distinct_subsequences](library/strings/subsequence.py) | 内容が同じなら同一として数える。既定は空を除く。O(N)期待時間。 | `部分列 異なる 種類数` |
| 最長共通部分列そのものを復元する | [lcs_restore](library/strings/subsequence.py) | O(NM)時間・空間。長さだけなら既存lcs_length。 | `LCS 復元` |
| K回以内の編集で文字列を一致させられるか | [edit_distance_bounded](library/strings/subsequence.py) | 挿入・削除・置換は各1。距離>KならK+1、帯状DPでO((K+1)min(N,M))。 | `編集距離 K以内` |
| 壁のある盤面で複数始点からの距離を求める | [grid_bfs](library/basic/grid_search.py) | 座標(row,column)、4近傍。未到達・壁は-1。 | `グリッド 複数始点 BFS` |
| 迷路の最短経路を復元する | [grid_shortest_path](library/basic/grid_search.py) | 始点・終点を含む座標list。到達不能None。 | `迷路 最短経路 復元` |
| 4方向・8方向につながるマスを分類する | [grid_components](library/basic/grid_search.py) | filledで対象文字を指定。成分ID配列とサイズ列。 | `グリッド 8近傍 連結成分` |
| 迷路で曲がる回数を最小化する | [grid_min_turns](library/basic/grid_search.py) | 方向を状態に追加した0-1 BFS。最初の方向は自由、到達不能-1。 | `迷路 方向転換 最小` |
| Nを1からNで割った商をまとめて足す | [floor_quotient_ranges / sum_floor_quotients](library/math/integer_count.py) | 分母が変わるN//i。商が同じ範囲を半開区間で列挙。O(sqrt N)。 | `整数除算 商 区間 総和` |
| a*x≡bの最小非負解と周期を求める | [linear_congruence](library/math/integer_count.py) | (解,周期)、解なしNone。aとmodが互いに素でなくてもよい。 | `一次合同式 解 周期` |
| φ・μを上限まで一括で計算する | [totient_sieve / mobius_sieve](library/math/integer_count.py) | 互いに素の計数・約数での包除。0番は0、1番は1。 | `トーシェント メビウス 一括` |

## そのまま使う例

値の変更後に、小さい順K個の総和を得る。`possible_values`には初期値と今後の変更値を全て含める。

```python
bag = FenwickMultiset(possible_values, A)
bag.discard(A[i])
bag.add(x)
A[i] = x
answer = bag.sum_smallest(K)
```

巨大回数の遷移と、到達できる頂点数。

```python
fg = FunctionalGraph([1, 2, 1, 2])
fg.jump(0, 10**18)        # => 2
fg.reachable_count(0)    # => 3
fg.distance(0, 3)        # => -1
```

0が答えになり得る部分和と、解なしの区別。

```python
indices = subset_sum_restore([2, 3, 7], 5)
if indices is None:
    print('No')
else:
    print(indices)  # [0, 1]。目標0なら[]も正しい解。
```

## 問題で確認する

次の17問は、入出力付きの提出用ファイルを生成できる。ABC15問・典型90の1問・EDPCの1問。公式サンプル47件をPyPyで実行した。解が複数あるABC271 DとABC396 Eは、制約・目標和・最適値を検査している。

| 問題 | 使用するファイル | 主な確認範囲 |
|---|---|---|
| [ABC357 E](https://atcoder.jp/contests/abc357/tasks/abc357_e) | [functional_graph](library/graphs/functional_graph.py) | 全頂点の到達数 |
| [ABC367 E](https://atcoder.jp/contests/abc367/tasks/abc367_e) | [functional_graph](library/graphs/functional_graph.py) | 0回・巨大回数の遷移 |
| [ABC396 E](https://atcoder.jp/contests/abc396/tasks/abc396_e) | [xor_dsu](library/structures/xor_dsu.py) | XOR制約・矛盾・総和最小の復元 |
| [ABC281 E](https://atcoder.jp/contests/abc281/tasks/abc281_e) | [fenwick_multiset](library/structures/fenwick_multiset.py) | スライド窓の小さい順K個の和 |
| [ABC330 E](https://atcoder.jp/contests/abc330/tasks/abc330_e) | [dynamic_mex](library/structures/dynamic_mex.py) | 点変更後のmex |
| [ABC211 D](https://atcoder.jp/contests/abc211/tasks/abc211_d) | [graph_recipes](library/graphs/graph_recipes.py) | 最短路数、到達不能 |
| [ABC214 E](https://atcoder.jp/contests/abc214/tasks/abc214_e) | [intervals](library/basic/intervals.py) | 整数閉区間への異なる割当 |
| [ABC233 D](https://atcoder.jp/contests/abc233/tasks/abc233_d) | [subarray_count](library/basic/subarray_count.py) | 負数を含む和Kの区間数 |
| [ABC247 E](https://atcoder.jp/contests/abc247/tasks/abc247_e) | [subarray_count](library/basic/subarray_count.py) | 指定最小値・最大値の区間数 |
| [ABC154 E](https://atcoder.jp/contests/abc154/tasks/abc154_e) | [digit_dp](library/basic/digit_dp.py) | 非零桁数を指定した桁DP |
| [EDPC S](https://atcoder.jp/contests/dp/tasks/dp_s) | [digit_dp](library/basic/digit_dp.py) | 桁和の剰余、0を除く |
| [ABC271 D](https://atcoder.jp/contests/abc271/tasks/abc271_d) | [knapsack_extra](library/basic/knapsack_extra.py) | 二択の和・選択復元 |
| [ABC211 C](https://atcoder.jp/contests/abc211/tasks/abc211_c) | [subsequence](library/strings/subsequence.py) | 指定部分列の選び方 |
| [ABC386 F](https://atcoder.jp/contests/abc386/tasks/abc386_f) | [subsequence](library/strings/subsequence.py) | K回以内の編集距離 |
| [ABC325 C](https://atcoder.jp/contests/abc325/tasks/abc325_c) | [grid_search](library/basic/grid_search.py) | 8近傍の連結成分 |
| [典型90 043](https://atcoder.jp/contests/typical90/tasks/typical90_aq) | [grid_search](library/basic/grid_search.py) | 最小方向転換回数 |
| [ABC230 E](https://atcoder.jp/contests/abc230/tasks/abc230_e) | [integer_count](library/math/integer_count.py) | 分母が変わる除算の総和 |

```powershell
# リポジトリ直下で実行
.venv\Scripts\python.exe cp_snippet_palette\verify\build.py --atcoder abc281_e
.venv\Scripts\python.exe cp_snippet_palette\verify\build.py --atcoder --list
```

出力先は`cp_snippet_palette/verify/build/問題ID.py`。提出時はそのファイルの内容を使う。

サンプルが直接カバーしないDAG到達判定、二部判定、区間併合・被覆、φ/μ、別のDP形式などは、[13件の専用テスト](tests/test_abc_toolkit.py)で小さな入力の全列挙・愚直計算・使用例と比較した。最大制約での速度・メモリとオンラインACは未確認。

追加分の検索はF5で反映する。F2の「ABCでの使い分け」表示を反映するにはパレットを起動し直す。
