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
    A_cum = [0]*(N+1)
    B_cum = [0]*(M+1)
    for i, a in enumerate(A):
        A_cum[i+1] = A_cum[i] + a
    for i, b in enumerate(B):
        B_cum[i+1] = B_cum[i] + b

    ans = 0
    for i, sa in enumerate(A_cum):
        if K - sa < 0:
            continue
        idx = bisect.bisect_right(B_cum, K-sa)
        ans = max(ans, i+idx)

    print(ans-1)





if __name__ == "__main__":
    main()