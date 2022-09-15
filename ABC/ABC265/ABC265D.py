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
    N, P, Q, R = NMI()
    A = NLI()
    C = list(accumulate([0]+A)) + [10**20]

    for x in range(N):
        start = C[x]
        y = bisect.bisect_left(C, start+P)
        if C[y] == start+P:
            z = bisect.bisect_left(C, start+P+Q)
            if C[z] == start+P+Q:
                w = bisect.bisect_left(C, start + P + Q + R)
                if C[w] == start + P + Q + R:
                    print("Yes")
                    exit()

    print("No")


if __name__ == "__main__":
    main()
