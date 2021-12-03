import sys
import math
from collections import defaultdict

sys.setrecursionlimit(100000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    N, K = NMI()
    C = NLI()
    P = NLI()
    D = defaultdict(lambda: 10**10)
    for c, p in zip(C, P):
        D[c] = min(D[c], p)

    if len(D.keys()) < K:
        print(-1)
    else:
        P = sorted(D.values())
        print(sum(P[:K]))


if __name__ == "__main__":
    main()
