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
EI = lambda m: [tuple(NMI()) for _ in range(m)]


def main():
    N = NI()
    F = []
    for i in range(5):
        for x in NMI():
            F.append((x, i))
    F.sort()

    L = [0] * 5
    R = [N] * 5
    ans = 0
    for x, alp in F:
        R[alp] -= 1
        others = set(range(5))
        others.discard(alp)

        for left in combinations(others, 2):
            right = others - set(left)
            tmp = 1
            for l in left:
                tmp *= L[l]
                tmp %= MOD99
            for r in right:
                tmp *= R[r]
                tmp %= MOD99

            ans += tmp * x % MOD99
            ans %= MOD99

        L[alp] += 1
    print(ans)


if __name__ == "__main__":
    main()
