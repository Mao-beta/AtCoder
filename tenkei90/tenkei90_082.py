import sys
import math
from collections import deque

sys.setrecursionlimit(100000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def solve(N):
    # 0以上N以下について求める
    K = len(str(N))
    res = 0
    for k in range(1, K+1):
        if k != K:
            # k==3なら100以上1000未満の900個の総和×k
            l = 10**(k-1)
            r = l * 10 - 1
        else:
            l = 10**(k-1)
            r = N

        n = (l + r) * (r - l + 1) // 2
        res += n * k
        res %= MOD

    return res


def main():
    L, R = NMI()
    ans = solve(R) - solve(L-1)
    print(ans % MOD)


if __name__ == "__main__":
    main()
