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
    A, B, C = NMI()
    dp = [[[0]*101 for _ in range(101)] for _ in range(101)]
    A, B, C = sorted([A, B, C])

    if A == B == 0:
        print(100-C)
        exit()

    if A == 0:
        dp = [[0] * 101 for _ in range(101)]
        for ab in range(198, 1, -1):
            for a in range(max(1, ab-99), min(99, ab)+1):
                b = ab - a
                if not (1 <= b <= 99): continue
                res = dp[a + 1][b] * a + dp[a][b + 1] * b + a + b
                dp[a][b] = res / (a+b)
        print(dp[B][C])
        exit()


    for abc in range(297, 2, -1):
        for a in range(max(1, abc-198), min(99, abc)+1):
            rem = abc - a
            for b in range(max(1, rem-99), min(99, abc)+1):
                c = abc - a - b
                if not (1 <= c <= 99): continue
                res = dp[a+1][b][c] * a + dp[a][b+1][c] * b +dp[a][b][c+1] * c + a+ b+ c
                dp[a][b][c] = res / (a+b+c)
    print(dp[A][B][C])



if __name__ == "__main__":
    main()
