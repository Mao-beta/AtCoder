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


def solve(N, P):

    if N % 2:
        ans = [N] * N
        m = (N+1) // 2
        ans[P.index(m)] = -1
    else:
        ans = [N-1] * N
        m = N//2
        ans[P.index(m)] = -1
        ans[P.index(m+1)] = -1

    for i in range(N):
        if 1 <= i <= N-2 and (P[i+1]-P[i]) * (P[i-1]-P[i]) >= 0:
            ans[i] = 3
            continue

        for k in range(2, N, 2):
            if 0 <= i+k < N and 0 <= i+k-1 < N and (P[i+k]-P[i]) * (P[i+k-1]-P[i]) >= 0:
                # print(i, k, (P[i + k] - P[i]), (P[i +k-1] - P[i]))
                ans[i] = k+1
                break
            if 0 <= i-k < N and 0 <= i-k+1 < N and (P[i-k]-P[i]) * (P[i-k+1]-P[i]) >= 0:
                # print(i, k, (P[i-k]-P[i]), (P[i-k+1]-P[i]))
                ans[i] = k+1
                break
            if 0 <= i-k//2 < N and 0 <= i+k//2 < N and (P[i-k//2]-P[i]) * (P[i+k//2]-P[i]) >= 0:
                # print(i, k, (P[i-k//2]-P[i]), (P[i+k//2]-P[i]))
                ans[i] = k+1
                break
            if i > 0 and k >= 4 and 0 <= i + k-1 < N and 0 <= i + k - 1-1 < N and (P[i + k-1] - P[i]) * (P[i + k-1 - 1] - P[i]) >= 0:
                # print(i, k, (P[i + k] - P[i]), (P[i + k - 1] - P[i]))
                ans[i] = k + 1
                break
            if i < N-1 and k >= 4 and 0 <= i - k+1 < N and 0 <= i - k + 2 < N and (P[i - k+1] - P[i]) * (P[i - k + 2] - P[i]) >= 0:
                # print(i, k, (P[i - k+1] - P[i]), (P[i - k + 2] - P[i]))
                ans[i] = k + 1
                break

    return ans


def guchoku(N, P):
    ans = [N+1] * N
    for i in range(N):
        for l in range(i+1):
            for r in range(i+1, N+1):
                g = r-l
                if g % 2 == 0:
                    continue
                p = P[l:r]
                p.sort()
                if p[g//2] != P[i]:
                    ans[i] = min(ans[i], g)
        if ans[i] == N+1:
            ans[i] = -1
    return ans


if __name__ == "__main__":
    N = NI()
    P = NLI()
    ans = solve(N, P)
    print(*ans)
    # N = 7
    # for P in permutations(range(1, N+1), N):
    #     print(P)
    #     P = list(P)
    #     res = solve(N, P)
    #     gu = guchoku(N, P)
    #     print(*res)
    #     print(*gu)
    #     assert res == gu

