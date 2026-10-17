# 旧統合版データ構造ライブラリ：点検結果と使い方

この文書は`_cp_structures.py`の旧APIと、最初の点検時の記録を説明する。2026-10-17時点の提出用ライブラリは[LIBRARY_GUIDE.md](cp_snippet_palette/LIBRARY_GUIDE.md)、ACL形式の呼び出しは[ACL_API.md](cp_snippet_palette/ACL_API.md)を参照する。

特に、この文書の`SegTree(V,segfunc,ide_ele)`とパレットの`segtree.py`にある`SegTree(op,e,v)`は引数順が異なる。旧APIが必要な場合は`_cp_structures.py`または`SegTree_compat.py`を使う。検索ツールの操作は[LOCAL_USAGE.md](cp_snippet_palette/LOCAL_USAGE.md)を参照。

対象：アップロードされた `貼り付けたMarkdown.md`（KindDeque / UnionFind / WeightedUnionFind / SegTree / BIT / LCATree / Deque / Heapq / SegmentTreeBeats / make_grid）と、この会話で修正した `segtree` / `lazy_segtree`。

この統合版はPython 3向け。頂点番号と区間の約束を統一し、旧呼び出しを極力保存した。配列は0-indexed、区間は原則`[l,r)`。例外は`LCATree`の1-indexed頂点と、旧`BIT.sum(i)`の`[0,i]`を含む前方和。

## ファイル構成

- `_cp_structures.py`：単一ファイルの統合版。クラス間に不要な相互依存なし。
- `cp_snippet_palette/snippets/structures/*.py`：独立した提出用スニペット。現在は一部をACL形式へ更新しており、旧統合版とAPIが同一とは限らない。`SegTree_compat.py`は旧APIと基底の`segtree`を含む。Windowsでは`SegTree.py`と`segtree.py`を区別できないため互換版に別名を付けている。
- `_cp_structures_tests.py`：固定シードの愚直実装比較・回帰テスト。
- 本ファイル：API一覧、修正理由、互換性の注意事項、使用例。

実行（同一フォルダーに置く）：

```bash
python _cp_structures_tests.py
```

検証結果：**11テスト群、1,637,651検査項目で全PASS**（検証時のPython 3環境で実行）。全入力・すべての単位元・任意の演算に対する正当性の数学的証明ではない。

## 重大な問題点と修正内容

| 元コード | 問題 | 修正・対応 |
|---|---|---|
| `SegmentTreeBeats._update_max` | `x < smax_v[k]` は誤り。chmax の停止条件は「2番目の最小値」`smin_v[k]`。`[1,2]` の範囲を 2 で chmax するだけでも不正な再帰が生じる | `x < smin_v[k]` に修正。ランダムな chmin/chmax/add/assign の組合せを愚直実装と検証 |
| `SegmentTreeBeats` | `10**18` を番兵にしており、入力値や更新値が大きいと実データと混同する | `math.inf` / `-math.inf` と代入保留の `None` を採用。配列長0、ダミー葉の実要素数も扱う |
| `Heapq.erase` | 要素の存在を確認せず削除予約する。存在しない値を消してから同値を `push` すると、その新規要素まで消える | `Counter` で論理的な出現数を保持。存在しない場合は `False`、存在すれば 1 個削除して `True`。削除済み要素が過多なら自動圧縮 |
| `KindDeque` | 両端の `pop` が値を返さない。個数0のキーが辞書に残る | 戻り値を追加。0個キーを削除し、種類数を追跡 |
| `WeightedUnionFind` | 未連結の `diff` が意味のない差を返す。同一集合に矛盾した差を追加しても黙って無視する | `diff` は未連結なら `ValueError`。矛盾する `unite` も `ValueError`。事前確認 `is_consistent` を追加 |
| `WeightedUnionFind.weights` | 元コードは各頂点の「親からの重み」をそのまま返すため、全頂点の「根からの重み」になっていない場合がある | 全頂点を圧縮してから根からの重みを返す。副作用のある内部リストそのものではなくコピーを返す |
| `UnionFind` | `all_group_members()` が代表元ごとに `members()` を呼び、概ね O(N²)。`group_count()` も毎回 O(N) | 1回の走査で全グループを構築。連結成分数を変数で保持して O(1) |
| `LCATree` | 高さの上限を `len(bin(n))` で過大評価し、親配列が余分。`distance` などが未実装。木ではない入力に対する訪問管理が弱い | `n.bit_length()` で高さ確保。非再帰で Euler 順序を記録し、祖先判定・距離・パス・ジャンプを実装。非木入力を拒否 |
| `Deque` | デフォルトで約30万個ぶんを初期確保。多数の小さなテストケースで非効率 | 小容量から必要時に2倍拡張。`max_size` で任意の事前予約も可能。負の添字・両端操作のランダムテストを実施 |
| `BIT` | 点取得・点代入・区間和・Fenwickの二分探索が不足 | `get` / `set` / `prod` / `lower_bound` / `all_sum` を追加。配列初期化は O(N) |
| `SegTree` と `segtree` | 同じ機能の2系統があり、更新メソッドの名前が異なる | `segtree` を基底として、従来の `SegTree.update(k,x)` と `SegTree.query(l,r)` を互換ラッパーにした |
| `lazy_segtree` | この会話で先行して見直したAPIを統合。境界探索で `OP` の重複計算あり | `max_right` / `min_left` の重複計算を解消。`to_list` を O(N) で実装 |

