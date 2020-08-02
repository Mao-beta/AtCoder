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
    N, K = NMI()
    A = NLI()
    ng = 0
    ok = 10**10

    for i in range(100):
        mid = (ok + ng) // 2
        if mid == 0:
            break
        tmp = 0
        for a in A:
            if a % mid == 0:
                tmp += a // mid - 1
            else:
                tmp += a // mid
        if tmp <= K:
            ok = mid
        else:
            ng = mid

    print(ok)


if __name__ == "__main__":
    main()