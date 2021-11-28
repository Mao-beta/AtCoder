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
    N, M = NMI()
    A = [SI() for _ in range(2*N)]
    R = [[0, i] for i in range(2*N)] # win, id

    for m in range(M):
        R.sort(key=lambda x: (-x[0], x[1]))
        for k in range(0, 2*N, 2):
            x, y = R[k][1], R[k+1][1]
            hx, hy = A[x][m], A[y][m]

            if hx == hy:
                pass
            elif (hx == "G" and hy == "C") or (hx == "C" and hy == "P") or (hx == "P" and hy == "G"):
                R[k][0] += 1
            else:
                R[k+1][0] += 1

        R.sort(key=lambda x: (-x[0], x[1]))

    for win, ID in R:
        print(ID+1)


if __name__ == "__main__":
    main()
