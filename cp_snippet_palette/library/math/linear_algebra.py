"""素数mod上の行列式・階数・逆行列・連立一次方程式。入力非破壊。
正方行列はO(n^3)、矩形n*mの掃き出しはO(n*m*min(n,m))、空間O(n*m)。
連立方程式の基底出力には、別途O(m*(m-rank))の時間・空間が必要。
法は素数（既定998244353）を渡す。素数判定はしない。任意modの行列式には使えない。
PyPy向け。Codon未確認。mod<2^31なら乗算・減算の1段の中間値は符号付き64bit内。
"""


def _copy_matrix(a, mod, columns=None):
    if mod < 2:
        raise ValueError("prime modulus required")
    if columns is None:
        columns = len(a[0]) if a else 0
    if columns < 0 or any(len(row) != columns for row in a):
        raise ValueError("invalid matrix shape")
    return [[x % mod for x in row] for row in a], columns


def _eliminate(a, columns, mod, reduced=False):
    """aを変更。正規化したピボット列と、行交換の符号込みの積を返す。"""
    pivots = []
    determinant = 1
    rows = len(a)
    width = len(a[0]) if a else columns
    for column in range(columns):
        rank = len(pivots)
        pivot = next((i for i in range(rank, rows) if a[i][column]), -1)
        if pivot == -1:
            continue
        if pivot != rank:
            a[rank], a[pivot] = a[pivot], a[rank]
            determinant = -determinant
        pivot_row = a[rank]
        value = pivot_row[column]
        determinant = determinant * value % mod
        inv = pow(value, mod - 2, mod)
        pivot_row[column] = 1
        for j in range(column + 1, width):
            pivot_row[j] = pivot_row[j] * inv % mod
        for i in range(0 if reduced else rank + 1, rows):
            if i == rank:
                continue
            row = a[i]
            factor = row[column]
            if factor:
                row[column] = 0
                for j in range(column + 1, width):
                    row[j] = (row[j] - factor * pivot_row[j]) % mod
        pivots.append(column)
        if len(pivots) == rows:
            break
    return pivots, determinant


def matrix_det(a, mod=998244353):
    """正方行列の行列式 mod 素数。0x0行列の行列式は1。"""
    rows, _ = _copy_matrix(a, mod, len(a))
    pivots, determinant = _eliminate(rows, len(a), mod)
    return determinant if len(pivots) == len(a) else 0


def matrix_rank(a, mod=998244353):
    """素数mod上の階数。行数または列数が0なら0。"""
    rows, columns = _copy_matrix(a, mod)
    pivots, _ = _eliminate(rows, columns, mod)
    return len(pivots)


def inverse_matrix(a, mod=998244353):
    """素数mod上の逆行列。特異ならNone、0x0なら[]。"""
    n = len(a)
    rows, _ = _copy_matrix(a, mod, n)
    for i in range(n):
        rows[i].extend(int(i == j) for j in range(n))
    pivots, _ = _eliminate(rows, n, mod, reduced=True)
    if len(pivots) != n:
        return None
    return [row[n:] for row in rows]


def linear_equations(a, b, mod=998244353, variables=None):
    """Ax=bの(一つの解, 同次解の基底リスト)。解なしNone。
    全解はx + sum(t[i]*basis[i])。自由変数は0の特解を返す。
    aが空で列数を指定したい場合はvariablesを渡す。返す各ベクトルは長さm。
    基底はm-rank本。掃き出しに加えてO(m*(m-rank))の出力領域を使う。
    """
    if len(a) != len(b):
        raise ValueError("row and right-hand-side lengths differ")
    rows, columns = _copy_matrix(a, mod, variables)
    for row, value in zip(rows, b):
        row.append(value % mod)
    pivots, _ = _eliminate(rows, columns, mod, reduced=True)
    rank = len(pivots)
    if any(row[-1] for row in rows[rank:]):
        return None
    solution = [0] * columns
    for i, column in enumerate(pivots):
        solution[column] = rows[i][-1]
    pivot_set = set(pivots)
    basis = []
    for free in range(columns):
        if free in pivot_set:
            continue
        vector = [0] * columns
        vector[free] = 1
        for i, column in enumerate(pivots):
            vector[column] = -rows[i][free] % mod
        basis.append(vector)
    return solution, basis
