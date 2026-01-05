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
    N, Q = NMI()
    S = SI()
    XY = EI(Q)
    XY = [[x-1, y-1] for x, y in XY]
    is_edge = [0] * N
    for i in range(N):
        if S[i] == S[(i+1)%N] == S[(i-1)%N]:
            is_edge[i] = 0
        else:
            is_edge[i] = 1
    for x, y in XY:
        if x > y:
            x, y = y, x
        if S[x] == S[y]:
            print(1)
        elif (x == 0 and y == N-1) or y-x == 1:
            print(1)
        elif is_edge[x] == 0 and is_edge[y] == 0:
            print(3)
        else:
            print(2)


if __name__ == "__main__":
    main()
