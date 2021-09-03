import sys
import math
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 998244353
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    N = NI()
    ans = 0
    for t in range(1, int(N**0.5)+1):
        ans += (t**2 + N) // (2*t) - t + 1
        ans %= MOD
    print(ans)


if __name__ == "__main__":
    main()
