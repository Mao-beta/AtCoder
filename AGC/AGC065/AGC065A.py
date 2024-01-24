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


def calc(N, K, A):
    ans = 0
    for i in range(N - 1):
        ans += (A[i + 1] - A[i]) % K
    return ans


def guchoku(N, K, A):
    ans = 0
    ansP = None
    for P in permutations(A):
        res = calc(N, K, P)
        if res > ans:
            ans = max(ans, res)
            ansP = P
    return ans, ansP


def main(N, K, A):
    Ma = max(A)
    ma = min(A)
    C = Counter(A)

    Mc = C.most_common()[0][1]
    top = ma
    bottom = Ma
    for x, k in C.most_common():
        if k == Mc:
            top = max(top, x)
            bottom = min(bottom, x)

    ans = K * (N-1 - (Mc-1)) + bottom - top
    return ans


if __name__ == "__main__":
    # N, K = NMI()
    # A = NLI()

    import random
    N = 7

    for _ in range(100):
        K = random.randint(20, 100)
        A = [random.randint(0, K-1) for _ in range(2)] * 2
        A += [random.randint(0, K - 1) for _ in range(N-4)]

        ans = main(N, K, A)
        gu, guP = guchoku(N, K, A)
        print(ans, gu, guP)
        assert ans == gu
