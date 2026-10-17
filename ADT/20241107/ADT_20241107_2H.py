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
    A = NLI()
    S = [SI() for _ in range(N)]
    Q = NI()
    UV = EI(Q)
    UV = [[x-1, y-1] for x, y in UV]
    INF = 10**12
    D = [[INF*1000]*N for _ in range(N)]
    for i in range(N):
        # D[i][i] = 0
        for j in range(N):
            if i == j:
                continue
            if S[i][j] == "N":
                continue
            D[i][j] = INF - A[j]
    for k in range(N):
        for i in range(N):
            for j in range(N):
                D[i][j] = min(D[i][j], D[i][k] + D[k][j])
    # print(*D, sep="\n")
    for u, v in UV:
        num, ma = divmod(D[u][v], INF)
        # print("#", num, ma)
        if ma > 0:
            num += 1
            ma -= INF
        a = -ma
        if num > N:
            print("Impossible")
        else:
            print(num, a+A[u])


if __name__ == "__main__":
    main()
