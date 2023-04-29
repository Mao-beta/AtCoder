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
    N, M, K = NMI()
    S = SI()

    total = S.count("x")
    # L[i]: 左からi個までxを変えられるときに何個oが続くか
    L = [N] * (total+1)
    cnt = 0
    for i, s in enumerate(S):
        if s == "x":
            L[cnt] = i
            cnt += 1

    if total * M == K:
        print(N * M)
        exit()

    # print(L)
    ans = 0
    x = 0
    for i, s in enumerate(S):
        tmp = 0
        if i == 0:
            k, r = divmod(K, total)
            tmp += k * N + L[r]

        elif S[i-1] == "x":
            k, r = divmod(K, total)
            if k >= M:
                continue
            if k == M-1:
                if r > total - x:
                    continue

            if r < total - x:
                tmp = i + k * N + (L[x+r] - i) - i
            else:
                tmp = i + k * N + (N-i) + L[r-(total-x)] - i

        if s == "x":
            x += 1

        ans = max(ans, tmp)

    print(ans)


if __name__ == "__main__":
    main()
