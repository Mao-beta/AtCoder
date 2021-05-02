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
    N = NI()
    A = NLI()
    colors = []
    for c, num in enumerate(A, 1):
        colors += [c] * num
    ans = [[0]*W for _ in range(H)]
    idx = 0
    for h in range(H):
        if h % 2 == 0:
            for w in range(W):
                ans[h][w] = colors[idx]
                idx += 1

        else:
            for w in range(W-1, -1, -1):
                ans[h][w] = colors[idx]
                idx += 1

    for row in ans:
        print(*row)


if __name__ == "__main__":
    main()
