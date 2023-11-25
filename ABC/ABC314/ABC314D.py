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
    N = NI()
    S = list(SI())
    Q = NI()
    TXC = [SLI() for _ in range(Q)]

    U = set()
    state = -1
    for t, x, c in TXC:
        t, x = int(t), int(x)
        x -= 1
        if t == 1:
            U.add(x)
            S[x] = c
        elif t == 2:
            state = 2
            U = set()
        else:
            state = 3
            U = set()

    ans = []
    for i, s in enumerate(S):
        if i in U or state == -1:
            ans.append(s)
        elif state == 2:
            ans.append(s.lower())
        else:
            ans.append(s.upper())

    print("".join(ans))


if __name__ == "__main__":
    main()
