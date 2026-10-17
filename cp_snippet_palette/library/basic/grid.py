"""グリッド変換。出典: _test.py, ABC237B。0-indexed。幅・高さは明示引数。
PyPy向け。Codonでは各行・要素の型を揃える。
"""


def to_index(row, col, width):
    return row * width + col


def to_position(index, width):
    return divmod(index, width)


def in_grid(row, col, height, width):
    return 0 <= row < height and 0 <= col < width


def transpose(grid):
    """O(HW)。新しいlistの行列を返す。"""
    if not grid:
        return []
    w = len(grid[0])
    if any(len(row) != w for row in grid):
        raise ValueError("grid must be rectangular")
    return [[row[x] for row in grid] for x in range(w)]


def rotate90(grid):
    """時計回りに90度回転。入力は変更しない。"""
    return [row[::-1] for row in transpose(grid)]
