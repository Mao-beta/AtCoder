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



def main():
    H, W = NMI()
    grid = [SI() for _ in range(H)]

    dp = [[0]*W for _ in range(H)]

    def hw_to_p(h, w):
        return 1 if grid[h][w] == "+" else -1

    for h in range(H-1, -1, -1):
        for w in range(W-1, -1, -1):
            if h == H-1 and w == W-1: continue
            is_Taka = True if (h+w)%2 == 0 else False

            if is_Taka:
                if h == H-1:
                    dp[h][w] = dp[h][w + 1] + hw_to_p(h, w + 1)
                elif w == W-1:
                    dp[h][w] = dp[h + 1][w] + hw_to_p(h + 1, w)
                else:
                    dp[h][w] = max(dp[h+1][w] + hw_to_p(h+1, w), dp[h][w+1] + hw_to_p(h, w+1))
            else:
                if h == H-1:
                    dp[h][w] = dp[h][w + 1] - hw_to_p(h, w + 1)
                elif w == W-1:
                    dp[h][w] = dp[h + 1][w] - hw_to_p(h + 1, w)
                else:
                    dp[h][w] = min(dp[h + 1][w] - hw_to_p(h + 1, w), dp[h][w + 1] - hw_to_p(h, w + 1))

    C = dp[0][0]
    if C > 0:
        print("Takahashi")
    elif C < 0:
        print("Aoki")
    else:
        print("Draw")


if __name__ == "__main__":
    main()
