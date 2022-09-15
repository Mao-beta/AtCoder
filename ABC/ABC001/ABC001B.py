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
    M = NI()
    if M < 100:
        print("00")
    elif M <= 5000:
        print(str(M)[:-2].zfill(2))
    elif M <= 30000:
        print(M // 1000 + 50)
    elif M <= 70000:
        print((M // 1000 - 30) // 5 + 80)
    else:
        print(89)


if __name__ == "__main__":
    main()
