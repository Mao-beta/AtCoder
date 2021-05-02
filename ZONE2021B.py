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
    N, D, H = NMI()
    B = [NLI() for _ in range(N)]
    ans = 0.0
    for d, h in B:
        x = H - (H-h)*D/(D-d)
        ans = max(ans, x)
    print(ans)


if __name__ == "__main__":
    main()
