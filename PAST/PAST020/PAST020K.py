import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.set_int_max_str_digits(10**6)
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
    M = NI()
    A = EI(4)

    def f(T):
        res = 0
        for x in T:
            res <<= 5
            res += x
        return res

    def g(r):
        return C>>15, (C>>10)%32, (C>>5)%32, C%32

    # (-4, -3, -2, -1)
    dp = [0] * (1<<20)
    for C in combinations(range(1, M+1), 4):
        ok = True
        for w in range(4):
            if A[0][w] == C[w] or A[0][w] == -1:
                pass
            else:
                ok = False
        if ok:
            dp[f(C)] = 1

    # print(dp[:200])

    for h in range(1, 4):
        for w in range(4):
            dp2 = [0] * (1<<20)
            for C, d in enumerate(dp):
                if d == 0:
                    continue
                gc = g(C)
                # print(h, w, (C>>15, (C>>10)%32, (C>>5)%32, C%32), d, A[h][w])
                if A[h][w] == -1:
                    for x in range(gc[-4]+1, M+1):
                        if w > 0 and x <= gc[-1]:
                            continue
                        nc = f((*gc[1:], x))
                        # print(nc)
                        dp2[nc] += d
                        dp2[nc] %= MOD99
                else:
                    x = A[h][w]
                    if x <= gc[-4]:
                        continue
                    if w > 0 and x <= gc[-1]:
                        continue
                    nc = f((*gc[1:], x))
                    # print(nc)
                    dp2[nc] += d
                    dp2[nc] %= MOD99

            dp, dp2 = dp2, dp

    # print(dp.values())
    ans = sum(dp) % MOD99
    print(ans)


if __name__ == "__main__":
    main()
