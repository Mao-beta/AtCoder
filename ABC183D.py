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
    N, W = NMI()
    people = [NLI() for _ in range(N)]
    L = [0] * 200010
    for s, t, p in people:
        L[s] += p
        L[t] -= p
    cum = [0]
    for l in L:
        cum.append(cum[-1] + l)
    print("Yes" if max(cum) <= W else "No")


if __name__ == "__main__":
    main()
