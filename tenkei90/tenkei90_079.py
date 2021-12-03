import sys
import math
from collections import defaultdict
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
    A = [NLI() for _ in range(H)]
    B = [NLI() for _ in range(H)]
    G = [[0]*W for _ in range(H)]
    for h in range(H):
        for w in range(W):
            G[h][w] = B[h][w] - A[h][w]

    ans = 0
    for h in range(H-1):
        for w in range(W-1):
            g = G[h][w]
            G[h][w] -= g
            G[h+1][w] -= g
            G[h][w+1] -= g
            G[h+1][w+1] -= g
            ans += abs(g)

    for h in range(H):
        for w in range(W):
            if G[h][w] != 0:
                print("No")
                exit()

    print("Yes")
    print(ans)


if __name__ == "__main__":
    main()
