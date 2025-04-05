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
    N, X = NMI()
    AC1 = []
    AC2 = []
    AC3 = []
    for i in range(N):
        v, a, c = NMI()
        if v == 1:
            AC1.append((a, c))
        elif v == 2:
            AC2.append((a, c))
        else:
            AC3.append((a, c))
    # カロリーi取るときの最大ビタミン
    dp1 = [0] * (X+1)
    dp2 = [0] * (X+1)
    dp3 = [0] * (X+1)

    for a, c in AC1:
        for i in range(X, -1, -1):
            if i >= c:
                dp1[i] = max(dp1[i], dp1[i-c]+a)
    for a, c in AC2:
        for i in range(X, -1, -1):
            if i >= c:
                dp2[i] = max(dp2[i], dp2[i-c]+a)
    for a, c in AC3:
        for i in range(X, -1, -1):
            if i >= c:
                dp3[i] = max(dp3[i], dp3[i-c]+a)
    # print(dp1)
    # print(dp2)
    # print(dp3)
    ans = 0
    for v1 in range(X+1):
        for v2 in range(X+1-v1):
            v3 = X-v1-v2
            ans = max(ans, min(dp1[v1], dp2[v2], dp3[v3]))
    print(ans)


if __name__ == "__main__":
    main()
