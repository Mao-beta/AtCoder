"""行列積・累乗。出典: _test.py, ABC358G。
入力は変更しない。通常の積O(nmk)、正方行列累乗O(n^3 log exponent)。
mod=0は剰余なし。Codonでは乗算・加算の途中も64bit以内に収める。
"""


def matrix_multiply(a, b, mod=0):
    if mod < 0:
        raise ValueError("mod must be nonnegative")
    if not a:
        return []
    k = len(b)
    m = len(b[0]) if b else 0
    if any(len(row) != k for row in a) or any(len(row) != m for row in b):
        raise ValueError("incompatible matrix shapes")
    result = [[0] * m for _ in a]
    for i, row in enumerate(a):
        for t, x in enumerate(row):
            if mod:
                x %= mod
            if x == 0:
                continue
            for j, y in enumerate(b[t]):
                if mod:
                    result[i][j] = (result[i][j] + x * (y % mod)) % mod
                else:
                    result[i][j] += x * y
    return result


def matrix_power(a, exponent, mod=0):
    n = len(a)
    if exponent < 0 or mod < 0 or any(len(row) != n for row in a):
        raise ValueError("nonnegative exponent/mod and square matrix required")
    result = [[int(i == j) for j in range(n)] for i in range(n)]
    base = [row[:] for row in a]
    if mod:
        result = [[x % mod for x in row] for row in result]
    while exponent:
        if exponent & 1:
            result = matrix_multiply(result, base, mod)
        exponent >>= 1
        if exponent:
            base = matrix_multiply(base, base, mod)
    return result


def max_plus_multiply(a, b, neg_inf=-(1 << 60)):
    """max-plus積。neg_infは有限値の下限より小さい番兵を指定する。"""
    if not a:
        return []
    k = len(b)
    m = len(b[0]) if b else 0
    if any(len(row) != k for row in a) or any(len(row) != m for row in b):
        raise ValueError("incompatible matrix shapes")
    result = [[neg_inf] * m for _ in a]
    for i, row in enumerate(a):
        for t, x in enumerate(row):
            if x == neg_inf:
                continue
            for j, y in enumerate(b[t]):
                if y != neg_inf:
                    result[i][j] = max(result[i][j], x + y)
    return result


def max_plus_power(a, exponent, neg_inf=-(1 << 60)):
    n = len(a)
    if exponent < 0 or any(len(row) != n for row in a):
        raise ValueError("square matrix and nonnegative exponent required")
    result = [[0 if i == j else neg_inf for j in range(n)] for i in range(n)]
    base = [row[:] for row in a]
    while exponent:
        if exponent & 1:
            result = max_plus_multiply(result, base, neg_inf)
        exponent >>= 1
        if exponent:
            base = max_plus_multiply(base, base, neg_inf)
    return result
