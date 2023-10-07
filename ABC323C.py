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
    N, M = NMI()
    A = NLI()
    S = [SI() for _ in range(N)]
    scores = list(range(1, N+1))
    rems = [[] for _ in range(N)]
    for i, s in enumerate(S):
        for a, ss in zip(A, s):
            if ss == "o":
                scores[i] += a
            else:
                rems[i].append(a)

    for i in range(N):
        elses = scores[:]
        elses.pop(i)
        m = max(elses)
        rems[i].sort()
        now = scores[i]
        ans = 0
        while now < m:
            ans += 1
            now += rems[i].pop()
        print(ans)


if __name__ == "__main__":
    main()
