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


def main():
    N, C = NMI()
    XV = EI(N)

    # 始点からi個以下まで行って帰らないときのMax
    dp1R = [0]
    dp1L = [0]
    # 始点からi個以下まで行って帰るときのMax
    dp2R = [0]
    dp2L = [0]

    nv = 0
    for x, v in XV:
        nv += v
        dp1R.append(max(dp1R[-1], nv-x))
        dp2R.append(max(dp2R[-1], nv-2*x))

    nv = 0
    for x, v in XV[::-1]:
        x = C - x
        nv += v
        dp1L.append(max(dp1L[-1], nv - x))
        dp2L.append(max(dp2L[-1], nv - 2 * x))

    ans = max(dp1R + dp1L)
    for i in range(1, N):
        ans = max(ans, dp1R[i] + dp2L[N-i])
        ans = max(ans, dp1L[i] + dp2R[N-i])

    print(ans)


if __name__ == "__main__":
    main()
