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
    S = SI()
    for i, s in enumerate(S):
        if s == "1":
            print("Takahashi" if i % 2 == 0 else "Aoki")
            exit()


if __name__ == "__main__":
    main()
