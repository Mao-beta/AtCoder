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
    N, M, K = NMI()
    H = sorted(NLI())
    B = sorted(NLI())
    ans = 0
    bi = 0
    for hi, h in enumerate(H):
        while bi < M:
            b = B[bi]
            if h > b:
                bi += 1
                continue
            else:
                ans += 1
                bi += 1
                break
    if ans >= K:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
