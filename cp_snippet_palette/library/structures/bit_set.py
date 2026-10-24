"""固定幅bit集合。出典: _BitSet.pyの用途をPython整数で整理。
PyPy専用。64bitを超える幅はCodonの通常intでは表せない。

演算量は整数の内部ワード数に比例。座標は0-indexed。

使い方（このファイルを解答の先頭に貼り付けてから実行）
    b = BitSet(5, 0b00101)
    b.set(1)
    b[2], b.count(), list(b.indices()), b.shifted(2).bits  # => (1, 3, [0, 1, 2], 28)
"""


class BitSet:
    """sizeビットの固定幅集合。valueの下位sizeビットで初期化（既定0）。
    b[i]で0/1を取得、setで変更。bits属性は整数bitset。PyPyの任意精度int向け。
    入力: sizeは非負整数の幅B、valueは初期bit列を表す整数。
    構築はO(ceil((B+value.bit_length())/w))程度、保持領域O(ceil(B/w))ワード。wは多倍長整数の内部ワード幅。
    """
    def __init__(self, size, value=0):
        """入力: sizeは非負整数の幅B、valueは初期bit列を表す整数。
        構築はO(ceil((B+value.bit_length())/w))程度、保持領域O(ceil(B/w))ワード。wは多倍長整数の内部ワード幅。
        """
        if size < 0:
            raise ValueError("negative size")
        self.size = size
        self.mask = (1 << size) - 1
        self.bits = value & self.mask

    def __getitem__(self, index):
        if not 0 <= index < self.size:
            raise IndexError(index)
        return (self.bits >> index) & 1

    def set(self, index, value=True):
        """0<=index<sizeのビットをbool(value)へ変更。戻り値なし、範囲外IndexError。
        時間O(ceil((size+1)/w))以内、演算で一時的に同程度の整数領域を使う。
        """
        if not 0 <= index < self.size:
            raise IndexError(index)
        if value:
            self.bits |= 1 << index
        else:
            self.bits &= ~(1 << index)

    def count(self):
        """1のビット数を返す。整数のbit_countを使用。
        時間O(ceil((size+1)/w))以内、演算で一時的に同程度の整数領域を使う。
        """
        return self.bits.bit_count()

    def shifted(self, amount):
        """amount>=0で左、負なら右へずらした新しいBitSet。幅を超えたビットは捨てる。
        amountは符号付き整数の移動幅。左へ大きくずらしてから幅を切るため、時間・一時空間はO(ceil((size+max(amount,0)+1)/w))以内。
        """
        value = self.bits << amount if amount >= 0 else self.bits >> -amount
        return BitSet(self.size, value)

    def indices(self):
        """1になっている位置を昇順にyieldする。リストが必要ならlist(b.indices())。
        1の個数をKとして全列挙はO(K*ceil((size+1)/w))以内、追加空間O(ceil((size+1)/w))ワード。
        """
        value = self.bits
        while value:
            bit = value & -value
            yield bit.bit_length() - 1
            value ^= bit
