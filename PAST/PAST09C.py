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
    PV = [SLI() + [i+1] for i in range(N)]
    ans = [0] * 6
    for x, j, i in PV[::-1]:
        if j == "WA": continue
        x = ord(x) - ord("A")
        ans[x] = i
    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
