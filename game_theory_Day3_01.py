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
    M = 10**5
    Y = [set() for _ in range(M+1)]
    for i in range(1, M+1):
        for j in range(i*2, M+1, i):
            Y[j].add(i)

    dp = [0] * (M+1)
    for i in range(2, M+1):
        Gi = set()
        for y in Y[i]:
            k = (i // y) % 2
            if k == 1:
                Gi.add(dp[y])
            else:
                Gi.add(0)
        for g in range(M+1):
            if g not in Gi:
                dp[i] = g
                break

    T = NI()
    for _ in range(T):
        N = NI()
        A = NLI()
        G = 0
        for a in A:
            G ^= dp[a]
        print(1 if G else 2)


if __name__ == "__main__":
    main()
