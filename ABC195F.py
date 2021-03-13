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
    A, B = NMI()
    P = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
    bits = []
    for n in range(A, B+1):
        b = 0
        for i, p in enumerate(P):
            if n % p == 0:
                b += 1 << i
        bits.append(b)

    dp = [0] * (2**20)
    dp[0] = 1

    for b in bits:
        for case in range(1 << 20):
            if case & b == 0:
                dp[case + b] += dp[case]
    print(sum(dp))


if __name__ == "__main__":
    main()
