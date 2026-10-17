# ACLに合わせた呼び出し方

対象は、このパレットの提出用ファイル。C++版ACLの意味・添字・半開区間・合成順を基準に、Pythonでのコンストラクタは[ac-library-python](https://github.com/not522/ac-library-python/tree/master/atcoder)に合わせた。`e`と`id_`は関数ではなく単位元の**値**を渡す。これは[公式C++版のテンプレート引数](https://atcoder.github.io/ac-library/production/document_ja/segtree.html)をPythonの引数へ移すための違い。

旧名の互換呼び出しは下表に分けた。新規コードでは「推奨API」を使う。PyCharmに保存済みのLive TemplateのXMLと、過去の解答ファイルは書き換えていない。パレットでは**File**の該当ファイルを選ぶ。

現行コードとの最終照合：2026-10-17。パレットでF2を押すと、選択中のファイルに対応する下表の説明と公開APIを確認できる。検索・コピー操作は[LOCAL_USAGE.md](LOCAL_USAGE.md)を参照。

## 対応表

| 機能・コピーするファイル | 推奨API | 戻り値・注意 | 旧呼び出し |
|---|---|---|---|
| [DSU](snippets/structures/UnionFind.py) | `DSU(n)`、`merge(a,b)`、`same(a,b)`、`leader(a)`、`size(a)`、`groups()` | mergeは代表元。groupsの順序は利用しない。 | `UnionFind`は別名。`unite`だけは統合したかのbool。 |
| [Fenwick Tree](snippets/structures/BIT.py) | `FenwickTree(n)`、`add(p,x)`、`sum(l,r)` | sumは`[l,r)`。初期値は0。配列からの構築は独自拡張。 | `BIT.sum(i)`だけは旧`[0,i]`。BITでも2引数なら`[l,r)`。 |
| [SegTree](snippets/structures/segtree.py) | `SegTree(op,e,v)` | vは長さnまたは初期配列。set/get/prod/all_prod/max_right/min_left。 | `segtree(v,op,e)`を保持。 |
| [LazySegTree](snippets/structures/lazy_segtree.py) | `LazySegTree(op,e,mapping,composition,id_,v)` | `apply(l,r,f)`は区間更新、`apply(p,f=f)`は1点更新。 | `lazy_segtree(v,op,e,mapping,composition,id_)`とapply_pointを保持。 |
| [SCC](library/graphs/scc.py) | `SCCGraph(n)`、`add_edge(u,v)`、`scc()` | 成分はトポロジカル順。 | `SCC`は別名。scc_ids/dagは独自拡張。 |
| [TwoSAT](library/graphs/scc.py) | `TwoSAT(n)`、`add_clause(i,f,j,g)`、`satisfiable()`、`answer()` | 節は`(x[i]==f) or (x[j]==g)`。判定がTrueの後だけanswerを解として使う。節追加後は再判定。 | `solve()`は解リスト、解なしNone。 |
| [最大流](library/graphs/max_flow.py) | `MFGraph(n)`、`add_edge(u,v,cap)`、`flow(s,t,flow_limit=None)` | 既に同じ引数順。edges/get_edge/change_edge/min_cutも使用可能。辺の端点名はPython版のsrc/dst。 | 変更なし。 |
| [最小費用流](library/graphs/min_cost_flow.py) | `MCFGraph(n)`、`add_edge(u,v,cap,cost)`、`flow(s,t,flow_limit=None)`、`slope(s,t,flow_limit=None)` | flowは(流量,費用)。元の費用は非負。flow/slopeは同じ個体で合計1回。 | 変更なし。 |
| [数論](library/math/number_theory.py) | `pow_mod(x,n,m)`、`inv_mod(x,m)`、`crt(r,m)`、`floor_sum(n,m,a,b)` | CRTは(最小非負解,周期)、解なし(0,0)。floor_sumはΣ floor((a*i+b)/m)。 | inv_gcd、負のa,b対応等は拡張。 |
| [文字列](library/strings/suffix_array.py) | `suffix_array(s,upper=None)`、`lcp_array(s,sa)`、`z_algorithm(s)` | upper指定時は整数列`0<=s[i]<=upper`。lcpは隣接する接尾辞間で長さn-1。 | 1引数SAも従来どおり。空列のLCPは拡張として[]。 |
| [畳み込み](library/math/polynomial.py) | `convolution(998244353,a,b)` | Python版と同じmod先頭。ただしこの実装は998244353専用。他のmodを指定するとValueError。 | `convolution(a,b)`も998244353として保持。 |
| [modint](library/math/scalar.py) | `with ModContext(m):` 内で `Modint(v=0)` | val()/mod()/inv()、`a**n`、`a//b`。C++形式のpow(n)と`/`も使用可能。 | `ModInt(value,mod)`は保持。ただし法の取得は旧`.mod`属性から`.mod()`へ変更。 |

`DSU()`、`FenwickTree()`、`SCCGraph()`、`TwoSAT()`はn=0を受け付ける。APIの対応は、上表に挙げた呼び出しの意味・引数順を対象とし、内部属性名やすべてのキーワード引数名まで同一にするものではない。

`SegTree_compat.py`には、さらに古い`SegTree(v,op,e)`とupdate/query/addを残している。**新しいSegTreeとは同じクラス名で引数順が違う**ため、旧解答を動かす用途に限る。新規コードでは`segtree.py`をコピーする。

## 短い例

以下のコードの前に、使うファイルをパレットから貼り付ける。

```python
fw = FenwickTree(3)
fw.add(0, 2)
fw.add(1, 5)
fw.add(2, 3)
assert fw.sum(1, 3) == 8

seg = SegTree(max, -1, [3, 1, 4])
seg.set(1, 5)
assert seg.prod(0, 2) == 5
assert seg.max_right(0, lambda value: value < 4) == 1

sat = TwoSAT(2)
sat.add_clause(0, True, 0, True)
sat.add_clause(0, False, 1, True)
if sat.satisfiable():
    assert sat.answer() == [True, True]

with ModContext(11):
    a, b = Modint(10), Modint(3)
    assert (a // b).val() == 7
    assert b.inv().val() == 4
    assert b.pow(4).val() == 4
```

アフィン更新・区間和の遅延セグ木では、集約値を`(和,長さ)`、更新を`(倍率,加算値)`にする。

```python
MOD = 998244353

def op(x, y):
    return ((x[0] + y[0]) % MOD, x[1] + y[1])

def mapping(f, x):
    a, b = f
    return ((a * x[0] + b * x[1]) % MOD, x[1])

def composition(f, g):
    # gを先に、fを後に適用する。
    return (f[0] * g[0] % MOD, (f[0] * g[1] + f[1]) % MOD)

seg = LazySegTree(op, (0, 0), mapping, composition, (1, 0),
                  [(1, 1), (2, 1), (3, 1)])
seg.apply(0, 3, (2, 1))   # [3, 5, 7]
seg.apply(1, f=(0, 9))    # [3, 9, 7]。1点更新には f= が必要。
assert seg.prod(0, 3)[0] == 19
```

1点更新に`apply(p,f)`と書くと、Python版ではfがright引数に入ってしまう。[Python版のapply定義](https://github.com/not522/ac-library-python/blob/master/atcoder/lazysegtree.py)に合わせて、`apply(p,f=f)`と書く。

## 対応範囲

- ACLにないWeightedUnionFind、HLD、WaveletMatrixなどは、それぞれの説明に従う。特にLCATreeは既存互換の1-indexed。
- 多項式ファイルは998244353用。ACLが持つ他の法、整数畳み込み、Modint配列の畳み込みまでは対応しない。
- modintはPython移植版のModContext方式。C++のset_modやstatic_modint型生成を再現したものではない。異なるmodの値を混ぜると例外。
- PyPy向けの変更であり、Codonコンパイルは未実施。ModContext、動的な型生成、コールバックなどはCodonで個別対応が必要。

## 照合元

データ構造：[DSU](https://atcoder.github.io/ac-library/production/document_ja/dsu.html)、[Fenwick Tree](https://atcoder.github.io/ac-library/production/document_ja/fenwicktree.html)、[Segtree](https://atcoder.github.io/ac-library/production/document_ja/segtree.html)、[Lazy Segtree](https://atcoder.github.io/ac-library/production/document_ja/lazysegtree.html)。

グラフ：[SCC](https://atcoder.github.io/ac-library/production/document_ja/scc.html)、[Two SAT](https://atcoder.github.io/ac-library/production/document_ja/twosat.html)、[Maxflow](https://atcoder.github.io/ac-library/production/document_ja/maxflow.html)、[MinCostFlow](https://atcoder.github.io/ac-library/production/document_ja/mincostflow.html)。

その他：[Math](https://atcoder.github.io/ac-library/production/document_ja/math.html)、[String](https://atcoder.github.io/ac-library/production/document_ja/string.html)、[Convolution](https://atcoder.github.io/ac-library/production/document_ja/convolution.html)、[Modint](https://atcoder.github.io/ac-library/production/document_ja/modint.html)。確認日：2026-10-17。
