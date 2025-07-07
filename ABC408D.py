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
        N = NI()
        S = SI()
        z = S.count("0")
        L = [0] * (N+1)
        R = [0] * (N+1)
        for i in range(N):
            if S[i] == "1":
                L[i+1] = L[i] + 1
            else:
                L[i+1] = L[i] - 1
        for i in range(N-1, -1, -1):
            if S[i] == "1":
                R[i] = R[i+1] + 1
            else:
                R[i] = R[i+1] - 1
        L = list(accumulate(L, min))
        R = list(accumulate(R[::-1], min))[::-1]
        # print(L)
        # print(R)
        ans = z
        for i in range(N+1):
            ans = min(z+L[i]+R[i], ans)
        print(ans)


if __name__ == "__main__":
    main()
