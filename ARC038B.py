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
    H, W = NMI()
    B = [SI() for _ in range(H)]
    is_win = [[False]*W for _ in range(H)]

    for h in range(H-1, -1, -1):
        for w in range(W-1, -1, -1):
            win_flag = False
            for dh, dw in [[1, 0], [0, 1], [1, 1]]:
                nh, nw = h+dh, w+dw
                if not (0 <= nh < H and 0 <= nw < W):
                    continue
                if B[nh][nw] == "#":
                    continue
                if not is_win[nh][nw]:
                    win_flag = True
            is_win[h][w] = win_flag

    print("First" if is_win[0][0] else "Second")


if __name__ == "__main__":
    main()
