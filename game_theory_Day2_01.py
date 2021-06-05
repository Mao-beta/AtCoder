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
    T = NI()
    for _ in range(T):
        N = NI()
        A = NLI()
        g = 0
        for a in A:
            g ^= a
        print("First" if g else "Second")


if __name__ == "__main__":
    main()
