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
    N, Q = NMI()
    A = NLI()
    G = []
    for i in range(N-1):
        G.append(A[i+1] - A[i])
    ans = sum([abs(a) for a in G])
    for _ in range(Q):
        l, r, v = NMI()
        l, r = l-1, r-1

        if l >= 1:
            ans -= abs(G[l-1])
            G[l-1] += v
            ans += abs(G[l-1])

        if r < N-1:
            ans -= abs(G[r])
            G[r] -= v
            ans += abs(G[r])

        print(ans)


if __name__ == "__main__":
    main()
