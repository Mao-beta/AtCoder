"""一点更新セグ木16種。File全体を貼り、用途に合うクラスを1つ構築する。
外部ライブラリ不要。0-indexed・[l,r)、shakayami/ACL-for-pythonと同じメソッド名。
set(p,x)/get(p)は元の要素形式。prod/all_prodは各クラスの集約値。
max_right/min_leftの判定にはprodと同じ形式が渡る。単位元でTrueかつ単調であること。
構築O(N)、点更新・区間集約・境界探索O(log N)。XOR基底のみ結合O(B²)。
PyPy向け。Codonコンパイル未確認。設計と使い分けはSEGTREE_RECIPES.mdを参照。

使い方（このファイルを解答の先頭に貼り付けてから実行）
    seg = range_sum([1, 2, 3])
    seg.set(1, 5)
    seg.prod(0, 3), seg.max_right(0, lambda s: s <= 6)  # => (9, 2)
    range_min([3, 1, 4]).prod(0, 3), range_max([3, 1, 4]).all_prod()  # => (1, 4)
    range_gcd([6, 10, 14]).all_prod()  # => 2
    range_xor([3, 5]).all_prod(), range_or([3, 5]).all_prod(), range_and([3, 5]).all_prod()  # => (6, 7, 1)
    range_min_count([2, 1, 1]).all_prod()  # => (1, 2)
    range_max_count([2, 1, 2]).all_prod()  # => (2, 2)
    range_top2([5, 3, 5, 2, 3]).all_prod()  # => (5, 2, 3, 2)
    range_max_subarray([-2, 3, -1, 4, -5]).all_prod()  # => (-1, 4, 1, 6)
    range_max_subarray([-5, -2], allow_empty=False).prod(0, 2)[3]  # => -2
    range_brackets('(()())').balanced(0, 6)  # => True
    range_affine_composite([(2, 1), (3, 4)]).all_prod()  # 3*(2*x+1)+4
    # => (6, 7)
    range_matrix_product([(1, 1, 1, 0)] * 3).all_prod()  # => (3, 2, 2, 1)
    basis = range_xor_basis([3, 5, 6], bits=3)
    basis.rank(0, 3), basis.max_xor(0, 3)  # => (2, 6)
    semi = semigroup_segtree([3, 1, 4], min)
    semi.prod(0, 3), semi.prod(1, 1)  # => (1, None)
"""

from math import gcd


class _MonoidTreeCore:
    """一般のセグメント木。0-indexed / 半開区間 [l,r)。

    segtree(V, OP, E)。V は初期配列。全てEなら [E] * N を渡す。
    OP は結合的二項演算、E は左右の単位元。可換性は不要。
    set / prod / max_right / min_left: O(log N)、get / all_prod: O(1)。
    境界探索の判定関数 f は f(E)=True で、拡張に対して True→False に単調。
    """

    def __init__(self, V, OP, E):
        """初期配列V、結合的演算OP、単位元Eから構築する。O(N)。"""
        n = len(V)
        self.n = n
        self.op = OP
        self.e = E
        self.log = (n - 1).bit_length() if n else 0
        self.size = 1 << self.log
        d = [E] * (2 * self.size)
        d[self.size : self.size + n] = V
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
        return self.d[self.size : self.size + self.n]

    def __len__(self):
        return self.n

    def __getitem__(self, p):
        return self.get(p)

    def __str__(self):
        return str(self.to_list())


class _MonoidPreset(_MonoidTreeCore):
    """葉の符号化と公開結果の変換をまとめる。演算本体はACL形式のセグ木。"""

    def __init__(self, V, OP, E):
        super().__init__([self._leaf(i, x) for i, x in enumerate(V)], OP, E)

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
        """位置pの元の要素を返す。O(1)。"""
        return self._value(super().get(p))

    def prod(self, l, r):
        """半開区間[l,r)の集約値。空区間の値は各クラスの説明を参照。"""
        return self._result(super().prod(l, r))

    def all_prod(self):
        """全体の集約値をO(1)で返す。"""
        return self._result(super().all_prod())

    def max_right(self, l, f):
        """f(prod(l,r))を満たす最大r。f(空区間)=True、右への拡張に対して単調。"""
        return super().max_right(l, lambda s: f(self._result(s)))

    def min_left(self, r, f):
        """f(prod(l,r))を満たす最小l。f(空区間)=True、左への拡張に対して単調。"""
        return super().min_left(r, lambda s: f(self._result(s)))

    def to_list(self):
        """現在の全要素を元の形式のlistで返す。O(N)。"""
        return [self._value(s) for s in super().to_list()]


