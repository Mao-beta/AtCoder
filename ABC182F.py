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
    N, X = NMI()
    A = NLI()
    nums = []
    rem = X
    for a in A[::-1]:
        nums.append(rem // a)
        rem = rem % a
    nums = nums[::-1]
    print(nums)
    A_lim = []
    for i in range(N-1):
        A_lim.append(A[i+1]//A[i])
    A_lim.append(2**100)
    print(A_lim)

    #dp[i][j] はiコ目の数まで見て繰り上がりを持ってるかどうかのときの場合の数
    dp = [[0, 0] for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(N):
        if nums[i] == A_lim[i] - 1:
            dp[i+1][0] += dp[i][0]
            dp[i+1][1] += dp[i][1] + dp[i][0]

        elif nums[i] == 0:
            dp[i+1][0] += dp[i][0] + dp[i][1]
            dp[i+1][1] += dp[i][0]

        else:
            dp[i+1][0] += dp[i][1] + dp[i][0]
            dp[i+1][1] += dp[i][1] + dp[i][0]
    print(dp)


    last_nonzero = -1
    for i, num in enumerate(nums):
        if num != 0:
            last_nonzero = i
    leng = N - last_nonzero
    print((dp[last_nonzero][0] + dp[last_nonzero][1])*leng)


if __name__ == "__main__":
    main()
