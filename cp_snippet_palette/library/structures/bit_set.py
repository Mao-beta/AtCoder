"""固定幅bit集合。出典: _BitSet.pyの用途をPython整数で整理。
PyPy専用。64bitを超える幅はCodonの通常intでは表せない。
演算量は整数の内部ワード数に比例。座標は0-indexed。
"""


class BitSet:
    def __init__(self, size, value=0):
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
        if not 0 <= index < self.size:
            raise IndexError(index)
        if value:
            self.bits |= 1 << index
        else:
            self.bits &= ~(1 << index)

    def count(self):
        return self.bits.bit_count()

    def shifted(self, amount):
        value = self.bits << amount if amount >= 0 else self.bits >> -amount
        return BitSet(self.size, value)

    def indices(self):
        value = self.bits
        while value:
            bit = value & -value
            yield bit.bit_length() - 1
            value ^= bit
