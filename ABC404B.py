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
    S = [SI() for _ in range(N)]
    T = [SI() for _ in range(N)]

    def rot(X):
        Y = [["." for _ in range(N)] for _ in range(N)]
        for i in range(N):
            for j in range(N):
                Y[j][N-i-1] = X[i][j]
        return Y

    ans = N**2
    for r in range(4):
        res = r
        for i in range(N):
            for j in range(N):
                if S[i][j] != T[i][j]:
                    res += 1
        S = rot(S)
        ans = min(ans, res)
    print(ans)


if __name__ == "__main__":
    main()
