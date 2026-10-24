"""部分集合変換・XOR畳み込み・GF(2)掃き出し・XOR基底。

出典: _Fractions.py, PAST012O, yuki_0074。XOR畳み込みと解空間の基底を追加。

整数bitsetの任意精度を使うためPyPy向け。Codonは符号bitを除く63bitまで。

使い方（このファイルを解答の先頭に貼り付けてから実行）
    subset_zeta([1, 2, 3, 4])  # => [1, 3, 4, 10]
    subset_zeta([1, 3, 4, 10], inverse=True)  # => [1, 2, 3, 4]
    basis = xor_basis([3, 5, 6])
    xor_maximum(basis), xor_minimax([0, 2])  # => (6, 2)

rowsのbit jは変数x_jの係数。下の式はx0 XOR x1 = 1。
    solve_gf2([0b11], [1], 2)  # => (1, 1)
    particular, basis = linear_equations_gf2([0b11], [1], 2)
    sorted([particular, particular ^ basis[0]])  # => [1, 2]
    walsh_hadamard([1, 2]), walsh_hadamard([3, 998244352], inverse=True)  # => ([3, 998244352], [1, 2])
    xor_convolution([1, 2], [3, 4])  # => [11, 10]
    and_convolution([1, 2], [3, 4])  # => [13, 8]
"""


def and_convolution(a, b, mod=998244353):
    """c[k]=sum(a[i]*b[j] for i&j==k)を返す。等長・長さ2^mの列を渡す。
    O(m*2^m)、入力非破壊。mod=0なら整数で計算。空列は[]。
    例: and_convolution([1,2],[3,4])は[13,8]。
    a/bは同じ長さN=2^kの整数係数list。添字がbit集合を表す。追加空間O(N)。
    """
    n = len(a)
    if len(b) != n or n & (n - 1) or mod < 0:
        raise ValueError("equal power-of-two lengths and nonnegative mod required")
    a, b = list(a), list(b)
    step = 1
    while step < n:
        for start in range(0, n, step * 2):
            for i in range(start, start + step):
                a[i] += a[i + step]
                b[i] += b[i + step]
                if mod:
                    a[i] %= mod
                    b[i] %= mod
        step *= 2
    c = [x * y % mod if mod else x * y for x, y in zip(a, b)]
    step = 1
    while step < n:
        for start in range(0, n, step * 2):
            for i in range(start, start + step):
                c[i] -= c[i + step]
                if mod:
                    c[i] %= mod
        step *= 2
    return c


def subset_zeta(values, inverse=False, mod=0):
    """values[mask]を部分集合上で合計したlistを返す。長さは2^k。
    結果[S]=sum(values[T] for T subset S)。inverse=Trueは逆のメビウス変換。
    mod=0は剰余なし、正なら剰余。入力非破壊、O(k*2^k)。
    valuesは長さN=2^kの整数列、inverseは逆変換を行うかのbool。追加空間O(N)。
    """
    n = len(values)
    if n == 0 or n & (n - 1) or mod < 0:
        raise ValueError("power-of-two length and nonnegative mod required")
    result = [x % mod for x in values] if mod else list(values)
    step = 1
    while step < n:
        for start in range(0, n, 2 * step):
            for i in range(start + step, start + 2 * step):
                result[i] += -result[i - step] if inverse else result[i - step]
                if mod:
                    result[i] %= mod
        step *= 2
    return result


def xor_basis(values):
    """非負整数のXOR基底を最上位bitの降順で返す。O(n*bit幅)。
    valuesは非負整数の列、n=len(values)、Bは最大値のbit長。O(nB)回のBbit整数演算。
    """
    basis = {}
    for value in values:
        if value < 0:
            raise ValueError("nonnegative integers required")
        while value:
            bit = value.bit_length() - 1
            if bit in basis:
                value ^= basis[bit]
            else:
                basis[bit] = value
                break
    return [basis[bit] for bit in sorted(basis, reverse=True)]


def xor_maximum(basis, initial=0):
    """xor_basisで作った基底から任意個を選び、initialとXORした値を最大化する。
    basisは最上位bitの降順。initial>=0。戻り値は最大値（選び方は返さない）。
    basisは非負整数の基底列。R=len(basis)、Bは値とinitialの最大bit長。時間O(R)回のBbit演算、追加空間O(B)bit。
    """
    result = initial
    for value in basis:
        result = max(result, result ^ value)
    return result


def xor_minimax(values):
    """min_x max(a^x)。非負整数列。O(n*bit幅)、再帰深さはbit幅。
    valuesは非負整数の列、n=len(values)、Bは最大値のbit長。O(nB)回のBbit整数演算。
    """
    if not values:
        return 0
    if any(x < 0 for x in values):
        raise ValueError("nonnegative integers required")

    def solve(a, bit):
        if bit < 0 or not a:
            return 0
        left = [x for x in a if not (x >> bit) & 1]
        right = [x for x in a if (x >> bit) & 1]
        if not left:
            return solve(right, bit - 1)
        if not right:
            return solve(left, bit - 1)
        return (1 << bit) + min(solve(left, bit - 1), solve(right, bit - 1))

    return solve(list(values), max(values).bit_length() - 1)


