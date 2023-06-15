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
    T = NI()
    for _ in range(T):
        N = NI()
        A = NLI()
        A = [x-1 for x in A]
        G = [[] for _ in range(N)]
        for i, a in enumerate(A):
            G[i].append(a)
            G[a].append(i)

        seen = [0] * N
        G = [list(set(GG)) for GG in G]
        # print(G)

        def is_cycle(start):
            res = False
            stack = deque()
            stack.append((start, N))
            seen[start] = 1
            while stack:
                now, par = stack.pop()
                # print("start", start, "now", now)
                for g in G[now]:
                    if g == par:
                        continue
                    if seen[g]:
                        res = True
                        continue
                    stack.append((g, now))
                    seen[g] = 1

            return res

        cycles = 0
        paths = 0
        for start in range(N):
            if seen[start]:
                continue
            if is_cycle(start):
                cycles += 1
            else:
                paths += 1

        # print("cycles", cycles, "paths", paths)
        if paths == 0:
            print(cycles, cycles)
        else:
            print(cycles+1, cycles+paths)


if __name__ == "__main__":
    main()
