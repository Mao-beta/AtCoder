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


def main():
    N = NI()
    can_match = [NLI() for _ in range(N)]

    # dp[case] 女の状態がcaseのときの場合の数
    dp = [0]*(1<<N)
    dp[0] = 1

    for case in range((1<<N)-1):
        i = bin(case).count("1")
        can_i = can_match[i]

        for female, is_ok in enumerate(can_i):
            if not is_ok: continue
            if (case>>female) & 1: continue

            next_case = case + (1<<female)
            dp[next_case] += dp[case]
            dp[next_case] %= MOD

    print(dp[-1])


if __name__ == "__main__":
    main()
