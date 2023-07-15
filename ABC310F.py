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
    A = NLI()
    # 状態case: (case>>i)&1=1のとき、iを作れる
    # 00000000000: 11bit
    dp = [0] * (1 << 11)
    dp[1<<0] = 1
    MASK = (1 << 11) - 1
    for a in A:
        dp2 = [0] * (1 << 11)
        inva = pow(a, MOD99-2, MOD99)
        for case in range(1 << 11):
            for x in range(1, a+1):
                if x <= 10:
                    case2 = ((case << x) & MASK) | case
                    dp2[case2] += dp[case] * inva % MOD99
                    dp2[case2] %= MOD99
                else:
                    dp2[case] += dp[case] * (a-10) % MOD99 * inva % MOD99
                    dp2[case] %= MOD99
                    break
        dp, dp2 = dp2, dp

    ans = sum(dp[1<<10:]) % MOD99
    print(ans)


if __name__ == "__main__":
    main()
