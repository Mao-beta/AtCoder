"""XOR差分を管理するDSU。追加制約の矛盾判定・成分ごとの最小和割当。
0-indexed、XOR値は非負整数。mergeはACL同様に統合後の代表元を返す。
非再帰・標準Python。Codonコンパイル未確認。

使い方（このファイル全体を貼り付けてから実行）
    uf = XorDSU(3)
    uf.merge(0, 1, 3)  # A[0]^A[1]=3
    uf.merge(0, 2, 4)
    uf.diff(1, 2), uf.same(0, 2), uf.size(1)  # => (7, True, 3)
    uf.is_consistent(1, 2, 5)  # => False
    uf.minimum_sum_values()  # => [0, 3, 4]
"""


class XorDSU:
    """XorDSU(n)。leader/same/merge/size/groupsとXOR用のdiff/potentialを用意。
    merge(a,b,w)はA[a]^A[b]=wを追加。矛盾はValueErrorで、矛盾する制約は採用しない。
    入力: nは非負整数の頂点数N。構築O(N)時間・空間。a/bは0..N-1の頂点番号、wは非負整数のXOR差。α(N)は逆Ackermann関数、実用上ほぼ定数。
    """

    def __init__(self, n):
        """入力: nは非負整数の頂点数N。構築O(N)時間・空間。a/bは0..N-1の頂点番号、wは非負整数のXOR差。α(N)は逆Ackermann関数、実用上ほぼ定数。
        """
        assert n >= 0
        self.n = n
        self._parent = [-1] * n
        self._xor = [0] * n

    def leader(self, a):
        """代表元。経路圧縮込み、償却O(α(N))。"""
        assert 0 <= a < self.n
        path, v = [], a
        while self._parent[v] >= 0:
            path.append(v)
            v = self._parent[v]
        value = 0
        for w in reversed(path):
            value ^= self._xor[w]
            self._xor[w] = value
            self._parent[w] = v
        return v

    def potential(self, a):
        """A[a]^A[leader(a)]。根の値を0とした割当。償却O(α(N))。"""
        self.leader(a)
        return self._xor[a]

    def same(self, a, b):
        """a,bが同じ成分か。償却O(α(N))。"""
        return self.leader(a) == self.leader(b)

    def size(self, a):
        """aの成分の頂点数。償却O(α(N))。"""
        return -self._parent[self.leader(a)]

    def diff(self, a, b):
        """A[a]^A[b]。未連結はValueError。償却O(α(N))。"""
        if not self.same(a, b):
            raise ValueError("vertices are not connected")
        return self._xor[a] ^ self._xor[b]

    def is_consistent(self, a, b, w):
        """追加制約A[a]^A[b]=wが矛盾しないか。成分は統合しない。
        償却O(α(N))時間、経路圧縮用の追加空間O(log(N+1))以内。
        """
        assert w >= 0
        return not self.same(a, b) or self._xor[a] ^ self._xor[b] == w

    def merge(self, a, b, w):
        """制約を追加し統合後の代表元を返す。矛盾はValueError。償却O(α(N))。"""
        assert w >= 0
        x, y = self.leader(a), self.leader(b)
        delta = self._xor[a] ^ self._xor[b] ^ w
        if x == y:
            if delta:
                raise ValueError("inconsistent XOR constraint")
            return x
        if self._parent[x] > self._parent[y]:
            x, y = y, x
        self._parent[x] += self._parent[y]
        self._parent[y] = x
        self._xor[y] = delta
        return x

    def groups(self):
        """成分ごとの頂点list。O(N α(N))。"""
        groups = {}
        for v in range(self.n):
            groups.setdefault(self.leader(v), []).append(v)
        return list(groups.values())

    def minimum_sum_values(self):
        """全制約を満たす非負整数列で総和が最小のものを1つ返す。O(N*(α(N)+B))。
        BはXOR値の最大ビット長。各成分・各bitで1が少ない向きを選ぶ。
        同数なら根のbitを0にする。過去に拒否した矛盾制約は考慮しない。
        """
        result = [0] * self.n
        for vertices in self.groups():
            bits = max((self._xor[v] for v in vertices), default=0).bit_length()
            shift = 0
            for bit in range(bits):
                ones = sum(self._xor[v] >> bit & 1 for v in vertices)
                if 2 * ones > len(vertices):
                    shift |= 1 << bit
            for v in vertices:
                result[v] = self._xor[v] ^ shift
        return result
