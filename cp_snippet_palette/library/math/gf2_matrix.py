"""GF(2)のbitset行列。各行を整数で表し、bit jが列j（0-indexed）。
加算はXOR、積はANDと偶奇。入力は変更しない。PyPy向け、Codon未確認。
Pythonの多倍長整数を利用するため、固定幅整数への置換は不可。

使い方（このファイルを解答の先頭に貼り付けてから実行）
    a = [0b11, 0b10]  # [[1,1],[0,1]]
    inverse = inverse_matrix_gf2(a)
    inverse, matrix_product_gf2(a, inverse, 2)  # => ([3, 2], [1, 2])
    matrix_rank_gf2([0b101, 0b011, 0b110], 3)  # => 2
    rows = [int(s[::-1], 2) for s in ['110', '011']]  # 左端を列0とする文字列
    [format(row, '03b')[::-1] for row in rows]  # => ['110', '011']
"""


def matrix_rank_gf2(rows, columns):
    """rowsのGF(2)上の階数。columnsは列数。空行列は0。
    O(N min(N,M))回のbitset演算、各演算はM bit分のコスト。
    rowsは非負整数のlistで、整数のbit jが列j（係数0/1）。N=len(rows)。
    N×M行列の入力領域はO(N*ceil(M/w))ワードで、wは多倍長整数の内部ワード幅。
    M=columnsは非負整数の列数。0<=row<2**M。空間O(min(N,M)*ceil(M/w))ワード。
    """
    if columns < 0 or any(row < 0 or row.bit_length() > columns for row in rows):
        raise ValueError("row is outside the column range")
    basis = {}
    for row in rows:
        while row:
            pivot = row.bit_length() - 1
            if pivot not in basis:
                basis[pivot] = row
                break
            row ^= basis[pivot]
    return len(basis)


def inverse_matrix_gf2(rows):
    """N×N行列の逆行列をbitset行のlistで返す。特異ならNone、0×0なら[]。
    O(N²)回の2N bit演算。入力のbit jが列j。
    rowsは非負整数のlistで、整数のbit jが列j（係数0/1）。N=len(rows)。
    N×M行列の入力領域はO(N*ceil(M/w))ワードで、wは多倍長整数の内部ワード幅。
    M=Nで各row<2**N。追加空間O(N*ceil(2*N/w))ワード。
    """
    n = len(rows)
    if any(row < 0 or row.bit_length() > n for row in rows):
        raise ValueError("matrix must be square")
    a = [row | (1 << (n + i)) for i, row in enumerate(rows)]
    for col in range(n):
        bit = 1 << col
        pivot = next((i for i in range(col, n) if a[i] & bit), -1)
        if pivot < 0:
            return None
        a[col], a[pivot] = a[pivot], a[col]
        row = a[col]
        for i in range(n):
            if i != col and a[i] & bit:
                a[i] ^= row
    return [row >> n for row in a]


def matrix_product_gf2(a, b, columns):
    """N×MのaとM×Kのbの積を返す。columns=Kを明示する。
    8列ずつのXOR表を利用。O(ceil(M/8)*(N+256))回のK bit演算。
    行数0・列数0にも対応。値は指定列数の範囲内の非負整数。
    a/bはbitset行のlist、N=len(a)、M=len(b)、K=columns。aの各行はMbit、bの各行はKbit以内。
    wを内部ワード幅とし、作業・出力空間O((N+256)*ceil(K/w))ワード。
    """
    m = len(b)
    if columns < 0 or any(x < 0 or x.bit_length() > m for x in a):
        raise ValueError("left matrix has invalid rows")
    if any(x < 0 or x.bit_length() > columns for x in b):
        raise ValueError("right matrix has invalid rows")
    result = [0] * len(a)
    for start in range(0, m, 8):
        table = [0]
        width = min(8, m - start)
        for row in b[start : start + width]:
            table += [x ^ row for x in table]
        mask = (1 << width) - 1
        for i, row in enumerate(a):
            result[i] ^= table[(row >> start) & mask]
    return result
