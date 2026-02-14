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
    AB = EI(M)
    AB = [[x-1, y-1] for x, y in AB]
    G = [[0]*N for _ in range(N)]
    for a, b in AB:
        G[a][b] = 1
        G[b][a] = 1
    ans = 10**18
    E = [(i, j) for i in range(N) for j in range(i+1, N)]
    for C in combinations(E, N):
        # print(C)
        D = [0] * N
        res = M + N
        for a, b in C:
            D[a] += 1
            D[b] += 1
            if G[a][b]:
                res -= 2
        if min(D) == max(D) == 2:
            ans = min(ans, res)
    print(ans)


if __name__ == "__main__":
    main()
