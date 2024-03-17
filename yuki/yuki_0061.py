import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
MOD99 = 998244353

input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()
SMI = lambda: input().split()
SLI = lambda: list(SMI())
EI = lambda m: [NLI() for _ in range(m)]


def main():
    Q = NI()
    for qi in range(Q):
        W, H, D, Mx, My, Hx, Hy, Vx, Vy = NMI()
        XY = [[0]*(H+1) for _ in range(W+1)]
        XY[Hx][Hy] = 1
        g = math.gcd(Vx, Vy)
        if Vx == 0:
            D *= abs(Vy)
            Vy //= abs(Vy)
        elif Vy == 0:
            D *= abs(Vx)
            Vx //= abs(Vx)
        else:
            Vx //= g
            Vy //= g

        nx, ny = Hx, Hy
        while D > 0:
            nx += Vx
            ny += Vy
            D = min(D, 4*(H+1)*(W+1))
            while True:
                if nx < 0:
                    nx = -nx
                    Vx = -Vx
                if nx > W:
                    nx = 2*W - nx
                    Vx = -Vx
                if ny < 0:
                    ny = -ny
                    Vy = -Vy
                if ny > H:
                    ny = 2*H - ny
                    Vy = -Vy
                if 0 <= nx <= W and 0 <= ny <= H:
                    break

            XY[nx][ny] = 1
            D -= 1
        if XY[Mx][My]:
            print("Hit")
        else:
            print("Miss")



if __name__ == "__main__":
    main()
