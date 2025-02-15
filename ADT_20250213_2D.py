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
    A = EI(M)
    X = [[1]*N for _ in range(N)]
    for i in range(N):
        X[i][i] = 0
    for a in A:
        for i in range(N-1):
            X[a[i]-1][a[i+1]-1] = 0
            X[a[i+1]-1][a[i]-1] = 0
    ans = 0
    for x in X:
        ans += sum(x)
    print(ans // 2)


if __name__ == "__main__":
    main()
