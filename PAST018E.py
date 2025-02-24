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
    A = []
    for _ in range(N):
        c, *a = NMI()
        A.append(set(a))
    ans = 0
    for k in range(2, N+1):
        for P in combinations(A, k):
            tmp = P[0].copy()
            for p in P:
                tmp &= p
            if all(t%2 for t in tmp):
                # print(P, tmp)
                ans += 1
    print(ans)


if __name__ == "__main__":
    main()
