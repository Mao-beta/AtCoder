"""ModInt・有理数。出典: _Fractions.py, _test.py。
PyPy向け。ループ内では通常のintと%の方が軽い。正確な有理数は標準Fractionを利用。
CodonでのFractionや動的な演算子ディスパッチは未対応扱い。
"""

from fractions import Fraction


class ModContext:
    """ACL Python版と同じ with ModContext(mod): で法を指定する。"""

    context = []

    def __init__(self, mod):
        if mod < 1:
            raise ValueError("mod must be positive")
        self.mod = mod

    def __enter__(self):
        self.context.append(self.mod)

    def __exit__(self, exc_type, exc_value, traceback):
        self.context.pop()

    @classmethod
    def get_mod(cls):
        if not cls.context:
            raise RuntimeError("use with ModContext(mod)")
        return cls.context[-1]


class Modint:
    """ACL Python版のModint(v=0)。val(), mod(), inv(), **, //を使える。

    C++ ACLのpow(n)とPythonの/も追加で対応。演算は新しい値を返す。
    """

    def __init__(self, v=0):
        self._mod = ModContext.get_mod()
        self.value = int(v) % self._mod

    def val(self):
        return self.value

    def mod(self):
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

    def inverse(self):
        """合成数modでも互いに素なら可。なければValueError。"""
        return self._new(pow(self.value, -1, self._mod))

    def __truediv__(self, other):
        return self * self._new(self._value(other)).inv()

    def __rtruediv__(self, other):
        return self.inverse() * other

    def __pow__(self, exponent):
        if exponent < 0:
            raise ValueError("nonnegative exponent required")
        return self._new(pow(self.value, exponent, self._mod))

    def __eq__(self, other):
        if isinstance(other, Modint):
            return self._mod == other._mod and self.value == other.value
        return self.value == self._value(other)

    inv = inverse
    pow = __pow__
    __floordiv__ = __truediv__
    __rfloordiv__ = __rtruediv__


def raw(v):
    """ACL Python版。0<=v<modであることを呼び出し側で保証する。"""
    result = Modint()
    assert 0 <= v < result.mod()
    result.value = v
    return result


class ModInt(Modint):
    """旧コンストラクタModInt(value, mod)の互換用。法の取得はmod()。"""

    def __init__(self, value=0, mod=998244353):
        if mod < 1:
            raise ValueError("mod must be positive")
        self._mod = mod
        self.value = int(value) % mod
