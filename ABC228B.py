import sys
import math
from collections import defaultdict
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    N, X = NMI()
    A = NLI()
    X -= 1
    B = set([X])
    while True:
        if A[X]-1 not in B:
            B.add(A[X]-1)
            X = A[X] - 1

        else:
            print(len(B))
            exit()


if __name__ == "__main__":
    main()
