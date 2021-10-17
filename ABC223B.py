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
    S = SI()
    L = []
    for i in range(len(S)):
        L.append(S[i:] + S[:i])
    L.sort()
    print(L[0])
    print(L[-1])


if __name__ == "__main__":
    main()
