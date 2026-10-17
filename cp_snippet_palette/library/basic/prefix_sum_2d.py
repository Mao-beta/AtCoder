"""2次元累積和。出典: _test.py: cum_2D/area_sum。
0-indexed・半開区間。前計算O(HW)、長方形和O(1)。入力は変更しない。
PyPy向け。Codonでは累積和・引き算の途中も符号付き64bit以内。
"""


def prefix_sum_2d(grid):
    h = len(grid)
    w = len(grid[0]) if h else 0
    prefix = [[0] * (w + 1) for _ in range(h + 1)]
    for y, row in enumerate(grid):
        if len(row) != w:
            raise ValueError("grid must be rectangular")
        total = 0
        for x, value in enumerate(row):
            total += value
            prefix[y + 1][x + 1] = prefix[y][x + 1] + total
    return prefix


def rectangle_sum(prefix, top, left, bottom, right):
    """[top,bottom) × [left,right)。空区間は0。"""
    if not (0 <= top <= bottom < len(prefix) and 0 <= left <= right < len(prefix[0])):
        raise IndexError("rectangle out of range")
    return (
        prefix[bottom][right]
        - prefix[top][right]
        - prefix[bottom][left]
        + prefix[top][left]
    )
