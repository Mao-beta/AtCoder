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


def solve(K):
    K -= 1
    X = [1]
    for _ in range(18):
        X.append(X[-1] * 9)

    D = 0
    for d in range(1, 18):
        if K >= X[d]:
            K -= X[d]
        else:
            D = d
            break

    res = [0] * D
    # D桁
    prev = 0
    for i in range(D):
        a, K = divmod(K, X[D-1-i])
        if prev <= a:
            a += 1
        prev = a
        res[i] = a

    return "".join(map(str, res))


def main():
    T = NI()
    for _ in range(T):
        K = NI()
        res = solve(K)
        print(res)


if __name__ == "__main__":
    main()