class range_sum(_MonoidPreset):
    """range_sum(V)。点代入・区間和。prodは数値、空は0。和の境界探索は非負列で使う。
    入力: Vは各クラスに記載した値の初期列（要素数だけの整数は不可）。N=len(V)。
    構築O(N)時間・空間、set/prod/境界探索はO(log(N+1))、all_prodはO(1)。 getはO(1)。
     pは0..N-1の更新位置、l/rは0<=l<=r<=Nの整数境界。
    """

    def __init__(self, V):
        """入力: Vは各クラスに記載した値の初期列（要素数だけの整数は不可）。N=len(V)。
        構築O(N)時間・空間、set/prod/境界探索はO(log(N+1))、all_prodはO(1)。 getはO(1)。
         pは0..N-1の更新位置、l/rは0<=l<=r<=Nの整数境界。
        """
        super().__init__(V, lambda x, y: x + y, 0)


class range_min(_MonoidPreset):
    """range_min(V)。点代入・区間最小値。空はfloat('inf')。
    入力: Vは各クラスに記載した値の初期列（要素数だけの整数は不可）。N=len(V)。
    構築O(N)時間・空間、set/prod/境界探索はO(log(N+1))、all_prodはO(1)。 getはO(1)。
     pは0..N-1の更新位置、l/rは0<=l<=r<=Nの整数境界。
    """

    def __init__(self, V):
        """入力: Vは各クラスに記載した値の初期列（要素数だけの整数は不可）。N=len(V)。
        構築O(N)時間・空間、set/prod/境界探索はO(log(N+1))、all_prodはO(1)。 getはO(1)。
         pは0..N-1の更新位置、l/rは0<=l<=r<=Nの整数境界。
        """
        super().__init__(V, min, float("inf"))


class range_max(_MonoidPreset):
    """range_max(V)。点代入・区間最大値。空は-float('inf')。
    入力: Vは各クラスに記載した値の初期列（要素数だけの整数は不可）。N=len(V)。
    構築O(N)時間・空間、set/prod/境界探索はO(log(N+1))、all_prodはO(1)。 getはO(1)。
     pは0..N-1の更新位置、l/rは0<=l<=r<=Nの整数境界。
    """

    def __init__(self, V):
        """入力: Vは各クラスに記載した値の初期列（要素数だけの整数は不可）。N=len(V)。
        構築O(N)時間・空間、set/prod/境界探索はO(log(N+1))、all_prodはO(1)。 getはO(1)。
         pは0..N-1の更新位置、l/rは0<=l<=r<=Nの整数境界。
        """
        super().__init__(V, max, -float("inf"))


class range_gcd(_MonoidPreset):
    """range_gcd(V)。整数の点代入・区間GCD。prodは非負、空は0。
    入力を絶対値へ正規化するため、get/to_listも非負の値を返す。
    入力: Vは各クラスに記載した値の初期列（要素数だけの整数は不可）。N=len(V)。
    構築O(N)時間・空間、set/prod/境界探索はO(log(N+1))、all_prodはO(1)。 getはO(1)。
     pは0..N-1の更新位置、l/rは0<=l<=r<=Nの整数境界。
    """

    def __init__(self, V):
        """入力: Vは各クラスに記載した値の初期列（要素数だけの整数は不可）。N=len(V)。
        構築O(N)時間・空間、set/prod/境界探索はO(log(N+1))、all_prodはO(1)。 getはO(1)。
         pは0..N-1の更新位置、l/rは0<=l<=r<=Nの整数境界。
        """
        super().__init__(V, gcd, 0)

    def _leaf(self, p, x):
        return abs(x)


