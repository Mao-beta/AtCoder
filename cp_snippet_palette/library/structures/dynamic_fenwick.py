"""疎なFenwick Tree。出典: ABC324G。0-indexed・半開区間。
1D:O(log n)、2D:O(log h log w)。2Dも必要な辞書要素だけ確保する。
PyPy向け。Codonでは座標・累積値を64bit以内にする。

使い方（このファイルを解答の先頭に貼り付けてから実行）
    bit = DynamicFenwickTree(10**9)
    bit.add(100, 3)
    bit.sum(100, 101), bit.sum0(101), bit.lower_bound(3)  # => (3, 3, 100)
    grid = DynamicFenwickTree2D(1000, 1000)
    grid.add(2, 3, 7)
    grid.sum(2, 3, 3, 4), grid.sum0(3, 4)  # => (7, 7)
"""


class DynamicFenwickTree:
    """長さnの全要素0の配列に点加算・区間和。0-indexed、半開区間。
    触れたFenwickノードだけ辞書に保存するので巨大な座標範囲向け。各操作O(log n)。
    入力: Nは配列長の非負整数。構築O(1)時間・空間。pは0<=p<Nの添字、l/rは0<=l<=r<=Nの境界、xは加算量、wは累積和の閾値。
    追加空間は更新Q回でO(Q log(n+1))ノード以内。
    """
    def __init__(self, N):
        """入力: Nは配列長の非負整数。構築O(1)時間・空間。pは0<=p<Nの添字、l/rは0<=l<=r<=Nの境界、xは加算量、wは累積和の閾値。
        追加空間は更新Q回でO(Q log(N+1))ノード以内。
        """
        if N < 0:
            raise ValueError("negative size")
        self.n = N
        self.data = {}

    def add(self, p, x):
        """A[p]+=x。0<=p<n。負の加算も可能。戻り値なし。
        時間O(log(n+1))回の辞書操作（期待計算量）。探索の追加空間O(1)。
        """
        if not 0 <= p < self.n:
            raise IndexError(p)
        i = p + 1
        while i <= self.n:
            self.data[i] = self.data.get(i, 0) + x
            i += i & -i

    def sum0(self, r):
        """[0,r)の和。0<=r<=n。空なら0。
        時間O(log(n+1))回の辞書操作（期待計算量）。探索の追加空間O(1)。
        """
        if not 0 <= r <= self.n:
            raise IndexError(r)
        result = 0
        while r:
            result += self.data.get(r, 0)
            r -= r & -r
        return result

    def sum(self, l, r):
        """[l,r)の和。0<=l<=r<=n。
        時間O(log(n+1))回の辞書操作（期待計算量）。探索の追加空間O(1)。
        """
        if not 0 <= l <= r <= self.n:
            raise IndexError("invalid range")
        return self.sum0(r) - self.sum0(l)

    def lower_bound(self, w):
        """全要素非負を前提に、sum0(i+1)>=wとなる最小i。なければn。
        時間O(log(n+1))回の辞書操作（期待計算量）。探索の追加空間O(1)。
        """
        if w <= 0:
            return 0
        index = 0
        bit = 1 << max(0, self.n.bit_length() - 1)
        while bit:
            nxt = index + bit
            if nxt <= self.n and self.data.get(nxt, 0) < w:
                w -= self.data.get(nxt, 0)
                index = nxt
            bit >>= 1
        return index


class DynamicFenwickTree2D:
    """height行width列、全要素0の疎な二次元Fenwick Tree。
    座標は(row,col)、長方形は半開。必要な辞書要素のみ確保。各操作O(log H log W)。
    入力: height/widthは非負整数の行数H/列数W。構築O(1)時間・空間。
    row/colは0-indexed、top/bottomとleft/rightは行/列の半開境界、valueは加算する数値。
    """
    def __init__(self, height, width):
        """入力: height/widthは非負整数の行数H/列数W。構築O(1)時間・空間。
        row/colは0-indexed、top/bottomとleft/rightは行/列の半開境界、valueは加算する数値。
        """
        if height < 0 or width < 0:
            raise ValueError("negative size")
        self.height, self.width = height, width
        self.data = {}

    def add(self, row, col, value):
        """A[row][col]+=value。0<=row<height,0<=col<width。戻り値なし。
        時間O(log(H+1)*log(W+1))回の辞書操作。0<=top<=bottom<=H、0<=left<=right<=W。更新で必要な辞書ノードだけ確保する。
        """
        if not (0 <= row < self.height and 0 <= col < self.width):
            raise IndexError("invalid position")
        i = row + 1
        while i <= self.height:
            j = col + 1
            while j <= self.width:
                self.data[i, j] = self.data.get((i, j), 0) + value
                j += j & -j
            i += i & -i

    def sum0(self, bottom, right):
        """[0,bottom)×[0,right)の和。引数は行・列の順。
        時間O(log(H+1)*log(W+1))回の辞書操作。0<=top<=bottom<=H、0<=left<=right<=W。更新で必要な辞書ノードだけ確保する。
        """
        if not (0 <= bottom <= self.height and 0 <= right <= self.width):
            raise IndexError("invalid prefix")
        result = 0
        i = bottom
        while i:
            j = right
            while j:
                result += self.data.get((i, j), 0)
                j -= j & -j
            i -= i & -i
        return result

    def sum(self, top, left, bottom, right):
        """[top,bottom)×[left,right)の和。引数は行・列・行・列。空なら0。
        時間O(log(H+1)*log(W+1))回の辞書操作。0<=top<=bottom<=H、0<=left<=right<=W。更新で必要な辞書ノードだけ確保する。
        """
        if not (0 <= top <= bottom <= self.height and 0 <= left <= right <= self.width):
            raise IndexError("invalid rectangle")
        return (
            self.sum0(bottom, right)
            - self.sum0(top, right)
            - self.sum0(bottom, left)
            + self.sum0(top, left)
        )
