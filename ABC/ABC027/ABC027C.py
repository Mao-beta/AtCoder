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
    B = bin(N)[3:]
    L = len(B)
    if L % 2 == 0:
        # Tは0を1にできれば勝ち
        # Aは1を0にできれば勝ち
        for i, x in enumerate(B):
            if i % 2 == 0 and x == "0":
                print("Takahashi")
                exit()
            elif i % 2 == 1 and x == "1":
                print("Aoki")
                exit()

        print("Aoki")

    else:
        # Aは0を1にできれば勝ち
        # Tは1を0にできれば勝ち
        for i, x in enumerate(B):
            if i % 2 == 0 and x == "1":
                print("Takahashi")
                exit()
            elif i % 2 == 1 and x == "0":
                print("Aoki")
                exit()

        print("Takahashi")



if __name__ == "__main__":
    main()
