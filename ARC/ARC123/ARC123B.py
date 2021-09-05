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


def main():
    N = NI()
    A = NLI()
    B = NLI()
    C = NLI()
    A.sort()
    B.sort()
    C.sort()

    INF = 10**10
    BB = [INF] * N
    lo = 0
    for i, a in enumerate(A):
        idx = bisect.bisect_right(B, a, lo=lo)
        lo = idx + 1
        if idx == N:
            break
        BB[i] = B[idx]

    CC = [INF] * N
    lo = 0
    for i, b in enumerate(BB):
        idx = bisect.bisect_right(C, b, lo=lo)
        lo = idx + 1
        if idx == N:
            break
        CC[i] = C[idx]

    ans = 0
    for c in CC:
        if c == INF:
            break
        else:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
