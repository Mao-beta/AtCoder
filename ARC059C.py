import sys
import math
from collections import defaultdict
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
    A = NLI()
    ans = 10**20
    for x in range(-100, 101):
        AX = [(a-x)**2 for a in A]
        ans = min(ans, sum(AX))
    print(ans)


if __name__ == "__main__":
    main()
