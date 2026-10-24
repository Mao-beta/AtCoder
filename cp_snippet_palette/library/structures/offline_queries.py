"""静的配列の区間種類数。クエリを右端順に処理するオフライン法。
O((N+Q)log N)、空間O(N+Q)。0-indexed、半開区間、空区間は0。
値はhash可能であること。入力は変更しない。PyPy向け、Codon未確認。

使い方（このファイルを解答の先頭に貼り付けてから実行）
    range_count_distinct([3, 1, 3, 2], [(0, 4), (0, 3), (2, 2)])  # => [3, 2, 0]
"""


def range_count_distinct(values, queries):
    """valuesの各[l,r)に含まれる異なる値の数をqueriesと同じ順のlistで返す。
    queriesは(l,r)の列。0<=l<=r<=len(values)。O((N+Q)log N)。
    valuesはhashableな値の列、queries=[(l,r),...]は0<=l<=r<=Nの整数境界。N=len(values)、Q=len(queries)。
    空間O(N+Q)。
    """
    n = len(values)
    queries = list(queries)
    bit, last, answer = [0] * (n + 1), {}, [0] * len(queries)

    def add(i, x):
        i += 1
        while i <= n:
            bit[i] += x
            i += i & -i

    def prefix(i):
        total = 0
        while i:
            total += bit[i]
            i -= i & -i
        return total

    end = 0
    for index in sorted(range(len(queries)), key=lambda i: queries[i][1]):
        l, r = queries[index]
        if not 0 <= l <= r <= n:
            raise IndexError("invalid range")
        while end < r:
            value = values[end]
            if value in last:
                add(last[value], -1)
            add(end, 1)
            last[value] = end
            end += 1
        answer[index] = prefix(r) - prefix(l)
    return answer
