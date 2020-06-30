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
    A = NLI()

    taste = set()
    l, r = 0, 0
    ans = 0
    for l in range(N):
        while r < N and A[r] not in taste:
            taste.add(A[r])
            r += 1
        ans = max(ans, r-l)

        if l == r:
            r += 1
        else:
            taste.discard(A[l])

    print(ans)


if __name__ == "__main__":
    main()