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


def make_grid(h, w, num): return [[int(num)] * w for _ in range(h)]


def main():
    N, K = NMI()
    K = abs(K)
    ans = 0
    for i in range(2, 2*N-K+1):
        X = K+i
        Y = i
        X = X-1 if X <= N+1 else 2*N-X+1
        Y = Y - 1 if Y <= N + 1 else 2 * N - Y + 1
        ans += X * Y
    print(ans)


if __name__ == "__main__":
    main()
