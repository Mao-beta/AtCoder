import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.set_int_max_str_digits(10**6)
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
    S = [list(SI()) for _ in range(N)]
    T = [[] for _ in range(101)]
    M = len(S[0])
    for s in S:
        M = max(len(s), M)
        while len(s) < M:
            s.append("*")
        for i, ss in enumerate(s):
            T[i].append(ss)

    for row in T:
        if row:
            print("".join(row[::-1]))


if __name__ == "__main__":
    main()