class range_xor(_MonoidPreset):
    """range_xor(V)。非負整数の点代入・区間XOR。空は0。
    入力: Vは各クラスに記載した値の初期列（要素数だけの整数は不可）。N=len(V)。
    構築O(N)時間・空間、set/prod/境界探索はO(log(N+1))、all_prodはO(1)。 getはO(1)。
     pは0..N-1の更新位置、l/rは0<=l<=r<=Nの整数境界。
    """

    def __init__(self, V):
        """入力: Vは各クラスに記載した値の初期列（要素数だけの整数は不可）。N=len(V)。
        構築O(N)時間・空間、set/prod/境界探索はO(log(N+1))、all_prodはO(1)。 getはO(1)。
         pは0..N-1の更新位置、l/rは0<=l<=r<=Nの整数境界。
        """
        super().__init__(V, lambda x, y: x ^ y, 0)


class range_or(_MonoidPreset):
    """range_or(V)。非負整数の点代入・区間OR。空は0。
    入力: Vは各クラスに記載した値の初期列（要素数だけの整数は不可）。N=len(V)。
    構築O(N)時間・空間、set/prod/境界探索はO(log(N+1))、all_prodはO(1)。 getはO(1)。
     pは0..N-1の更新位置、l/rは0<=l<=r<=Nの整数境界。
    """

    def __init__(self, V):
        """入力: Vは各クラスに記載した値の初期列（要素数だけの整数は不可）。N=len(V)。
        構築O(N)時間・空間、set/prod/境界探索はO(log(N+1))、all_prodはO(1)。 getはO(1)。
         pは0..N-1の更新位置、l/rは0<=l<=r<=Nの整数境界。
        """
        super().__init__(V, lambda x, y: x | y, 0)


class range_and(_MonoidPreset):
    """range_and(V)。非負整数の点代入・区間AND。空は-1（全ビット1の単位元）。
    入力: Vは各クラスに記載した値の初期列（要素数だけの整数は不可）。N=len(V)。
    構築O(N)時間・空間、set/prod/境界探索はO(log(N+1))、all_prodはO(1)。 getはO(1)。
     pは0..N-1の更新位置、l/rは0<=l<=r<=Nの整数境界。
    """

    def __init__(self, V):
        """入力: Vは各クラスに記載した値の初期列（要素数だけの整数は不可）。N=len(V)。
        構築O(N)時間・空間、set/prod/境界探索はO(log(N+1))、all_prodはO(1)。 getはO(1)。
         pは0..N-1の更新位置、l/rは0<=l<=r<=Nの整数境界。
        """
        super().__init__(V, lambda x, y: x & y, -1)


class range_min_count(_MonoidPreset):
    """range_min_count(V)。prodは(最小値,その個数)、空は(inf,0)。set/getは数値。
    入力: Vは各クラスに記載した値の初期列（要素数だけの整数は不可）。N=len(V)。
    構築O(N)時間・空間、set/prod/境界探索はO(log(N+1))、all_prodはO(1)。 getはO(1)。
     pは0..N-1の更新位置、l/rは0<=l<=r<=Nの整数境界。
    """

    def __init__(self, V):
        """入力: Vは各クラスに記載した値の初期列（要素数だけの整数は不可）。N=len(V)。
        構築O(N)時間・空間、set/prod/境界探索はO(log(N+1))、all_prodはO(1)。 getはO(1)。
         pは0..N-1の更新位置、l/rは0<=l<=r<=Nの整数境界。
        """
        def op(x, y):
            if x[0] == y[0]:
                return x[0], x[1] + y[1]
            return x if x[0] < y[0] else y

        super().__init__(V, op, (float("inf"), 0))

    def _leaf(self, p, x):
        return x, 1

    def _value(self, s):
        return s[0]


