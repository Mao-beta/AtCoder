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
    A = NLI()
    S = [SI() for _ in range(N)]
    P = [i+1 for i in range(N)]
    C = [[] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            s = S[i][j]
            if s == "o":
                P[i] += A[j]
            else:
                C[i].append(A[j])
    for i in range(N):
        M = max(P[:i] + P[i+1:])
        C[i].sort(reverse=True)
        now = P[i]
        ans = 0
        for k, c in enumerate(C[i], start=1):
            if now > M:
                break
            ans = k
            now += c
        print(ans)


if __name__ == "__main__":
    main()
