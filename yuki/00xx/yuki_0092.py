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


def main():
    N, M, K = NMI()
    ABC = EI(M)
    C2I = defaultdict(list)
    for a, b, c in ABC:
        C2I[c].append([a, b])
    D = NLI()
    S = set(range(1, N+1))
    for d in D:
        T = set()
        for a, b in C2I[d]:
            if a in S:
                T.add(b)
            if b in S:
                T.add(a)
        S = T
    print(len(S))
    print(*sorted(list(S)))


if __name__ == "__main__":
    main()
