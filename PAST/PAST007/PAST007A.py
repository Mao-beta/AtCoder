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
    n = 0
    for i, k in enumerate(S, start=1):
        k = int(k)
        if i == 15:
            if n % 10 == k:
                print("Yes")
            else:
                print("No")

        else:
            if i % 2 == 1:
                n += 3 * k
            else:
                n += k


if __name__ == "__main__":
    main()
