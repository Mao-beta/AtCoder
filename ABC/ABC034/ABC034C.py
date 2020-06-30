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


def cmb_mod(n, r, m):
    fact = [1] * (n+1)
    inv = [1] * (n+1)
    for i in range(1, n+1):
        fact[i] *= fact[i-1] * i % m
        inv[i] *= inv[i-1] * pow(i, m-2, m) % m
    return fact[n] * inv[r] * inv[n-r] % m


def main():
    W, H = NMI()
    print(cmb_mod(W+H-2, W-1, MOD))


if __name__ == "__main__":
    main()