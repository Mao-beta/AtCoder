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
    PAB = EI(N)
    Q = NI()
    X = [NI() for _ in range(Q)]
    # i個残っててテンションjのときに最終的にいくつになるか
    dp = [[0]*1001 for _ in range(N+1)]
    for j in range(1001):
        dp[0][j] = j
    for i, (p, a, b) in enumerate(PAB[::-1]):
        for j in range(1001):
            if p >= j:
                dp[i+1][j] = dp[i][j+a]
            else:
                dp[i+1][j] = dp[i][max(0, j-b)]
    B = [b for _, _, b in PAB]
    CB = list(accumulate([0]+B))
    for x in X:
        if x <= 1000:
            print(dp[N][x])
            continue

        idx = bisect.bisect_left(CB, x-1000)
        # print(x, CB, idx)
        if idx > N:
            print(x - CB[N])
        else:
            x = max(0, x-CB[idx])
            print(dp[N-idx][x])


if __name__ == "__main__":
    main()
