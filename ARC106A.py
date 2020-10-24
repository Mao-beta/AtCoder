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
    for a in range(1, 40):
        for b in range(1, 31):
            if N == 3**a + 5**b:
                print(a, b)
                exit()
    print(-1)


if __name__ == "__main__":
    main()
