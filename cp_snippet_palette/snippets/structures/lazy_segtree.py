"""遅延評価セグメント木。APIはshakayami/ACL-for-pythonに準拠。

使い方（このファイルを解答の先頭に貼り付けてから実行）
区間加算・区間和の例。集約値は(和,要素数)、更新値は加算量。
    op = lambda x, y: (x[0]+y[0], x[1]+y[1])
    mapping = lambda f, x: (x[0]+f*x[1], x[1])
    composition = lambda f, g: f+g  # 先にg、その後f
    seg = lazy_segtree([(v, 1) for v in [1, 2, 3]], op, (0, 0), mapping, composition, 0)
    seg.apply(0, 2, 5)  # [6,7,3]。区間は[l,r)
    seg.apply_point(2, 4)  # [6,7,7]
    seg.prod(0, 3), seg.get(1)  # => ((20, 3), (7, 1))
一次関数x <- a*x+bでは、composition(f,g)はgの後にfを適用する。
    compose = lambda f, g: (f[0]*g[0], f[0]*g[1]+f[1])
    compose((2, 1), (3, 4))  # => (6, 9)
"""


class lazy_segtree:
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
    入力: Vは集約値の初期列、N=len(V)。
    OP/Eは結合演算/単位元、MAPPINGは(f,x)へ更新適用、COMPOSITIONは(f,g)へgの後にfの合成を返す関数、IDは恒等更新。
    構築O(N)時間・空間（各演算O(1)）。pは0..N-1、0<=l<=r<=N、xは集約値、fは更新値、gは集約値をboolへ変換する境界探索の判定関数。
    """

    def __init__(self, V, OP, E, MAPPING, COMPOSITION, ID):
        """入力: Vは集約値の初期列、N=len(V)。
        OP/Eは結合演算/単位元、MAPPINGは(f,x)へ更新適用、COMPOSITIONは(f,g)へgの後にfの合成を返す関数、IDは恒等更新。
        構築O(N)時間・空間（各演算O(1)）。pは0..N-1、0<=l<=r<=N、xは集約値、fは更新値、gは集約値をboolへ変換する境界探索の判定関数。
        """
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
