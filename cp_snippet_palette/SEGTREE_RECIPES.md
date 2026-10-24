# セグ木・遅延セグ木の設定済み派生版

33種類の集約・更新を用意した。**コールバックや内部tupleを組まず、元の配列を渡して構築できる。** 一点更新は[segtree_monoids.py](library/structures/segtree_monoids.py)、区間更新は[lazy_segtree_actions.py](library/structures/lazy_segtree_actions.py)をFileごとコピーする。それぞれ単体で動き、通常のsegtree/lazy_segtreeを別途貼る必要はない。

パレットで`range_top2`、`二乗和`、`連続ビット`などを検索してFileを選ぶ。F2の先頭に短い使用例があり、このページの表でも用途・戻り値・設計を確認できる。クラス名を特定できたら、`seg = range_top2(A)`のように使う。2ファイルを同時に貼ることもできる。

## 共通の使い方

設計の根拠は[モノイドの解説](ALGORITHMS.md#セグメント木のモノイド集)と[遅延作用の解説](ALGORITHMS.md#遅延セグメント木の作用集)を参照する。各ノードで保持する情報、左右の結合式、更新の合成・適用条件をまとめた。F2でも選択ファイルの解説を読める。

添字は0始まり、区間は`[l,r)`。**AtCoderの1始まり・両端を含む`[L,R]`は、`(L-1,R)`へ変換する。** コンストラクタの先頭に初期配列を渡す。引数順とメソッド名はshakayami/ACL-for-pythonに合わせ、各派生クラスが演算・単位元・写像を設定する。

| 操作 | 意味 |
|---|---|
| `seg.set(p,x)` | A[p]をxへ置換。内部tupleへの変換は不要。 |
| `seg.get(p)` | 現在の要素。剰余を使う派生版は正規化後の値、range_gcdは絶対値。 |
| `seg.prod(l,r)` / `seg.all_prod()` | 区間 / 全体の集約値。下表の戻り値になる。 |
| `seg.apply(l,r,f)` / `seg.apply_point(p,f)` | 遅延セグ木の区間 / 一点更新。fの形式は下表。 |
| `seg.max_right(l,pred)` | pred(prod(l,r))が真となる最大r。 |
| `seg.min_left(r,pred)` | pred(prod(l,r))が真となる最小l。 |
| `seg.to_list()` | 現在の全要素を元の形式で取り出す。O(N)。 |

境界探索では`pred(空区間の値)=True`が必要で、区間を広げると真から偽へ一度だけ変わる条件にする。例えば非負列の和の上限、最大値の上限、連続1の長さの上限など。負数を含む和や剰余を取った和では、その単調性を仮定できない。

構築はO(N)、更新・区間取得・境界探索はO(log N)、all_prodはO(1)。通常版のgetはO(1)、遅延版のgetはO(log N)。XOR基底の結合はO(B²)なので、その版だけ構築上界O(N B²)、更新・集約O(B² log N)。整数の桁数に依存する演算コストは別途かかる。

## 一点更新の16種類

以下のクラスはすべて[segtree_monoids.py](library/structures/segtree_monoids.py)にある。表の`V`は初期配列。

| やりたいこと | 構築するクラス | prodの戻り値・空区間 | モノイドの設計 |
|---|---|---|---|
| 点代入して和を取る | [range_sum(V)](library/structures/segtree_monoids.py) | 和。空は0。 | 足し算、単位元0。点加算だけならFenwickも候補。 |
| 点代入して最小値を取る | [range_min(V)](library/structures/segtree_monoids.py) | 最小値。空はinf。 | min、単位元inf。 |
| 点代入して最大値を取る | [range_max(V)](library/structures/segtree_monoids.py) | 最大値。空は-inf。 | max、単位元-inf。 |
| 点代入してGCDを取る | [range_gcd(V)](library/structures/segtree_monoids.py) | 非負GCD。空は0。 | gcd、単位元0。要素も絶対値で保持する。 |
| 点代入してXORを取る | [range_xor(V)](library/structures/segtree_monoids.py) | XOR。空は0。 | XOR、単位元0。非負整数用。 |
| 点代入してORを取る | [range_or(V)](library/structures/segtree_monoids.py) | OR。空は0。 | OR、単位元0。非負整数用。 |
| 点代入してANDを取る | [range_and(V)](library/structures/segtree_monoids.py) | AND。空は-1。 | 全ビット1の-1を単位元にする。非負整数用。 |
| 最小値が何個あるか数える | [range_min_count(V)](library/structures/segtree_monoids.py) | (最小値,個数)。空は(inf,0)。 | 小さい側を採用。同値なら個数を足す。 |
| 最大値が何個あるか数える | [range_max_count(V)](library/structures/segtree_monoids.py) | (最大値,個数)。空は(-inf,0)。 | 大きい側を採用。同値なら個数を足す。 |
| 2番目に大きい値・個数を取る | [range_top2(V)](library/structures/segtree_monoids.py) | (最大値,個数,異なる第2位,個数)。欠けた値はNone、個数0。 | 左右の上位2値を統合。同じ値の重複をまとめる。 |
| 最大部分配列和を取る | [range_max_subarray(V,allow_empty=True)](library/structures/segtree_monoids.py) | (sum,prefix,suffix,best)。空は(0,0,0,0)。Falseなら最大値3つが-inf。 | 左内・右内・左suffix＋右prefixの3候補。 |
| 括弧の点変更・交換と区間判定 | [range_brackets(V)](library/structures/segtree_monoids.py) | (balance,min_prefix,max_prefix)。空は(0,0,0)。 | '('を+1、')'を-1。右のprefixに左のbalanceを足す。balanced(l,r)も用意。 |
| 一次関数を左から順に合成する | [range_affine_composite(V,mod=998244353)](library/structures/segtree_monoids.py) | (a,b)。空は恒等関数(1,0)。 | V[i]=(a,b)。左f、右gの結合はg∘f。mod=0なら厳密整数。 |
| 2×2行列の積を取る | [range_matrix_product(V,mod=998244353)](library/structures/segtree_monoids.py) | (a00,a01,a10,a11)。空は単位行列。 | 左行列×右行列。mod=0可。列ベクトルに作用させると右が先。 |
| 区間から選ぶ部分集合XORを最大化する | [range_xor_basis(V,bits=60)](library/structures/segtree_monoids.py) | 正規化した線形基底tuple。空は()。 | XOR基底の併合。max_xor(l,r,x=0)、rank(l,r)も用意。Bはビット数。 |
| 単位元を作りにくい結合的演算を使う | [semigroup_segtree(V,OP)](library/structures/segtree_monoids.py) | OPの集約値。空はNone。 | Noneを単位元として半群をモノイドへ拡張。要素・OPの結果にNoneを使わない。 |

## 区間更新の17種類

以下のクラスはすべて[lazy_segtree_actions.py](library/structures/lazy_segtree_actions.py)にある。`apply(l,r,f)`のfを表に示す。

| やりたいこと | 構築するクラス | 更新fとprodの戻り値 | 保持する情報・設計 |
|---|---|---|---|
| 区間加算・区間和 | [range_add_sum(V)](library/structures/lazy_segtree_actions.py) | f=加算量。prodは和、空0。 | (和,長さ)。和にf×長さを足す。 |
| 区間代入・区間和 | [range_assign_sum(V)](library/structures/lazy_segtree_actions.py) | f=代入値。prodは和、空0。 | (和,長さ)。新しい代入が古い代入を上書き。Noneが恒等更新なので0も代入可。 |
| 加算・乗算・代入を混ぜて区間和 | [range_affine_sum(V,mod=998244353)](library/structures/lazy_segtree_actions.py) | f=(a,b)でx←a*x+b。prodは和、空0。 | (和,長さ)。加算(1,b)、乗算(a,0)、代入(0,b)。mod=0可。 |
| 区間加算・最小値 | [range_add_min(V)](library/structures/lazy_segtree_actions.py) | f=加算量。prodは最小値、空inf。 | (最小値,長さ)。空区間は更新しても空のまま。 |
| 区間加算・最大値 | [range_add_max(V)](library/structures/lazy_segtree_actions.py) | f=加算量。prodは最大値、空-inf。 | (最大値,長さ)。全要素への同じ加算はmaxにも加算できる。 |
| 区間加算・最小値の個数 | [range_add_min_count(V)](library/structures/lazy_segtree_actions.py) | f=加算量。prodは(最小値,個数)、空(inf,0)。 | 最小値だけ加算し個数は保持。全要素非負なら最小値0の個数を数える用途にも使える。 |
| 負の倍率を含む一次変換とmin/max | [range_affine_minmax(V)](library/structures/lazy_segtree_actions.py) | f=(a,b)。prodは(min,max)、空(inf,-inf)。 | (min,max,長さ)。a<0でmin/maxを交換。剰余なし。 |
| chmin・chmax・代入とmin/max | [range_clamp_minmax(V)](library/structures/lazy_segtree_actions.py) | f=(lo,hi)、lo<=hi。prodは(min,max)、空(inf,-inf)。 | clampの合成もclamp。chmin/chmax/assignメソッドもある。和は扱わない。 |
| 0/1反転・転倒数 | [range_flip_inversions(V)](library/structures/lazy_segtree_actions.py) | f=Trueで反転。prodは(zeros,ones,inversions)、空(0,0,0)。 | 結合時に左ones×右zerosを加算。反転時はzeros×ones−inversions。 |
| 0/1反転・代入・最長連続長 | [range_binary_runs(V)](library/structures/lazy_segtree_actions.py) | f=(to0,to1)。prodは(n,p0,s0,b0,p1,s1,b1)、空は全て0。 | prefix/suffix/bestを0と1の両方で保持。flip/assign/longestを使うと簡潔。 |
| 括弧を区間で交換して正当性を判定 | [range_flip_brackets(V)](library/structures/lazy_segtree_actions.py) | f=Trueで'('と')'を交換。prodは(balance,min_prefix,max_prefix)。空(0,0,0)。 | balanceの符号反転、min_prefixとmax_prefixを符号付きで交換。balancedもある。 |
| 一次変換・和と二乗和 | [range_affine_sum_squares(V,mod=998244353)](library/structures/lazy_segtree_actions.py) | f=(a,b)。prodは(sum,sum_square)、空(0,0)。 | (S1,S2,長さ)。S2←a²S2+2abS1+b²n。mod=0なら分散の分子なども厳密計算可。 |
| 2列へ加算して積の総和 | [range_pair_add_product(V,mod=998244353)](library/structures/lazy_segtree_actions.py) | Vは(A[i],B[i])の列。f=(da,db)。prodは(sumA,sumB,sumAB)、空(0,0,0)。 | (sumA,sumB,sumAB,長さ)。sumABにda×sumB+db×sumA+da×db×nを足す。mod=0可。 |
| 添字に比例する加算・代入と区間和 | [range_index_affine_sum(V,mod=0)](library/structures/lazy_segtree_actions.py) | f=(a,b,c)でA[i]←a*A[i]+b*i+c。prodは和、空0。 | (和,添字和,長さ)。iは配列全体の添字。等差列はadd_progression/assign_progressionも可。 |
| 数字列を区間代入して数値化 | [range_digit_assign(V,mod=998244353,base=10)](library/structures/lazy_segtree_actions.py) | f=数字。prodはその区間を読んだ数値mod mod、空0。 | (値,base^長さ,長さ)。111...を事前計算。0も代入可、Noneが恒等更新。2<=base<=mod。 |
| 区間代入・最大部分配列和 | [range_assign_max_subarray(V,allow_empty=True)](library/structures/lazy_segtree_actions.py) | f=代入値。prodは(sum,prefix,suffix,best)。空の扱いは通常版と同じ。 | 4集約値と長さ。同じ値で埋めた区間のbestは値×長さまたは1要素から計算できる。 |
| 区間加算・GCD | [range_add_gcd(V)](library/structures/lazy_segtree_actions.py) | f=加算量。prodは非負GCD、空0。set/getは符号付き整数。 | (先頭,末尾,隣接差分GCD,長さ)。一様加算で差分GCDは変わらない。 |

## よく使う呼び出し例

2番目に大きい値の個数。値の順位は重複を除いて数える。

```python
seg = range_top2([5, 3, 5, 2, 3])
seg.set(3, 3)
seg.prod(0, 5)     # => (5, 2, 3, 3)
seg.prod(0, 5)[3]  # => 3
```

区間加算・乗算・代入を同じ木へ適用する。

```python
seg = range_affine_sum([1, 2, 3])
seg.apply(0, 2, (1, 5))     # 加算。[6,7,3]
seg.apply(1, 3, (2, 0))     # 乗算。[6,14,6]
seg.apply_point(0, (0, 4))  # 一点代入。[4,14,6]
seg.prod(0, 3)             # => 24
```

二列それぞれへの加算と、対応要素の積の総和。

```python
A, B = [1, 2], [3, 4]
seg = range_pair_add_product(list(zip(A, B)))
seg.apply(0, 2, (2, 0))  # Aだけに+2
seg.apply(0, 2, (0, 1))  # Bだけに+1
seg.prod(0, 2)[2]        # => 32
```

等差列の左端はクエリのlを基準に指定できる。

```python
seg = range_index_affine_sum([0] * 5)
seg.add_progression(1, 4, first=2, step=3)
seg.to_list()  # => [0, 2, 5, 8, 0]
seg.assign_progression(2, 4, first=10, step=-1)
seg.to_list()  # => [0, 2, 10, 9, 0]
```

## 設計を変更するときの確認点

1. **結合則を満たす要約を持つ。** 最大部分配列和なら全体和だけでは足りず、prefix・suffix・bestが必要。順序に依存する演算は左と右を交換しない。
2. **空区間を表す。** 和は0、最大値は-infなど。単位元を用意しづらい半群にはNoneを追加できる。空であることが必要な遅延更新では長さや個数も持たせる。
3. **更新を要約だけから計算できる形にする。** 区間和には長さ、二乗和には一次の和、積の和には両列の和、加算GCDには隣接差分を加える。
4. **更新の合成順を固定する。** `composition(f,g)`はgの後にf。一次変換なら`(a_f*a_g, a_f*b_g+b_f)`。加算だけでは順序を間違えても発見しにくいので、代入・倍率を混ぜて確認する。
5. **反転に必要な反対側の情報も持つ。** ビットの最長連続長は0/1両方、括弧反転はmin/maxのprefix両方を持つ。

この集約だけで扱えない操作もある。chmin/chmaxと**区間和**は[SegmentTreeBeats](snippets/structures/SegmentTreeBeats.py)、要素の挿入・削除・**並びの逆順化**は[DynamicSequence](library/structures/dynamic_sequence.py)を使う。最大部分配列和への任意の区間加算は、ここで使う4集約値では更新できない。等差列の加算・代入だけなら既存の[ArithmeticSegmentTree](library/structures/range_arithmetic.py)も選べる。

## verifyに使う問題

| 派生版 | 基本問題・検証先 | 確認範囲 |
|---|---|---|
| range_top2 | [ABC343 F Second Largest Query](https://atcoder.jp/contests/abc343/tasks/abc343_f) | 点更新、異なる第2位の個数。公式サンプル3件。 |
| range_binary_runs | [ABC322 F Vacation Query](https://atcoder.jp/contests/abc322/tasks/abc322_f) | ビット反転と連続1。公式サンプル1件。代入・連続0はローカル比較。 |
| range_pair_add_product | [ABC357 F Two Sequence Queries](https://atcoder.jp/contests/abc357/tasks/abc357_f) | 両列への加算と積の和。公式サンプル2件。 |
| range_brackets | [ABC223 F Parenthesis Checking](https://atcoder.jp/contests/abc223/tasks/abc223_f) | 2点交換と括弧列判定。公式サンプル3件。range_flip_bracketsの区間反転はローカル比較。 |
| range_digit_assign | [ABL E Replace Digits](https://atcoder.jp/contests/abl/tasks/abl_e) | 数字代入と全体値。公式サンプル2件。0代入・他の基数はローカル比較。 |
| range_flip_inversions | [practice2 L Lazy Segment Tree](https://atcoder.jp/contests/practice2/tasks/practice2_l) | ビット反転と転倒数。公式サンプル1件。 |
| range_affine_sum | [Range Affine Range Sum](https://judge.yosupo.jp/problem/range_affine_range_sum) / [Range Affine Point Get](https://judge.yosupo.jp/problem/range_affine_point_get) | 既存LCアダプターを派生版へ変更し、公式サンプルで確認。 |
| range_affine_composite | [Point Set Range Composite](https://judge.yosupo.jp/problem/point_set_range_composite) | 既存LCアダプターで非可換な合成順を確認。 |
| range_min | [Static RMQ](https://judge.yosupo.jp/problem/staticrmq) | 既存LCアダプターで区間取得を確認。点更新はローカル比較。 |
| 上記以外の派生版・追加操作 | [test_segtree_recipes.py](tests/test_segtree_recipes.py) | 配列との比較・空区間・境界探索・結合則・作用則・使用例。専用オンラインverifyは未実施。 |

AtCoderの6問も、入出力を付けた提出用1ファイルを生成できる。リポジトリ直下で実行する。

```powershell
.venv\Scripts\python.exe cp_snippet_palette\verify\build.py --atcoder abc343_f
.venv\Scripts\python.exe cp_snippet_palette\verify\build.py --atcoder abc322_f
.venv\Scripts\python.exe cp_snippet_palette\verify\build.py range_affine_range_sum
```

出力先は`cp_snippet_palette/verify/build/問題ID.py`。AtCoder用の一覧は`--atcoder --list`、LC用の一覧は`--list`で表示する。

今回の確認はPyPyによるローカル実行。新規テスト7件には33種類の設計、モノイド・作用則、使用例、AtCoder6問の公式サンプル12件を含む。変更したLC4問を含む第2弾の50問・91サンプルも通している。最大制約での時間・メモリ、オンラインAC、Codonコンパイルは未確認。
