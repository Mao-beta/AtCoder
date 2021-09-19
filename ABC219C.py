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
    before = "abcdefghijklmnopqrstuvwxyz"

    X = SI()
    N = NI()
    S = [SI() for _ in range(N)]
    table = str.maketrans(X, before)

    SX = [(s.translate(table), i) for i, s in enumerate(S)]
    SX.sort()
    ans = [S[i] for s, i in SX]
    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
