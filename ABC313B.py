import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations

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
    X = [[0]*N for _ in range(N)]
    AB = [[x-1, y-1] for x, y in AB]
    for a, b in AB:
        X[a][b] = 1
        X[b][a] = -1
    
    for k in range(N):
        for i in range(N):
            for j in range(N):
                ik = X[i][k]
                kj = X[k][j]
                if ik * kj == 1:
                    X[i][j] = ik

    for i in range(N):
        if sum(X[i]) == N-1:
            print(i+1)
            exit()

    print(-1)


if __name__ == "__main__":
    main()
