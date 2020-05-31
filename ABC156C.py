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
    X = NLI()
    ans = 10**20
    for i in range(100):
        sq = 0
        for x in X:
            sq += (i-x)**2
        ans = min(ans, sq)
    print(ans)


if __name__ == "__main__":
    main()