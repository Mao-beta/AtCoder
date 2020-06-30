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
    R = []
    for i in range(N):
        R.append(NI())
    R = sorted(R, reverse=True)
    ans = sum([r**2 * (-1)**i for i, r in enumerate(R)])
    print(ans*math.pi)


if __name__ == "__main__":
    main()