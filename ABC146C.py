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


def main():
    A, B, X = NMI()
    ng = 10**20
    ok = 0
    while abs(ok-ng) > 1:
        mid = (ok + ng) // 2
        il = mid
        sl = len(str(mid))
        if (il*A + sl*B) <= X:
            ok = mid
        else:
            ng = mid
    print(min(ok, 10**9))


if __name__ == "__main__":
    main()