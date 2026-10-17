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


def make_grid(h, w, num): return [[int(num)] * w for _ in range(h)]


def main():
    N = NI()
    Q = NI()
    querys = [NLI() for _ in range(Q)]
    col = [i for i in range(N)]
    row = [i for i in range(N)]
    t_flag = False
    for query in querys:
        if query[0] == 3:
            t_flag = not t_flag
            continue

        x, a, b = query[0], query[1]-1, query[2]-1
        if x == 4:
            if t_flag:
                a, b = b, a
            r, c = row[a], col[b]
            print(N*r + c)

        if t_flag:
            x = 3 - x
        if x == 1:
            row[a], row[b] = row[b], row[a]
            continue

        if x == 2:
            col[a], col[b] = col[b], col[a]
            continue




if __name__ == "__main__":
    main()