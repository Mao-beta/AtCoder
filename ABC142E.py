import sys
import math
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def make_grid(h, w, num): return [[int(num)] * w for _ in range(h)]


def main():
    N, M = NMI()
    keys = {}
    for i in range(M):
        a, b = NMI()
        C = NLI()
        case = 0
        for c in C:
            case += 2**(c-1)
        keys[i+1] = (a, case)

    dp = [[10**10] * (2**N) for _ in range(M+1)]
    dp[0][0] = 0

    for key in range(0, M):
        for case in range(2**N):
            if dp[key][case] == 10**10:
                continue
            next_case = case | keys[key+1][1]
            dp[key+1][next_case] = min(dp[key][case] + keys[key+1][0], dp[key+1][next_case])
            dp[key+1][case] = min(dp[key][case], dp[key+1][case])
    ans = dp[M][2**N-1]
    print(ans if ans < 10**10 else -1)



if __name__ == "__main__":
    main()