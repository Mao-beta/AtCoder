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
    a, b = NMI()
    ans = b - a
    if a * b < 0:
        ans -= 1
    print(ans)


if __name__ == "__main__":
    main()
