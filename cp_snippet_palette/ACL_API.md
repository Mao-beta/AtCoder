# ACL-for-pythonに合わせた呼び出し方

基準は **[shakayami/ACL-for-python](https://github.com/shakayami/ACL-for-python)**。2026-10-18に[コミット9234fd3](https://github.com/shakayami/ACL-for-python/tree/9234fd354a71e5f27810235539a3625f74aec087)のソースと照合した。クラス・関数名、引数順とキーワード名、戻り値の形をこの実装に合わせる。

添字・頂点番号・順位は0始まり、配列や整数座標の区間は半開区間`[l,r)`。参照先に1始まりの仕様があっても、この規約を優先する。セグ木の`E`と遅延セグ木の`ID`は値を渡す。初期値は配列で渡し、長さNなら`[E] * N`とする。旧コンストラクタや別名への自動変換は行わない。

## 何をコピーしてどう呼ぶか

| コピーするファイル | 呼び出し | 戻り値・注意点 |
|---|---|---|
| [UnionFind.py](snippets/structures/UnionFind.py) | `dsu(N)`、`merge(a,b)`、`same(a,b)`、`leader(a)`、`size(a)`、`groups()` | mergeは代表元。統合の成否をboolで判定しない。groupsは代表元順、成分内は頂点番号順。 |
| [BIT.py](snippets/structures/BIT.py) | `fenwick_tree(N)`、`add(p,x)`、`sum(l,r)`、`sum0(r)` | 初期値は0。sum0は`[0,r)`。sumは常に2引数。 |
| [segtree.py](snippets/structures/segtree.py) | `segtree(V, OP, E)` | `set(p,x)`、`get(p)`、`prod(l,r)`、`all_prod()`、`max_right(l,f)`、`min_left(r,f)`。Vは配列。 |
| [lazy_segtree.py](snippets/structures/lazy_segtree.py) | `lazy_segtree(V, OP, E, MAPPING, COMPOSITION, ID)` | 区間更新は`apply(l,r,f)`、一点更新は`apply_point(p,f)`。 |
| [scc.py](library/graphs/scc.py) | `scc(N, edges)` | edgesは`[(u,v),...]`。成分ごとの頂点listをトポロジカル順に返す。 |
| [scc.py](library/graphs/scc.py) | `two_sat(n, clause)` | clauseは`[(i,f,j,g),...]`で`(x[i]==f) or (x[j]==g)`。解のboolリスト、充足不能ならNone。 |
| [max_flow.py](library/graphs/max_flow.py) | `mf_graph(n_)`、`add_edge(From_,To_,Cap_)`、`flow(s,t,flow_limit)` | add_edgeは辺ID。get_edgeは属性`From,To,Cap,Flow`のedge。edges()はdictのlist、edges(False)はedgeのlist。 |
| [min_cost_flow.py](library/graphs/min_cost_flow.py) | `mcf_graph(N)`、`add_edge(From,To,cap,cost)`、`flow(s,t,flow_limit)`、`slope(s,t,flow_limit)` | add_edgeの戻り値はNone。get_edge/edgesはキー`from,to,cap,flow,cost`のdict。flowは(流量,費用)、slopeはその端点のlist。 |
| [number_theory.py](library/math/number_theory.py) | `inv_gcd(a,b)`、`inv_mod(x,m)`、`crt(r,m)`、`floor_sum(n,m,a,b)` | inv_gcdは(gcd,逆元)、crtは(最小非負解,周期)、解なしは(0,0)。floor_sumは負のa,bにも対応。 |
| [factorize64.py](library/math/factorize64.py) | `is_probable_prime(n)`、`prime_fact(N)`、`divisors(N)`、`totient(N)`、`lcm(x,y)` | prime_factはCounter({素数:指数})。64bit範囲で使用。約数の順序は未指定。 |
| [suffix_array.py](library/strings/suffix_array.py) | `String(s).suffix_array()`、`String(s).lcp_array(sa=None)`、`String(s).z_algorithm()` | sは文字列・整数列。lcp_arrayのsa省略時は内部でSAを作る。 |
| [polynomial.py](library/math/polynomial.py) | `FFT(MOD).convolution(a,b)` | 係数は低次から。素数MODを指定。NTT長はMOD-1を割り切る2冪。998244353なら最大2**23。片方が40係数以下なら直接計算。 |
| [polynomial.py](library/math/polynomial.py) | `FPS(L)`、`inv(d=-1)`、`diff()`、`integral()`、`log(deg=-1)`、`exp(deg=-1)`、`sqrt(deg=-1)`、`powfps(k,deg=-1)` | 998244353固定。係数は`.Func`。d/degは係数数、-1は入力の係数数。sqrtの解なしはFPS([])。 |

フローのflow_limit省略値は`2**63-1`。最小費用流は元の辺費用が非負で、flow/slopeは1オブジェクトにつき合計1回。指定流量を送れない場合も部分結果を返すため、戻り値の流量を確認する。

## そのまま使える例

対応するファイルを貼り付けた後に実行する。

```python
uf = dsu(5)
if not uf.same(0, 1):
    uf.merge(0, 1)
bit = fenwick_tree(3)
for i, value in enumerate([3, 1, 4]):
    bit.add(i, value)
bit.sum(1, 3), bit.sum0(2)  # => (5, 4)
seg = segtree([3, 1, 4], max, -1)
seg.set(1, 5)
seg.prod(0, 2)  # => 5
scc(3, [(0, 1), (1, 0), (1, 2)])  # => [[0, 1], [2]]
answer = two_sat(2, [(0, True, 0, True), (0, False, 1, True)])
answer  # => [True, True]
if answer is None:  # []も有効な解なので「if not answer」は使わない
    print("解なし")
```

区間を`x ← a*x+b`で更新して区間和を取得する例。`composition(f,g)`は先にg、その後fを適用する。

```python
MOD = 998244353
op = lambda x, y: ((x[0] + y[0]) % MOD, x[1] + y[1])
mapping = lambda f, x: ((f[0]*x[0] + f[1]*x[1]) % MOD, x[1])
composition = lambda f, g: (f[0]*g[0] % MOD, (f[0]*g[1] + f[1]) % MOD)
seg = lazy_segtree([(1, 1), (2, 1), (3, 1)],
                  op, (0, 0), mapping, composition, (1, 0))
seg.apply(0, 2, (2, 1))     # [3,5,3]
seg.apply_point(2, (0, 7))  # [3,5,7]
seg.prod(0, 3)[0]          # => 15
```

辺情報は最大流と最小費用流で形式が異なる。

```python
g = mf_graph(2)
edge_id = g.add_edge(0, 1, 3)
g.flow(0, 1)              # => 3
g.get_edge(edge_id).Flow  # => 3
g.edges()[0]["flow"]      # => 3
g.edges(False)[0].Cap     # => 3
h = mcf_graph(2)
h.add_edge(0, 1, 3, 5)    # 戻り値なし。最初の辺のIDは0
h.flow(0, 1, 2)           # => (2, 10)
h.get_edge(0)["flow"]     # => 2
text = String("banana")
text.suffix_array()       # => [5, 3, 1, 0, 4, 2]
text.lcp_array()          # => [1, 3, 0, 0, 2]
FFT(998244353).convolution([1, 2], [3, 4])  # => [3, 10, 8]
FPS([1, -1]).inv(5).Func       # => [1, 1, 1, 1, 1]
FPS([1, 1]).powfps(3, 4).Func  # => [1, 3, 3, 1]
```

## 設定済みの派生版

[セグ木の派生版33種](SEGTREE_RECIPES.md)では、range_top2(V)やrange_affine_sum(V)がOP/E/MAPPING等を内部で設定する。メソッド名は同じで、set/getに元の要素を渡せる。prodの戻り値とapplyの更新値は派生版ごとの表に従う。通常のsegtree/lazy_segtreeのAPIは変更していない。

## 独自拡張と実装上の違い

- fenwick_tree.from_list(values)は初期配列からO(N)で構築する。get/set/lower_bound/to_listも利用できる。lower_boundは全要素非負の場合だけ使う。
- dsu.group_count()は成分数。scc_ids(N,edges)は頂点ごとの成分番号、scc_dag(N,edges)は縮約DAG。
- StringはUnicode・空入力にも対応し、空入力のLCPは[]。longest_common_substring(s,t)は共通区間を返す。
- 多項式のfps_*関数はlistを入出力し、sizeは係数数。fps_sqrtの解なしはNone。FPSの多点評価・Taylor Shift、多項式GCD/逆元なども独自拡張。
- 指定先のFPSにある次数指定・平方根・比較の不具合は引き継がず、指定係数数と数学的な演算結果を優先する。内部の実装方式やエラー時の例外型まで同一とは限らない。
- WeightedUnionFind、HLD、WaveletMatrix、Modintなど指定先にないAPIは、各ファイルの説明に従う。

## 独自ライブラリの共通規約

2026-10-18に重複した旧名を削除し、次の呼び出しへ統一した。順位`k=0`は最小・最大・最初の出現を意味する。`merge`の戻り値を真偽値として統合の成否に使わず、必要なら事前に`same`を確認する。

配列の添字と平面上の実座標は区別する。`OfflineFenwick2D.prefix_sum(x,y)`は負の座標も含めた「x未満かつy未満」の全点の和なので、この名前を使う。`DynamicFenwickTree2D.sum0(bottom,right)`は0始まりの格子の原点からの和。

| 対象 | 現在の呼び出し | 戻り値・境界・計算量 |
|---|---|---|
| WeightedUnionFind | `WeightedUnionFind(N)`、`leader(a)`、`same(a,b)`、`merge(a,b,w)`、`potential(a)`、`diff(a,b)` | `potential[b]-potential[a]=w`を課す。mergeは新規統合・既存制約との一致のどちらも代表元。矛盾はValueError。基本操作は償却O(α(N))。 |
| LCATree / HLD | `lca(u,v)`、`distance(u,v)`、`kth_ancestor(v,k)`、`jump(u,v,k)` | 頂点は0始まり、根の既定値は0。距離は辺数、存在しない祖先・経路上の頂点は-1。O(log N)。 |
| BiSegTree | `BiSegTree(V,OP,E)`、`set(p,x)`、`get(p)`、`prod(l,r)`、`prod_reverse(l,r)` | 初期配列Vを渡す。正順・逆順の集約O(log N)、空区間はE。経路は`path_prod(hld,seg,u,v,edge=False)`でO(log² N)。 |
| SegmentTreeBeats | `SegmentTreeBeats(V)`、`chmin(l,r,x)`、`chmax(l,r,x)`、`add(l,r,x)`、`assign(l,r,x)` | 更新の戻り値はNone。chmin/chmaxは償却解析が必要で単発最悪O(N)。加算・代入はO(log N)。 |
| SegmentTreeBeatsの集計 | `min(l,r)`、`max(l,r)`、`sum(l,r)`、`prod(l,r)` | prodは(最小,最大,和)、空区間は(inf,-inf,0)。集計O(log N)。`get(p)`・`set(p,x)`も使える。 |
| fenwick_tree / DynamicFenwickTree | `add(p,x)`、`sum0(r)`、`sum(l,r)` | sum0は[0,r)、sumは[l,r)。O(log N)。疎な版は辞書の期待計算量。2Dの`sum0(bottom,right)`は原点からの長方形和。 |
| WaveletMatrix | `get(i)`、`count(l,r,value)`、`count_less(l,r,value)`、`kth_smallest(l,r,k)`、`kth_largest(l,r,k)` | getは元の値、countは一致数、count_lessは未満の個数。順位範囲外はIndexError。O(log(σ+1))、σは値の種類数。 |
| 出現位置の検索 | `WaveletMatrix.select(value,k,default=-1)`、`FullyIndexableDictionary.select(bit,k,default=-1)` | 第1引数が探す値、第2引数が0始まりの出現順位。位置を0始まりで返し、なければdefault。Wavelet版O(log(σ+1) log(N+1))、bit版O(log(N+1))。 |
| SortedSet / SortedMultiset | `bisect_left(x)`、`bisect_right(x)`、`s[k]` | x未満・x以下の個数と、k番目の値。順位はbisectと同じ意味。O(√N)。 |
| AVLTree | `set(key,val)`、`get(key,default=None)`、`discard(key)`、`kth(k)`、`ge(key)`、`lt(key)` | getの未登録はdefault、`tree[key]`の未登録はKeyError。discardは削除できたかのbool。ge/ltは条件を満たすキー、なければNone。O(log N)。 |
| Heapq | `push(x)`、`discard(x)`、`top()`、`pop()` | discardは値xを1個削除できたかのbool。空のtop/popはIndexError。遅延削除を含め償却O(log N)。 |
| LiChaoTree / LiChaoInt | `add_line(a,b)`、`query(x)` | y=a*x+bを追加し、最小/最大の値を取得。有効な直線がなければNone、定義域外はValueError。Int版の範囲は[xmin,xmax)。O(log N)またはO(log U)、Uは整数定義域の長さ。 |
| Line / 多角形 | `Line.intersection(other)`、`locate(point)`、`contains(point)`、`contains_strict(point)` | 直線の唯一の交点はPoint、平行・一致はNone。多角形のlocateは外-1・境界0・内1、containsは境界を含むbool。線分の幾何学的な端点は含む。 |
| Modint | `with ModContext(mod):`内で`Modint(v)`、`val()`、`inv()`、`x**n`、`x/y` | 法付き整数。加減乗算O(1)、逆元・除算O(log mod)、n乗O(log(n+1))回の整数演算。 |
| GF(2)の方程式 | `solve_gf2(rows,rhs,variables)` / `linear_equations_gf2(rows,rhs,variables)` | 前者は(rank,特解bitset)、後者は(特解bitset,核の基底list)。解なしは両方None。入力行のbit jが変数j。 |

更新と集計を併用する例。各クラスのファイルを貼り付けて使う。

```python
uf = WeightedUnionFind(3)
uf.merge(0, 1, 5)         # => 0（代表元）
uf.merge(1, 2, -2)        # => 0
uf.diff(0, 2)            # => 3
wm = WaveletMatrix([5, 1, 5, 3])
wm.kth_smallest(0, 4, 0) # => 1
wm.kth_largest(0, 4, 0)  # => 5
wm.count(0, 4, 5)        # => 2
wm.select(5, 1)          # => 2（2回目の出現位置）
seg = SegmentTreeBeats([1, 5, 3, 7])
seg.chmin(0, 4, 4)
seg.add(1, 3, 10)
seg.prod(0, 4)           # => (1, 14, 32)
```

## 削除した旧形式

`SegTree_compat.py`、大文字のSegTree/LazySegTree、旧BITの閉区間sum、DSU/UnionFind別名、SCCGraph/TwoSATクラス、MFGraph/MCFGraph、関数形式のSA/LCP/Z、modを先頭に取るconvolution、公開FormalPowerSeriesは同梱APIから削除した。過去の解答ファイルやuserのLive Templateは書き換えていない。パレットでは**File**を選んで現行APIをコピーする。

今回削除した主な名前は、WeightedUnionFindのfind/unite/is_same/get_weight、LCATree.get_LCA、fenwick_tree.prod/range_sum、WaveletMatrix.quantile/kth_min/kth_max/range_rank/access、AVLのinsert/delete/member/lower_bound/upper_bound/find_kth_element、Heapq.erase/peek、Beatsのupdate_min/update_max/add_val/update_val/query系・range_*別名、BiSegTree.fold_lr/fold_rl、HLD.dist/path_fold_noncomm、ModInt互換クラス・Modint.inverse/pow/`//`、Line.intersection_point。置き換え先と戻り値は上の表を使う。パレットはF5で読み直せる。

参照元：[segtree](https://github.com/shakayami/ACL-for-python/blob/master/segtree.py)、[lazy_segtree](https://github.com/shakayami/ACL-for-python/blob/master/lazysegtree.py)、[maxflow](https://github.com/shakayami/ACL-for-python/blob/master/maxflow.py)、[mincostflow](https://github.com/shakayami/ACL-for-python/blob/master/mincostflow.py)、[String](https://github.com/shakayami/ACL-for-python/blob/master/acl_string.py)、[FFT](https://github.com/shakayami/ACL-for-python/blob/master/convolution.py)、[FPS](https://github.com/shakayami/ACL-for-python/blob/master/fps.py)。