def _gf2_rref(rows, rhs, variables):
    if variables < 0 or len(rows) != len(rhs):
        raise ValueError("invalid dimensions")
    if any(x < 0 or x >> variables for x in rows) or any(b not in (0, 1) for b in rhs):
        raise ValueError("invalid binary coefficients")
    a = [row | (b << variables) for row, b in zip(rows, rhs)]
    pivots = []
    rank = 0
    for column in range(variables):
        pivot = next((i for i in range(rank, len(a)) if (a[i] >> column) & 1), -1)
        if pivot == -1:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        for i in range(len(a)):
            if i != rank and (a[i] >> column) & 1:
                a[i] ^= a[rank]
        pivots.append(column)
        rank += 1
    return a, pivots


def solve_gf2(rows, rhs, variables):
    """Ax=b。rowsは各行の係数bitset。戻り値(rank, 一つの解bitset)。矛盾があればNone。
    O(m*n)個の整数XOR。自由変数を0にした解を返す。入力を変更しない。
    入力: rowsは非負整数の列でbit jが変数x_jの係数、rhsは同じ長さの0/1定数列。variables=nは変数数、m=len(rows)は式数。
    0<=rows[i]<2**n。消去はO(m*n)回の(n+1)bit整数演算で、係数の作業領域O(m*ceil((n+1)/w))ワード。wは内部ワード幅。
    """
    a, pivots = _gf2_rref(rows, rhs, variables)
    rank = len(pivots)
    mask = (1 << variables) - 1
    if any((row & mask) == 0 and (row >> variables) for row in a):
        return None
    answer = 0
    for i, column in enumerate(pivots):
        if (a[i] >> variables) & 1:
            answer |= 1 << column
    return rank, answer


def linear_equations_gf2(rows, rhs, variables):
    """GF(2)のAx=bを解き、(特解bitset, 同次解の基底bitsetのリスト)を返す。
    解なしNone。bit jが変数j。全解は特解と基底の任意部分集合のXOR。
    入力非破壊。掃き出しはO(行数*変数数)個の整数XOR、基底復元はO(変数数^2)。
    入力: rowsは非負整数の列でbit jが変数x_jの係数、rhsは同じ長さの0/1定数列。variables=nは変数数、m=len(rows)は式数。
    0<=rows[i]<2**n。消去はO(m*n)回の(n+1)bit整数演算で、係数の作業領域O(m*ceil((n+1)/w))ワード。wは内部ワード幅。
    """
    a, pivots = _gf2_rref(rows, rhs, variables)
    rank = len(pivots)
    if any(row >> variables for row in a[rank:]):
        return None
    solution = 0
    for i, column in enumerate(pivots):
        if a[i] >> variables:
            solution |= 1 << column
    pivot_set = set(pivots)
    basis = []
    for free in range(variables):
        if free in pivot_set:
            continue
        vector = 1 << free
        for i, column in enumerate(pivots):
            if a[i] >> free & 1:
                vector |= 1 << column
        basis.append(vector)
    return solution, basis


def walsh_hadamard(values, inverse=False, mod=998244353):
    """長さ2^kのXOR変換（FWHT）。入力非破壊、時間O(n log n)、空間O(n)。
    modは1より大きい奇数。inverse=Trueは逆変換。素数でなくてもよい。
    valuesは長さN=2^kの整数列、n=N。inverseは逆変換を行うかのbool。
    """
    n = len(values)
    if n == 0 or n & (n - 1) or mod <= 1 or mod % 2 == 0:
        raise ValueError("power-of-two length and odd modulus > 1 required")
    result = [x % mod for x in values]
    half = 1
    while half < n:
        for start in range(0, n, half * 2):
            for i in range(start, start + half):
                x, y = result[i], result[i + half]
                total, difference = x + y, x - y
                result[i] = total - mod if total >= mod else total
                result[i + half] = difference + mod if difference < 0 else difference
        half *= 2
    if inverse:
        scale = pow(n, -1, mod)
        result = [x * scale % mod for x in result]
    return result


def xor_convolution(a, b, mod=998244353):
    """c[k]=sum(a[i]*b[j] for i^j==k) mod mod。等長・長さ2^k、奇数mod。
    時間O(n log n)、空間O(n)。入力を変更しない。
    a/bは同じ長さN=2^kの整数係数list。添字がbit集合を表す。追加空間O(N)。
    """
    if len(a) != len(b):
        raise ValueError("equal lengths required")
    fa = walsh_hadamard(a, mod=mod)
    fb = walsh_hadamard(b, mod=mod)
    product = [x * y % mod for x, y in zip(fa, fb)]
    return walsh_hadamard(product, inverse=True, mod=mod)
