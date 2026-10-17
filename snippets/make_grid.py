"""整数の2次元配列を作る。"""

def make_grid(h, w, num=0):
    """h×w の整数二次元配列を生成する。O(hw)。各行は独立。"""
    num = int(num)
    return [[num] * w for _ in range(h)]

