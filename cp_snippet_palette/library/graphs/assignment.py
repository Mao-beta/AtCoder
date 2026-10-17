"""最小費用割当（Hungarian法）。負の費用可、非再帰、入力非破壊。
n行m列、n<=m。全行を相異なる列へ割り当てる。時間O(n^2*m)、補助空間O(n+m)。
PyPy向け。Codon未確認。64bit処理系では費用・ポテンシャルの中間値にも注意。
"""


def assignment(cost):
    """(最小費用, 各行の割当先列)を返す。空なら(0, [])。列番号は0-indexed。
    長方形も可。n>mや不揃いな行はValueError。禁止辺は扱わない。
    """
    n = len(cost)
    if not n:
        return 0, []
    m = len(cost[0])
    if n > m or any(len(row) != m for row in cost):
        raise ValueError("rectangular cost matrix with rows <= columns required")
    u, v = [0] * (n + 1), [0] * (m + 1)
    matched_row = [0] * (m + 1)
    previous = [0] * (m + 1)
    for row in range(1, n + 1):
        matched_row[0] = row
        slack = [None] * (m + 1)
        used = [False] * (m + 1)
        column = 0
        while True:
            used[column] = True
            i = matched_row[column]
            values = cost[i - 1]
            delta, next_column = None, 0
            for j in range(1, m + 1):
                if used[j]:
                    continue
                reduced = values[j - 1] - u[i] - v[j]
                if slack[j] is None or reduced < slack[j]:
                    slack[j] = reduced
                    previous[j] = column
                if delta is None or slack[j] < delta:
                    delta, next_column = slack[j], j
            for j in range(m + 1):
                if used[j]:
                    u[matched_row[j]] += delta
                    v[j] -= delta
                elif slack[j] is not None:
                    slack[j] -= delta
            column = next_column
            if matched_row[column] == 0:
                break
        while column:
            prev = previous[column]
            matched_row[column] = matched_row[prev]
            column = prev
    result = [-1] * n
    for j in range(1, m + 1):
        if matched_row[j]:
            result[matched_row[j] - 1] = j - 1
    return sum(cost[i][result[i]] for i in range(n)), result
