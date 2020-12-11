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


def make_grid_int(h, w, num): return [[int(num)] * w for _ in range(h)]


def main():
    R, C, K = NMI()
    grid = make_grid_int(R, C, 0)
    for i in range(K):
        r, c, v = NMI()
        grid[r-1][c-1] = v

    dp0 = [[0 for _ in range(C + 2)] for _ in range(R + 2)]
    dp1 = [[0 for _ in range(C + 2)] for _ in range(R + 2)]
    dp2 = [[0 for _ in range(C + 2)] for _ in range(R + 2)]
    dp3 = [[0 for _ in range(C + 2)] for _ in range(R + 2)]

    for r in range(R+1):
        for c in range(C+1):
            now0 = dp0[r][c]
            now1 = dp1[r][c]
            now2 = dp2[r][c]
            now3 = dp3[r][c]
            try:
                val = grid[r][c]
            except:
                val = 0

            dp0[r+1][c] = max(now3, dp0[r+1][c])

            # 取って下
            dp0[r+1][c] = max(now0 + val, now1 + val, now2 + val, dp0[r+1][c])
            # 取らずに下
            dp0[r+1][c] = max(now0, now1, now2, now3, dp0[r+1][c])
            # 取って横
            dp1[r][c+1] = max(now0 + val, dp1[r][c+1])
            dp2[r][c+1] = max(now1 + val, dp2[r][c+1])
            dp3[r][c+1] = max(now2 + val, dp3[r][c+1])

            # 取らずに横
            dp1[r][c+1] = max(now1, dp1[r][c+1])
            dp2[r][c+1] = max(now2, dp2[r][c+1])
            dp0[r][c+1] = max(now0, dp0[r][c+1])

    print(max(dp0[R][C], dp1[R][C], dp2[R][C], dp3[R][C]))


if __name__ == "__main__":
    main()
