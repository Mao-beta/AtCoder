import sys
import math
from collections import deque

sys.setrecursionlimit(100000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    H, W = NMI()
    G = [list(SI()) for _ in range(H)]

    ALL = {"1", "2", "3", "4", "5"}
    for h in range(H):
        for w in range(W):
            if G[h][w] != ".": continue
            adj = set()
            for dh, dw in [[-1, 0], [0, 1], [0, -1], [1, 0]]:
                nh, nw = h+dh, w+dw
                if nh < 0 or nh >= H or nw < 0 or nw >= W:
                    continue
                if G[nh][nw] == ".": continue
                adj.add(G[nh][nw])

            rem = ALL - adj
            G[h][w] = rem.pop()

    for row in G:
        print("".join(row))



if __name__ == "__main__":
    main()
