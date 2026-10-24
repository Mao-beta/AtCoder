"""グリッド変換。出典: _test.py, ABC237B。0-indexed。幅・高さは明示引数。
PyPy向け。Codonでは各行・要素の型を揃える。

使い方（このファイルを解答の先頭に貼り付けてから実行）
    to_index(1, 2, 4), to_position(6, 4), in_grid(1, 2, 3, 4)  # => (6, (1, 2), True)
    transpose([[1, 2], [3, 4]])  # => [[1, 3], [2, 4]]
    rotate90([[1, 2], [3, 4]])  # => [[3, 1], [4, 2]]
"""


def to_index(row, col, width):
    """0-indexedの(row,col)をrow*width+colに平坦化する。widthは列数。範囲検査なし。
    座標・添字・縦横の長さは整数。時間・追加空間O(1)。
    """
    return row * width + col


def to_position(index, width):
    """平坦化した非負indexを(row,col)へ戻す。width>0。divmod(index,width)を返す。
    座標・添字・縦横の長さは整数。時間・追加空間O(1)。
    """
    return divmod(index, width)


def in_grid(row, col, height, width):
    """0<=row<heightかつ0<=col<widthならTrue。近傍探索の境界判定に使う。
    座標・添字・縦横の長さは整数。時間・追加空間O(1)。
    """
    return 0 <= row < height and 0 <= col < width


def transpose(grid):
    """長方形grid（行の列）の転置を新しいlist[list]で返す。O(HW)。空なら[]。
    入力は行ごとの長さが等しい二次元列。H=len(grid)、Wは各行の長さ。時間・返す配列の空間O(HW)。
    """
    if not grid:
        return []
    w = len(grid[0])
    if any(len(row) != w for row in grid):
        raise ValueError("grid must be rectangular")
    return [[row[x] for row in grid] for x in range(w)]


def rotate90(grid):
    """長方形gridを時計回りに90度回転したlist[list]を返す。O(HW)、入力は変更しない。
    入力は行ごとの長さが等しい二次元列。H=len(grid)、Wは各行の長さ。時間・返す配列の空間O(HW)。
    """
    return [row[::-1] for row in transpose(grid)]
