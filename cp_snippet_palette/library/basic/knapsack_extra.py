"""価値DP・個数制限・個数無制限ナップサックと、部分和の選択復元。
重量・目標和は非負整数。bitset復元は任意精度整数を使うためPyPy向け。
通常の0/1・容量DPはsubset_dp.pyのknapsack_01を使う。

使い方（このファイル全体を貼り付けてから実行）
    knapsack_by_value([(3, 4), (4, 5), (2, 3)], 6)  # => 8
    bounded_knapsack([(2, 3, 2), (3, 5, 1)], 7)  # => 11
    knapsack_unbounded([(2, 3), (3, 5)], 7)  # => 11
    subset_sum_restore([2, 3, 7], 5)  # => [0, 1]
    two_choice_sum([(1, 3), (2, 4)], 5)  # => [1, 0]
"""

from collections import deque


def knapsack_by_value(items, capacity):
    """items=(重さ,価値)の列、各1個。容量以下の最大価値を返す。重さ・価値とも非負整数。
    V=価値総和としてO(NV)時間・O(V)空間。重量が巨大、価値総和が小さいときに使う。
    capacityは許される重さの上限を表す非負整数。N=len(items)は品物の種類数。各tupleの順序は(重さ,価値[,個数])で、入力のitemsは変更しない。
    """
    assert capacity >= 0
    items = list(items)
    assert all(w >= 0 and v >= 0 for w, v in items)
    total = sum(v for w, v in items)
    dp = [capacity + 1] * (total + 1)
    dp[0] = 0
    used = 0
    for weight, value in items:
        for v in range(used, -1, -1):
            if dp[v] + weight < dp[v + value]:
                dp[v + value] = dp[v] + weight
        used += value
    return max(v for v, weight in enumerate(dp) if weight <= capacity)


def bounded_knapsack(items, capacity):
    """items=(重さ,価値,最大個数)の列。容量以下の最大価値。選ばなくてもよい。
    重さ・最大個数は非負整数、価値は負でも可。単調dequeでO(N*capacity)時間・O(capacity)空間。
    capacityは許される重さの上限を表す非負整数。N=len(items)は品物の種類数。各tupleの順序は(重さ,価値[,個数])で、入力のitemsは変更しない。
    """
    assert capacity >= 0
    dp = [0] * (capacity + 1)
    for weight, value, count in items:
        assert weight >= 0 and count >= 0
        if weight == 0:
            gain = max(0, value) * count
            dp = [x + gain for x in dp]
            continue
        previous = dp
        dp = previous[:]
        for r in range(min(weight, capacity + 1)):
            queue = deque()
            for j, w in enumerate(range(r, capacity + 1, weight)):
                while queue and queue[0][0] < j - count:
                    queue.popleft()
                score = previous[w] - j * value
                while queue and queue[-1][1] <= score:
                    queue.pop()
                queue.append((j, score))
                dp[w] = queue[0][1] + j * value
    return dp[capacity]


def knapsack_unbounded(items, capacity):
    """items=(正の整数の重さ,価値)。各品物を何個でも使い、容量以下の価値を最大化。
    選ばなくてもよい。重さ0は不可。O(N*capacity)時間・O(capacity)空間。
    capacityは許される重さの上限を表す非負整数。N=len(items)は品物の種類数。各tupleの順序は(重さ,価値[,個数])で、入力のitemsは変更しない。
    """
    assert capacity >= 0
    dp = [0] * (capacity + 1)
    for weight, value in items:
        assert weight > 0
        for w in range(weight, capacity + 1):
            dp[w] = max(dp[w], dp[w - weight] + value)
    return dp[capacity]


def subset_sum_restore(values, target):
    """各要素を高々1回選び和targetにする元の添字list。無理ならNone、target=0なら[]。
    非負整数列。新しく到達した和だけ親を保存。O(N+target)回のbitset演算、O(target)空間。
    各bitset演算は最大target+1 bitを扱う。低bit抽出にも多倍長整数のコストがかかる。
    valuesは非負整数の列、targetは目標和の非負整数。N=len(values)。空間O(target+N)以内。
    """
    assert target >= 0
    values = list(values)
    assert all(v >= 0 for v in values)
    if target == 0:
        return []
    mask, bits = (1 << (target + 1)) - 1, 1
    parent = [-1] * (target + 1)
    for i, value in enumerate(values):
        if value > target:
            continue
        fresh = ((bits << value) & mask) & ~bits
        bits |= fresh
        while fresh:
            bit = fresh & -fresh
            parent[bit.bit_length() - 1] = i
            fresh ^= bit
        if bits >> target & 1:
            result = []
            while target:
                i = parent[target]
                result.append(i)
                target -= values[i]
            return result[::-1]
    return None


def two_choice_sum(choices, target):
    """各(a,b)から必ず1つ選び和targetにする。選択を0/1のlistで返し、無理ならNone。
    a,b,targetは非負整数。O(N*ceil(target/w))時間・空間のbitset履歴を使う。
    復元は末尾からaを優先。同じ目標へ複数解があればその1つ。
    choices=[(a,b), ...]は各回の選択肢。N=len(choices)、wは多倍長整数の内部ワード幅。
    target=0も含め時間・保存領域はO(N*ceil((target+1)/w))が目安。
    """
    assert target >= 0
    choices = list(choices)
    assert all(a >= 0 and b >= 0 for a, b in choices)
    history, mask = [1], (1 << (target + 1)) - 1
    for a, b in choices:
        bits = history[-1]
        history.append(
            ((bits << a if a <= target else 0) | (bits << b if b <= target else 0))
            & mask
        )
    if not (history[-1] >> target & 1):
        return None
    answer = [0] * len(choices)
    for i in range(len(choices) - 1, -1, -1):
        a, b = choices[i]
        if target >= a and history[i] >> (target - a) & 1:
            target -= a
        else:
            answer[i] = 1
            target -= b
    return answer
