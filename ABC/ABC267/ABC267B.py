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
    if S[0] == "1":
        print("No")
        exit()

    R = [3, 2, 4, 1, 3, 5, 0, 2, 4, 6]
    X = [0] * 7
    for i, s in enumerate(S):
        if s == "1":
            X[R[i]] = 1

    for l in range(7):
        for r in range(l+2, 7):
            if X[l] == 1 and X[r] == 1:
                for m in range(l+1, r):
                    if X[m] == 0:
                        print("Yes")
                        exit()

    print("No")



if __name__ == "__main__":
    main()
