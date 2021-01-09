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
    T = NI()
    querys = [NLI() for _ in range(T)]

    for N, S, K in querys:
        K %= N
        g = math.gcd(N, S)
        g = math.gcd(g, K)
        N, S, K = N // g, S // g, K // g
        try:
            x = (N-S) * pow(K, -1, N) % N
            print(x)
        except:
            print(-1)


if __name__ == "__main__":
    main()
