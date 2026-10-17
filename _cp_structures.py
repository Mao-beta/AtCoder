"""競技プログラミング用データ構造ライブラリ（Python 3）。

すべて 0-indexed（LCATree の頂点番号のみ、元コードと互換の 1-indexed）。
区間は [l, r) の半開区間。クラス名・旧メソッド名は極力維持する。
必要なクラスだけ提出コードへ貼り付けても利用可能。
"""

from collections import Counter, deque
from heapq import heapify, heappop, heappush
from math import inf

MOD = 10**9 + 7
MOD99 = 998244353


def make_grid(h, w, num=0):
    """h×w の整数二次元配列を生成する。O(hw)。各行は独立。"""
    num = int(num)
    return [[num] * w for _ in range(h)]


class KindDeque:
    """要素の出現数と異なる値の種類数を O(1) で追跡する deque。

    D: 実体の collections.deque
    C[x]: 値 x の個数（存在しないキーでも 0、通常の Counter と同じ）
    kind: 現在の異なる値の種類数

    要素はハッシュ可能であること。両端操作・count・kind は償却 O(1)。
    """

    def __init__(self, iterable=()):
        self.D = deque(iterable)
        self.C = Counter(self.D)
        self._k = len(self.C)

    @property
    def kind(self):
        """現在存在する値の種類数。O(1)。"""
        return self._k

    def __len__(self):
        return len(self.D)

    def __iter__(self):
        return iter(self.D)

    def __getitem__(self, i):
        """deque 同様、中央の添字アクセスは O(N)。"""
        return self.D[i]

    def __contains__(self, x):
        return self.C.get(x, 0) > 0

    def count(self, x):
        """x の個数を返す。O(1)。"""
        return self.C.get(x, 0)

    def append(self, x):
        self.D.append(x)
        if self.C[x] == 0:
            self._k += 1
        self.C[x] += 1

    def appendleft(self, x):
        self.D.appendleft(x)
        if self.C[x] == 0:
            self._k += 1
        self.C[x] += 1

    def _remove_count(self, x):
        if self.C[x] == 1:
            del self.C[x]
            self._k -= 1
        else:
            self.C[x] -= 1

    def pop(self):
        """右端から取り出して返す。空なら IndexError。O(1)。"""
        x = self.D.pop()
        self._remove_count(x)
        return x

    def popleft(self):
        """左端から取り出して返す。空なら IndexError。O(1)。"""
        x = self.D.popleft()
        self._remove_count(x)
        return x

    def extend(self, iterable):
        for x in iterable:
            self.append(x)

    def extendleft(self, iterable):
        """deque と同じく、入力の順番を反転して左側へ追加する。"""
        for x in iterable:
            self.appendleft(x)

    def rotate(self, k=1):
        """右に k 個回転する。出現数は不変。"""
        self.D.rotate(k)

    def clear(self):
        self.D.clear()
        self.C.clear()
        self._k = 0

    def __repr__(self):
        return f"KindDeque({list(self.D)!r})"


class UnionFind:
    """素集合データ構造（Union by size + 経路圧縮）。頂点は 0..n-1。

    find / leader: 代表元、unite: 異なる集合を統合したら True。
    merge: 統合後の代表元（ACL 流）、is_same / same: 同じ集合か。
    find / unite / size: 償却 O(α(N))。
    groups / all_group_members: O(N α(N))、members(x): O(N α(N))。
    """

    def __init__(self, n):
        assert n >= 0
        self.n = n
        self.par = [-1] * n   # 根では -サイズ、他では親の番号
        self._group_count = n

    def find(self, x):
        """x の代表元を返す。非再帰。"""
        p = self.par
        root = x
        while p[root] >= 0:
            root = p[root]
        while x != root:
            nxt = p[x]
            p[x] = root
            x = nxt
        return root

    leader = find

    def is_same(self, x, y):
        return self.find(x) == self.find(y)

    same = is_same

    def merge(self, x, y):
        """集合を統合して代表元を返す。既に同じ集合なら変更しない。"""
        x, y = self.find(x), self.find(y)
        if x == y:
            return x
        p = self.par
        if p[x] > p[y]:
            x, y = y, x
        p[x] += p[y]
        p[y] = x
        self._group_count -= 1
        return x

    def unite(self, x, y):
        """異なる集合を統合したら True、既に同じなら False。"""
        x, y = self.find(x), self.find(y)
        if x == y:
            return False
        p = self.par
        if p[x] > p[y]:
            x, y = y, x
        p[x] += p[y]
        p[y] = x
        self._group_count -= 1
        return True

    def size(self, x):
        return -self.par[self.find(x)]

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, v in enumerate(self.par) if v < 0]

    def group_count(self):
        """連結成分数。O(1)。"""
        return self._group_count

    def all_group_members(self):
        """{代表元: 頂点リスト} を一度の走査で作る。O(N α(N))。"""
        res = {}
        for i in range(self.n):
            res.setdefault(self.find(i), []).append(i)
        return res

    def groups(self):
        """全連結成分の頂点リストを返す（ACL 形式）。"""
        return list(self.all_group_members().values())

    def __len__(self):
        return self.n

    def __repr__(self):
        return f"UnionFind({self.groups()!r})"


