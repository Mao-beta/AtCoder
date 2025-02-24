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
    Q = NI()
    first = 0
    L = [0]
    for _ in range(Q):
        qi, *X = NMI()
        if qi == 1:
            L.append(L[-1] + X[0])
        elif qi == 2:
            first += 1
        else:
            ans = L[X[0]-1+first] - L[first]
            print(ans)


if __name__ == "__main__":
    main()
