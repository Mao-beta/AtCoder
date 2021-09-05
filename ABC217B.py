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
    S = {"ABC", "ARC", "AGC", "AHC"}
    S.discard(SI())
    S.discard(SI())
    S.discard(SI())
    print(S.pop())


if __name__ == "__main__":
    main()
