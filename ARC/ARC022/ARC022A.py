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
    S = SI()
    i, c, t = 0, 0, 0
    for s in S:
        if s == 'i' or s == 'I': i = 1
        if (s == 'c' or s == 'C') and i == 1: c = 1
        if (s == 't' or s == 'T') and i*c == 1: t = 1
    print("YES" if t else "NO")


if __name__ == "__main__":
    main()