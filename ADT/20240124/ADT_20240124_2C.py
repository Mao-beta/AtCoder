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
EI = lambda m: [NLI() for _ in range(m)]


def main():
    N = NI()
    A = [SI() for _ in range(N)]
    for i in range(N):
        for j in range(i+1, N):
            if A[i][j] == "W" and A[j][i] != "L":
                print("incorrect")
                return
            if A[i][j] != "L" and A[j][i] == "W":
                print("incorrect")
                return
            if A[i][j] == "L" and A[j][i] != "W":
                print("incorrect")
                return
            if A[i][j] != "W" and A[j][i] == "L":
                print("incorrect")
                return
            if A[i][j] == "D" and A[j][i] != "D":
                print("incorrect")
                return
            if A[i][j] != "D" and A[j][i] == "D":
                print("incorrect")
                return
    print("correct")


if __name__ == "__main__":
    main()
