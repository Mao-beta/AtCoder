"""半分全列挙・0/1ナップサック。出典: _test.py, algorithm_math/030.py。

非負の重さを想定。値は負でもよい。整数bitset版はPyPy専用。

使い方（このファイルを解答の先頭に貼り付けてから実行）
    subset_sums([2, 3])  # => [0, 2, 3, 5]
    split_and_list([2, 3])  # => ([0, 2], [0, 3])
    subset_sums_by_size([2, 3])  # => [[0], [2, 3], [5]]
    knapsack_01([(2, 4), (3, 5)], 4)  # => 5
    bits = subset_sum_bits([2, 3], 5)
    [k for k in range(6) if (bits >> k) & 1]  # => [0, 2, 3, 5]
"""


def subset_sums(values):
    """O(2^n)。空集合を含む全ての部分集合和。重複を保持する。
    入力: valuesは整数の列で負数・重複も可。N=len(values)。空集合を含む。
    時間・出力空間O(2^N)。
    """
    result = [0]
    for value in values:
        result += [x + value for x in result]
    return result


def split_and_list(values):
    """valuesを中央で二分し、それぞれの部分集合和の昇順リスト(left,right)を返す。
    空集合の0と重複を含む。片側を走査し、他方を二分探索する半分全列挙向け。
    入力: valuesは整数の列で負数・重複も可。N=len(values)。空集合を含む。
    時間O(N*2^ceil(N/2))、出力空間O(2^ceil(N/2))。ソートを含む。
    """
    mid = len(values) // 2
    return sorted(subset_sums(values[:mid])), sorted(subset_sums(values[mid:]))


def subset_sums_by_size(values):
    """result[k]: k要素を選ぶ部分集合和のリスト。
    入力: valuesは整数の列で負数・重複も可。N=len(values)。空集合を含む。
    戻り値は長さN+1のlistで、result[k]はk個選んだ和のlist。時間・出力空間O(2^N)。
    """
    result = [[] for _ in range(len(values) + 1)]
    result[0] = [0]
    for i, value in enumerate(values):
        for k in range(i + 1, 0, -1):
            result[k].extend(x + value for x in result[k - 1])
    return result


def knapsack_01(items, capacity):
    """items=[(非負整数の重さ,価値),...]から各品物を高々1個選ぶ。
    総重量<=capacityの最大価値を返す。選ばない選択も可、復元はしない。
    capacity>=0。O(n*capacity)時間・O(capacity)空間。
    n=len(items)は品物数。容量W=capacityとして時間O(n*(W+1))、空間O(W+1)。
    """
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
    """PyPy用。戻り値のbit kが1なら和kを作れる。0<=k<=limit。
    入力: valuesは非負整数の列、limitは記録する和の上限の非負整数。N=len(values)、wは多倍長整数の内部ワード幅。
    時間O(N*ceil((limit+1)/w))、空間O(ceil((limit+1)/w))ワード。
    """
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
