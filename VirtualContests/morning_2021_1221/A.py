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
    h1, m1, h2, m2, K = NMI()
    t = (h2 - h1) * 60 + (m2 - m1)
    print(t - K)


if __name__ == "__main__":
    main()
