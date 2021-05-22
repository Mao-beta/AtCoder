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
    A = NLI()
    D = deque()
    for i, a in enumerate(A):
        if i % 2 == 0:
            D.append(a)
        else:
            D.appendleft(a)
    if N % 2:
        D = reversed(D)
    print(*D)


if __name__ == "__main__":
    main()
