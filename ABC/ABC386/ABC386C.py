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
    K = NI()
    S = SI()
    T = SI()
    N, M = len(S), len(T)
    if abs(N-M) >= 2:
        print("No")
    elif N == M:
        tmp = 0
        for s, t in zip(S, T):
            if s != t:
                tmp += 1
        if tmp <= 1:
            print("Yes")
        else:
            print("No")
    else:
        if N < M:
            S, T = T, S
            N, M = M, N
        l = 0
        for i in range(M):
            if S[i] == T[i]:
                l += 1
            else:
                break
        r = 0
        for i in range(M):
            if S[N-1-i] == T[M-1-i]:
                r += 1
            else:
                break
        if l + r >= M:
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    main()