**訂正：旧 `SegTree.query` に `r -= 1` がないのはバグではない。** `r` が奇数なら `r-1` のノードを先に使用し、その直後に `r >>= 1` しているため、`r -= 1` の有無で次の `r` が変わらない。複数の長さ・全区間で旧実装の正当性を別途検証した。標準的な実装へ統一したのは可読性のため。

## API一覧

| クラス | 初期化 | よく使うメソッド |
|---|---|---|
| `KindDeque` | `KindDeque(iterable=())` | `append`, `appendleft`, `pop`, `popleft`, `count`, `kind`, `extend`, `rotate`, `clear`, `len` |
| `UnionFind` | `UnionFind(n)` | `find`, `leader`, `unite` (bool), `merge` (代表元), `same`, `size`, `groups`, `members`, `group_count` |
| `WeightedUnionFind` | `WeightedUnionFind(n)` | `unite(x,y,w)`, `diff(x,y)`, `get_weight`, `is_consistent`, `groups`, `size` |
| `segtree` | `segtree(V,OP,E)` | `set`, `get`, `prod`, `all_prod`, `max_right`, `min_left`, `to_list` |
| `SegTree` | `SegTree(V,segfunc,ide_ele)` | `update(k,x)`, `query(l,r)`, `add`, および `segtree` の全メソッド |
| `lazy_segtree` | `lazy_segtree(V,OP,E,MAPPING,COMPOSITION,ID)` | `set`, `get`, `prod`, `apply(l,r,f)`, `apply_point`, `all_prod`, `max_right`, `min_left`, `to_list` |
| `BIT` | `BIT(n)` または `BIT(arr)` | `add`, `set`, `get`, `sum(i)`（両端含む前方和）, `prefix_sum(r)`, `prod(l,r)`, `lower_bound(w)` |
| `LCATree` | `LCATree(n,edges,root=1)` | `lca`, `get_LCA`, `kth_ancestor`, `distance`, `jump`, `get_path`, `is_ancestor`, `subtree_size` |
| `Deque` | `Deque(src_arr=None,max_size=8)` | `append`, `appendleft`, `pop`, `popleft`, `d[i]`, `d[i]=x`, `rotate`, `extend`, `clear` |
| `Heapq` | `Heapq(iterable=())` | `build`, `push`, `top`, `peek`, `pop`, `erase`, `count`, `compact`, `len` |
| `SegmentTreeBeats` | `SegmentTreeBeats(n,a=None)` または `SegmentTreeBeats(arr)` | `update_min` (chmin), `update_max` (chmax), `add_val`, `update_val`, `query_min/max/sum`, `query`, `all_min/max/sum`, `get`, `set`, `to_list` |

## 注意するべき API 差分

1. **通常Segment Tree**：`segtree.set(i,x)` は値変更、`segtree.update(k)` は内部ノード再計算（旧仕様）。`SegTree.update(i,x)` は旧APIの点変更。同じ `update` でも意味が異なるので混同しない。
2. **WeightedUnionFind**：`unite` は新規統合時 `True`、既に統合されていて制約が整合する場合 `False`、矛盾なら `ValueError`。従来はどちらも暗黙の `None` だった。`merge` は `unite` の別名。
3. **BITの `sum(i)`**：元コードを維持し、**添字 `i` を含む** `[0,i]` の和。半開区間で考えたいときは `prefix_sum(r)` か `prod(l,r)` を使う。
4. **BITの `lower_bound(w)`**：各要素が非負である場合だけ使用する。`sum(i) >= w` となる最小0-index `i`。存在しなければ `n`、`w<=0` なら0。
5. **LCATree**：頂点が1始まりなのは元コードの互換性のため。木以外のグラフは `ValueError`。0始まりの問題では辺と root を +1 して使うか、実装を適宜変える。
6. **Heapq**：`erase` は「値による1個削除」であり、インデックス指定削除ではない。`build` は入力配列を破壊しない。`compact()` は内部ヒープを整理するが、普通は自動整理だけでよい。
7. **SegmentTreeBeats**：従来の `update_min / update_max` を引き続き使える。新しい `range_chmin / range_chmax / range_add / range_assign` は同義。数値のみ対象。
8. **Deque**：`max_size` は初期予約容量であり最大サイズの制限ではない。以前のデフォルト約30万件事前確保はしない。高速化したいことが明らかな大規模ケースは `Deque(max_size=N)` と指定可能。
9. **旧サンプルの `main()` / `segfunc` / `ide_ele` / `input` のグローバル置換**：ライブラリとは独立なので統合版には含めない。提出コードで自分の問題に応じて定義する。

