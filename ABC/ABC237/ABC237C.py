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
    S = SI()
    SR = S.rstrip("a")
    SL = S.lstrip("a")
    ra = len(S) - len(SR)
    la = len(S) - len(SL)
    S = S.strip("a")

    if S == S[::-1] and ra >= la:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
