"""半分全列挙・0/1ナップサック。出典: _test.py, algorithm_math/030.py。
非負の重さを想定。値は負でもよい。整数bitset版はPyPy専用。
"""


def subset_sums(values):
    """O(2^n)。空集合を含む全ての部分集合和。重複を保持する。"""
    result = [0]
    for value in values:
        result += [x + value for x in result]
    return result


def split_and_list(values):
    mid = len(values) // 2
    return sorted(subset_sums(values[:mid])), sorted(subset_sums(values[mid:]))


def subset_sums_by_size(values):
    """result[k]: k要素を選ぶ部分集合和のリスト。"""
    result = [[] for _ in range(len(values) + 1)]
    result[0] = [0]
    for i, value in enumerate(values):
        for k in range(i + 1, 0, -1):
            result[k].extend(x + value for x in result[k - 1])
    return result


def knapsack_01(items, capacity):
    """items=[(重さ,価値),...]。O(nW)時間・O(W)空間。"""
    if capacity < 0:
        raise ValueError("negative capacity")
    dp = [0] * (capacity + 1)
    for weight, value in items:
        if weight < 0:
            raise ValueError("negative weight")
        for w in range(capacity, weight - 1, -1):
            dp[w] = max(dp[w], dp[w - weight] + value)
    return dp[capacity]


def subset_sum_bits(values, limit):
    """PyPy用。戻り値のbit kが1なら和kを作れる。0<=k<=limit。"""
    if limit < 0:
        raise ValueError("negative limit")
    bits = 1
    mask = (1 << (limit + 1)) - 1
    for value in values:
        if value < 0:
            raise ValueError("negative value")
        if value <= limit:
            bits = (bits | (bits << value)) & mask
    return bits
