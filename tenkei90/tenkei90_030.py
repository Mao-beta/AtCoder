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
    P = [0] * (N+1)
    for i in range(N+1):
        if i <= 1:
            P[i] = -1
            continue

        if P[i] != 0: continue

        for j in range(i, N+1, i):
            P[j] += 1

    ans = [1 for p in P if p >= K]
    print(sum(ans))


if __name__ == "__main__":
    main()