## 使用例

### UnionFind / WeightedUnionFind

```python
uf = UnionFind(5)
assert uf.unite(0, 2)
assert not uf.unite(0, 2)
assert uf.same(0, 2)
assert uf.size(0) == 2
assert uf.group_count() == 4

wuf = WeightedUnionFind(3)
wuf.unite(0, 1, 3)   # potential[1]-potential[0]=3
wuf.unite(1, 2, -2)  # potential[2]-potential[1]=-2
assert wuf.diff(0, 2) == 1
assert not wuf.is_consistent(0, 2, 5)
```

### Segment Tree の両方のAPI

```python
seg = segtree([4, 1, 3], min, float('inf'))
assert seg.prod(0, 3) == 1
seg.set(1, 5)
assert seg.all_prod() == 3

old = SegTree([4, 1, 3], min, float('inf'))
old.update(1, 5)
assert old.query(0, 3) == 3
```

### Lazy Segment Tree：区間加算 / 区間和

```python
V = [1, 2, 3, 4]
seg = lazy_segtree(
    [(x, 1) for x in V],
    OP=lambda a, b: (a[0] + b[0], a[1] + b[1]),
    E=(0, 0),
    MAPPING=lambda f, x: (x[0] + f * x[1], x[1]),
    COMPOSITION=lambda f, g: f + g,
    ID=0,
)
seg.apply(1, 3, 10)
assert seg.prod(0, 4)[0] == 30
assert seg.max_right(0, lambda v: v[0] <= 13) == 2
assert seg.min_left(4, lambda v: v[0] <= 17) == 2
```

**重要：** `COMPOSITION(f,g)` は「先にg、次にf」。更新が上書きやアフィン変換なら順序が重要になる。また `OP` / `MAPPING` / `COMPOSITION` は必要な代数的条件（結合律・単位元・分配則・合成則）を満たす必要がある。`max_right` / `min_left` の条件関数は拡張時に True から False に単調に変化し、かつ初期集約 E で True でなければならない。

### BIT：prefix sum と lower_bound

```python
fw = BIT([2, 0, 3, 1])
assert fw.sum(2) == 5       # [0, 2] を含む
assert fw.prefix_sum(2) == 2  # [0, 2) を集約
assert fw.prod(1, 4) == 4
assert fw.lower_bound(3) == 2  # 最初に累積和が3以上となる添字
fw.add(1, 4)
assert fw.get(1) == 4
```

### LCATree：距離・パス・ジャンプ

```python
tree = LCATree(5, [(1, 2), (1, 3), (3, 4), (3, 5)], root=1)
assert tree.lca(4, 5) == 3
assert tree.distance(2, 4) == 3
assert tree.get_path(2, 4) == [2, 1, 3, 4]
assert tree.jump(2, 4, 2) == 3
assert tree.kth_ancestor(4, 2) == 1
assert tree.subtree_size(3) == 3
```

### Segment Tree Beats：混在する更新

```python
st = SegmentTreeBeats([1, 10, 5, 3])
st.update_min(0, 4, 6)   # [1, 6, 5, 3]
st.update_max(1, 3, 4)   # [1, 6, 5, 3]
st.add_val(0, 2, 2)      # [3, 8, 5, 3]
st.update_val(3, 4, 10)  # [3, 8, 5, 10]
assert st.query(0, 4) == (3, 10, 26)
assert st.query_sum(1, 3) == 13
assert st.all_max() == 10
```

## 検証方法と限界

- 愚直なリスト／`collections.deque`／辞書／`Counter`／単純な親配列と比較する固定シードのランダムテストを提供。
- Segment Treeは可換な区間和と非可換な連結、境界探索を検証。
- Lazy Segment Treeは区間加算と区間代入、空配列、二分探索を検証。
- Segment Tree Beatsは大量の chmin/chmax/add/assign と区間min/max/sumを混合し、非2冪長、0長、全域、大きい整数を検証。
- 木構造はランダムな木と愚直LCA、深さ、距離、祖先、パス比較で検証。
- 特定の競技・採点環境でのTLE/MLEを保証するものではない。特に Python の Segment Tree Beats は多数の配列と再帰呼び出しを伴うため、厳しい制約での採用は実測を推奨。
