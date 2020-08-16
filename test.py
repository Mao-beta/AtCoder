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


# nCr 要math
def cmb(n, r):
    return math.factorial(n) // math.factorial(r) // math.factorial(n-r)

# # nCrの剰余
# def combinations_mod(n, r, mod=1000000007):
#     """Returns nCr in mod."""
#     r = min(r, n - r)
#     combs = 1
#     for i, j in zip(range(n - r + 1, n + 1), range(1, r + 1)):
#         combs *= (i % mod) * pow(j, mod - 2, mod)
#         combs %= mod
#     return combs


# 二項係数計算用　階乗と逆元の初期化
def combination_mod_initialize(n, MOD=10**9+7):
    fac = [1]*(n+1)
    inv = [1]*(n+1)
    for i in range(1, n+1):
        fac[i] = fac[i-1] * i % MOD
        inv[i] = inv[i-1] * pow(i, -1, MOD) % MOD
    return fac, inv

# 二項係数　高速
def combination_mod(n, r, fac, inv, mod=10**9+7):
    return fac[n] * inv[r] * inv[n-r]



# Nの素因数分解を辞書で返す
def prime_fact(n):
    root = int(math.sqrt(n))
    prime_dict = {}
    for i in range(2, root+1):
        cnt = 0
        while n % i == 0:
            cnt += 1
            n = n // i
        if cnt:
            prime_dict[i] = cnt
    if n != 1:
        prime_dict[n] = 1
    return prime_dict


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

    def __str__(self):
        return "{0}/{1}".format(self.numerator, self.denominator)



def main():
    A = [[2,0,0],[0,1,0],[0,0,1]]
    print(pow_matrix(A,1000000))

if __name__ == "__main__":
    main()