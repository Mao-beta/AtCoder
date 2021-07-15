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
    N = NI()
    C = sorted(NLI())
    ans = 1
    for i, c in enumerate(C):
        if c <= i:
            print(0)
            exit()
        ans = ans * (c - i) % MOD

    print(ans)


if __name__ == "__main__":
    main()