class WeightedUnionFind:
    """ポテンシャル差を管理する Union-Find（加法群、0-indexed）。

    unite(x, y, w): potential[y] - potential[x] = w を課す。
    diff(x, y): 同じ集合に属する場合の potential[y] - potential[x]。
    get_weight(x): 所属する根を 0 とした x のポテンシャル。

    unite は新しく統合したら True、既に同一で条件が一致すれば False、
    既存の条件と矛盾すれば ValueError。事前確認には is_consistent を使う。
    diff は未連結なら ValueError（無意味な差を返さない）。
    各種の木操作は償却 O(α(N))。
    """

    def __init__(self, n):
        assert n >= 0
        self.n = n
        self.par = [-1] * n
        self.weight = [0] * n  # 親→自分の差。find 後は根→自分の差
        self._group_count = n

    def find(self, x):
        """x の代表元を返す。経路圧縮時に重みも更新（非再帰）。"""
        p, w = self.par, self.weight
        path = []
        v = x
        while p[v] >= 0:
            path.append(v)
            v = p[v]
        root = v
        acc = 0
        for v in reversed(path):
            acc += w[v]
            w[v] = acc
            p[v] = root
        return root

    leader = find

    def is_same(self, x, y):
        return self.find(x) == self.find(y)

    same = is_same

    def get_weight(self, x):
        self.find(x)
        return self.weight[x]

    def diff(self, x, y):
        """potential[y]-potential[x]。未連結なら ValueError。"""
        rx = self.find(x)
        ry = self.find(y)
        if rx != ry:
            raise ValueError("x と y は未連結です")
        return self.weight[y] - self.weight[x]

    def is_consistent(self, x, y, w):
        """potential[y]-potential[x]=w が既存の条件と矛盾しないか。"""
        rx, ry = self.find(x), self.find(y)
        return rx != ry or self.weight[y] - self.weight[x] == w

    def unite(self, x, y, w=0):
        """potential[y]-potential[x]=w を設定。矛盾は ValueError。"""
        rx, ry = self.find(x), self.find(y)
        delta = w + self.weight[x] - self.weight[y]
        if rx == ry:
            if delta != 0:
                raise ValueError("既存の重み制約と矛盾します")
            return False
        p = self.par
        if p[rx] > p[ry]:
            rx, ry = ry, rx
            delta = -delta
        p[rx] += p[ry]
        p[ry] = rx
        self.weight[ry] = delta
        self._group_count -= 1
        return True

    merge = unite      # 重み付き版の merge は unite と同じ真偽値を返す
    potential = get_weight

    def size(self, x):
        return -self.par[self.find(x)]

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, v in enumerate(self.par) if v < 0]

    def group_count(self):
        return self._group_count

    def all_group_members(self):
        res = {}
        for i in range(self.n):
            res.setdefault(self.find(i), []).append(i)
        return res

    def groups(self):
        return list(self.all_group_members().values())

    def weights(self):
        """すべての頂点について、所属根からのポテンシャルを返す。O(Nα(N))。"""
        for i in range(self.n):
            self.find(i)
        return self.weight[:]

    def __len__(self):
        return self.n

    def __repr__(self):
        return f"WeightedUnionFind({self.groups()!r})"


class segtree:
    """一般のセグメント木。0-indexed / 半開区間 [l,r)。

    segtree(V, OP, E)。V は初期配列、または要素が E の長さ N（整数）。
    OP は結合的二項演算、E は左右の単位元。可換性は不要。
    set / prod / max_right / min_left: O(log N)、get / all_prod: O(1)。
    境界探索の判定関数 f は f(E)=True で、拡張に対して True→False に単調。
    """

    def __init__(self, V, OP, E):
        if isinstance(V, int):
            assert V >= 0
            n = V
            V = [E] * n
        else:
            n = len(V)
        self.n = n
        self.op = OP
        self.e = E
        self.log = (n - 1).bit_length() if n else 0
        self.size = 1 << self.log
        d = [E] * (2 * self.size)
        d[self.size:self.size + n] = V
        for k in range(self.size - 1, 0, -1):
            d[k] = OP(d[k << 1], d[k << 1 | 1])
        self.d = d

    def update(self, k):
        """内部ノード k を子から再計算する。O(1)。通常の要素変更は set。"""
        self.d[k] = self.op(self.d[k << 1], self.d[k << 1 | 1])

    def set(self, p, x):
        """V[p] = x。O(log N)。"""
        assert 0 <= p < self.n
        p += self.size
        d, op = self.d, self.op
        d[p] = x
        while p > 1:
            p >>= 1
            d[p] = op(d[p << 1], d[p << 1 | 1])

    def get(self, p):
        """V[p] を返す。O(1)。"""
        assert 0 <= p < self.n
        return self.d[p + self.size]

    def prod(self, l, r):
        """[l,r) の OP 集約値。空区間は E。O(log N)。"""
        assert 0 <= l <= r <= self.n
        l += self.size
        r += self.size
        sm_l = sm_r = self.e
        d, op = self.d, self.op
        while l < r:
            if l & 1:
                sm_l = op(sm_l, d[l])
                l += 1
            if r & 1:
                r -= 1
                sm_r = op(d[r], sm_r)
            l >>= 1
            r >>= 1
        return op(sm_l, sm_r)

    def all_prod(self):
        """配列全体の集約値。O(1)。"""
        return self.d[1]

    def max_right(self, l, f):
        """f(prod(l,r)) が True である最大 r（0<=l<=r<=N）。O(log N)。

        f(E)=True、r を右に伸ばすと True→False で戻らないこと。
        全域で True なら N を返す。
        """
        assert 0 <= l <= self.n
        assert f(self.e)
        if l == self.n:
            return self.n
        l += self.size
        sm, d, op = self.e, self.d, self.op
        while True:
            while (l & 1) == 0:
                l >>= 1
            nxt = op(sm, d[l])
            if not f(nxt):
                while l < self.size:
                    l <<= 1
                    nxt = op(sm, d[l])
                    if f(nxt):
                        sm = nxt
                        l += 1
                return l - self.size
            sm = nxt
            l += 1
            if (l & -l) == l:
                break
        return self.n

    def min_left(self, r, f):
        """f(prod(l,r)) が True である最小 l（0<=l<=r<=N）。O(log N)。

        f(E)=True、l を左に伸ばすと True→False で戻らないこと。
        全域で True なら 0 を返す。
        """
        assert 0 <= r <= self.n
        assert f(self.e)
        if r == 0:
            return 0
        r += self.size
        sm, d, op = self.e, self.d, self.op
        while True:
            r -= 1
            while r > 1 and (r & 1):
                r >>= 1
            nxt = op(d[r], sm)
            if not f(nxt):
                while r < self.size:
                    r = r << 1 | 1
                    nxt = op(d[r], sm)
                    if f(nxt):
                        sm = nxt
                        r -= 1
                return r + 1 - self.size
            sm = nxt
            if (r & -r) == r:
                break
        return 0

    def to_list(self):
        """全要素をリストで取得する。O(N)。"""
        return self.d[self.size:self.size + self.n]

    def __len__(self):
        return self.n

    def __getitem__(self, p):
        return self.get(p)

    def __str__(self):
        return str(self.to_list())


