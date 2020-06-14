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
    T = NLI()
    A = NLI()
    B = NLI()
    gap = [a-b for a, b in zip(A, B)]

    if T[0]*gap[0] + T[1]*gap[1] == 0:
        print("infinity")
        exit()

    if gap[0]*gap[1] > 0 or abs(T[0]*gap[0]) > abs(T[1]*gap[1]):
        print(0)
        exit()

    x = abs(gap[0]*T[0])
    y = abs(T[0]*gap[0] + T[1]*gap[1])
    if x % y == 0:
        print(x // y * 2)
        exit()
    else:
        print(x // y * 2 + 1)



if __name__ == "__main__":
    main()