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
    N = NI()
    TKA = [NLI() for _ in range(N)]

    seen = [0] * N

    def rec(now):
        if seen[now]:
            return

        t, k, *A = TKA[now]
        seen[now] += t
        for a in A:
            a -= 1
            if seen[a]:
                continue
            rec(a)

    rec(N-1)
    print(sum(seen))


if __name__ == "__main__":
    main()
