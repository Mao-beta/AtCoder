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
    T = NI()
    for _ in range(T):
        N = NI()
        A = NLI()
        B = NLI()
        G = [[a+b, i] for i, (a, b) in enumerate(zip(A, B))]
        G.sort(reverse=True)
        ap = 0
        bp = 0

        for i, (_, idx) in enumerate(G):
            if i % 2 == 0:
                ap += A[idx]
            else:
                bp += B[idx]

        if ap > bp:
            print("First")
        elif ap == bp:
            print("Tie")
        else:
            print("Second")


if __name__ == "__main__":
    main()
