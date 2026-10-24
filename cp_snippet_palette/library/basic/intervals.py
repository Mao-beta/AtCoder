"""区間の併合・被覆長・スケジューリング・異なる整数の割当。
原則[l,r)の半開区間。assign_distinct_in_intervalsだけは整数の閉区間[l,r]。
入力を変更しない。座標は負でもよい。標準Pythonのみ。

使い方（このファイル全体を貼り付けてから実行）
    merge_intervals([(1, 4), (3, 6), (8, 9)])  # => [(1, 6), (8, 9)]
    interval_union_length([(1, 4), (3, 6)])  # => 5
    covered_lengths([(1, 4), (3, 6)])  # => [0, 4, 1]
    schedule_intervals([(0, 3), (1, 2), (2, 4)])  # => [1, 2]
    assign_distinct_in_intervals([(2, 2), (1, 3), (1, 2)])  # => [2, 3, 1]
"""

from heapq import heappush, heappop


def merge_intervals(intervals):
    """半開区間を併合し、昇順で互いに離れた区間listを返す。隣接区間も併合。
    空区間は無視、l>rは不可。O(N log N)。
    入力: intervals=[(l,r), ...]は数値端点の半開区間列。N=len(intervals)。時間O(N log(N+1))、作業空間O(N)。
    """
    result = []
    for l, r in sorted(intervals):
        assert l <= r
        if l == r:
            continue
        if result and l <= result[-1][1]:
            result[-1] = (result[-1][0], max(r, result[-1][1]))
        else:
            result.append((l, r))
    return result


def interval_union_length(intervals):
    """半開区間の和集合の長さ。重複は一度だけ数える。O(N log N)。
    入力: intervals=[(l,r), ...]は数値端点の半開区間列。N=len(intervals)。時間O(N log(N+1))、作業空間O(N)。
    """
    return sum(r - l for l, r in merge_intervals(intervals))


def covered_lengths(intervals):
    """result[k]=ちょうどk本に覆われた長さ。k>=1、result[0]は常に0。
    半開区間、O(N log N)。未被覆の無限領域は数えない。空入力は[0]。
    入力: intervals=[(l,r), ...]は数値端点の半開区間列。N=len(intervals)。時間O(N log(N+1))、作業空間O(N)。
    """
    intervals = list(intervals)
    events = {}
    for l, r in intervals:
        assert l <= r
        events[l] = events.get(l, 0) + 1
        events[r] = events.get(r, 0) - 1
    result = [0] * (len(intervals) + 1)
    count, previous = 0, 0
    for x, delta in sorted(events.items()):
        if count:
            result[count] += x - previous
        count += delta
        previous = x
    return result


def schedule_intervals(intervals):
    """重ならない半開区間を最多選択し、元の添字を実施順に返す。l<rが必要。
    終了位置=次の開始位置は許す。重みなし、O(N log N)。
    入力: intervals=[(l,r), ...]は数値端点の半開区間列。N=len(intervals)。時間O(N log(N+1))、作業空間O(N)。
    """
    tasks = []
    for i, (l, r) in enumerate(intervals):
        assert l < r
        tasks.append((r, l, i))
    end, result = None, []
    for r, l, i in sorted(tasks):
        if end is None or end <= l:
            result.append(i)
            end = r
    return result


def assign_distinct_in_intervals(intervals):
    """整数の閉区間[l,r]ごとに、互いに異なる整数を1個ずつ割り当てる。
    元の順の割当list、無理ならNone。l<=r、O(N log N)。巨大座標でも座標幅に比例しない。
    入力: intervals=[(l,r), ...]は整数端点の閉区間列。N=len(intervals)。時間O(N log(N+1))、空間O(N)。
    """
    intervals = list(intervals)
    tasks = sorted((l, r, i) for i, (l, r) in enumerate(intervals))
    if any(l > r for l, r in intervals):
        return None
    answer = [0] * len(tasks)
    heap, i, value = [], 0, 0
    while i < len(tasks) or heap:
        if not heap:
            value = tasks[i][0]
        while i < len(tasks) and tasks[i][0] <= value:
            _, r, j = tasks[i]
            heappush(heap, (r, j))
            i += 1
        r, j = heappop(heap)
        if r < value:
            return None
        answer[j] = value
        value += 1
    return answer
