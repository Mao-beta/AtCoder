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
    N, X, Y = NMI()
    counts = [0] * N
    for i in range(1, N):
        for j in range(i+1, N+1):
            dist = min(abs(j-i), abs(i-X) + 1 + abs(Y-j))
            counts[dist] += 1

    for d in counts[1:]:
        print(d)


if __name__ == "__main__":
    main()