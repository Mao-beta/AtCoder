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


def main():
    N = NI()
    A = [NLI() for _ in range(N-1)]
    ans = -10**10
    for X in product([0, 1, 2], repeat=N):
        tmp = 0
        for i in range(N):
            for j in range(i+1, N):
                if X[i] == X[j]:
                    # print(i, j)
                    tmp += A[i][j-i-1]
        ans = max(ans, tmp)

    print(ans)



if __name__ == "__main__":
    main()
