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
    N, M = NMI()
    A = NLI()
    B = NLI()
    G = [A[0]*(-1)**i - A[i] for i in range(N)]
    bc = 0
    for i in range(N-1):
        G[i+1] += B[i] - bc
        bc += B[i]
        G[i] %= M
    G[-1] %= M
    Even = [G[i] % M for i in range(0, N, 2)]
    Odd = [G[i] % M for i in range(1, N, 2)]
    Even.sort()
    Odd.sort()
    ans = 10**18
    EN = len(Even)
    ON = len(Odd)
    SG = sum(G)
    # print(Even, Odd)
    for i, p in enumerate(Even):
        tmp = SG
        x = M-p
        k = EN - i
        kd = bisect.bisect_right(Odd, x)
        tmp += kd * M - k * M
        if N % 2:
            tmp += x
        if x < M:
            ans = min(ans, tmp)

        tmp = SG
        x = M-p-1
        k = EN - i - 1
        kd = bisect.bisect_right(Odd, x)
        tmp += kd * M - k * M
        if N % 2:
            tmp += x
        if x < M:
            ans = min(ans, tmp)
    # print(G, Even, Odd)
    for i, p in enumerate(Odd):
        tmp = SG
        x = p
        kd = i
        k = EN - bisect.bisect_right(Even, M-x)
        tmp += kd * M - k * M
        if N % 2:
            tmp += x
        if x < M:
            ans = min(ans, tmp)
        # print(SG, i, p, x, kd, k, tmp, ans)

        tmp = SG
        x = p+1
        kd = i+1
        k = EN - bisect.bisect_right(Even, M - x)
        tmp += kd * M - k * M
        if N % 2:
            tmp += x
        if x < M:
            ans = min(ans, tmp)
        # print(tmp)


    tmp = SG
    x = 0
    kd = 0
    k = 0
    tmp += kd * M - k * M
    if N % 2:
        tmp += x
    if x < M:
        ans = min(ans, tmp)

    print(ans)


if __name__ == "__main__":
    main()
