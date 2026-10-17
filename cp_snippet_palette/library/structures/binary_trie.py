"""非負整数の多重集合。出典: _Binary_Trie.py。
必要分だけノードを確保。add/discard/count/kth/min_xorはO(bit幅)。kthは0-indexed。
PyPy向け。Codonではbits<=63。削除ノードは再利用するが領域は縮めない。
"""


class BinaryTrie:
    def __init__(self, bits=30):
        if bits <= 0:
            raise ValueError("bits must be positive")
        self.bits = bits
        self.children = [[-1, -1]]
        self.counts = [0]

    def __len__(self):
        return self.counts[0]

    def _check(self, value):
        if value < 0 or value >> self.bits:
            raise ValueError("value outside bit width")

    def add(self, value):
        self._check(value)
        u = 0
        self.counts[0] += 1
        for bit in range(self.bits - 1, -1, -1):
            side = (value >> bit) & 1
            if self.children[u][side] == -1:
                self.children[u][side] = len(self.counts)
                self.children.append([-1, -1])
                self.counts.append(0)
            u = self.children[u][side]
            self.counts[u] += 1

    def count(self, value):
        self._check(value)
        u = 0
        for bit in range(self.bits - 1, -1, -1):
            u = self.children[u][(value >> bit) & 1]
            if u == -1:
                return 0
        return self.counts[u]

    def discard(self, value):
        if not self.count(value):
            return False
        u = 0
        self.counts[u] -= 1
        for bit in range(self.bits - 1, -1, -1):
            u = self.children[u][(value >> bit) & 1]
            self.counts[u] -= 1
        return True

    def kth(self, k, xor=0):
        """各要素にxorを取った値のうち、小さい方からk番目の値を返す。"""
        self._check(xor)
        if not 0 <= k < len(self):
            raise IndexError(k)
        u, answer = 0, 0
        for bit in range(self.bits - 1, -1, -1):
            side = (xor >> bit) & 1
            child = self.children[u][side]
            count = 0 if child == -1 else self.counts[child]
            if k >= count:
                k -= count
                side ^= 1
                answer |= 1 << bit
            u = self.children[u][side]
        return answer

    def min_xor(self, value):
        return self.kth(0, value)

    def count_less(self, value):
        if value <= 0:
            return 0
        if value >> self.bits:
            return len(self)
        u, answer = 0, 0
        for bit in range(self.bits - 1, -1, -1):
            side = (value >> bit) & 1
            left = self.children[u][0]
            if side and left != -1:
                answer += self.counts[left]
            u = self.children[u][side]
            if u == -1:
                break
        return answer
