"""遅延セグ木17種。File全体を貼れば、コールバック定義なしで構築できる。
0-indexed・[l,r)。set/getは要素形式、prod/all_prodは各クラスの集約値。
区間更新はapply(l,r,f)、一点更新はapply_point(p,f)。fの形式はクラスごとに記載。
max_right/min_leftの判定にはprodと同じ形式が渡る。空区間でTrueかつ単調であること。
構築O(N)、更新・取得・境界探索O(log N)、all_prod O(1)。固定長tupleを利用する。
PyPy向け、Codonコンパイル未確認。添字と要素の順序は固定。
ビット反転は0/1の交換であり、要素の並びを逆順にする操作ではない。
設計・操作一覧・verify候補はSEGTREE_RECIPES.mdを参照。

使い方（このファイルを解答の先頭に貼り付けてから実行）
    seg = range_add_sum([1, 2, 3])
    seg.apply(0, 2, 5)
    seg.get(1), seg.prod(0, 3)  # => (7, 16)
    seg = range_assign_sum([1, 2, 3]); seg.apply(0, 2, 0)
    seg.all_prod()  # => 3
    seg = range_affine_sum([1, 2, 3]); seg.apply(0, 3, (2, 1))
    seg.all_prod()  # => 15
    seg = range_add_min([3, 1, 4]); seg.apply(0, 2, -2)
    seg.all_prod()  # => -1
    seg = range_add_max([3, 1, 4]); seg.apply(0, 2, 5)
    seg.all_prod()  # => 8
    seg = range_add_min_count([2, 1, 1]); seg.apply(0, 3, 3)
    seg.all_prod()  # => (4, 2)
    seg = range_affine_minmax([1, 3, -2]); seg.apply(0, 3, (-2, 1))
    seg.all_prod()  # => (-5, 5)
    seg = range_clamp_minmax([1, 8, -2]); seg.apply(0, 3, (0, 5))
    seg.all_prod(), seg.to_list()  # => ((0, 5), [1, 5, 0])
    seg = range_flip_inversions([1, 0, 1, 0]); seg.apply(0, 4, True)
    seg.inversions(0, 4)  # => 1
    seg = range_binary_runs('001110'); seg.flip(0, 2)
    seg.longest(0, 6)  # => 5
    seg.assign(1, 4, 0)
    seg.longest(0, 6, bit=0)  # => 3
    seg = range_flip_brackets('()'); seg.apply(0, 2, True)
    seg.balanced(0, 2)  # => False
    seg = range_affine_sum_squares([1, 2]); seg.apply(0, 2, (2, 1))
    seg.all_prod()  # => (8, 34)
    seg = range_pair_add_product([(1, 3), (2, 4)]); seg.apply(0, 2, (2, 1))
    seg.all_prod()  # => (7, 9, 32)
    seg = range_index_affine_sum([0] * 5); seg.add_progression(1, 4, first=2, step=3)
    seg.to_list(), seg.all_prod()  # => ([0, 2, 5, 8, 0], 15)
    seg = range_digit_assign('12345'); seg.apply(1, 4, 0)
    seg.all_prod(), seg.prod(1, 4)  # => (10005, 0)
    seg = range_assign_max_subarray([-2, 3, -1, 4], allow_empty=False); seg.apply(1, 3, -5)
    seg.prod(0, 4)[3]  # => 4
    seg = range_add_gcd([6, 10, 14]); seg.apply(0, 3, 2)
    seg.to_list(), seg.all_prod()  # => ([8, 12, 16], 4)
上記の時間は演算・写像・比較1回がO(1)の場合。OPや大きい整数のコストは別に掛ける。
"""

from math import gcd


