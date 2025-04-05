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
    T = NI()
    for _ in range(T):
        _N, K = NMI()
        K -= 1
        N = bin(_N)[2:]
        Z = N.count("0")
        R = [0] * len(N)
        for i in range(len(N)):
            if N[i] == "0" and K >= 2**(Z-1):
                R[i] = 1
                K -= 2**(Z-1)
            if N[i] == "0":
                Z -= 1
        if K > 0:
            print(-1)
        else:
            R = "".join(map(str, R))
            print(int(R, 2) + _N)


if __name__ == "__main__":
    main()
