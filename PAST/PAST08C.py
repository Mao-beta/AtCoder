import sys
import math
from collections import Counter

sys.setrecursionlimit(100000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    N, X = NMI()
    A = NLI()
    C = Counter(A)
    print(C[X])


if __name__ == "__main__":
    main()
