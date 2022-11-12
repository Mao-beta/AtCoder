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


def main():
    N = NI()
    S = [SI() for _ in range(N)]

    for s in S:
        if s[0] not in "HDCS":
            print("No")
            exit()
        if s[1] not in "A23456789TJQK":
            print("No")
            exit()

    if len(set(S)) != N:
        print("No")
    else:
        print("Yes")


if __name__ == "__main__":
    main()
