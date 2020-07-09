import sys
import math
from collections import deque
from itertools import combinations_with_replacement
from itertools import product
sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def make_grid(h, w, num): return [[int(num)] * w for _ in range(h)]


def main():
    H, W, K = NMI()
    grid = [SI() for _ in range(H)]

    n = H + W
    ans = 0
    for case in range(2**n):
        cnt = 0
        for i in range(H):
            for j in range(W):
                if (case >> i) & 1:
                    if (case >> j + H) & 1:
                        if grid[i][j] == "#":
                            cnt += 1
        if cnt == K:
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()