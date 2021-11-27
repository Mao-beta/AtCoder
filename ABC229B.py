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
    A, B = SI().split()
    A = A.zfill(18)
    B = B.zfill(18)
    for a, b in zip(A, B):
        a, b = int(a), int(b)
        if a + b >= 10:
            print("Hard")
            exit()
    print("Easy")


if __name__ == "__main__":
    main()
