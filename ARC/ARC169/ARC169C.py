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


def main():
    N = NI()
    A = NLI()
    dp = [deque() for _ in range(N+1)]
    sums = [0] * (N+1)
    total = 0

    if A[0] == -1:
        for i in range(1, N+1):
            dp[i].appendleft(1)
            total += 1
            sums[i] += 1
    else:
        for i in range(1, N+1):
            if A[0] == i:
                dp[i].appendleft(1)
                total += 1
                sums[i] += 1
            else:
                dp[i].appendleft(0)

    for ai in range(1, N):
        vals = [0] + [total - sums[i] for i in range(1, N+1)]

        if A[ai] == -1:
            for i in range(1, N+1):
                val = vals[i]
                dp[i].appendleft(val)
                total += val
                sums[i] += val

            for i in range(1, N + 1):
                if len(dp[i]) > i:
                    x = dp[i].pop()
                    total -= x
                    sums[i] -= x
        else:
            a = A[ai]
            val = total - sums[a]
            dp[a].appendleft(val)
            total += val
            sums[a] += val

            for i in range(1, N+1):
                if A[ai] != i:
                    dp[i] = deque([0])
                    total -= sums[i]
                    sums[i] = 0

            if len(dp[a]) > a:
                x = dp[a].pop()
                total -= x
                sums[a] -= x

        total %= MOD99
        for i in range(1, N + 1):
            sums[i] %= MOD99

    print(total % MOD99)



if __name__ == "__main__":
    main()