class SegTree(segtree):
    """旧 SegTree API の互換クラス。上位の segtree の探索機能も利用可能。

    SegTree(V, segfunc, ide_ele)。update(k,x) / query(l,r) / add(k,x)
    は旧名を維持。新しい操作には set / prod / max_right / min_left も使える。
    """

    def __init__(self, init_val, segfunc, ide_ele):
        super().__init__(init_val, segfunc, ide_ele)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = self.size
        self.tree = self.d

    def update(self, k, x):
        """旧API: k 番目の値を x に置き換える。O(log N)。"""
        self.set(k, x)

    def query(self, l, r):
        """旧API: [l,r) の集約値を返す。O(log N)。"""
        return self.prod(l, r)

    def add(self, k, x):
        """旧API: 数値要素 V[k] += x。O(log N)。"""
        self.set(k, self.get(k) + x)


class lazy_segtree:
    """遅延評価セグメント木。0-indexed / 半開区間 [l,r)。

    lazy_segtree(V, OP, E, MAPPING, COMPOSITION, ID)
    - OP(x,y): 結合的集約。E は左右の単位元。
    - MAPPING(f,x): 更新操作 f を集約値 x に適用。
    - COMPOSITION(f,g): 「先に g、その後 f」の合成操作。
      MAPPING(COMPOSITION(f,g),x) == MAPPING(f,MAPPING(g,x))。
    - ID: 恒等更新。MAPPING(ID,x)==x。
    - MAPPING(f,OP(x,y))==OP(MAPPING(f,x),MAPPING(f,y)) が必要。

    集約値に適用する操作の定義に注意（区間加算・区間和なら要素数が必要）。
    MAPPING(f,E)==E も満たすこと（空区間は更新後も空区間）。
    更新操作は値の共有によって破壊されないよう、関数は非破壊的に実装する。
    更新・区間取得・境界探索は O(log N)、all_prod は O(1)。
    """

    def __init__(self, V, OP, E, MAPPING, COMPOSITION, ID):
        if isinstance(V, int):
            assert V >= 0
            n = V
            V = [E] * n
        else:
            n = len(V)
        self.n = n
        self.log = (n - 1).bit_length() if n else 0
        self.size = 1 << self.log
        self.op = OP
        self.e = E
        self.mapping = MAPPING
        self.composition = COMPOSITION
        self.identity = ID
        size = self.size
        d = [E] * (2 * size)
        d[size:size + n] = V
        for k in range(size - 1, 0, -1):
            d[k] = OP(d[k << 1], d[k << 1 | 1])
        self.d = d
        self.lz = [ID] * size

    def update(self, k):
        """内部ノード k を両子から再計算する。O(1)。"""
        d = self.d
        d[k] = self.op(d[k << 1], d[k << 1 | 1])

    def all_apply(self, k, f):
        """ノード k 全域に f を適用し、子への未伝播操作を合成する。O(1)。"""
        self.d[k] = self.mapping(f, self.d[k])
        if k < self.size:
            self.lz[k] = self.composition(f, self.lz[k])

    def push(self, k):
        """k に保留した操作を両子へ伝播する。O(1)。"""
        f = self.lz[k]
        self.all_apply(k << 1, f)
        self.all_apply(k << 1 | 1, f)
        self.lz[k] = self.identity

    def set(self, p, x):
        """V[p]=x に置換する。O(log N)。"""
        assert 0 <= p < self.n
        p += self.size
        push = self.push
        for i in range(self.log, 0, -1):
            push(p >> i)
        self.d[p] = x
        update = self.update
        for i in range(1, self.log + 1):
            update(p >> i)

    def get(self, p):
        """V[p] を返す。O(log N)。"""
        assert 0 <= p < self.n
        p += self.size
        push = self.push
        for i in range(self.log, 0, -1):
            push(p >> i)
        return self.d[p]

    def prod(self, l, r):
        """[l,r) の区間集約。空区間は E。O(log N)。"""
        assert 0 <= l <= r <= self.n
        if l == r:
            return self.e
        l += self.size
        r += self.size
        push = self.push
        for i in range(self.log, 0, -1):
            if ((l >> i) << i) != l:
                push(l >> i)
            if ((r >> i) << i) != r:
                push((r - 1) >> i)
        d, op = self.d, self.op
        sm_l = sm_r = self.e
        while l < r:
            if l & 1:
                sm_l = op(sm_l, d[l])
                l += 1
            if r & 1:
                r -= 1
                sm_r = op(d[r], sm_r)
            l >>= 1
            r >>= 1
        return op(sm_l, sm_r)

    def all_prod(self):
        """配列全体の集約値。O(1)。"""
        return self.d[1]

    def apply_point(self, p, f):
        """位置 p に更新 f を適用する。O(log N)。"""
        assert 0 <= p < self.n
        p += self.size
        push = self.push
        for i in range(self.log, 0, -1):
            push(p >> i)
        self.d[p] = self.mapping(f, self.d[p])
        update = self.update
        for i in range(1, self.log + 1):
            update(p >> i)

    def apply(self, l, r, f):
        """[l,r) の各要素へ更新 f を適用。空区間なら何もしない。O(log N)。"""
        assert 0 <= l <= r <= self.n
        if l == r:
            return
        l += self.size
        r += self.size
        push = self.push
        for i in range(self.log, 0, -1):
            if ((l >> i) << i) != l:
                push(l >> i)
            if ((r >> i) << i) != r:
                push((r - 1) >> i)
        l0, r0 = l, r
        all_apply = self.all_apply
        while l < r:
            if l & 1:
                all_apply(l, f)
                l += 1
            if r & 1:
                r -= 1
                all_apply(r, f)
            l >>= 1
            r >>= 1
        update = self.update
        for i in range(1, self.log + 1):
            if ((l0 >> i) << i) != l0:
                update(l0 >> i)
            if ((r0 >> i) << i) != r0:
                update((r0 - 1) >> i)

    def max_right(self, l, g):
        """g(prod(l,r)) が True である最大 r。g(E)=True、単調性が必要。O(log N)。"""
        assert 0 <= l <= self.n
        assert g(self.e)
        if l == self.n:
            return self.n
        l += self.size
        push = self.push
        for i in range(self.log, 0, -1):
            push(l >> i)
        sm, d, op = self.e, self.d, self.op
        while True:
            while (l & 1) == 0:
                l >>= 1
            nxt = op(sm, d[l])
            if not g(nxt):
                while l < self.size:
                    push(l)
                    l <<= 1
                    nxt = op(sm, d[l])
                    if g(nxt):
                        sm = nxt
                        l += 1
                return l - self.size
            sm = nxt
            l += 1
            if (l & -l) == l:
                break
        return self.n

    def min_left(self, r, g):
        """g(prod(l,r)) が True である最小 l。g(E)=True、単調性が必要。O(log N)。"""
        assert 0 <= r <= self.n
        assert g(self.e)
        if r == 0:
            return 0
        r += self.size
        push = self.push
        for i in range(self.log, 0, -1):
            push((r - 1) >> i)
        sm, d, op = self.e, self.d, self.op
        while True:
            r -= 1
            while r > 1 and (r & 1):
                r >>= 1
            nxt = op(d[r], sm)
            if not g(nxt):
                while r < self.size:
                    push(r)
                    r = r << 1 | 1
                    nxt = op(d[r], sm)
                    if g(nxt):
                        sm = nxt
                        r -= 1
                return r + 1 - self.size
            sm = nxt
            if (r & -r) == r:
                break
        return 0

    def to_list(self):
        """全要素を取り出す。保留操作の伝播を含むため O(N)。"""
        push = self.push
        for k in range(1, self.size):
            push(k)
        return self.d[self.size:self.size + self.n]

    def __len__(self):
        return self.n

    def __getitem__(self, p):
        return self.get(p)

    def __str__(self):
        return str(self.to_list())


