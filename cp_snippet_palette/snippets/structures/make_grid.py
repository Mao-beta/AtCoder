"""整数の2次元配列を作る。

使い方（このファイルを解答の先頭に貼り付けてから実行）
    grid = make_grid(2, 3, 0)
    grid[0][1] = 5  # 他の行には影響しない
    grid  # => [[0, 5, 0], [0, 0, 0]]
"""

def make_grid(h, w, num=0):
    """h×w の整数二次元配列を生成する。O(hw)。各行は独立。
    h/wは非負整数の行数/列数、numは全セルへ入れる初期整数値。空間O(hw)。
    """
    num = int(num)
    return [[num] * w for _ in range(h)]

