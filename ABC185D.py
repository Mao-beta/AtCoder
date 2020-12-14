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
    N, M = NMI()
    A = NLI()

    if N == M:
        print(0)
        exit()
    if M == 0:
        print(1)
        exit()

    A.sort()
    l = 1
    gaps = []
    for a in A:
        if a - l > 0:
            gaps.append(a - l)
        l = a + 1
    if l != N+1:
        gaps.append(N+1 - l)
    k = min(gaps)
    ans = 0
    for g in gaps:
        if g % k == 0:
            ans += g // k
        else:
            ans += g // k + 1
    print(ans)


if __name__ == "__main__":
    main()
