import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.set_int_max_str_digits(10**6)
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


def main():
    # 末尾がX=A[i]の部分列の個数dp[i]は(A[i]のX個前に出てくるXの位置+1, A[i]のX-1個前に出てくるXの位置)の総和になる。
    N = NI()
    A = NLI()
    D = defaultdict(list)
    for i, a in enumerate(A):
        D[a].append(i)
    I2Di = [0] * N
    for a, L in D.items():
        for j, i in enumerate(L):
            I2Di[i] = j

    dp = [0] * (N+1)
    dp[0] = 1
    cum = [0] * (N+2)
    cum[1] = 1
    for i in range(N):
        a = A[i]
        j = I2Di[i]
        if j+1 < a:
            l, r = 0, 0
        elif j+1 == a:
            l = 0
            r = D[a][0] + 1
        else:
            l = D[a][j-a] + 1
            r = D[a][j-a+1] + 1

        dp[i+1] += cum[r] - cum[l]
        dp[i+1] %= MOD99
        cum[i+2] = cum[i+1] + dp[i+1]
        cum[i+2] %= MOD99
        print(i, a, l, r, j, dp, cum)
    print(dp, cum)
    print(cum[N])


if __name__ == "__main__":
    main()
