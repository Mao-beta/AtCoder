"""座標圧縮・LIS・転倒数・RLE。出典: _test.py, _Strings.py, _inversion_num.py。
0-indexed。入力を変更しない。LISは番兵値を使わず任意の整数に対応。
PyPy向け。Codonでは各列を同一型にし、転倒数を64bit内に収める。
"""

from bisect import bisect_left, bisect_right


def compress(values):
    """O(n log n)。圧縮した列と、元の値を昇順に並べた復元表を返す。"""
    order = sorted(set(values))
    ids = {x: i for i, x in enumerate(order)}
    return [ids[x] for x in values], order


def lis_indices(values, strict=True):
    """O(n log n)。最長増加部分列の添字を復元。strict=Falseで非減少列。"""
    tails, ends = [], []
    prev = [-1] * len(values)
    search = bisect_left if strict else bisect_right
    for i, x in enumerate(values):
        k = search(tails, x)
        if k:
            prev[i] = ends[k - 1]
        if k == len(tails):
            tails.append(x)
            ends.append(i)
        else:
            tails[k] = x
            ends[k] = i
    result = []
    v = ends[-1] if ends else -1
    while v != -1:
        result.append(v)
        v = prev[v]
    return result[::-1]


def lis_length(values, strict=True):
    """O(n log n)時間・O(LIS長)空間。"""
    tails = []
    search = bisect_left if strict else bisect_right
    for x in values:
        k = search(tails, x)
        if k == len(tails):
            tails.append(x)
        else:
            tails[k] = x
    return len(tails)


def inversion_count(values):
    """O(n log n)。i<jかつa[i]>a[j]の組数。同値は数えない。"""
    a, order = compress(values)
    bit = [0] * (len(order) + 1)
    answer = 0
    for count, x in enumerate(a):
        i, smaller_equal = x + 1, 0
        while i:
            smaller_equal += bit[i]
            i -= i & -i
        answer += count - smaller_equal
        i = x + 1
        while i < len(bit):
            bit[i] += 1
            i += i & -i
    return answer


def run_length_encode(values):
    """O(n)。[(値, 連続数), ...]。空入力は[]。"""
    result = []
    for x in values:
        if result and result[-1][0] == x:
            result[-1] = (x, result[-1][1] + 1)
        else:
            result.append((x, 1))
    return result


def run_length_decode(runs):
    """O(復元長)。文字列に戻す場合は''.join(result)。"""
    result = []
    for value, count in runs:
        if count < 0:
            raise ValueError("count must be nonnegative")
        result.extend([value] * count)
    return result
