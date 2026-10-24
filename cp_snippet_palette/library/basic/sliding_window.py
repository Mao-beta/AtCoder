"""スライド最小値・最大長方形。出典: ADT_20231207_2I.py, AOJ/DPL_3_B.py。

スライド最小値O(n)、ヒストグラム最大長方形O(n)、グリッド版O(HW)。
PyPy向け。Codonでは面積を64bit以内にする。

使い方（このファイルを解答の先頭に貼り付けてから実行）
    sliding_min([4, 2, 3, 1], 2)  # => [2, 2, 1]
    area_min_sliding([[4, 2, 3], [5, 6, 1]], 2, 2)  # => [[2, 1]]
    largest_rectangle_in_histogram([2, 1, 2])  # => 3
    largest_rectangle_in_grid([[1, 1, 0], [1, 1, 1]])  # => 4
"""

from collections import deque


def sliding_min(values, width):
    """valuesの連続width要素ごとの最小値を左端順に返す。O(n)。
    width>0が必要。width>len(values)なら[]、戻り値の長さは通常n-width+1。
    valuesは比較可能な要素の列、widthは正の整数の窓幅。n=len(values)。作業空間O(min(n,width))、出力空間O(n)。
    """
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
    """長方形gridの各height×width領域の最小値を二次元listで返す。
    結果[r][c]は左上(r,c)の領域。height,width>0。領域が収まらなければ[]。O(HW)。
    gridは比較可能な要素の長方形二次元列。H/Wは入力の行数/列数、height/widthは正の整数の窓の行数/列数。空間O(HW)。
    """
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
    """非負の高さ。幅1の棒を並べたヒストグラムの最大面積。
    入力: heightsは非負整数の高さの列。N=len(heights)。最大面積を整数で返す。時間・空間O(N)。
    """
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
    """真の要素だけでできた最大長方形の面積を整数で返す。O(HW)。
    gridは長方形の二次元配列。0/Falseを壁として扱い、座標は返さない。
    H=len(grid)、Wは各行の長さ。文字0も真と判定されるので、0/1の文字列なら整数・boolの二次元列へ変換する。追加空間O(W)。
    """
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
