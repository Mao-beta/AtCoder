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
        N, K = NMI()
        ans = [1 << (K-1)] * N
        for b in range(K-1, -1, -1):
            B = 1 << b
            r = 1 << (K-1-b)
            for i in range(N):
                ans[i] += B * int((i % r)<(r>>1))
        print(*ans)


if __name__ == "__main__":
    main()
