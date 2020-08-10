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
    XYH = [NLI() for _ in range(N)]
    XYH.sort(key= lambda x: x[2], reverse=True)
    H = 10**10
    for cx in range(101):
        for cy in range(101):
            is_badc = False
            for i, xyh in enumerate(XYH):
                x, y, h = xyh
                if i == 0:
                    H = h + abs(cx - x) + abs(cy - y)
                else:
                    if max(H - abs(cx-x) - abs(cy-y), 0) != h:
                        is_badc = True

            if not is_badc:
                print(cx, cy, H)
                exit()



if __name__ == "__main__":
    main()