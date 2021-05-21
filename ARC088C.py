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
    X, Y = NMI()
    ans = 1
    a = X
    while a * 2 <= Y:
        a *= 2
        ans += 1
    print(ans)


if __name__ == "__main__":
    main()
