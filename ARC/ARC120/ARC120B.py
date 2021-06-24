import sys
import math
from collections import Counter

sys.setrecursionlimit(1000000)
MOD = 998244353
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    H, W = NMI()
    grid = [SI() for _ in range(H)]
    is_Rs = [0] * (H+W-1)
    for h in range(H):
        for w in range(W):
            if grid[h][w] == "R":
                if is_Rs[h+w] == -1:
                    print(0)
                    exit()
                is_Rs[h+w] = 1
            elif grid[h][w] == "B":
                if is_Rs[h+w] == 1:
                    print(0)
                    exit()
                is_Rs[h+w] = -1

    C = Counter(is_Rs)
    print(pow(2, C[0], MOD))


if __name__ == "__main__":
    main()
