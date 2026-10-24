"""行列積・累乗。出典: _test.py, ABC358G。

入力は変更しない。通常の積O(nmk)、正方行列累乗O(n^3 log exponent)。
mod=0は剰余なし。Codonでは乗算・加算の途中も64bit以内に収める。

使い方（このファイルを解答の先頭に貼り付けてから実行）
    matrix_multiply([[1, 2]], [[3], [4]])  # => [[11]]
    matrix_power([[1, 1], [1, 0]], 5, 998244353)  # => [[8, 5], [5, 3]]
    max_plus_multiply([[1, 2]], [[3], [4]])  # => [[6]]
    max_plus_power([[0, 3], [2, 0]], 2)  # => [[5, 3], [2, 5]]
"""


def matrix_multiply(a, b, mod=0):
    """a(n×k), b(k×m)の積を新しい二次元listで返す。形が合わないとValueError。
    mod=0は整数のまま、mod>0は各要素を剰余にする。O(nkm)。
    入力: a,bは数値の二次元list（行ごと）。n=len(a)、kはaの列数=bの行数、mはbの列数。出力の空間O(nm)。
    """
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
    """正方行列aの非負整数exponent乗。0乗は単位行列。
    mod=0は剰余なし、mod>0は剰余。入力非破壊、O(n^3 log exponent)。
    入力: aはN×Nの数値行列を行ごとに並べた二次元list、exponentは非負整数K。N=len(a)。時間O(N³*(1+log(K+1)))、作業空間O(N²)。
    """
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
    """c[i][j]=max_t(a[i][t]+b[t][j])を返す。a(n×k),b(k×m)。
    到達不能はneg_inf。全有限値より小さく、計算結果と一致しない番兵を指定する。
    通常の行列積と違い、積が加算、和がmax。O(nkm)、入力非破壊。
    入力: a,bは数値の二次元list（行ごと）。n=len(a)、kはaの列数=bの行数、mはbの列数。出力の空間O(nm)。
    """
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
    """max-plus積で正方行列aをexponent回掛ける。exponent>=0。
    a[u][v]が辺の得点なら、結果[u][v]はちょうどexponent辺での最大得点。
    0乗は対角0・他neg_inf。到達不能の番兵はmax_plus_multiplyと同じ。
    入力: aはN×Nの数値行列を行ごとに並べた二次元list、exponentは非負整数K。N=len(a)。時間O(N³*(1+log(K+1)))、作業空間O(N²)。
    """
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