class BIT:
    """Fenwick Tree（区間和）。0-indexed。

    BIT(n) または BIT(初期配列) を O(N) で構築。
    add(i,x): A[i]+=x、set(i,x): A[i]=x、get(i): A[i]。
    sum(i): A[0]+...+A[i]（元コードと同じ「右端を含む」仕様）。
    prefix_sum(r): [0,r)、prod(l,r): [l,r)、all_sum(): 全体。
    lower_bound(w): prefix_sum(i+1)>=w を満たす最小の i。なければ n。
    lower_bound は全要素非負（累積和が単調）である場合だけ有効。
    構築 O(N)、get O(1)、add/set/sum/prod/lower_bound O(log N)。
    """

    def __init__(self, n):
        if isinstance(n, int):
            assert n >= 0
            arr = [0] * n
        else:
            arr = list(n)
        self.n = len(arr)
        self.each = [0] + arr[:]  # 元コードの 1-indexed 内部配列を維持
        self.data = self.each[:]
        for i in range(1, self.n + 1):
            j = i + (i & -i)
            if j <= self.n:
                self.data[j] += self.data[i]

    def prefix_sum(self, r):
        """[0,r) の和。0<=r<=N。O(log N)。"""
        assert 0 <= r <= self.n
        s, data = 0, self.data
        while r:
            s += data[r]
            r -= r & -r
        return s

    def sum(self, i):
        """[0,i] の和。i=-1 の場合は 0（元コード互換）。"""
        assert -1 <= i < self.n
        return self.prefix_sum(i + 1)

    def prod(self, l, r):
        """[l,r) の和。O(log N)。"""
        assert 0 <= l <= r <= self.n
        return self.prefix_sum(r) - self.prefix_sum(l)

    range_sum = prod

    def all_sum(self):
        return self.prefix_sum(self.n)

    def add(self, i, x):
        """A[i]+=x。O(log N)。"""
        assert 0 <= i < self.n
        i += 1
        self.each[i] += x
        data, n = self.data, self.n
        while i <= n:
            data[i] += x
            i += i & -i

    def get(self, i):
        """A[i]。O(1)。"""
        assert 0 <= i < self.n
        return self.each[i + 1]

    def set(self, i, x):
        """A[i]=x。O(log N)。"""
        self.add(i, x - self.get(i))

    def lower_bound(self, w):
        """sum(i)>=w となる最小 i（0-indexed）。存在しなければ N。

        w<=0 なら 0 を返す。要素が非負であることが前提。O(log N)。
        """
        if w <= 0:
            return 0
        idx = 0
        bit = 1 << (self.n.bit_length() - 1) if self.n else 0
        data, n = self.data, self.n
        while bit:
            nxt = idx + bit
            if nxt <= n and data[nxt] < w:
                w -= data[nxt]
                idx = nxt
            bit >>= 1
        return idx if idx < n else n

    def to_list(self):
        return self.each[1:]

    def __getitem__(self, i):
        return self.get(i)

    def __len__(self):
        return self.n

    def __repr__(self):
        return f"BIT({self.to_list()!r})"


