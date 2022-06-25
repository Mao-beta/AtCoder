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


def main():
    N = NI()
    S = list(map(int, SI()))
    W = NLI()
    WS = [[w, int(s)] for w, s in zip(W, S)]
    WS.sort()

    f = sum(S)
    ans = f

    for i, (w, s) in enumerate(WS):
        if s == 0:
            f += 1
        else:
            f -= 1

        if i == N-1 or WS[i+1][0] != w:
            ans = max(ans, f)

    print(ans)


if __name__ == "__main__":
    main()
