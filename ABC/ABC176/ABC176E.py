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
    H, W, M = NMI()
    bombs = defaultdict(int)
    rows = [0]*H
    cols = [0]*W
    for _ in range(M):
        h, w = NMI()
        h, w = h-1, w-1
        bombs[h * 10**6 + w] = 1
        rows[h] += 1
        cols[w] += 1
    rows_i = [[r, i] for i, r in enumerate(rows)]
    cols_i = [[c, i] for i, c in enumerate(cols)]
    rows_i.sort(reverse=True)
    cols_i.sort(reverse=True)

    rmax = rows_i[0][0]
    cmax = cols_i[0][0]
    for r, i in rows_i:
        if r <= rmax - 1:
            break
        for c, j in cols_i:
            if c <= cmax - 1:
                break
            if i * 10**6 + j not in bombs:
                print(rmax + cmax)
                exit()
    print(cmax+rmax-1)


if __name__ == "__main__":
    main()