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
        N, C = NMI()
        C -= 1
        S = [list(SI()) for _ in range(N)]

        dp = [[0]*N for _ in range(N)]
        for h in range(N):
            dp[h][C] = 1
        low = [0] * N
        for h in range(N):
            for w in range(N):
                if S[h][w] == "#":
                    low[w] = max(low[w], h)

        for h in range(N-2, -1, -1):
            for w in range(N):
                if dp[h][w]:
                    continue
                ok = False
                if w-1 >= 0 and dp[h+1][w-1]:
                    ok = True
                if dp[h+1][w]:
                    ok = True
                if w+1 < N and dp[h+1][w+1]:
                    ok = True
                if not ok:
                    continue
                if S[h][w] == ".":
                    dp[h][w] = 1
                    continue
                if low[w] == h:
                    for hh in range(h+1):
                        dp[hh][w] = 1

        ans = ["1" if s > 0 else "0" for s in dp[0]]
        print("".join(ans))


if __name__ == "__main__":
    main()
