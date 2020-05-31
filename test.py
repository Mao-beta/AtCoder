import sys
import math
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def make_grid(h, w, num): return [[int(num)] * w for _ in range(h)]

#隣接リスト 1-order
def make_adjlist_d(n, edges):
    res = [[] for _ in range(n+1)]
    for edge in edges:
        res[edge[0]].append(edge[1])
        res[edge[1]].append(edge[0])
    return res

def make_adjlist_nond(n, edges):
    res = [[] for _ in range(n+1)]
    for edge in edges:
        res[edge[0]].append(edge[1])
    return res


#nCr
def cmb(n, r):
    return math.factorial(n) // math.factorial(r) // math.factorial(n-r)


def combinations_mod(n, r, mod=1000000007):
    """Returns nCr in mod."""
    r = min(r, n - r)
    combs = 1
    for i, j in zip(range(n - r + 1, n + 1), range(1, r + 1)):
        combs *= (i % mod) * pow(j, mod - 2, mod)
        combs %= mod
    return combs




#素因数分解
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


def main():
    pass


if __name__ == "__main__":
    main()