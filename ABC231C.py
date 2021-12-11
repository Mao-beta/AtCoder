import sys
import math
from collections import deque
import bisect

sys.setrecursionlimit(100000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    N, Q = NMI()
    A = NLI()
    A.sort()
    for _ in range(Q):
        x = NI()
        print(N - bisect.bisect_left(A, x))


if __name__ == "__main__":
    main()
