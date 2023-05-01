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
    N = NI()
    S = list(map(int, SI()))
    X = [0] * (N+1)

    X[0] = 1
    X[1] = S[0]
    c = 1
    for i in range(2, N+1):
        c = (c + X[i - 1]) % MOD99
        X[i] = (X[i-1] * 10 + c * S[i-1]) % MOD99

    Y = [0]
    for i in range(N-1, -1, -1):
        Y.append((Y[-1] + S[i] * pow(10, N-1-i, MOD99)) % MOD99)
    Y = Y[::-1]

    # print(X)
    # print(Y)

    ans = 0
    for x, y in zip(X, Y):
        ans += x * y % MOD99
        ans %= MOD99

    print(ans)


if __name__ == "__main__":
    main()
