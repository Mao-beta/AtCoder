import sys
import math
from collections import deque
import bisect


sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def make_grid(h, w, num): return [[int(num)] * w for _ in range(h)]


def main():
    N, M, K = NMI()
    A = NLI()
    B = NLI()
    # sumを先に計算したい →　累積和
    SA = [0]
    SB = [0]
    for a in A:
        SA.append(SA[-1] + a)
    for b in B:
        SB.append(SB[-1] + b)
    print(A)
    print(SA)
    print(SB)
    print(bisect.bisect_right(SB, 230)-1)

if __name__ == "__main__":
    main()