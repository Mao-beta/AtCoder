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
    N, M = NMI()
    A = NLI()
    B = NLI()
    A.sort()
    B.sort()

    ai = 0
    bi = 0
    ans = 10**10
    while ai < N and bi < M:
        a, b = A[ai], B[bi]
        ans = min(ans, abs(a-b))
        if a < b:
            ai += 1
        else:
            bi += 1

    print(ans)


if __name__ == "__main__":
    main()