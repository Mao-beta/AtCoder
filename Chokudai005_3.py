import sys
import math
from collections import deque
from collections import Counter
sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def make_grid(h, w, num): return [[int(num)] * w for _ in range(h)]


def main():
    id, N, K = NMI()
    grid = [list(map(int, list(SI()))) for _ in range(N)]
    print(900)
    for i in range(100):
        for c in range(1, 10):
            print(51,51,c)


if __name__ == "__main__":
    main()