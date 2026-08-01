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
    N, M = NMI()
    ans = 10**10
    A = NLI()
    B = NLI()

    for t in range(2):
        X = [0] * N
        X[0] = t
        for i in range(1, N):
            X[i] = (B[i-1] - X[i-1]) % 2
        tmp = 0
        for i in range(N):
            tmp += (X[i] - A[i]) % 2
        ans = min(ans, tmp)
    print(ans)


if __name__ == "__main__":
    main()
