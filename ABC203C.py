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
    N, K = NMI()
    F = [NLI() for _ in range(N)]
    F.sort()
    now = 0
    m = K
    for a, b in F:
        if now + m < a:
            print(now + m)
            exit()

        m -= a - now
        m += b
        now = a
    print(now + m)


if __name__ == "__main__":
    main()
