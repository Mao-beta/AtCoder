"""Mo法。出典: _Mo.pyの未完成骨格をコールバック方式に整理。
0-indexed・半開区間。O((n+q)sqrt(n))回程度のadd/remove。PyPy向け。
"""

from math import isqrt


def mo_order(n, queries):
    """元のクエリIDを処理順に返す。空入力にも対応。"""
    if n < 0 or any(not 0 <= l <= r <= n for l, r in queries):
        raise ValueError("invalid query range")
    width = max(1, n // max(1, isqrt(len(queries))))
    return sorted(
        range(len(queries)),
        key=lambda i: (
            queries[i][0] // width,
            queries[i][1] * (-1 if queries[i][0] // width & 1 else 1),
        ),
    )


def mo_solve(n, queries, add, remove, answer):
    """add/removeに添字を渡す。answer()は現在の答えを返す。初期状態は空区間。
    左右で操作が異なる非可換問題ではmo_orderだけ使い、移動処理を自分で書く。
    """
    result = [None] * len(queries)
    left = right = 0
    for index in mo_order(n, queries):
        l, r = queries[index]
        while left > l:
            left -= 1
            add(left)
        while right < r:
            add(right)
            right += 1
        while left < l:
            remove(left)
            left += 1
        while right > r:
            right -= 1
            remove(right)
        result[index] = answer()
    return result
