"""Mo法。出典: _Mo.pyの未完成骨格をコールバック方式に整理。
0-indexed・半開区間。O((n+q)sqrt(n))回程度のadd/remove。PyPy向け。

使い方（このファイルを解答の先頭に貼り付けてから実行）
    values = [2, 5, 3]
    total = [0]  # コールバックで共有する集計状態
    def add(i):
        total[0] += values[i]
    def remove(i):
        total[0] -= values[i]
    mo_solve(3, [(0, 2), (1, 3), (1, 1)], add, remove, lambda: total[0])  # => [7, 8, 0]
    sorted(mo_order(3, [(0, 2), (1, 3)]))  # => [0, 1]
"""

from math import isqrt


def mo_order(n, queries):
    """長さnの配列に対するqueries=[(l,r),...]をMo順に処理するためのクエリID列。
    0<=l<=r<=nの半開区間。配列やqueriesは変更しない。並べ替えO(q log q)。
    nは配列長の非負整数、q=len(queries)。各境界は整数。出力・作業空間O(q)。
    """
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
    """半開区間queries=[(l,r),...]の答えを入力順のlistで返す。
    add(i)/remove(i)は値ではなく配列の添字iを受けて現在区間の状態を更新する。
    answer()で現在の答えを取得。状態は空区間から開始する。
    answerはスナップショットを返すこと。可変listならコピーして返す。
    左右で更新方法が異なる非可換問題はmo_orderを使い、自分で移動を書く。
    nは配列長、q=len(queries)、B=max(1,n//max(1,isqrt(q)))。時間O(q log(q+1)+n²/B+qB)回程度の端移動・ソート。
    端移動ごとにadd/removeを1回、各答えにanswerを1回呼ぶので、それぞれのコストを掛ける。結果用空間O(q)、集計状態は別。
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
