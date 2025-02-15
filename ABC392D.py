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
    N = NI()
    P = [[] for _ in range(10**5+1)]
    D = [[0] * N for _ in range(N)]
    for i in range(N):
        K, *A = NMI()
        C = Counter(A)
        for a, k in C.items():
            for x, j in P[a]:
                D[i][j] += x * k / K
                D[j][i] += x * k / K
            P[a].append([k/K, i])
    ans = 0
    for i in range(N):
        ans = max(ans, max(D[i]))
    print(ans)


if __name__ == "__main__":
    main()
