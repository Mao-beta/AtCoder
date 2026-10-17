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
    N = NI()
    PEs = []
    for _ in range(N):
        m = NI()
        PEs.append(EI(m))

    CP = defaultdict(Counter)
    for i, PE in enumerate(PEs):
        for p, e in PE:
            CP[p][i] = e

    tops = [0] * N
    for p, C in CP.items():
        MC = list(C.most_common())
        if len(MC) == 1:
            tops[MC[0][0]] = 1
        else:
            if MC[0][1] == MC[1][1]:
                continue
            tops[MC[0][0]] = 1

    print(sum(tops) + int(min(tops) == 0))


if __name__ == "__main__":
    main()