class LCATree:
    """二分累乗法で LCA を求める木（元コード互換の 1-indexed）。

    LCATree(n, edges, root=1)。edges は (u,v) の非向辺、頂点 1..n。
    入力は連結な木であること。閉路・未連結は ValueError。
    get_LCA / lca(u,v): 最小共通祖先 O(log N)。
    kth_ancestor(v,k): k 個上の祖先（なければ -1） O(log N)。
    distance(u,v): 辺の本数 O(log N)。
    jump(u,v,k): u→v のパスの k 番目の頂点（0-indexed、範囲外 -1）。
    is_ancestor(u,v): u が v の祖先（自身を含む）か。O(1)。
    subtree_size(v): v を根とする部分木の頂点数。O(1)。
    get_path(u,v): パス上の頂点のリスト。O(パス長 + log N)。
    構築 O(N log N)、メモリ O(N log N)。再帰なし。
    """

    @staticmethod
    def make_adjlist_nond(n, edges):
        """1-indexed の無向隣接リストを構築する。"""
        g = [[] for _ in range(n + 1)]
        for edge in edges:
            u, v = edge[0], edge[1]
            if not (1 <= u <= n and 1 <= v <= n) or u == v:
                raise ValueError("辺の頂点番号が不正です")
            g[u].append(v)
            g[v].append(u)
        return g

    def __init__(self, n, edges, root=1):
        if n < 1 or not 1 <= root <= n:
            raise ValueError("n>=1、1<=root<=n が必要です")
        self.n = n
        self.root = root
        self.max_double = max(1, n.bit_length())
        self.adj = self.make_adjlist_nond(n, edges)
        self.parent = [[-1] * (n + 1) for _ in range(self.max_double)]
        self.depth = [-1] * (n + 1)
        self.tin = [-1] * (n + 1)
        self.tout = [-1] * (n + 1)

        self.depth[root] = 0
        timer = 0
        stack = [(root, False)]
        par = self.parent[0]
        while stack:
            v, exiting = stack.pop()
            if exiting:
                self.tout[v] = timer
                continue
            self.tin[v] = timer
            timer += 1
            stack.append((v, True))
            for u in reversed(self.adj[v]):
                if u == par[v]:
                    continue
                if self.depth[u] != -1:
                    raise ValueError("入力グラフに閉路があります")
                par[u] = v
                self.depth[u] = self.depth[v] + 1
                stack.append((u, False))

        if timer != n:
            raise ValueError("入力グラフは連結ではありません")

        for j in range(1, self.max_double):
            prev, curr = self.parent[j - 1], self.parent[j]
            for v in range(1, n + 1):
                p = prev[v]
                curr[v] = prev[p] if p != -1 else -1

    def kth_ancestor(self, v, k):
        """v の k 世代上の祖先。存在しなければ -1。O(log N)。"""
        assert 1 <= v <= self.n and k >= 0
        if k > self.depth[v]:
            return -1
        bit = 0
        while k:
            if k & 1:
                v = self.parent[bit][v]
            k >>= 1
            bit += 1
        return v

    def get_LCA(self, x, y):
        """x, y の LCA。O(log N)。"""
        assert 1 <= x <= self.n and 1 <= y <= self.n
        if self.depth[x] < self.depth[y]:
            x, y = y, x
        x = self.kth_ancestor(x, self.depth[x] - self.depth[y])
        if x == y:
            return x
        for i in range(self.max_double - 1, -1, -1):
            if self.parent[i][x] != self.parent[i][y]:
                x = self.parent[i][x]
                y = self.parent[i][y]
        return self.parent[0][x]

    lca = get_LCA

    def distance(self, x, y):
        """x と y の間の辺数。O(log N)。"""
        p = self.get_LCA(x, y)
        return self.depth[x] + self.depth[y] - 2 * self.depth[p]

    def is_ancestor(self, u, v):
        """u が v の祖先か（自身も含む）。O(1)。"""
        assert 1 <= u <= self.n and 1 <= v <= self.n
        return self.tin[u] <= self.tin[v] < self.tout[u]

    def subtree_size(self, v):
        """v を根とした部分木のサイズ。O(1)。"""
        assert 1 <= v <= self.n
        return self.tout[v] - self.tin[v]

    def jump(self, u, v, k):
        """u から v に向かうパスで k 辺進んだ位置。範囲外なら -1。"""
        assert 1 <= u <= self.n and 1 <= v <= self.n and k >= 0
        p = self.get_LCA(u, v)
        a = self.depth[u] - self.depth[p]
        b = self.depth[v] - self.depth[p]
        if k > a + b:
            return -1
        return self.kth_ancestor(u, k) if k <= a else self.kth_ancestor(v, a + b - k)

    def get_path(self, u, v):
        """u→v のパス上の頂点を順に返す。"""
        p = self.get_LCA(u, v)
        left, right = [], []
        par = self.parent[0]
        while u != p:
            left.append(u)
            u = par[u]
        left.append(p)
        while v != p:
            right.append(v)
            v = par[v]
        return left + right[::-1]

    def __len__(self):
        return self.n


