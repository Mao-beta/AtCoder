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


def print_err(*args):
    print(*args, file=sys.stderr)


def main():
    N, X = NMI()
    AB = EI(N)
    dp = [[0]*(X+1) for _ in range(N+1)]
    dp[0][0] = 1
    for i, (a, b) in enumerate(AB):
        for j in range(X+1):
            if dp[i][j] == 0:
                continue
            for x in range(b+1):
                nj = j + a * x
                if nj > X:
                    break
                if nj == X:
                    print("Yes")
                    exit()
                dp[i+1][nj] = 1
    print("No")


if __name__ == "__main__":
    main()
