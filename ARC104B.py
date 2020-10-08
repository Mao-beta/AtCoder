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
    N, S = SI().split()
    N = int(N)
    AT = [0] * (N+1)
    CG = [0] * (N+1)
    for i, s in enumerate(S):
        i += 1
        if s == "A":
            AT[i] = AT[i-1] + 1
            CG[i] = CG[i - 1]
        elif s == "T":
            AT[i] = AT[i-1] - 1
            CG[i] = CG[i - 1]
        elif s == "C":
            AT[i] = AT[i - 1]
            CG[i] = CG[i-1] + 1
        elif s == "G":
            AT[i] = AT[i - 1]
            CG[i] = CG[i-1] - 1
    ans = 0
    for i in range(N):
        for j in range(i+1, N+1):
            if AT[i] == AT[j] and CG[i] == CG[j]:
                ans += 1
    print(ans)


if __name__ == "__main__":
    main()
