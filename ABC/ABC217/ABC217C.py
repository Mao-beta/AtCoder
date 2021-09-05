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


def main():
    N = NI()
    P = NLI()
    Q = [0] * N
    for i, p in enumerate(P, start=1):
        p -= 1
        Q[p] = i
    print(*Q)


if __name__ == "__main__":
    main()
