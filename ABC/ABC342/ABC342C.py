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
    S = SI()
    Q = NI()
    CD = [SLI() for _ in range(Q)]
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    A = {s: s for s in alphabets}
    for c, d in CD:
        for a, x in list(A.items()):
            if x == c:
                A[a] = d
    S = list(S)
    for i, s in enumerate(S):
        S[i] = A[s]
    print("".join(S))


if __name__ == "__main__":
    main()
