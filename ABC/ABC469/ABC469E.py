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
    N, K = NMI()
    S = [int(s == "o") for s in SI()]
    R2L = [-1] * (N+1)
    l = N
    k = 0
    for r in range(N, 0, -1):
        if l > r:
            l = r
            k = 0
        while l > 0 and k < K:
            if S[l-1] == 1:
                k += 1
            l -= 1
        if k >= K:
            R2L[r] = l
        if S[r-1] == 1:
            k -= 1


    def judge(X):
        T = list(accumulate([0]+[s-X for s in S]))
        M = list(accumulate(T, min))
        for r in range(N, 0, -1):
            if R2L[r] < 0:
                break
            if T[r] - M[R2L[r]] >= 0:
                return True
        return False

    ok = 0
    ng = 1
    for _ in range(30):
        X = (ok + ng) / 2
        if judge(X):
            ok = X
        else:
            ng = X

    print(ok)


if __name__ == "__main__":
    main()
