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
    N = NI()
    AB = EI(N)
    S = sum([b for a, b in AB])
    if S % 3:
        print(-1)
        return
    INF = N+1
    dp = [[[INF]*501 for _ in range(501)] for _ in range(N+1)]
    dp[0][0][0] = 0
    for i in range(N):
        a, b = AB[i]
        for j in range(501):
            for k in range(501):
                d = dp[i][j][k]
                if d == INF:
                    continue
                for x in range(1, 4):
                    if x == a:
                        add = 0
                    else:
                        add = 1
                    if x == 1:
                        nj = j + b
                    else:
                        nj = j
                    if x == 2:
                        nk = k + b
                    else:
                        nk = k
                    if nj > 500 or nk > 500:
                        continue
                    dp[i+1][nj][nk] = min(dp[i+1][nj][nk], d + add)
    ans = dp[N][S//3][S//3]
    if ans == INF:
        print(-1)
    else:
        print(ans)


if __name__ == "__main__":
    main()
