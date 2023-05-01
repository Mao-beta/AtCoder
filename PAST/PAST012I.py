import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations

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


def floor_sum(n, m, a, b):
    # sum_{i=0}^{n-1} floor((a*i+b)//m)を高速に求める
    # y = (a*x + b) / m より下の格子点の数
    ans = 0
    if a >= m:
        ans += (n-1) * n * (a//m)//2
        a %= m
    if b >= m:
        ans += n * (b//m)
        b %= m
    y_max = (a*n+b) // m
    x_max = (y_max * m - b)
    if y_max == 0:
        return ans
    ans += (n - (x_max + a-1)//a) * y_max
    ans += floor_sum(y_max, a, m, (a - x_max % a) % a)
    return ans


def main():
    T = NI()
    for _ in range(T):
        N, A, M = NMI()
        ans = floor_sum(N, M, A, A) * M
        ans += (N - N // (M // math.gcd(M, A))) * M
        ans -= A * N * (N+1) // 2
        print(ans)


if __name__ == "__main__":
    main()