class _LazyActionTreeCore:
    """遅延評価セグメント木。0-indexed / 半開区間 [l,r)。

    lazy_segtree(V, OP, E, MAPPING, COMPOSITION, ID)。Vは初期配列。
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
        d[size : size + n] = V
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
        """半開区間[l,r)にfを適用する。1点にはapply_point(p,f)。O(log N)。"""
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
        return self.d[self.size : self.size + self.n]

    def __len__(self):
        return self.n

    def __getitem__(self, p):
        return self.get(p)

    def __str__(self):
        return str(self.to_list())


class _LazyPreset(_LazyActionTreeCore):
    """公開APIの要素・集約値と、内部の長さ付きモノイドを変換する。"""

    def __init__(self, V, OP, E, MAPPING, COMPOSITION, ID):
        super().__init__(
            [self._leaf(i, x) for i, x in enumerate(V)], OP, E, MAPPING, COMPOSITION, ID
        )

    def _leaf(self, p, x):
        return x

    def _value(self, s):
        return s

    def _result(self, s):
        return s

    def set(self, p, x):
        """元の要素形式のxでA[p]を置換する。O(log N)。"""
        super().set(p, self._leaf(p, x))

    def get(self, p):
        """位置pの要素を元の形式で返す。遅延伝播を含みO(log N)。"""
        return self._value(super().get(p))

    def prod(self, l, r):
        """半開区間[l,r)の集約値。空区間の値は各クラスを参照。O(log N)。"""
        return self._result(super().prod(l, r))

    def all_prod(self):
        """全体の集約値をO(1)で返す。"""
        return self._result(super().all_prod())

    def max_right(self, l, g):
        """g(prod(l,r))を満たす最大r。g(空区間)=True、右への拡張に対して単調。"""
        return super().max_right(l, lambda s: g(self._result(s)))

    def min_left(self, r, g):
        """g(prod(l,r))を満たす最小l。g(空区間)=True、左への拡張に対して単調。"""
        return super().min_left(r, lambda s: g(self._result(s)))

    def to_list(self):
        """全要素を元の形式のlistで返す。遅延伝播を含みO(N)。"""
        return [self._value(s) for s in super().to_list()]


class _LazyScalar(_LazyPreset):
    def _leaf(self, p, x):
        return x, 1

    def _value(self, s):
        return s[0]

    def _result(self, s):
        return s[0]


class range_add_sum(_LazyScalar):
    """range_add_sum(V)。apply(l,r,delta)で区間加算。prodは和、空は0。
    内部は(和,長さ)。負の値も可。和で境界探索する場合は更新後も全要素非負が必要。
    入力: Vは各クラスに記載した値の初期列（要素数だけの整数は不可）。N=len(V)。
    構築O(N)時間・空間、set/prod/境界探索はO(log(N+1))、all_prodはO(1)。 get/apply/apply_pointもO(log(N+1))。
     pは0..N-1の更新位置、l/rは0<=l<=r<=Nの整数境界。
    """

    def __init__(self, V):
        """入力: Vは各クラスに記載した値の初期列（要素数だけの整数は不可）。N=len(V)。
        構築O(N)時間・空間、set/prod/境界探索はO(log(N+1))、all_prodはO(1)。 get/apply/apply_pointもO(log(N+1))。
         pは0..N-1の更新位置、l/rは0<=l<=r<=Nの整数境界。
        """
        super().__init__(
            V,
            lambda x, y: (x[0] + y[0], x[1] + y[1]),
            (0, 0),
            lambda f, x: (x[0] + f * x[1], x[1]),
            lambda f, g: f + g,
            0,
        )


class range_assign_sum(_LazyScalar):
    """range_assign_sum(V)。apply(l,r,value)で区間代入。prodは和、空は0。
    0や負数も代入できる。Noneは恒等更新専用で、値としては使わない。
    入力: Vは各クラスに記載した値の初期列（要素数だけの整数は不可）。N=len(V)。
    構築O(N)時間・空間、set/prod/境界探索はO(log(N+1))、all_prodはO(1)。 get/apply/apply_pointもO(log(N+1))。
     pは0..N-1の更新位置、l/rは0<=l<=r<=Nの整数境界。
    """

    def __init__(self, V):
        """入力: Vは各クラスに記載した値の初期列（要素数だけの整数は不可）。N=len(V)。
        構築O(N)時間・空間、set/prod/境界探索はO(log(N+1))、all_prodはO(1)。 get/apply/apply_pointもO(log(N+1))。
         pは0..N-1の更新位置、l/rは0<=l<=r<=Nの整数境界。
        """
        super().__init__(
            V,
            lambda x, y: (x[0] + y[0], x[1] + y[1]),
            (0, 0),
            lambda f, x: x if f is None else (f * x[1], x[1]),
            lambda f, g: g if f is None else f,
            None,
        )


class range_affine_sum(_LazyScalar):
    """range_affine_sum(V,mod=998244353)。apply(l,r,(a,b))でx←a*x+b。
    prodは区間和、空は0。加算=(1,b)、代入=(0,b)、乗算=(a,0)。mod=0なら厳密整数。
    composition(f,g)はgの後にf。mod付きの和は境界探索の単調性が通常成り立たない。
    入力: Vは各クラスに記載した値の初期列（要素数だけの整数は不可）。N=len(V)。
    構築O(N)時間・空間、set/prod/境界探索はO(log(N+1))、all_prodはO(1)。 get/apply/apply_pointもO(log(N+1))。
     pは0..N-1の更新位置、l/rは0<=l<=r<=Nの整数境界。modは法の整数（0なら剰余なし、対応クラスのみ）。
    """

    def __init__(self, V, mod=998244353):
        """入力: Vは各クラスに記載した値の初期列（要素数だけの整数は不可）。N=len(V)。
        構築O(N)時間・空間、set/prod/境界探索はO(log(N+1))、all_prodはO(1)。 get/apply/apply_pointもO(log(N+1))。
         pは0..N-1の更新位置、l/rは0<=l<=r<=Nの整数境界。modは法の整数（0なら剰余なし、対応クラスのみ）。
        """
        assert mod >= 0
        self.mod = mod
        reduce = lambda x: x % mod if mod else x
        super().__init__(
            V,
            lambda x, y: (reduce(x[0] + y[0]), x[1] + y[1]),
            (0, 0),
            lambda f, x: (reduce(f[0] * x[0] + f[1] * x[1]), x[1]),
            lambda f, g: (reduce(f[0] * g[0]), reduce(f[0] * g[1] + f[1])),
            (1, 0),
        )

    def _leaf(self, p, x):
        return (x % self.mod if self.mod else x), 1


class range_add_min(_LazyScalar):
    """range_add_min(V)。apply(l,r,delta)で加算、prodは最小値、空はinf。
    内部に長さを持ち、空区間に更新を適用しても単位元を変えない。
    入力: Vは各クラスに記載した値の初期列（要素数だけの整数は不可）。N=len(V)。
    構築O(N)時間・空間、set/prod/境界探索はO(log(N+1))、all_prodはO(1)。 get/apply/apply_pointもO(log(N+1))。
     pは0..N-1の更新位置、l/rは0<=l<=r<=Nの整数境界。
    """

    def __init__(self, V):
        """入力: Vは各クラスに記載した値の初期列（要素数だけの整数は不可）。N=len(V)。
        構築O(N)時間・空間、set/prod/境界探索はO(log(N+1))、all_prodはO(1)。 get/apply/apply_pointもO(log(N+1))。
         pは0..N-1の更新位置、l/rは0<=l<=r<=Nの整数境界。
        """
        super().__init__(
            V,
            lambda x, y: (min(x[0], y[0]), x[1] + y[1]),
            (float("inf"), 0),
            lambda f, x: (x[0] + f, x[1]) if x[1] else x,
            lambda f, g: f + g,
            0,
        )


class range_add_max(_LazyScalar):
    """range_add_max(V)。apply(l,r,delta)で加算、prodは最大値、空は-inf。
    入力: Vは各クラスに記載した値の初期列（要素数だけの整数は不可）。N=len(V)。
    構築O(N)時間・空間、set/prod/境界探索はO(log(N+1))、all_prodはO(1)。 get/apply/apply_pointもO(log(N+1))。
     pは0..N-1の更新位置、l/rは0<=l<=r<=Nの整数境界。
    """

    def __init__(self, V):
        """入力: Vは各クラスに記載した値の初期列（要素数だけの整数は不可）。N=len(V)。
        構築O(N)時間・空間、set/prod/境界探索はO(log(N+1))、all_prodはO(1)。 get/apply/apply_pointもO(log(N+1))。
         pは0..N-1の更新位置、l/rは0<=l<=r<=Nの整数境界。
        """
        super().__init__(
            V,
            lambda x, y: (max(x[0], y[0]), x[1] + y[1]),
            (-float("inf"), 0),
            lambda f, x: (x[0] + f, x[1]) if x[1] else x,
            lambda f, g: f + g,
            0,
        )


class range_add_min_count(_LazyScalar):
    """range_add_min_count(V)。apply(l,r,delta)で加算、prodは(最小値,その個数)。
    空は(inf,0)。最小値の被覆数を数える用途。set/getは数値。
    入力: Vは各クラスに記載した値の初期列（要素数だけの整数は不可）。N=len(V)。
    構築O(N)時間・空間、set/prod/境界探索はO(log(N+1))、all_prodはO(1)。 get/apply/apply_pointもO(log(N+1))。
     pは0..N-1の更新位置、l/rは0<=l<=r<=Nの整数境界。
    """

    def __init__(self, V):
        """入力: Vは各クラスに記載した値の初期列（要素数だけの整数は不可）。N=len(V)。
        構築O(N)時間・空間、set/prod/境界探索はO(log(N+1))、all_prodはO(1)。 get/apply/apply_pointもO(log(N+1))。
         pは0..N-1の更新位置、l/rは0<=l<=r<=Nの整数境界。
        """
        def op(x, y):
            if x[0] == y[0]:
                return x[0], x[1] + y[1]
            return x if x[0] < y[0] else y

        super().__init__(
            V,
            op,
            (float("inf"), 0),
            lambda f, x: (x[0] + f, x[1]) if x[1] else x,
            lambda f, g: f + g,
            0,
        )

    def _result(self, s):
        return s


class _LazyMinMax(_LazyPreset):
    def _leaf(self, p, x):
        return x, x, 1

    def _value(self, s):
        return s[0]

    def _result(self, s):
        return s[0], s[1]


class range_affine_minmax(_LazyMinMax):
    """range_affine_minmax(V)。apply(l,r,(a,b))でx←a*x+b。負のaにも対応。
    prodは(最小値,最大値)、空は(inf,-inf)。加算=(1,b)、代入=(0,b)、符号反転=(-1,0)。
    剰余は取らない。a<0ならmin/maxを交換する。
    入力: Vは各クラスに記載した値の初期列（要素数だけの整数は不可）。N=len(V)。
    構築O(N)時間・空間、set/prod/境界探索はO(log(N+1))、all_prodはO(1)。 get/apply/apply_pointもO(log(N+1))。
     pは0..N-1の更新位置、l/rは0<=l<=r<=Nの整数境界。
    """

    def __init__(self, V):
        """入力: Vは各クラスに記載した値の初期列（要素数だけの整数は不可）。N=len(V)。
        構築O(N)時間・空間、set/prod/境界探索はO(log(N+1))、all_prodはO(1)。 get/apply/apply_pointもO(log(N+1))。
         pは0..N-1の更新位置、l/rは0<=l<=r<=Nの整数境界。
        """
        def mapping(f, x):
            if not x[2]:
                return x
            a, b = f
            lo, hi = (x[0], x[1]) if a >= 0 else (x[1], x[0])
            return a * lo + b, a * hi + b, x[2]

        super().__init__(
            V,
            lambda x, y: (min(x[0], y[0]), max(x[1], y[1]), x[2] + y[2]),
            (float("inf"), -float("inf"), 0),
            mapping,
            lambda f, g: (f[0] * g[0], f[0] * g[1] + f[1]),
            (1, 0),
        )


class range_clamp_minmax(_LazyMinMax):
    """range_clamp_minmax(V)。apply(l,r,(lo,hi))で全要素を[lo,hi]へ切り詰める。
    lo<=hi。prodは(最小値,最大値)、空は(inf,-inf)。和はこの情報だけでは求められない。
    chmin/chmax/assignも使用可能。区間和まで必要ならSegmentTreeBeatsを使う。
    入力: Vは各クラスに記載した値の初期列（要素数だけの整数は不可）。N=len(V)。
    構築O(N)時間・空間、set/prod/境界探索はO(log(N+1))、all_prodはO(1)。 get/apply/apply_pointもO(log(N+1))。
     pは0..N-1の更新位置、l/rは0<=l<=r<=Nの整数境界。
    """

    def __init__(self, V):
        """入力: Vは各クラスに記載した値の初期列（要素数だけの整数は不可）。N=len(V)。
        構築O(N)時間・空間、set/prod/境界探索はO(log(N+1))、all_prodはO(1)。 get/apply/apply_pointもO(log(N+1))。
         pは0..N-1の更新位置、l/rは0<=l<=r<=Nの整数境界。
        """
        def clamp(v, f):
            return min(max(v, f[0]), f[1])

        super().__init__(
            V,
            lambda x, y: (min(x[0], y[0]), max(x[1], y[1]), x[2] + y[2]),
            (float("inf"), -float("inf"), 0),
            lambda f, x: (clamp(x[0], f), clamp(x[1], f), x[2]) if x[2] else x,
            lambda f, g: (clamp(g[0], f), clamp(g[1], f)),
            (-float("inf"), float("inf")),
        )

    def chmin(self, l, r, upper):
        """各A[i]←min(A[i],upper)。O(log N)。"""
        self.apply(l, r, (-float("inf"), upper))

    def chmax(self, l, r, lower):
        """各A[i]←max(A[i],lower)。O(log N)。"""
        self.apply(l, r, (lower, float("inf")))

    def assign(self, l, r, value):
        """各A[i]をvalueへ代入。O(log N)。"""
        self.apply(l, r, (value, value))


class range_flip_inversions(_LazyPreset):
    """range_flip_inversions(V)。0/1列の区間反転と転倒数。文字列'010'も渡せる。
    apply(l,r,True)で0と1を交換。prodは(0の個数,1の個数,転倒数)、空は(0,0,0)。
    反転後の転倒数はzeros*ones-inversions。get/setは整数0/1。
    入力: Vは各クラスに記載した値の初期列（要素数だけの整数は不可）。N=len(V)。
    構築O(N)時間・空間、set/prod/境界探索はO(log(N+1))、all_prodはO(1)。 get/apply/apply_pointもO(log(N+1))。
     pは0..N-1の更新位置、l/rは0<=l<=r<=Nの整数境界。
    """

    def __init__(self, V):
        """入力: Vは各クラスに記載した値の初期列（要素数だけの整数は不可）。N=len(V)。
        構築O(N)時間・空間、set/prod/境界探索はO(log(N+1))、all_prodはO(1)。 get/apply/apply_pointもO(log(N+1))。
         pは0..N-1の更新位置、l/rは0<=l<=r<=Nの整数境界。
        """
        super().__init__(
            V,
            lambda x, y: (x[0] + y[0], x[1] + y[1], x[2] + y[2] + x[1] * y[0]),
            (0, 0, 0),
            lambda f, x: (x[1], x[0], x[0] * x[1] - x[2]) if f else x,
            lambda f, g: bool(f) ^ bool(g),
            False,
        )

    def _leaf(self, p, x):
        x = int(x)
        assert x in (0, 1)
        return 1 - x, x, 0

    def _value(self, s):
        return s[1]

    def inversions(self, l, r):
        """[l,r)の転倒数だけを返す。O(log N)。"""
        return self.prod(l, r)[2]


class range_binary_runs(_LazyPreset):
    """range_binary_runs(V)。0/1列の反転・代入と最長連続0/1。文字列も可。
    apply(l,r,(to0,to1))は0をto0、1をto1に置換する。値は0/1。
    flip(l,r)とassign(l,r,bit)を使えば更新tupleを組まなくてよい。
    prodは(n,prefix0,suffix0,best0,prefix1,suffix1,best1)、空は全て0。
    get/setは整数0/1。longest(l,r,bit=1)で連続長だけ取得できる。
    入力: Vは各クラスに記載した値の初期列（要素数だけの整数は不可）。N=len(V)。
    構築O(N)時間・空間、set/prod/境界探索はO(log(N+1))、all_prodはO(1)。 get/apply/apply_pointもO(log(N+1))。
     pは0..N-1の更新位置、l/rは0<=l<=r<=Nの整数境界。
    """

    def __init__(self, V):
        """入力: Vは各クラスに記載した値の初期列（要素数だけの整数は不可）。N=len(V)。
        構築O(N)時間・空間、set/prod/境界探索はO(log(N+1))、all_prodはO(1)。 get/apply/apply_pointもO(log(N+1))。
         pは0..N-1の更新位置、l/rは0<=l<=r<=Nの整数境界。
        """
        def op(x, y):
            return (
                x[0] + y[0],
                x[1] + (y[1] if x[1] == x[0] else 0),
                y[2] + (x[2] if y[2] == y[0] else 0),
                max(x[3], y[3], x[2] + y[1]),
                x[4] + (y[4] if x[4] == x[0] else 0),
                y[5] + (x[5] if y[5] == y[0] else 0),
                max(x[6], y[6], x[5] + y[4]),
            )

        def mapping(f, x):
            if f[0] == f[1]:
                n = x[0]
                return (n, 0, 0, 0, n, n, n) if f[0] else (n, n, n, n, 0, 0, 0)
            return (x[0], x[4], x[5], x[6], x[1], x[2], x[3]) if f[0] else x

        super().__init__(
            V, op, (0,) * 7, mapping, lambda f, g: (f[g[0]], f[g[1]]), (0, 1)
        )

    def _leaf(self, p, x):
        x = int(x)
        assert x in (0, 1)
        return (1, 0, 0, 0, 1, 1, 1) if x else (1, 1, 1, 1, 0, 0, 0)

    def _value(self, s):
        return s[4]

    def flip(self, l, r):
        """[l,r)の0と1を交換する。順序は変えない。O(log N)。"""
        self.apply(l, r, (1, 0))

    def assign(self, l, r, bit):
        """[l,r)をbit（0/1）で埋める。O(log N)。"""
        assert bit in (0, 1)
        self.apply(l, r, (bit, bit))

    def longest(self, l, r, bit=1):
        """[l,r)内のbitの最長連続長。空は0。O(log N)。"""
        assert bit in (0, 1)
        return self.prod(l, r)[6 if bit else 3]


class range_flip_brackets(_LazyPreset):
    """range_flip_brackets(V)。括弧列の'('と')'を区間で交換する。
    apply(l,r,True)で反転。prodは(balance,min_prefix,max_prefix)、空は(0,0,0)。
    set/getは括弧文字。balanced(l,r)で正しい括弧列かを判定。文字の並びは逆順にしない。
    入力: Vは各クラスに記載した値の初期列（要素数だけの整数は不可）。N=len(V)。
    構築O(N)時間・空間、set/prod/境界探索はO(log(N+1))、all_prodはO(1)。 get/apply/apply_pointもO(log(N+1))。
     pは0..N-1の更新位置、l/rは0<=l<=r<=Nの整数境界。
    """

    def __init__(self, V):
        """入力: Vは各クラスに記載した値の初期列（要素数だけの整数は不可）。N=len(V)。
        構築O(N)時間・空間、set/prod/境界探索はO(log(N+1))、all_prodはO(1)。 get/apply/apply_pointもO(log(N+1))。
         pは0..N-1の更新位置、l/rは0<=l<=r<=Nの整数境界。
        """
        super().__init__(
            V,
            lambda x, y: (x[0] + y[0], min(x[1], x[0] + y[1]), max(x[2], x[0] + y[2])),
            (0, 0, 0),
            lambda f, x: (-x[0], -x[2], -x[1]) if f else x,
            lambda f, g: bool(f) ^ bool(g),
            False,
        )

    def _leaf(self, p, x):
        assert x in ("(", ")")
        return (1, 0, 1) if x == "(" else (-1, -1, 0)

    def _value(self, s):
        return "(" if s[0] == 1 else ")"

    def balanced(self, l, r):
        """[l,r)が正しい括弧列ならTrue。空もTrue。O(log N)。"""
        total, low, _ = self.prod(l, r)
        return total == 0 and low >= 0


class range_affine_sum_squares(_LazyPreset):
    """range_affine_sum_squares(V,mod=998244353)。apply(l,r,(a,b))でx←a*x+b。
    prodは(sum(x),sum(x*x))、空は(0,0)。set/getは数値。mod=0なら厳密整数。
    内部は(sum,sum_square,length)。二乗和はa²*S2+2ab*S1+b²*lengthで更新する。
    入力: Vは各クラスに記載した値の初期列（要素数だけの整数は不可）。N=len(V)。
    構築O(N)時間・空間、set/prod/境界探索はO(log(N+1))、all_prodはO(1)。 get/apply/apply_pointもO(log(N+1))。
     pは0..N-1の更新位置、l/rは0<=l<=r<=Nの整数境界。modは法の整数（0なら剰余なし、対応クラスのみ）。
    """

    def __init__(self, V, mod=998244353):
        """入力: Vは各クラスに記載した値の初期列（要素数だけの整数は不可）。N=len(V)。
        構築O(N)時間・空間、set/prod/境界探索はO(log(N+1))、all_prodはO(1)。 get/apply/apply_pointもO(log(N+1))。
         pは0..N-1の更新位置、l/rは0<=l<=r<=Nの整数境界。modは法の整数（0なら剰余なし、対応クラスのみ）。
        """
        assert mod >= 0
        self.mod = mod
        reduce = lambda x: x % mod if mod else x

        def mapping(f, x):
            a, b = f
            return (
                reduce(a * x[0] + b * x[2]),
                reduce(a * a * x[1] + 2 * a * b * x[0] + b * b * x[2]),
                x[2],
            )

        super().__init__(
            V,
            lambda x, y: (reduce(x[0] + y[0]), reduce(x[1] + y[1]), x[2] + y[2]),
            (0, 0, 0),
            mapping,
            lambda f, g: (reduce(f[0] * g[0]), reduce(f[0] * g[1] + f[1])),
            (1, 0),
        )

    def _leaf(self, p, x):
        if self.mod:
            x %= self.mod
        return x, x * x % self.mod if self.mod else x * x, 1

    def _value(self, s):
        return s[0]

    def _result(self, s):
        return s[0], s[1]


class range_pair_add_product(_LazyPreset):
    """range_pair_add_product(V,mod=998244353)。V=[(A[i],B[i]),...]。
    apply(l,r,(da,db))でAにda、Bにdbを同時加算。prodは(sum(A),sum(B),sum(A*B))。
    空は(0,0,0)。set/getは(a,b)。mod=0は厳密整数。ABの更新には加算前の両方の和を使う。
    入力: Vは各クラスに記載した値の初期列（要素数だけの整数は不可）。N=len(V)。
    構築O(N)時間・空間、set/prod/境界探索はO(log(N+1))、all_prodはO(1)。 get/apply/apply_pointもO(log(N+1))。
     pは0..N-1の更新位置、l/rは0<=l<=r<=Nの整数境界。modは法の整数（0なら剰余なし、対応クラスのみ）。
    """

    def __init__(self, V, mod=998244353):
        """入力: Vは各クラスに記載した値の初期列（要素数だけの整数は不可）。N=len(V)。
        構築O(N)時間・空間、set/prod/境界探索はO(log(N+1))、all_prodはO(1)。 get/apply/apply_pointもO(log(N+1))。
         pは0..N-1の更新位置、l/rは0<=l<=r<=Nの整数境界。modは法の整数（0なら剰余なし、対応クラスのみ）。
        """
        assert mod >= 0
        self.mod = mod
        reduce = lambda x: x % mod if mod else x

        def mapping(f, x):
            da, db = f
            return (
                reduce(x[0] + da * x[3]),
                reduce(x[1] + db * x[3]),
                reduce(x[2] + da * x[1] + db * x[0] + da * db * x[3]),
                x[3],
            )

        super().__init__(
            V,
            lambda x, y: (
                reduce(x[0] + y[0]),
                reduce(x[1] + y[1]),
                reduce(x[2] + y[2]),
                x[3] + y[3],
            ),
            (0, 0, 0, 0),
            mapping,
            lambda f, g: (reduce(f[0] + g[0]), reduce(f[1] + g[1])),
            (0, 0),
        )

    def _leaf(self, p, x):
        a, b = x
        if self.mod:
            a %= self.mod
            b %= self.mod
        return a, b, a * b % self.mod if self.mod else a * b, 1

    def _value(self, s):
        return s[0], s[1]

    def _result(self, s):
        return s[0], s[1], s[2]


class range_index_affine_sum(_LazyPreset):
    """range_index_affine_sum(V,mod=0)。apply(l,r,(a,b,c))でA[i]←a*A[i]+b*i+c。
    iは配列全体での0-indexedの添字。prodは和、空は0。mod=0は厳密整数。
    内部は(sum,index_sum,length)。等差列の加算・代入は専用メソッドでも指定できる。
    入力: Vは各クラスに記載した値の初期列（要素数だけの整数は不可）。N=len(V)。
    構築O(N)時間・空間、set/prod/境界探索はO(log(N+1))、all_prodはO(1)。 get/apply/apply_pointもO(log(N+1))。
     pは0..N-1の更新位置、l/rは0<=l<=r<=Nの整数境界。modは法の整数（0なら剰余なし、対応クラスのみ）。
    """

    def __init__(self, V, mod=0):
        """入力: Vは各クラスに記載した値の初期列（要素数だけの整数は不可）。N=len(V)。
        構築O(N)時間・空間、set/prod/境界探索はO(log(N+1))、all_prodはO(1)。 get/apply/apply_pointもO(log(N+1))。
         pは0..N-1の更新位置、l/rは0<=l<=r<=Nの整数境界。modは法の整数（0なら剰余なし、対応クラスのみ）。
        """
        assert mod >= 0
        self.mod = mod
        reduce = lambda x: x % mod if mod else x
        super().__init__(
            V,
            lambda x, y: (reduce(x[0] + y[0]), x[1] + y[1], x[2] + y[2]),
            (0, 0, 0),
            lambda f, x: (reduce(f[0] * x[0] + f[1] * x[1] + f[2] * x[2]), x[1], x[2]),
            lambda f, g: (
                reduce(f[0] * g[0]),
                reduce(f[0] * g[1] + f[1]),
                reduce(f[0] * g[2] + f[2]),
            ),
            (1, 0, 0),
        )

    def _leaf(self, p, x):
        return (x % self.mod if self.mod else x), p, 1

    def _value(self, s):
        return s[0]

    def _result(self, s):
        return s[0]

    def add_progression(self, l, r, first, step=0):
        """A[i]+=first+(i-l)*step。firstは区間左端lの加算量。O(log N)。"""
        self.apply(l, r, (1, step, first - step * l))

    def assign_progression(self, l, r, first, step=0):
        """A[i]=first+(i-l)*step。firstは区間左端lの代入値。O(log N)。"""
        self.apply(l, r, (0, step, first - step * l))


class range_digit_assign(_LazyPreset):
    """range_digit_assign(V,mod=998244353,base=10)。数字列の区間代入と数値化。
    Vは数字の列（10進なら文字列も可）。0<=digit<base<=mod、base>=2。
    apply(l,r,digit)で同じ数字を代入。0も有効、Noneは恒等更新専用。
    prodは[l,r)を左から読んだbase進数mod mod、空は0。get/setは整数digit。
    桁数・baseの冪・111...を事前計算するので、法が合成数でも除算なしで動く。
    入力: Vは各クラスに記載した値の初期列（要素数だけの整数は不可）。N=len(V)。
    構築O(N)時間・空間、set/prod/境界探索はO(log(N+1))、all_prodはO(1)。 get/apply/apply_pointもO(log(N+1))。
     pは0..N-1の更新位置、l/rは0<=l<=r<=Nの整数境界。modはbase以上の正整数の法。0は指定できない。
    """

    def __init__(self, V, mod=998244353, base=10):
        """入力: Vは各クラスに記載した値の初期列（要素数だけの整数は不可）。N=len(V)。
        構築O(N)時間・空間、set/prod/境界探索はO(log(N+1))、all_prodはO(1)。 get/apply/apply_pointもO(log(N+1))。
         pは0..N-1の更新位置、l/rは0<=l<=r<=Nの整数境界。modはbase以上の正整数の法。0は指定できない。
        """
        assert 2 <= base <= mod
        self.mod, self.base = mod, base
        units = [0] * (len(V) + 1)
        for i in range(len(V)):
            units[i + 1] = (units[i] * base + 1) % mod
        super().__init__(
            V,
            lambda x, y: ((x[0] * y[1] + y[0]) % mod, x[1] * y[1] % mod, x[2] + y[2]),
            (0, 1, 0),
            lambda f, x: x if f is None else (f * units[x[2]] % mod, x[1], x[2]),
            lambda f, g: g if f is None else f,
            None,
        )

    def _leaf(self, p, x):
        x = int(x)
        assert 0 <= x < self.base
        return x, self.base % self.mod, 1

    def _value(self, s):
        return s[0]

    def _result(self, s):
        return s[0]


class range_assign_max_subarray(_LazyPreset):
    """range_assign_max_subarray(V,allow_empty=True)。区間代入と最大部分配列和。
    apply(l,r,value)で代入。prodは(全体和,最大prefix和,最大suffix和,最大部分配列和)。
    空はTrueなら(0,0,0,0)、Falseなら(0,-inf,-inf,-inf)。set/getは数値。
    Noneは恒等更新専用。区間加算はこの集約情報では処理できない。
    入力: Vは各クラスに記載した値の初期列（要素数だけの整数は不可）。N=len(V)。
    構築O(N)時間・空間、set/prod/境界探索はO(log(N+1))、all_prodはO(1)。 get/apply/apply_pointもO(log(N+1))。
     pは0..N-1の更新位置、l/rは0<=l<=r<=Nの整数境界。
    """

    def __init__(self, V, allow_empty=True):
        """入力: Vは各クラスに記載した値の初期列（要素数だけの整数は不可）。N=len(V)。
        構築O(N)時間・空間、set/prod/境界探索はO(log(N+1))、all_prodはO(1)。 get/apply/apply_pointもO(log(N+1))。
         pは0..N-1の更新位置、l/rは0<=l<=r<=Nの整数境界。
        """
        self.allow_empty = allow_empty
        e = 0 if allow_empty else -float("inf")

        def op(x, y):
            return (
                x[0] + y[0],
                max(x[1], x[0] + y[1]),
                max(y[2], y[0] + x[2]),
                max(x[3], y[3], x[2] + y[1]),
                x[4] + y[4],
            )

        def mapping(f, x):
            if f is None or not x[4]:
                return x
            total = f * x[4]
            best = max(0, total) if allow_empty else max(f, total)
            return total, best, best, best, x[4]

        super().__init__(
            V, op, (0, e, e, e, 0), mapping, lambda f, g: g if f is None else f, None
        )

    def _leaf(self, p, x):
        best = max(0, x) if self.allow_empty else x
        return x, best, best, best, 1

    def _value(self, s):
        return s[0]

    def _result(self, s):
        return s[:4]


class range_add_gcd(_LazyPreset):
    """range_add_gcd(V)。整数列への区間加算と区間GCD。apply(l,r,delta)。
    prodは非負GCD、空は0。set/getは元の符号付き整数。
    内部は(first,last,gcd_of_adjacent_differences,length)。一様加算で差分GCDは変化しない。
    入力: Vは各クラスに記載した値の初期列（要素数だけの整数は不可）。N=len(V)。
    構築O(N)時間・空間、set/prod/境界探索はO(log(N+1))、all_prodはO(1)。 get/apply/apply_pointもO(log(N+1))。
     pは0..N-1の更新位置、l/rは0<=l<=r<=Nの整数境界。
    """

    def __init__(self, V):
        """入力: Vは各クラスに記載した値の初期列（要素数だけの整数は不可）。N=len(V)。
        構築O(N)時間・空間、set/prod/境界探索はO(log(N+1))、all_prodはO(1)。 get/apply/apply_pointもO(log(N+1))。
         pは0..N-1の更新位置、l/rは0<=l<=r<=Nの整数境界。
        """
        def op(x, y):
            if not x[3]:
                return y
            if not y[3]:
                return x
            return x[0], y[1], gcd(gcd(x[2], y[2]), abs(y[0] - x[1])), x[3] + y[3]

        super().__init__(
            V,
            op,
            (0, 0, 0, 0),
            lambda f, x: (x[0] + f, x[1] + f, x[2], x[3]) if x[3] else x,
            lambda f, g: f + g,
            0,
        )

    def _leaf(self, p, x):
        return x, x, 0, 1

    def _value(self, s):
        return s[0]

    def _result(self, s):
        return gcd(abs(s[0]), s[2]) if s[3] else 0
