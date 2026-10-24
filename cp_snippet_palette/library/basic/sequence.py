"""座標圧縮・LIS・転倒数・RLE。出典: _test.py, _Strings.py, _inversion_num.py。
0-indexed。入力を変更しない。LISは番兵値を使わず任意の整数に対応。
PyPy向け。Codonでは各列を同一型にし、転倒数を64bit内に収める。

使い方（このファイルを解答の先頭に貼り付けてから実行）
    compress([40, 10, 40])  # => ([1, 0, 1], [10, 40])
    a = [3, 1, 2, 2, 5]
    [a[i] for i in lis_indices(a)], lis_length(a, strict=False)  # => ([1, 2, 5], 4)
    inversion_count([3, 1, 2])  # => 2
    run_length_encode('aaabb')  # => [('a', 3), ('b', 2)]
    ''.join(run_length_decode([('a', 3), ('b', 2)]))  # => 'aaabb'
"""

from bisect import bisect_left, bisect_right


def compress(values):
    """比較可能かつhashableな値の列を座標圧縮する。戻り値(ids,original)。
    originalは重複を除いた昇順リスト。original[ids[i]]==values[i]。O(n log n)。
    valuesは長さNの再走査可能な列。計算量のn/Nはlen(values)。追加空間はO(N)以内。
    """
    order = sorted(set(values))
    ids = {x: i for i, x in enumerate(order)}
    return [ids[x] for x in values], order


def lis_indices(values, strict=True):
    """最長増加部分列の元配列上の添字リストを返す（値の列ではない）。
    strict=Trueは狭義増加、Falseは同値を許す非減少。空なら[]。O(n log n)。
    valuesは長さNの再走査可能な列。計算量のn/Nはlen(values)。追加空間はO(N)以内。
    valuesの要素は大小比較可能、strictは狭義増加を要求するかを表すbool。
    """
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
    """最長増加部分列の長さ。strict=Falseなら非減少列。空なら0。
    O(n log n)時間・O(LIS長)空間。要素は比較可能であること。
    valuesは長さNの再走査可能な列。計算量のn/Nはlen(values)。追加空間はO(N)以内。
    valuesの要素は大小比較可能、strictは狭義増加を要求するかを表すbool。
    """
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
    """O(n log n)。i<jかつa[i]>a[j]の組数。同値は数えない。
    valuesは長さNの再走査可能な列。計算量のn/Nはlen(values)。追加空間はO(N)以内。
    要素は大小比較可能かつhashableで、重複を許す。返す整数は剰余を取らない。
    """
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
    """O(n)。[(値, 連続数), ...]。空入力は[]。
    valuesは長さNの再走査可能な列。計算量のn/Nはlen(values)。追加空間はO(N)以内。
    要素は等号比較できればよく、隣接する同値だけをまとめる。
    """
    result = []
    for x in values:
        if result and result[-1][0] == x:
            result[-1] = (x, result[-1][1] + 1)
        else:
            result.append((x, 1))
    return result


def run_length_decode(runs):
    """(値,非負の個数)の列を通常のlistへ復元する。O(復元長)。
    文字列が欲しいときは"".join(run_length_decode(runs))。
    runs=[(value,count), ...]、countは非負整数。R=len(runs)、L=sum(count)。空のrunも含め時間O(R+L)、出力空間O(L)。
    """
    result = []
    for value, count in runs:
        if count < 0:
            raise ValueError("count must be nonnegative")
        result.extend([value] * count)
    return result
