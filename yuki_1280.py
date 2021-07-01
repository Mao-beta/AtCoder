import sys
import math
from collections import defaultdict
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def zeta(n, dp):
    """
    高速ゼータ変換　和集合のリストから積集合のリストへ変換など
    """
    dp = dp.copy()
    for j in range(n):
        bit = 1<<j
        for i in range(1<<n):
            if i & bit == 0:
                dp[i] += dp[i | bit]
    return dp


def mobius(n, dp):
    """
    高速メビウス変換　積集合のリストから和集合のリストへ変換など
    """
    dp = dp.copy()
    for j in range(n):
        bit = 1<<j
        for i in range(1<<n):
            if i & bit == 0:
                dp[i] -= dp[i | bit]
    return dp


def lcm(a, b):
    return a*b // math.gcd(a, b)


def main():
    N, L, H = NMI()
    C = NLI()

    nums = [0]*(1<<N)

    for case in range(1<<N):
        div = 1
        for i in range(N):
            if (case>>i) & 1:
                div = lcm(div, C[i])
        nums[case] = H // div - (L-1) // div

    mob = mobius(N, nums)
    ans = 0
    for i in range(N):
        ans += mob[1<<i]
    print(ans)


if __name__ == "__main__":
    main()
