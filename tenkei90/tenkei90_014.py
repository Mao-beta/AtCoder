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
    A = sorted(NLI())
    B = sorted(NLI())
    S = [abs(a-b) for a, b in zip(A, B)]
    print(sum(S))


if __name__ == "__main__":
    main()
