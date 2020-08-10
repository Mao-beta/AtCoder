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
    K = NI()
    tmp = 7
    for i in range(1000005):

        if tmp % K == 0:
            print(i+1)
            exit()
        tmp = tmp * 10 + 7
        tmp = tmp % K
    print(-1)


if __name__ == "__main__":
    main()