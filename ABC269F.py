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
    N, M = NMI()
    Q = NI()
    querys = [NLI() for _ in range(Q)]
    inv2 = pow(2, MOD99-2, MOD99)

    def g(i, j):
        return ((i-1) * M + j) % MOD99

    for a, b, c, d in querys:
        h = (b-a+1)
        w = (d-c+1)

        ac = g(a, c)
        bd = g(b, d)
        m = (ac + bd) * inv2

        ans = 0
        total = m % MOD99 * h % MOD99 * w % MOD99

        if h % 2 and w % 2:
            if (a + c) % 2:
                n = h * w // 2
                ans = m * n % MOD99
            else:
                n = h * w // 2 + 1
                ans = m * n % MOD99

        elif h % 2 == 0 and w % 2:
            if (a + d) % 2:
                gap = h // 2 * M % MOD99
                ans = (total + gap) * inv2 % MOD99
            else:
                gap = h // 2 * M % MOD99
                ans = (total - gap) * inv2 % MOD99

        elif h % 2 and w % 2 == 0:
            if (b + c) % 2:
                gap = w // 2 % MOD99
                ans = (total + gap) * inv2 % MOD99
            else:
                gap = w // 2 % MOD99
                ans = (total - gap) * inv2 % MOD99

        else:
            ans = total * inv2 % MOD99

        print(ans)


if __name__ == "__main__":
    main()