class Deque:
    """リングバッファによる両端キュー。整数添字でのランダムアクセス O(1)。

    Deque(src_arr=None, max_size=8)。max_size は初期予約容量（上限ではない）。
    append/appendleft/pop/popleft は償却 O(1)、添字取得・代入 O(1)。
    extend と走査は O(k)、rotate は O(min(k mod N, N-k mod N))。
    必要時に容量を倍増させる。大容量の事前確保が必要なら max_size を指定。
    """

    def __init__(self, src_arr=None, max_size=8):
        arr = [] if src_arr is None else list(src_arr)
        self.N = max(1, max_size, len(arr))
        self.buf = arr + [None] * (self.N - len(arr))
        self.head = 0
        self._size = len(arr)
        self.tail = self._size % self.N

    def __len__(self):
        return self._size

    def is_full(self):
        return self._size == self.N

    def is_empty(self):
        return self._size == 0

    def __index(self, i):
        n = self._size
        if not -n <= i < n:
            raise IndexError("deque index out of range")
        if i < 0:
            i += n
        return (self.head + i) % self.N

    def __grow(self):
        old, capacity = self.buf, self.N
        self.N *= 2
        self.buf = [old[(self.head + i) % capacity] for i in range(self._size)]
        self.buf.extend([None] * (self.N - self._size))
        self.head = 0
        self.tail = self._size

    def append(self, x):
        if self.is_full():
            self.__grow()
        self.buf[self.tail] = x
        self.tail = (self.tail + 1) % self.N
        self._size += 1

    def appendleft(self, x):
        if self.is_full():
            self.__grow()
        self.head = (self.head - 1) % self.N
        self.buf[self.head] = x
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from an empty deque")
        self.tail = (self.tail - 1) % self.N
        x = self.buf[self.tail]
        self.buf[self.tail] = None
        self._size -= 1
        return x

    def popleft(self):
        if self.is_empty():
            raise IndexError("pop from an empty deque")
        x = self.buf[self.head]
        self.buf[self.head] = None
        self.head = (self.head + 1) % self.N
        self._size -= 1
        return x

    def extend(self, iterable):
        for x in iterable:
            self.append(x)

    def extendleft(self, iterable):
        for x in iterable:
            self.appendleft(x)

    def rotate(self, k=1):
        """右に k 個回転。負数は左回転。"""
        if not self._size:
            return
        k %= self._size
        if k <= self._size - k:
            for _ in range(k):
                self.appendleft(self.pop())
        else:
            for _ in range(self._size - k):
                self.append(self.popleft())

    def clear(self):
        self.buf = [None] * self.N
        self.head = self.tail = self._size = 0

    def __getitem__(self, i):
        return self.buf[self.__index(i)]

    def __setitem__(self, i, x):
        self.buf[self.__index(i)] = x

    def __iter__(self):
        for i in range(self._size):
            yield self.buf[(self.head + i) % self.N]

    def __reversed__(self):
        for i in range(self._size - 1, -1, -1):
            yield self.buf[(self.head + i) % self.N]

    def __repr__(self):
        return f"Deque({list(self)!r})"

    __str__ = __repr__


class Heapq:
    """heapq を使う削除可能な最小ヒープ（遅延削除方式）。

    push / pop / top / erase / clean / build を提供。
    erase(x): 存在する x のうち1個を削除し True、なければ False。
    top / pop: 空なら exc（デフォルト None）。
    len(H): 論理上存在する要素数。count(x): x の個数。
    push / pop / erase は償却 O(log N)、top も clean が必要なときは
    償却 O(log N)（clean 不要なら O(1)）。compact() は O(N)。
    削除済み要素が多い場合は自動的に再構築してメモリを抑える。
    """

    def __init__(self, iterable=()):
        self.q = []
        self.p = []
        self.C = Counter()
        self._size = 0
        self.build(iterable)

    def build(self, a):
        """入力をコピーして再構築。既存の保留削除も消す。O(N)。"""
        self.q = list(a)
        heapify(self.q)
        self.p = []
        self.C = Counter(self.q)
        self._size = len(self.q)

    def push(self, x):
        heappush(self.q, x)
        self.C[x] += 1
        self._size += 1

    def erase(self, x):
        """現在存在する x を1個削除する。なければ False。"""
        if self.C.get(x, 0) == 0:
            return False
        self.C[x] -= 1
        if self.C[x] == 0:
            del self.C[x]
        self._size -= 1
        heappush(self.p, x)
        self.clean()
        if len(self.q) > max(64, 2 * self._size):
            self.compact()
        return True

    def compact(self):
        """論理上存在する要素だけでヒープを作り直す。O(N)。"""
        self.q = list(self.C.elements())
        heapify(self.q)
        self.p = []

    def clean(self):
        """削除予約と物理ヒープの最小値が一致する限り掃除する。"""
        q, p = self.q, self.p
        while q and p and q[0] == p[0]:
            heappop(q)
            heappop(p)

    def pop(self, exc=None):
        """最小値を取り出す。空なら exc。"""
        self.clean()
        if not self.q:
            return exc
        x = heappop(self.q)
        self.C[x] -= 1
        if self.C[x] == 0:
            del self.C[x]
        self._size -= 1
        return x

    def top(self, exc=None):
        """最小値を返す（削除しない）。空なら exc。"""
        self.clean()
        return self.q[0] if self.q else exc

    peek = top

    def count(self, x):
        return self.C.get(x, 0)

    def __contains__(self, x):
        return self.C.get(x, 0) > 0

    def __len__(self):
        return self._size

    def __bool__(self):
        return self._size > 0


