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


def make_cumulative(A):
    C = [0] * (len(A) + 1)
    for i, a in enumerate(A):
        i += 1
        C[i] = C[i - 1] + a
    return C


def main():
    Q = NI()
    querys = [NLI() for _ in range(Q)]
    N = 100010
    hurui = [1] * N
    for i in range(N):
        if i <= 1:
            hurui[i] = 0
            continue
        if hurui[i] == 0:
            continue
        for j in range(i*2, N, i):
            hurui[j] = 0
    like_2017 = hurui[:]
    for i in range(N):
        if hurui[i] == 0 or i <= 2:
            continue
        if hurui[(i+1)//2] == 0:
            like_2017[i] = 0
    like_2017[2] = 0
    C = make_cumulative(like_2017)[1:]

    for q in querys:
        print(C[q[1]] - C[q[0]-1])

if __name__ == "__main__":
    main()