"""スライド最小値・最大長方形。出典: ADT_20231207_2I.py, AOJ/DPL_3_B.py。
スライド最小値O(n)、ヒストグラム最大長方形O(n)、グリッド版O(HW)。
PyPy向け。Codonでは面積を64bit以内にする。
"""

from collections import deque


def sliding_min(values, width):
    if width <= 0:
        raise ValueError("width must be positive")
    q = deque()
    answer = []
    for i, x in enumerate(values):
        while q and q[0] <= i - width:
            q.popleft()
        while q and values[q[-1]] >= x:
            q.pop()
        q.append(i)
        if i + 1 >= width:
            answer.append(values[q[0]])
    return answer


def area_min_sliding(grid, height, width):
    """各height×width領域の最小値。収まる領域がなければ[]。"""
    if height <= 0 or width <= 0:
        raise ValueError("window must be positive")
    if not grid:
        return []
    w = len(grid[0])
    if any(len(row) != w for row in grid):
        raise ValueError("grid must be rectangular")
    if height > len(grid) or width > w:
        return []
    rows = [sliding_min(row, width) for row in grid]
    columns = [
        sliding_min([row[x] for row in rows], height) for x in range(w - width + 1)
    ]
    return [[column[y] for column in columns] for y in range(len(grid) - height + 1)]


def largest_rectangle_in_histogram(heights):
    """非負の高さ。幅1の棒を並べたヒストグラムの最大面積。"""
    stack = []
    best = 0
    for i in range(len(heights) + 1):
        h = heights[i] if i < len(heights) else 0
        if h < 0:
            raise ValueError("negative height")
        start = i
        while stack and stack[-1][1] > h:
            start, old = stack.pop()
            best = max(best, old * (i - start))
        if not stack or stack[-1][1] < h:
            stack.append((start, h))
    return best


def largest_rectangle_in_grid(grid):
    """真の要素だけでできた最大長方形。0/Falseを壁として扱う。"""
    if not grid:
        return 0
    heights = [0] * len(grid[0])
    best = 0
    for row in grid:
        if len(row) != len(heights):
            raise ValueError("grid must be rectangular")
        for x, value in enumerate(row):
            heights[x] = heights[x] + 1 if value else 0
        best = max(best, largest_rectangle_in_histogram(heights))
    return best
