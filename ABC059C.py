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


# 配列から累積和を返す
def make_cumulative(A):
    C = [0] * (len(A) + 1)
    for i, a in enumerate(A):
        i += 1
        C[i] = C[i - 1] + a
    return C


def main():
    N = NI()
    A = NLI()
    C = make_cumulative(A)[1:]
    PM = []
    MP = []
    for i in range(len(A)):
        PM.append((-1) ** i)
        MP.append((-1) ** (i+1))
    diff = 0
    ans = 0
    for c, sign in zip(C, PM):
        if (c + diff) * sign > 0:
            pass
        else:
            if c + diff > 0:
                ans += c + diff + 1
                diff = - c - 1
            elif c + diff < 0:
                ans += 1 - c - diff
                diff = 1 - c
            else:
                ans += 1
                diff += sign

    diff = 0
    ans2 = 0
    for c, sign in zip(C, MP):
        if (c + diff) * sign > 0:
            pass
        else:
            if c + diff > 0:
                ans2 += c + diff + 1
                diff = - c - 1
            elif c + diff < 0:
                ans2 += 1 - c - diff
                diff = 1 - c
            else:
                ans2 += 1
                diff += sign

    print(min(ans, ans2))

if __name__ == "__main__":
    main()