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
    T = NI()
    for _ in range(T):
        L, R = NMI()
        if 2*L > R:
            print(0)
            continue
        ans = (R-2*L+2)*(R-2*L+1)//2
        print(ans)



if __name__ == "__main__":
    main()
