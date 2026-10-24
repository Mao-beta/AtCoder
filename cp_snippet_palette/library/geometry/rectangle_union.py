"""長方形の和集合面積。出典: ABC449F。
rectangles=[(left,bottom,right,top),...]。半開長方形、退化長方形は無視。

座標圧縮＋被覆長セグ木。O(n log n)。PyPy向け、Codonは面積・座標差を64bit内に。

使い方（このファイルを解答の先頭に貼り付けてから実行）
    rectangle_union_area([(0, 0, 2, 2), (1, 1, 3, 3)])  # => 7
"""


def rectangle_union_area(rectangles):
    """rectangles=[(left,bottom,right,top),...]の和集合の面積を返す。
    座標順はx,y,x,y。軸平行・半開長方形で、重なりを一度だけ数える。
    退化長方形は無視、逆転した端点はValueError。空なら0。O(n log n)。
    端点は数値、n=len(rectangles)。追加空間O(n)。
    """
    events, coords = [], []
    for left, bottom, right, top in rectangles:
        if left > right or bottom > top:
            raise ValueError("reversed rectangle")
        if left == right or bottom == top:
            continue
        events.append((left, 1, bottom, top))
        events.append((right, -1, bottom, top))
        coords.extend((bottom, top))
    if not events:
        return 0
    coords = sorted(set(coords))
    index = {v: i for i, v in enumerate(coords)}
    n = len(coords) - 1
    count, length = [0] * (4 * n), [0] * (4 * n)

    def update(l, r, delta, k, left, right):
        if r <= left or right <= l:
            return
        if l <= left and right <= r:
            count[k] += delta
        else:
            mid = (left + right) // 2
            update(l, r, delta, 2 * k, left, mid)
            update(l, r, delta, 2 * k + 1, mid, right)
        if count[k]:
            length[k] = coords[right] - coords[left]
        elif right - left == 1:
            length[k] = 0
        else:
            length[k] = length[2 * k] + length[2 * k + 1]

    events.sort()
    prev, area = events[0][0], 0
    for x, delta, bottom, top in events:
        area += (x - prev) * length[1]
        update(index[bottom], index[top], delta, 1, 0, n)
        prev = x
    return area
