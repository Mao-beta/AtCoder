"""非負整数の多重集合。出典: _Binary_Trie.py。

必要分だけノードを確保。add/discard/count/kth/min_xorはO(bit幅)。kthは0-indexed。
PyPy向け。Codonではbits<=63。削除ノードは再利用するが領域は縮めない。

使い方（このファイルを解答の先頭に貼り付けてから実行）
    trie = BinaryTrie(bits=4)
    trie.add(3); trie.add(3); trie.add(7)
    trie.count(3), trie.kth(1), trie.count_less(7), trie.min_xor(6)  # => (2, 3, 2, 1)
    trie.discard(3), len(trie)  # => (True, 2)
"""


class BinaryTrie:
    """0<=value<2**bitsの整数の多重集合。BinaryTrie(bits=30)は空。
    重複を含む個数はlen(trie)。各操作O(bits)、ノードは必要時に確保する。
    bitsは最大値.bit_length()以上を指定。kthの順位は0-indexed。
    入力: bitsは正の整数の固定bit幅B。構築O(1)時間・空間。value/xorは0<=値<2**Bの整数（count_lessの閾値だけ範囲外可）。
    kは0-indexed順位。Q回追加したとき確保ノード数はO(QB)以内で、削除しても配列領域は縮まらない。
    """
    def __init__(self, bits=30):
        """入力: bitsは正の整数の固定bit幅B。構築O(1)時間・空間。value/xorは0<=値<2**Bの整数（count_lessの閾値だけ範囲外可）。
        kは0-indexed順位。Q回追加したとき確保ノード数はO(QB)以内で、削除しても配列領域は縮まらない。
        """
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
        """valueを1個追加する。範囲外はValueError。戻り値なし。
        時間O(B)、探索の補助空間O(B)以内。Bは構築時のbits。
        """
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
        """valueの個数を返す。未登録なら0、ビット幅の範囲外はValueError。
        時間O(B)、探索の補助空間O(B)以内。Bは構築時のbits。
        """
        self._check(value)
        u = 0
        for bit in range(self.bits - 1, -1, -1):
            u = self.children[u][(value >> bit) & 1]
            if u == -1:
                return 0
        return self.counts[u]

    def discard(self, value):
        """valueを1個削除できたらTrue、なければFalse。範囲外はValueError。
        時間O(B)、探索の補助空間O(B)以内。Bは構築時のbits。
        """
        if not self.count(value):
            return False
        u = 0
        self.counts[u] -= 1
        for bit in range(self.bits - 1, -1, -1):
            u = self.children[u][(value >> bit) & 1]
            self.counts[u] -= 1
        return True

    def kth(self, k, xor=0):
        """各要素aをa^xorへ変換して並べたときの0-indexedのk番目の値。
        元の要素ではなくXOR後の値を返す。元の要素は戻り値^xor。範囲外kはIndexError。
        時間O(B)、探索の補助空間O(B)以内。Bは構築時のbits。
        """
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
        """min(a^value)の値を返す。相手の要素が欲しければ戻り値^value。
        空集合はIndexError。valueは指定ビット幅内。
        時間O(B)、探索の補助空間O(B)以内。Bは構築時のbits。
        """
        return self.kth(0, value)

    def count_less(self, value):
        """value未満の要素数。重複も数える。valueがビット幅の外でも問い合わせ可能。
        時間O(B)、探索の補助空間O(B)以内。Bは構築時のbits。
        """
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
