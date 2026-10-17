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


def calc(i, j, i2, j2, is_8neighbor=0):
    if is_8neighbor:
        return max(abs(i - i2), abs(j - j2))
    else:
        return abs(i - i2) + abs(j - j2)


def main():
    N, A, B = NMI()
    CD = EI(N) + [[A,B], [1,1]]
    INF = 10**20
    # [Ci,Di]...と[A,B][1,1]のN+2個のbitDP lastがj
    dp = [[INF]*(N+2) for _ in range(1<<(N+2))]
    dp[1<<(N+1)][N+1] = 0
    for b in range(1<<(N+2)):
        for j in range(N+2):
            if dp[b][j] >= INF:
                continue
            for x in range(N+2):
                if (b >> x) & 1:
                    continue
                nb = b | (1<<x)
                nj = x
                is_8neighbor = (b >> N) & 1
                g = calc(*CD[j], *CD[nj], is_8neighbor)
                dp[nb][nj] = min(dp[nb][nj], dp[b][j] + g)
    ans = INF
    for b in range(1<<(N+2)):
        if (b & ((1<<N)-1)) == (1<<N)-1:
            ans = min(ans, min(dp[b]))
    print(ans)


if __name__ == "__main__":
    main()
