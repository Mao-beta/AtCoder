"""連続部分配列の個数・最小値/最大値の総和。空部分配列は数えない。
sum_leqだけ非負列限定。それ以外は負数も可。各関数O(N)、入力は変更しない。

使い方（このファイル全体を貼り付けてから実行）
    count_subarrays_sum([1, -1, 1], 1)  # => 3
    count_subarrays_sum_leq([1, 0, 2], 2)  # => 5
    count_subarrays_distinct_at_most([1, 2, 1], 1)  # => 3
    count_subarrays_distinct_exact([1, 2, 1], 2)  # => 3
    count_subarrays_minmax([1, 3, 2, 1], 1, 3)  # => 4
    sum_subarray_min([3, 1, 2]), sum_subarray_max([3, 1, 2])  # => (9, 14)
"""


def count_subarrays_sum(values, target):
    """和がtargetの連続部分配列数。負数可、期待O(N)時間・O(N)空間。
    入力: valuesは整数の列。N=len(values)。答えは剰余を取らない整数。
    targetは求める区間和の整数（負も可）。
    """
    seen, total, answer = {0: 1}, 0, 0
    for value in values:
        total += value
        answer += seen.get(total - target, 0)
        seen[total] = seen.get(total, 0) + 1
    return answer


def count_subarrays_sum_leq(values, limit):
    """非負列の和<=limitの部分配列数。0も可。負数入りはValueError。O(N)。
    入力: valuesは整数の列。N=len(values)。答えは剰余を取らない整数。
    limitは区間和の上限の整数。valuesは非負に限る。追加空間O(1)。
    """
    if any(x < 0 for x in values):
        raise ValueError("values must be nonnegative")
    if limit < 0:
        return 0
    left = total = answer = 0
    for right, value in enumerate(values):
        total += value
        while total > limit:
            total -= values[left]
            left += 1
        answer += right - left + 1
    return answer


def count_subarrays_distinct_at_most(values, k):
    """異なる要素が高々k種類の部分配列数。要素はhash可能。k<=0なら0。O(N)期待時間。
    valuesはhashableな要素の列、kは種類数の整数。N=len(values)。空間O(N)以内。
    """
    if k <= 0:
        return 0
    counts, left, answer = {}, 0, 0
    for right, value in enumerate(values):
        counts[value] = counts.get(value, 0) + 1
        while len(counts) > k:
            x = values[left]
            counts[x] -= 1
            if not counts[x]:
                del counts[x]
            left += 1
        answer += right - left + 1
    return answer


def count_subarrays_distinct_exact(values, k):
    """異なる要素がちょうどk種類の部分配列数。k<=0なら0。O(N)期待時間。
    valuesはhashableな要素の列、kは種類数の整数。N=len(values)。空間O(N)以内。
    """
    return count_subarrays_distinct_at_most(
        values, k
    ) - count_subarrays_distinct_at_most(values, k - 1)


def count_subarrays_minmax(values, minimum, maximum):
    """最小値がminimumかつ最大値がmaximumの部分配列数。O(N)時間・O(1)空間。
    入力: valuesは整数の列。N=len(values)。答えは剰余を取らない整数。
    minimum/maximumは要求する最小値/最大値の整数。minimum>maximumなら答え0。
    """
    if minimum > maximum:
        return 0
    bad = low = high = -1
    answer = 0
    for i, value in enumerate(values):
        if not minimum <= value <= maximum:
            bad = i
        if value == minimum:
            low = i
        if value == maximum:
            high = i
        answer += max(0, min(low, high) - bad)
    return answer


def sum_subarray_min(values):
    """全ての非空連続部分配列の最小値の総和。単調スタック、O(N)時間・空間。
    同値の寄与を二重計数しない。剰余を取る場合は返り値に%modを適用する。
    入力: valuesは整数の列。N=len(values)。答えは剰余を取らない整数。
    """
    stack = []
    answer = 0
    n = len(values)
    for right in range(n + 1):
        while stack and (right == n or values[stack[-1]] >= values[right]):
            i = stack.pop()
            left = stack[-1] if stack else -1
            answer += values[i] * (i - left) * (right - i)
        stack.append(right)
    return answer


def sum_subarray_max(values):
    """全ての非空連続部分配列の最大値の総和。負数・重複可、O(N)時間・空間。
    入力: valuesは整数の列。N=len(values)。答えは剰余を取らない整数。
    """
    return -sum_subarray_min([-x for x in values])
