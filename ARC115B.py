import sys
import math
from collections import deque
from itertools import accumulate

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
    C = [NLI() for _ in range(N)]

    w_gaps = [C[0][i+1] - C[0][i] for i in range(N-1)]
    for row in C:
        now_gaps = [row[i + 1] - row[i] for i in range(N - 1)]
        if w_gaps != now_gaps:
            print("No")
            exit()

    h_gaps = [C[i+1][0] - C[i][0] for i in range(N-1)]
    for w in range(N):
        now_gaps = [C[i+1][w] - C[i][w] for i in range(N-1)]
        if h_gaps != now_gaps:
            print("No")
            exit()


    w_cum = [0]+list(accumulate(w_gaps))
    h_cum = [0]+list(accumulate(h_gaps))

    mw = min(w_cum)
    mh = min(h_cum)
    w_cum = [x-mw for x in w_cum]
    h_cum = [x-mh for x in h_cum]

    gap = C[0][0] - w_cum[0] - h_cum[0]
    w_cum = [x+gap for x in w_cum]

    print("Yes")
    print(*h_cum)
    print(*w_cum)


if __name__ == "__main__":
    main()
