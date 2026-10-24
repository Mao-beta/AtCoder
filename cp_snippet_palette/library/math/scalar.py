"""Modint・有理数。出典: _Fractions.py, _test.py。
PyPy向け。ループ内では通常のintと%の方が軽い。正確な有理数は標準Fractionを利用。
CodonでのFractionや動的な演算子ディスパッチは未対応扱い。

使い方（このファイルを解答の先頭に貼り付けてから実行）
    with ModContext(7):
        x = Modint(10)
        result = ((x + 5).val(), (x / 2).val(), x.inv().val(), raw(6).val())
    result  # => (1, 5, 5, 6)
    Fraction(1, 3) + Fraction(1, 6)  # 有理数は標準ライブラリを利用
    # => Fraction(1, 2)
"""

from fractions import Fraction


class ModContext:
    """with ModContext(mod): で法を指定する。shakayami/ACL-for-pythonの対象外。
    入力: modは正整数の法。構築O(1)時間・空間、withの出入りは償却O(1)。
    """

    context = []

    def __init__(self, mod):
        """入力: modは正整数の法。構築O(1)時間・空間、withの出入りは償却O(1)。
        """
        if mod < 1:
            raise ValueError("mod must be positive")
        self.mod = mod

    def __enter__(self):
        self.context.append(self.mod)

    def __exit__(self, exc_type, exc_value, traceback):
        self.context.pop()

    @classmethod
    def get_mod(cls):
        """最も内側のwith ModContext(mod)の法を返す。with外ならRuntimeError。
        時間・追加空間O(1)回の整数演算。
        """
        if not cls.context:
            raise RuntimeError("use with ModContext(mod)")
        return cls.context[-1]


class Modint:
    """with ModContext(mod)内でModint(v)を構築する。vは整数、既定0。
    +,-,*,/,**に対応。/は逆元を掛ける剰余除算。
    val()/int(x)で代表値、mod()で法、inv()で逆元、x**nで非負整数乗を取得。
    同じ法のModintとintを演算可能。法が違う値同士はValueError。
    入力: vは整数の初期値、法は現在のModContextから取得する。構築O(1)回の整数演算・空間。
    四則の加減乗算O(1)、逆元・除算O(log mod)、n乗O(log(n+1))回の整数演算。
    """

    def __init__(self, v=0):
        """入力: vは整数の初期値、法は現在のModContextから取得する。構築O(1)回の整数演算・空間。
        四則の加減乗算O(1)、逆元・除算O(log mod)、n乗O(log(n+1))回の整数演算。
        """
        self._mod = ModContext.get_mod()
        self.value = int(v) % self._mod

    def val(self):
        """0<=value<modの整数の代表値を返す。int(x)と同じ。
        時間・追加空間O(1)回の整数演算。
        """
        return self.value

    def mod(self):
        """この値が構築された際の法をintで返す。現在のModContextには依存しない。
        時間・追加空間O(1)回の整数演算。
        """
        return self._mod

    def _new(self, value):
        result = object.__new__(type(self))
        result._mod = self._mod
        result.value = value % self._mod
        return result

    def __int__(self):
        return self.value

    def __repr__(self):
        return "{}({}, mod={})".format(type(self).__name__, self.value, self._mod)

    def _value(self, other):
        if isinstance(other, Modint):
            if self._mod != other._mod:
                raise ValueError("different moduli")
            return other.value
        return int(other) % self._mod

    def __add__(self, other):
        return self._new(self.value + self._value(other))

    __radd__ = __add__

    def __sub__(self, other):
        return self._new(self.value - self._value(other))

    def __rsub__(self, other):
        return self._new(self._value(other) - self.value)

    def __mul__(self, other):
        return self._new(self.value * self._value(other))

    __rmul__ = __mul__

    def __neg__(self):
        return self._new(-self.value)

    def inv(self):
        """合成数modでも互いに素なら可。なければValueError。
        引数なし。時間O(log mod)回の整数演算、追加空間O(1)個の整数。modはこの値の法。
        """
        return self._new(pow(self.value, -1, self._mod))

    def __truediv__(self, other):
        return self * self._new(self._value(other)).inv()

    def __rtruediv__(self, other):
        return self.inv() * other

    def __pow__(self, exponent):
        if exponent < 0:
            raise ValueError("nonnegative exponent required")
        return self._new(pow(self.value, exponent, self._mod))

    def __eq__(self, other):
        if isinstance(other, Modint):
            return self._mod == other._mod and self.value == other.value
        return self.value == self._value(other)



def raw(v):
    """現在のModContextの法で、代表値vを持つModintを返す。
    独自API。with内で使い、0<=v<modを呼び出し側で保証する。
    時間・追加空間O(1)回の整数演算。
    """
    result = Modint()
    assert 0 <= v < result.mod()
    result.value = v
    return result
