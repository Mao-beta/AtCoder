import sys
import math
from collections import deque
import heapq as hq

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def make_grid(h, w, num): return [[int(num)] * w for _ in range(h)]


def main():
    N, M = NMI()
    C = [[0, 0, 0]] + [[i+1]+NLI() for i in range(M)]
    D = {i: [] for i in range(N+1)}
    names = {}
    for c in C[1:]:
        D[c[1]].append([c[2], c[0]])
    for p, YI in D.items():
        YI.sort()
        t = 1
        for y, i in YI:
            names[i] = str(p).zfill(6) + str(t).zfill(6)
            t += 1
    for i in range(1, M+1):
        print(names[i])



if __name__ == "__main__":
    main()