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
    N, A, B = NMI()
    S = (1 + N) * N // 2

    A, B = min(A, B), max(A, B)
    L = A * B // math.gcd(A, B)

    Ak = N // A
    Bk = N // B
    ABk = N // L

    def f(k, x):
        # xの倍数k個以下の和
        return (1+k) * k // 2 * x

    if B % A == 0:
        ans = S - f(Ak, A)
        print(ans)
        exit()

    ans = S - f(Ak, A) - f(Bk, B) + f(ABk, L)
    print(ans)


if __name__ == "__main__":
    main()
