import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

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


def solve(N, S):
    res = 0
    C = [[0]*N for _ in range(N)]
    for h in range(N):
        for w in range(N):
            if w < N-1:
                C[h][w+1] += C[h][w] + int(S[h][w] == "o")
    D = [[0] * N for _ in range(N)]
    for w in range(N):
        for h in range(N):
            if h < N-1:
                D[h+1][w] += D[h][w] + int(S[h][w] == "o")

    for h in range(N):
        for w in range(N):
            if S[h][w] == "o":
                res += C[h][w] * D[h][w]
    return res


def main():
    N = NI()
    S = [SI() for _ in range(N)]
    ans = 0
    ans += solve(N, S)
    S = S[::-1]
    ans += solve(N, S)
    S = [row[::-1] for row in S]
    ans += solve(N, S)
    S = S[::-1]
    ans += solve(N, S)
    print(ans)

if __name__ == "__main__":
    main()