class range_max_count(_MonoidPreset):
    """range_max_count(V)。prodは(最大値,その個数)、空は(-inf,0)。set/getは数値。
    入力: Vは各クラスに記載した値の初期列（要素数だけの整数は不可）。N=len(V)。
    構築O(N)時間・空間、set/prod/境界探索はO(log(N+1))、all_prodはO(1)。 getはO(1)。
     pは0..N-1の更新位置、l/rは0<=l<=r<=Nの整数境界。
    """

    def __init__(self, V):
        """入力: Vは各クラスに記載した値の初期列（要素数だけの整数は不可）。N=len(V)。
        構築O(N)時間・空間、set/prod/境界探索はO(log(N+1))、all_prodはO(1)。 getはO(1)。
         pは0..N-1の更新位置、l/rは0<=l<=r<=Nの整数境界。
        """
        def op(x, y):
            if x[0] == y[0]:
                return x[0], x[1] + y[1]
            return x if x[0] > y[0] else y

        super().__init__(V, op, (-float("inf"), 0))

    def _leaf(self, p, x):
        return x, 1

    def _value(self, s):
        return s[0]


class range_top2(_MonoidPreset):
    """range_top2(V)。異なる上位2値と個数を(v1,c1,v2,c2)で返す。
    値が存在しない部分は(None,0)。2番目がなければc2=0。set/getは数値。
    入力: Vは各クラスに記載した値の初期列（要素数だけの整数は不可）。N=len(V)。
    構築O(N)時間・空間、set/prod/境界探索はO(log(N+1))、all_prodはO(1)。 getはO(1)。
     pは0..N-1の更新位置、l/rは0<=l<=r<=Nの整数境界。
    """

    def __init__(self, V):
        """入力: Vは各クラスに記載した値の初期列（要素数だけの整数は不可）。N=len(V)。
        構築O(N)時間・空間、set/prod/境界探索はO(log(N+1))、all_prodはO(1)。 getはO(1)。
         pは0..N-1の更新位置、l/rは0<=l<=r<=Nの整数境界。
        """
        def op(x, y):
            first = second = None
            c1 = c2 = 0
            for value, count in (
                (x[0], x[1]),
                (x[2], x[3]),
                (y[0], y[1]),
                (y[2], y[3]),
            ):
                if not count:
                    continue
                if not c1 or value > first:
                    second, c2 = first, c1
                    first, c1 = value, count
                elif value == first:
                    c1 += count
                elif not c2 or value > second:
                    second, c2 = value, count
                elif value == second:
                    c2 += count
            return first, c1, second, c2

        super().__init__(V, op, (None, 0, None, 0))

    def _leaf(self, p, x):
        return x, 1, None, 0

    def _value(self, s):
        return s[0]


