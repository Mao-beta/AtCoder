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
    N, K = NMI()
    A = NLI()
    INF = 10**10
    ans = INF
    D = deque()
    C = [0] * (K+1)
    now = 0

    for a in A:
        D.append(a)
        if 1 <= a <= K:
            if C[a] == 0:
                now += 1
            C[a] += 1

        while D:
            if D[0] > K:
                D.popleft()
            elif C[D[0]] > 1:
                C[D[0]] -= 1
                D.popleft()
            else:
                break

        if now == K:
            ans = min(ans, len(D))

    if ans == INF:
        ans = 0

    print(ans)


if __name__ == "__main__":
    main()
