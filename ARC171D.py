import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
MOD99 = 998244353

input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()
SMI = lambda: input().split()
SLI = lambda: list(SMI())
EI = lambda m: [NLI() for _ in range(m)]



def popcount(x):
    x = ((x >> 1)  & 0x55555555) + (x & 0x55555555)
    x = ((x >> 2)  & 0x33333333) + (x & 0x33333333)
    x = ((x >> 4)  & 0x0f0f0f0f) + (x & 0x0f0f0f0f)
    x = ((x >> 8)  & 0x00ff00ff) + (x & 0x00ff00ff)
    x = ((x >> 16) & 0x0000ffff) + (x & 0x0000ffff)
    return x
def bit_reverse(x):
    x = (x >> 16) | (x << 16)
    x = ((x >> 8) & 0x00FF00FF) | ((x << 8) & 0xFF00FF00)
    x = ((x >> 4) & 0x0F0F0F0F) | ((x << 4) & 0xF0F0F0F0)
    x = ((x >> 2) & 0x33333333) | ((x << 2) & 0xCCCCCCCC)
    x = ((x >> 1) & 0x55555555) | ((x << 1) & 0xAAAAAAAA)
    return x
def ctz(x): return popcount(~x & (x - 1))
def clz(x): return ctz(bit_reverse(x))


def chromatic_number(n, uvs):
    edge = [0] * n
    for uv in uvs:
        u, v = uv
        edge[u] |= 1 << v
        edge[v] |= 1 << u
    dp = [0] * (1 << n)
    dp[0] = 1
    cur = [0] * (1 << n)
    for bit in range(1, 1 << n):
        v = ctz(bit)
        dp[bit] = dp[bit ^ (1 << v)] + dp[(bit ^ (1 << v)) & (~edge[v])]
    for bit in range(1 << n):
        if (n - popcount(bit)) & 1:
            cur[bit] = -1
        else:
            cur[bit] = 1
    for k in range(1, n):
        tmp = 0
        for bit in range(1 << n):
            cur[bit] *= dp[bit]
            tmp += cur[bit]
        if tmp != 0:
            res = k
            break
    else:
        res = n
    return res


def main():
    P, B, N, M = NMI()
    edges = EI(M)
    edges = [[x-1, y] for x, y in edges]
    res = chromatic_number(N+1, edges)

    if res > P:
        print("No")
    else:
        print("Yes")


if __name__ == "__main__":
    main()
