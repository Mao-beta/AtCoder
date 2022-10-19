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


def main():
    X, Y = map(int, SI().split("/"))
    g = math.gcd(X, Y)
    X //= g
    Y //= g
    n = int(2 * X / Y)
    ans = []
    for N in range(max(1, n-100), max(1, n+100)):
        if N * X % Y:
            continue
        M = N * (N+1) // 2 - N * X // Y
        if N < M or M < 1:
            continue
        ans.append([N, M])

    if ans:
        for row in ans:
            print(*row)
    else:
        print("Impossible")


if __name__ == "__main__":
    main()
