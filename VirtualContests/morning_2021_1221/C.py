import sys
import math
from collections import deque

sys.setrecursionlimit(100000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    N, K = NMI()
    P = NLI()
    P = [(1+p)/2 for p in P]
    S = sum(P[:K])
    ans = S
    for i in range(N-K):
        S -= P[i]
        S += P[i+K]
        ans = max(ans, S)
    print(ans)


if __name__ == "__main__":
    main()
