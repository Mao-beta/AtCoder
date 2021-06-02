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
    Q = [NLI() for _ in range(T)]

    for N, M in Q:
        if M == 1:
            print(2)
            continue

        if N % 2:
            print(1)
        else:
            print(2)

        """
        Ys = set()
        for i in range(1, 10**3 + 1):
            if i**2 > M: break

            if M % i == 0:
                Ys.add(i)
                Ys.add(M // i)

        g = len(Ys) - 1
        """


if __name__ == "__main__":
    main()