class range_max_subarray(_MonoidPreset):
    """range_max_subarray(V,allow_empty=True)。最大部分配列和の点更新。
    prodは(全体和,最大prefix和,最大suffix和,最大部分配列和)。set/getは数値。
    空部分列を許す既定値では各最大値>=0。Falseなら非空を要求し、空区間は(0,-inf,-inf,-inf)。
    入力: Vは各クラスに記載した値の初期列（要素数だけの整数は不可）。N=len(V)。
    構築O(N)時間・空間、set/prod/境界探索はO(log(N+1))、all_prodはO(1)。 getはO(1)。
     pは0..N-1の更新位置、l/rは0<=l<=r<=Nの整数境界。
    """

    def __init__(self, V, allow_empty=True):
        """入力: Vは各クラスに記載した値の初期列（要素数だけの整数は不可）。N=len(V)。
        構築O(N)時間・空間、set/prod/境界探索はO(log(N+1))、all_prodはO(1)。 getはO(1)。
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
            )

        super().__init__(V, op, (0, e, e, e))

    def _leaf(self, p, x):
        best = max(0, x) if self.allow_empty else x
        return x, best, best, best

    def _value(self, s):
        return s[0]


class range_brackets(_MonoidPreset):
    """range_brackets(V)。Vは'('と')'の文字列または列。set(p,'(')で点更新。
    prodは(balance,min_prefix,max_prefix)。空prefixを含む。空区間は(0,0,0)。
    balanced(l,r)は正しい括弧列かを返す。任意区間の並び替えは扱わない。
    入力: Vは各クラスに記載した値の初期列（要素数だけの整数は不可）。N=len(V)。
    構築O(N)時間・空間、set/prod/境界探索はO(log(N+1))、all_prodはO(1)。 getはO(1)。
     pは0..N-1の更新位置、l/rは0<=l<=r<=Nの整数境界。
    """

    def __init__(self, V):
        """入力: Vは各クラスに記載した値の初期列（要素数だけの整数は不可）。N=len(V)。
        構築O(N)時間・空間、set/prod/境界探索はO(log(N+1))、all_prodはO(1)。 getはO(1)。
         pは0..N-1の更新位置、l/rは0<=l<=r<=Nの整数境界。
        """
        def op(x, y):
            return x[0] + y[0], min(x[1], x[0] + y[1]), max(x[2], x[0] + y[2])

        super().__init__(V, op, (0, 0, 0))

    def _leaf(self, p, x):
        assert x in ("(", ")")
        return (1, 0, 1) if x == "(" else (-1, -1, 0)

    def _value(self, s):
        return "(" if s[0] == 1 else ")"

    def balanced(self, l, r):
        """[l,r)が正しい括弧列ならTrue。空もTrue。O(log N)。"""
        total, low, _ = self.prod(l, r)
        return total == 0 and low >= 0


class range_affine_composite(_MonoidPreset):
    """range_affine_composite(V,mod=998244353)。V[i]=(a,b)はa*x+b。
    prod(l,r)は左から順に関数を適用した合成(a,b)。空は(1,0)。set/getも(a,b)。
    mod=0で整数の厳密計算。値の桁数が増えると演算コストも増える。
    入力: Vは各クラスに記載した値の初期列（要素数だけの整数は不可）。N=len(V)。
    構築O(N)時間・空間、set/prod/境界探索はO(log(N+1))、all_prodはO(1)。 getはO(1)。
     pは0..N-1の更新位置、l/rは0<=l<=r<=Nの整数境界。modは法の整数（0なら剰余なし、対応クラスのみ）。
    """

    def __init__(self, V, mod=998244353):
        """入力: Vは各クラスに記載した値の初期列（要素数だけの整数は不可）。N=len(V)。
        構築O(N)時間・空間、set/prod/境界探索はO(log(N+1))、all_prodはO(1)。 getはO(1)。
         pは0..N-1の更新位置、l/rは0<=l<=r<=Nの整数境界。modは法の整数（0なら剰余なし、対応クラスのみ）。
        """
        assert mod >= 0
        self.mod = mod

        def op(x, y):
            a, b = y[0] * x[0], y[0] * x[1] + y[1]
            return (a % mod, b % mod) if mod else (a, b)

        super().__init__(V, op, (1 % mod if mod else 1, 0))

    def _leaf(self, p, x):
        a, b = x
        return (a % self.mod, b % self.mod) if self.mod else (a, b)


class range_matrix_product(_MonoidPreset):
    """range_matrix_product(V,mod=998244353)。2×2行列を(a00,a01,a10,a11)で渡す。
    prod(l,r)はM[l]*M[l+1]*...*M[r-1]、空は単位行列。mod=0なら厳密整数。
    列ベクトルへの作用は右の行列が先。左から関数を適用するrange_affine_compositeと向きが異なる。
    入力: Vは各クラスに記載した値の初期列（要素数だけの整数は不可）。N=len(V)。
    構築O(N)時間・空間、set/prod/境界探索はO(log(N+1))、all_prodはO(1)。 getはO(1)。
     pは0..N-1の更新位置、l/rは0<=l<=r<=Nの整数境界。modは法の整数（0なら剰余なし、対応クラスのみ）。
    """

    def __init__(self, V, mod=998244353):
        """入力: Vは各クラスに記載した値の初期列（要素数だけの整数は不可）。N=len(V)。
        構築O(N)時間・空間、set/prod/境界探索はO(log(N+1))、all_prodはO(1)。 getはO(1)。
         pは0..N-1の更新位置、l/rは0<=l<=r<=Nの整数境界。modは法の整数（0なら剰余なし、対応クラスのみ）。
        """
        assert mod >= 0
        self.mod = mod

        def op(x, y):
            a, b, c, d = x
            e, f, g, h = y
            z = (a * e + b * g, a * f + b * h, c * e + d * g, c * f + d * h)
            return tuple(v % mod for v in z) if mod else z

        one = 1 % mod if mod else 1
        super().__init__(V, op, (one, 0, 0, one))

    def _leaf(self, p, x):
        assert len(x) == 4
        return tuple(v % self.mod for v in x) if self.mod else tuple(x)


class range_xor_basis(_MonoidPreset):
    """range_xor_basis(V,bits=60)。0<=V[i]<2**bits。区間の部分集合XORの線形基底。
    prodは最高位ビットの降順の基底tuple、空は()。set/getは非負整数。
    rankは独立数、max_xorは部分集合XORに初期値xをXORした最大値。
    結合O(B²)、点更新・区間取得O(B² log N)、構築上界O(N B²)。大規模入力では重い。
    入力: Vは非負整数列、bitsは最大bit幅B、N=len(V)。構築O(N*B²)時間・O(N*B)空間。
    rank/max_xorも区間基底の取得を含めO(B² log(N+1))時間。 pは0..N-1の更新位置、l/rは0<=l<=r<=Nの整数境界。
    """

    def __init__(self, V, bits=60):
        """入力: Vは非負整数列、bitsは最大bit幅B、N=len(V)。構築O(N*B²)時間・O(N*B)空間。
        rank/max_xorも区間基底の取得を含めO(B² log(N+1))時間。 pは0..N-1の更新位置、l/rは0<=l<=r<=Nの整数境界。
        """
        assert bits >= 0
        self.bits = bits

        def op(x, y):
            if not x:
                return y
            if not y:
                return x
            basis = list(x)
            for v in y:
                for p in basis:
                    v = min(v, v ^ p)
                if v:
                    basis.append(v)
                    basis.sort(reverse=True)
            # 同じ部分空間を常に同じtupleにする。区間の分割方法に依存させない。
            for i in range(len(basis) - 1, -1, -1):
                for j in range(i):
                    basis[j] = min(basis[j], basis[j] ^ basis[i])
            return tuple(basis)

        super().__init__(V, op, ())

    def _leaf(self, p, x):
        assert 0 <= x < (1 << self.bits)
        return (x,) if x else ()

    def _value(self, s):
        return s[0] if s else 0

    def rank(self, l, r):
        """[l,r)のXOR線形基底の次元。表現できるXORは2**rank種類。
        N=len(V)、B=bitsとして時間O(B² log(N+1))、一時的な基底はO(B)個の整数。
        """
        return len(self.prod(l, r))

    def max_xor(self, l, r, x=0):
        """[l,r)から選ぶ部分集合のXORとxをXORした最大値。x>=0。
        N=len(V)、B=bitsとして時間O(B² log(N+1))、一時的な基底はO(B)個の整数。
        """
        assert x >= 0
        for v in self.prod(l, r):
            x = max(x, x ^ v)
        return x


class semigroup_segtree(_MonoidPreset):
    """semigroup_segtree(V,OP)。単位元を用意しにくい結合的演算をそのまま渡す。
    Noneを空区間の単位元として追加する。入力要素とOPの結果にNoneを使わない。
    prod(l,l)=None、それ以外は左からOPで畳み込んだ値。OPは非破壊的に実装する。
    入力: Vは各クラスに記載した値の初期列（要素数だけの整数は不可）。N=len(V)。
    構築O(N)時間・空間、set/prod/境界探索はO(log(N+1))、all_prodはO(1)。 getはO(1)。
     pは0..N-1の更新位置、l/rは0<=l<=r<=Nの整数境界。
    上記の時間は演算・写像・比較1回がO(1)の場合。OPや大きい整数のコストは別に掛ける。
    """

    def __init__(self, V, OP):
        """入力: Vは各クラスに記載した値の初期列（要素数だけの整数は不可）。N=len(V)。
        構築O(N)時間・空間、set/prod/境界探索はO(log(N+1))、all_prodはO(1)。 getはO(1)。
         pは0..N-1の更新位置、l/rは0<=l<=r<=Nの整数境界。
        """
        def op(x, y):
            if x is None:
                return y
            if y is None:
                return x
            return OP(x, y)

        super().__init__(V, op, None)

    def _leaf(self, p, x):
        assert x is not None
        return x
