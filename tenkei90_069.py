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

    if N == 1:
        print(K)
        exit()
    if N == 2:
        print(K*(K-1)%MOD)
        exit()
    if K <= 2:
        print(0)
        exit()

    ans = K*(K-1)%MOD * pow(K-2, N-2, MOD) % MOD
    print(ans)


if __name__ == "__main__":
    main()
