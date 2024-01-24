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
    A = EI(9)
    for h in range(9):
        if len(set(A[h])) < 9:
            print("No")
            return
    B = list(zip(*A))
    for h in range(9):
        if len(set(B[h])) < 9:
            print("No")
            return

    for i in range(9):
        H, W = divmod(i, 3)
        tmp = []
        for h in range(3):
            for w in range(3):
                tmp.append(A[H*3+h][W*3+w])
        if len(set(tmp)) < 9:
            print("No")
            return

    print("Yes")


if __name__ == "__main__":
    main()
