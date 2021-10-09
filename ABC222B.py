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
    N, P = NMI()
    A = NLI()
    A = [1 if a < P else 0 for a in A]
    print(sum(A))


if __name__ == "__main__":
    main()