class SegmentTreeBeats:
    """Segment Tree Beats。0-indexed / 半開区間 [l,r)。

    SegmentTreeBeats(n, a=None) または SegmentTreeBeats(初期配列)。
    update_min(l,r,x): A[i] = min(A[i], x)（range chmin）。
    update_max(l,r,x): A[i] = max(A[i], x)（range chmax）。
    add_val(l,r,x): A[i] += x。
    update_val(l,r,x): A[i] = x（range assign）。
    query_min/max/sum(l,r): 区間最小値/最大値/和。
    query(l,r): (min, max, sum) のタプル。
    get(i) / set(i,x) / all_min/max/sum / to_list を追加。

    空区間の min/max/sum はそれぞれ inf/-inf/0。
    典型的な chmin/chmax 更新は償却計算量で評価する（毎回の最悪 O(log N)
    ではない）。区間加算・代入・クエリは O(log N)。構築 O(N)。
    """

    def __init__(self, n, a=None):
        if not isinstance(n, int):
            if a is not None:
                raise ValueError("配列を第一引数にする場合、第二引数は省略してください")
            a = list(n)
            n = len(a)
        if n < 0:
            raise ValueError("n は非負の整数としてください")
        if a is None:
            a = [0] * n
        elif len(a) != n:
            raise ValueError("a の長さは n と一致させてください")
        self.n = n
        self.n0 = 1 << ((n - 1).bit_length() if n else 0)
        m = 2 * self.n0 - 1  # 0-indexed 完全二分木
        self.inf = inf
        self.max_v = [-inf] * m
        self.smax_v = [-inf] * m
        self.max_c = [0] * m
        self.min_v = [inf] * m
        self.smin_v = [inf] * m
        self.min_c = [0] * m
        self.len = [0] * m  # 実在要素数（ダミー葉を数えない）
        self.sum = [0] * m
        self.ladd = [0] * m
        self.lval = [None] * m  # None は代入なし（実値の ±inf と区別する）
        base = self.n0 - 1
        for i in range(n):
            k = base + i
            v = a[i]
            self.max_v[k] = self.min_v[k] = self.sum[k] = v
            self.max_c[k] = self.min_c[k] = self.len[k] = 1
        for k in range(base - 1, -1, -1):
            self.len[k] = self.len[2 * k + 1] + self.len[2 * k + 2]
            self.update(k)

    def update(self, k):
        """内部ノード k を両子から集約。O(1)。"""
        lc, rc = 2 * k + 1, 2 * k + 2
        self.sum[k] = self.sum[lc] + self.sum[rc]
        max_v, smax_v, max_c = self.max_v, self.smax_v, self.max_c
        if max_v[lc] < max_v[rc]:
            max_v[k] = max_v[rc]
            max_c[k] = max_c[rc]
            smax_v[k] = max(max_v[lc], smax_v[rc])
        elif max_v[lc] > max_v[rc]:
            max_v[k] = max_v[lc]
            max_c[k] = max_c[lc]
            smax_v[k] = max(smax_v[lc], max_v[rc])
        else:
            max_v[k] = max_v[lc]
            max_c[k] = max_c[lc] + max_c[rc]
            smax_v[k] = max(smax_v[lc], smax_v[rc])
        min_v, smin_v, min_c = self.min_v, self.smin_v, self.min_c
        if min_v[lc] < min_v[rc]:
            min_v[k] = min_v[lc]
            min_c[k] = min_c[lc]
            smin_v[k] = min(smin_v[lc], min_v[rc])
        elif min_v[lc] > min_v[rc]:
            min_v[k] = min_v[rc]
            min_c[k] = min_c[rc]
            smin_v[k] = min(min_v[lc], smin_v[rc])
        else:
            min_v[k] = min_v[lc]
            min_c[k] = min_c[lc] + min_c[rc]
            smin_v[k] = min(smin_v[lc], smin_v[rc])

    def update_node_max(self, k, x):
        """ノード全体の最大値のみを x に下げる（必要条件確認済み）。"""
        if self.max_c[k] == 0 or self.max_v[k] <= x:
            return
        old = self.max_v[k]
        self.sum[k] += (x - old) * self.max_c[k]
        if old == self.min_v[k]:
            self.min_v[k] = x
        elif old == self.smin_v[k]:
            self.smin_v[k] = x
        self.max_v[k] = x
        if self.lval[k] is not None:
            self.lval[k] = min(self.lval[k], x)

    def update_node_min(self, k, x):
        """ノード全体の最小値のみを x に上げる（必要条件確認済み）。"""
        if self.min_c[k] == 0 or x <= self.min_v[k]:
            return
        old = self.min_v[k]
        self.sum[k] += (x - old) * self.min_c[k]
        if old == self.max_v[k]:
            self.max_v[k] = x
        elif old == self.smax_v[k]:
            self.smax_v[k] = x
        self.min_v[k] = x
        if self.lval[k] is not None:
            self.lval[k] = max(self.lval[k], x)

    def addall(self, k, x):
        """ノード全体へ加算（内部用）。O(1)。"""
        if self.len[k] == 0:
            return
        self.max_v[k] += x
        self.min_v[k] += x
        if self.smax_v[k] != -inf:
            self.smax_v[k] += x
        if self.smin_v[k] != inf:
            self.smin_v[k] += x
        self.sum[k] += self.len[k] * x
        if self.lval[k] is not None:
            self.lval[k] += x
        else:
            self.ladd[k] += x

    def updateall(self, k, x):
        """ノード全体を x に代入（内部用）。O(1)。"""
        if self.len[k] == 0:
            return
        self.max_v[k] = self.min_v[k] = x
        self.smax_v[k] = -inf
        self.smin_v[k] = inf
        self.max_c[k] = self.min_c[k] = self.len[k]
        self.sum[k] = x * self.len[k]
        self.lval[k] = x
        self.ladd[k] = 0

    def push(self, k):
        """未伝播の代入・加算・chmin/chmax 制約を子へ渡す。O(1)。"""
        if k >= self.n0 - 1:
            return
        lc, rc = 2 * k + 1, 2 * k + 2
        if self.lval[k] is not None:
            self.updateall(lc, self.lval[k])
            self.updateall(rc, self.lval[k])
            self.lval[k] = None
            return
        if self.ladd[k]:
            self.addall(lc, self.ladd[k])
            self.addall(rc, self.ladd[k])
            self.ladd[k] = 0
        for c in (lc, rc):
            if self.max_v[c] > self.max_v[k]:
                self.update_node_max(c, self.max_v[k])
            if self.min_v[c] < self.min_v[k]:
                self.update_node_min(c, self.min_v[k])

    def _update_min(self, x, a, b, k, l, r):
        if b <= l or r <= a or self.max_v[k] <= x:
            return
        if a <= l and r <= b and self.smax_v[k] < x:
            self.update_node_max(k, x)
            return
        self.push(k)
        mid = (l + r) >> 1
        self._update_min(x, a, b, 2 * k + 1, l, mid)
        self._update_min(x, a, b, 2 * k + 2, mid, r)
        self.update(k)

    def _update_max(self, x, a, b, k, l, r):
        if b <= l or r <= a or x <= self.min_v[k]:
            return
        # chmax では「2番目に小さい値」を比較する（元コードの smax_v は誤り）。
        if a <= l and r <= b and x < self.smin_v[k]:
            self.update_node_min(k, x)
            return
        self.push(k)
        mid = (l + r) >> 1
        self._update_max(x, a, b, 2 * k + 1, l, mid)
        self._update_max(x, a, b, 2 * k + 2, mid, r)
        self.update(k)

    def _add_val(self, x, a, b, k, l, r):
        if b <= l or r <= a:
            return
        if a <= l and r <= b:
            self.addall(k, x)
            return
        self.push(k)
        mid = (l + r) >> 1
        self._add_val(x, a, b, 2 * k + 1, l, mid)
        self._add_val(x, a, b, 2 * k + 2, mid, r)
        self.update(k)

    def _update_val(self, x, a, b, k, l, r):
        if b <= l or r <= a:
            return
        if a <= l and r <= b:
            self.updateall(k, x)
            return
        self.push(k)
        mid = (l + r) >> 1
        self._update_val(x, a, b, 2 * k + 1, l, mid)
        self._update_val(x, a, b, 2 * k + 2, mid, r)
        self.update(k)

    def update_min(self, a, b, x):
        """[a,b) の各要素を min(A[i],x) に更新（chmin）。償却計算量。"""
        assert 0 <= a <= b <= self.n
        if a != b:
            self._update_min(x, a, b, 0, 0, self.n0)

    range_chmin = update_min

    def update_max(self, a, b, x):
        """[a,b) の各要素を max(A[i],x) に更新（chmax）。償却計算量。"""
        assert 0 <= a <= b <= self.n
        if a != b:
            self._update_max(x, a, b, 0, 0, self.n0)

    range_chmax = update_max

    def add_val(self, a, b, x):
        """[a,b) の各要素に x を足す。O(log N)。"""
        assert 0 <= a <= b <= self.n
        if a != b:
            self._add_val(x, a, b, 0, 0, self.n0)

    range_add = add_val

    def update_val(self, a, b, x):
        """[a,b) の各要素を x にする。O(log N)。"""
        assert 0 <= a <= b <= self.n
        if a != b:
            self._update_val(x, a, b, 0, 0, self.n0)

    range_assign = update_val

    def _query_max(self, a, b, k, l, r):
        if b <= l or r <= a:
            return -inf
        if a <= l and r <= b:
            return self.max_v[k]
        self.push(k)
        mid = (l + r) >> 1
        return max(self._query_max(a, b, 2 * k + 1, l, mid),
                   self._query_max(a, b, 2 * k + 2, mid, r))

    def _query_min(self, a, b, k, l, r):
        if b <= l or r <= a:
            return inf
        if a <= l and r <= b:
            return self.min_v[k]
        self.push(k)
        mid = (l + r) >> 1
        return min(self._query_min(a, b, 2 * k + 1, l, mid),
                   self._query_min(a, b, 2 * k + 2, mid, r))

    def _query_sum(self, a, b, k, l, r):
        if b <= l or r <= a:
            return 0
        if a <= l and r <= b:
            return self.sum[k]
        self.push(k)
        mid = (l + r) >> 1
        return self._query_sum(a, b, 2 * k + 1, l, mid) + self._query_sum(a, b, 2 * k + 2, mid, r)

    def _query_stats(self, a, b, k, l, r):
        if b <= l or r <= a:
            return inf, -inf, 0
        if a <= l and r <= b:
            return self.min_v[k], self.max_v[k], self.sum[k]
        self.push(k)
        mid = (l + r) >> 1
        x = self._query_stats(a, b, 2 * k + 1, l, mid)
        y = self._query_stats(a, b, 2 * k + 2, mid, r)
        return min(x[0], y[0]), max(x[1], y[1]), x[2] + y[2]

    def query_max(self, a, b):
        """[a,b) の最大値。空区間は -inf。O(log N)。"""
        assert 0 <= a <= b <= self.n
        return -inf if a == b else self._query_max(a, b, 0, 0, self.n0)

    def query_min(self, a, b):
        """[a,b) の最小値。空区間は inf。O(log N)。"""
        assert 0 <= a <= b <= self.n
        return inf if a == b else self._query_min(a, b, 0, 0, self.n0)

    def query_sum(self, a, b):
        """[a,b) の和。空区間は 0。O(log N)。"""
        assert 0 <= a <= b <= self.n
        return 0 if a == b else self._query_sum(a, b, 0, 0, self.n0)

    def query(self, a, b):
        """[a,b) の (最小値, 最大値, 和) を一度の探索で返す。O(log N)。"""
        assert 0 <= a <= b <= self.n
        return (inf, -inf, 0) if a == b else self._query_stats(a, b, 0, 0, self.n0)

    def all_max(self):
        return self.max_v[0]

    def all_min(self):
        return self.min_v[0]

    def all_sum(self):
        return self.sum[0]

    def get(self, i):
        """A[i] を取得する。O(log N)。"""
        assert 0 <= i < self.n
        k, l, r = 0, 0, self.n0
        while r - l > 1:
            self.push(k)
            mid = (l + r) >> 1
            if i < mid:
                k = 2 * k + 1
                r = mid
            else:
                k = 2 * k + 2
                l = mid
        return self.sum[k]

    def set(self, i, x):
        """A[i]=x。O(log N)。"""
        assert 0 <= i < self.n
        self.update_val(i, i + 1, x)

    def to_list(self):
        """実要素の配列を返す。保留操作を全展開し、O(N)。"""
        for k in range(self.n0 - 1):
            self.push(k)
        base = self.n0 - 1
        return self.sum[base:base + self.n]

    def __len__(self):
        return self.n

    def __getitem__(self, i):
        return self.get(i)

    def __str__(self):
        return str(self.to_list())
