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
    S = SI()
    X, Y = NMI()

    x_list = []
    y_list = []
    is_first_move = True

    num = 0
    is_y = True
    for i, s in enumerate(S):
        if is_first_move:
            if s == "F":
                X -= 1
            else:
                is_first_move = False

        else:
            if s == "F":
                num += 1
            else:
                if is_y:
                    y_list.append(num)
                else:
                    x_list.append(num)
                num = 0
                is_y = not is_y

    if is_y:
        y_list.append(num)
    else:
        x_list.append(num)

    N = len(S)
    XN = len(x_list)
    YN = len(y_list)
    X_dp = [0]*(2*N+2)
    Y_dp = [0]*(2*N+2)

    X_dp[N] = 1
    Y_dp[N] = 1

    for i, f in enumerate(x_list):
        tmp_dp = [0]*(2*N+2)
        for x in range(2*N+2):
            xm = x - f
            xp = x + f
            if 0 <= xm <= 2*N+1:
                tmp_dp[xm] = tmp_dp[xm] | X_dp[x]
            if 0 <= xp <= 2*N+1:
                tmp_dp[xp] = tmp_dp[xp] | X_dp[x]
        X_dp = tmp_dp

    for i, f in enumerate(y_list):
        tmp_dp = [0] * (2 * N + 2)
        for y in range(2*N+2):
            ym = y - f
            yp = y + f
            if 0 <= ym <= 2*N+1:
                tmp_dp[ym] = tmp_dp[ym] | Y_dp[y]
            if 0 <= yp <= 2*N+1:
                tmp_dp[yp] = tmp_dp[yp] | Y_dp[y]
        Y_dp = tmp_dp

    print("Yes" if X_dp[N+X] & Y_dp[N+Y] else "No")



if __name__ == "__main__":
    main()
