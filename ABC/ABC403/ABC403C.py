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
    N, M, Q = NMI()
    D = set()
    ok = [0] * (N+1)
    for _ in range(Q):
        qi, *X = NMI()
        if qi == 1:
            x, y = X
            D.add((x, y))
        elif qi == 2:
            ok[X[0]] = 1
        else:
            x, y = X
            if ok[x] or (x, y) in D:
                print("Yes")
            else:
                print("No")


if __name__ == "__main__":
    main()
