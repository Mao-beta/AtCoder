import sys
import math
from collections import defaultdict
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    N = NI()
    TA = [NLI() for _ in range(N)]
    nt, na = 0, 0
    for t, a in TA:
        if t >= nt and a >= na:
            nt = t
            na = a
        elif t >= nt and a < na:
            k = na // a if na % a == 0 else na // a + 1
            nt = k*t
            na = k*a
        elif t < nt and a >= na:
            k = nt // t if nt % t == 0 else nt // t + 1
            nt = k*t
            na = k*a
        else:
            kt = nt // t if nt % t == 0 else nt // t + 1
            ka = na // a if na % a == 0 else na // a + 1
            k = max(kt, ka)
            nt = k * t
            na = k * a
    print(nt+na)



if __name__ == "__main__":
    main()