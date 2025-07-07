import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.set_int_max_str_digits(10 ** 6)
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
    N, C = NMI()
    A = [NI() for _ in range(N)]
    A = [x-1 for x in A]
    ans = 10**20
    for x in range(10):
        for y in range(10):
            if x == y:
                continue
            B = [x, y] * N
            tmp = 0
            for a, b in zip(A, B):
                if a != b:
                    tmp += C
            ans = min(ans, tmp)
            B = [y, x] * N
            tmp = 0
            for a, b in zip(A, B):
                if a != b:
                    tmp += C
            ans = min(ans, tmp)
    print(ans)


if __name__ == "__main__":
    main()
