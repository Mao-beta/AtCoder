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


def main():
    N = NI()
    S = [list(SI()) for _ in range(N)]
    ans = 0
    for h in range(N):
        for w in range(N-1, -1, -1):
            if S[h][w] == "o":
                continue
            ans += 1
            for ww in range(w, -1, -1):
                S[h][ww] = "o"
            if h == N-1:
                continue
            for ww in range(w, N):
                S[h+1][ww] = "o"
    print(ans)


if __name__ == "__main__":
    main()
