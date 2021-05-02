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


def make_grid(h, w, num): return [[int(num)] * w for _ in range(h)]


def main():
    N, M, K = NMI()

    if N == M == 1:
        print(K)
        exit()
    elif N == 1:
        print(pow(K, M, MOD))
        exit()
    elif M == 1:
        print(pow(K, N, MOD))
        exit()

    ans = 0
    for x in range(1, K+1):
        case = pow(K-x+1, M, MOD) - pow(K-x, M, MOD)
        ans += pow(x, N, MOD) * case
        ans %= MOD
    print(ans)


if __name__ == "__main__":
    main()
