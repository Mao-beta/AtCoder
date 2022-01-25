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
    N, M = NMI()
    S = SLI()
    T = SLI()
    ans = ["No"] * N
    D = {s: i for i, s in enumerate(S)}
    for t in T:
        ans[D[t]] = "Yes"
    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
