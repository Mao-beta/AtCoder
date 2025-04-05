import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.set_int_max_str_digits(10 ** 6)
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
    X = NLI()
    L = NI()
    Q = NI()
    AB = EI(Q)
    # G[i][j]: iから2^j日かけて到達できるMax
    G = [[0]*20 for _ in range(N)]
    for i in range(N):
        x = X[i]
        idx = bisect.bisect_right(X, x+L)
        G[i][0] = idx-1
    for j in range(1, 20):
        for i in range(N):
            G[i][j] = G[G[i][j-1]][j-1]
    for a, b in AB:
        if a > b:
            a, b = b, a
        a, b = a-1, b-1
        ans = 0
        while a < b:
            if G[a][0] >= b:
                ans += 1<<0
                break
            for j in range(19, -1, -1):
                if G[a][j] >= b:
                    continue
                ans += 1<<j
                a = G[a][j]
                break
        print(ans)


if __name__ == "__main__":
    main()
