import sys
import math
from collections import deque

# 再帰の深さ設定
sys.setrecursionlimit(1000000)
# 剰余初期化
MOD = 10 ** 9 + 7
MOD99 = 998244353

# 入力
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()

# アルファベットと数字の対応
alp_to_num = {chr(i+97): i for i in range(26)}
ALP_to_num = {chr(i+97).upper(): i for i in range(26)}
num_to_alp = {i: chr(i+97) for i in range(26)}
num_to_ALP = {i: chr(i+97).upper() for i in range(26)}


# グリッドの初期化　縦、横、初期値
def make_grid_int(h, w, num): return [[int(num)] * w for _ in range(h)]
def make_grid_bool(h, w, bool): return [[bool] * w for _ in range(h)]

#隣接リスト 1-index
def make_adjlist_nond(n, edges):
    res = [[] for _ in range(n+1)]
    for edge in edges:
        res[edge[0]].append(edge[1])
        res[edge[1]].append(edge[0])
    return res

def make_adjlist_d(n, edges):
    res = [[] for _ in range(n+1)]
    for edge in edges:
        res[edge[0]].append(edge[1])
    return res


# K以下の積を満たす部分列の長さの最大値を得る尺取り法
def syakutori_mul(array, K):
    n = len(array)
    l, r = 0, 0
    mul = 1
    res = 0
    for l in range(n):
        while r < n and mul * array[r] <= K:
            mul *= array[r]
            r += 1
        res = max(res, r-l)
        if l == r:
            r += 1
        else:
            mul = mul // array[l]
    return res


# 狭義単調増加列のカウント
def syakutori_acc(array):
    n = len(array)
    r = 1
    res = 0
    for l in range(n):
        while 0 < r < n and (r <= l or array[r] > array[r-1]):
            r += 1
        res += r-l
        if l == r:
            r += 1

    return res


"""
# 尺取り法テンプレ
def syakutori(array):
    n = len(array)
    r = 1
    # 戻り値の初期値
    res = 0

    # 左端を全探索
    for l in range(n):
        # 頑張って右端を伸ばす部分 常に満たしたい条件をwhileで指定
        while 「満たしたい条件」:
            if r >= n:
                break
            r += 1

        # 区間の長さに応じて何かをする
        res += 「何らかの値」

        # 左端が追い付いたときに右端をずらす
        if l == r:
            r += 1

    return res
"""


""" 2**n bit全探索テンプレ
    for case in range(2**n):
        test = ""
        for i in range(n):
            if (case >> i) & 1:
                test = "1" + test
            else:
                test = "0" + test
        print(test)
"""

# 正方行列の積 mod
def mul_matrix(A, B, mod=10**9+7):
    size = len(A)
    ans = [[0] * size for _ in range(size)]
    for h in range(size):
        for w in range(size):
            for i in range(size):
                ans[h][w] += A[h][i] * B[i][w] % mod
                ans[h][w] %= mod
    return ans

# 正方行列の累乗 mod
def pow_matrix(A, n, mod=10**9+7):
    if n == 1:
        size = len(A)
        E = [[0] * size for _ in range(size)]
        for i in range(size):
            E[i][i] = 1
        return mul_matrix(A, E, mod)

    if n % 2 == 0:
        tA = pow_matrix(A, n//2, mod)
        return mul_matrix(tA, tA, mod)
    else:
        tA = pow_matrix(A, n-1, mod)
        return mul_matrix(tA, A, mod)


# 配列から累積和を返す
def make_cumulative(A):
    C = [0] * (len(A) + 1)
    for i, a in enumerate(A):
        i += 1
        C[i] = C[i - 1] + a
    return C


# 有理数クラス
class MyFraction:
    def __init__(self, a, b):
        assert b != 0, "分母が0です"

        if b < 0:
            a, b = -a, -b
        if a == 0:
            b = 1

        g = math.gcd(a, b)
        self.numerator = a // g
        self.denominator = b // g

    def __add__(self, other):
        Fa_n, Fa_d = self.get_nd()
        Fb_n, Fb_d = other.get_nd()
        F_n = Fa_d * Fb_n + Fa_n * Fb_d
        F_d = Fa_d * Fb_d
        return MyFraction(F_n, F_d)

    def __sub__(self, other):
        Fa_n, Fa_d = self.get_nd()
        Fb_n, Fb_d = other.get_nd()
        F_n = - Fa_d * Fb_n + Fa_n * Fb_d
        F_d = Fa_d * Fb_d
        return MyFraction(F_n, F_d)

    def __mul__(self, other):
        Fa_n, Fa_d = self.get_nd()
        Fb_n, Fb_d = other.get_nd()
        F_n = Fa_n * Fb_n
        F_d = Fa_d * Fb_d
        return MyFraction(F_n, F_d)

    def __truediv__(self, other):
        Fa_n, Fa_d = self.get_nd()
        Fb_d, Fb_n = other.get_nd()
        F_n = Fa_n * Fb_n
        F_d = Fa_d * Fb_d
        return MyFraction(F_n, F_d)

    def __repr__(self):
        return "{0}/{1}".format(self.numerator, self.denominator)

    def get_nd(self):
        return (self.numerator, self.denominator)


def main():
    print(MyFraction(1,2) / MyFraction(1, 4) + MyFraction(-2, 1))


if __name__ == "__main__":
    main()