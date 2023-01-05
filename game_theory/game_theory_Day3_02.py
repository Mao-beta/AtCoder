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
    T = NI()
    Grundy = [[0]*15 for _ in range(15)]

    D = [(-2, 1), (-2, -1), (1, -2), (-1, -2)]
    for s in range(29):
        for x in range(15):
            y = s - x
            if not (0 <= y < 15):
                continue
            Gxy = set()
            for dx, dy in D:
                nx, ny = x+dx, y+dy
                if not (0 <= nx < 15 and 0 <= ny < 15):
                    continue
                Gxy.add(Grundy[nx][ny])
            for g in range(10):
                if g not in Gxy:
                    Grundy[x][y] = g
                    break

    for _ in range(T):
        K = NI()
        XY = [NLI() for _ in range(K)]
        G = 0
        for x, y in XY:
            x, y = x-1, y-1
            G ^= Grundy[x][y]
        print("First" if G else "Second")


if __name__ == "__main__":
    main()
