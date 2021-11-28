import sys
import math
from collections import deque

sys.setrecursionlimit(100000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    N = NI()
    S = NLI()

    A = [0] * 1001
    for a in range(1, 1001):
        for b in range(1, 1001):
            s = 4*a*b + 3*a + 3*b
            if s < 1001:
                A[s] = 1

    ans = 0
    for s in S:
        if A[s] == 0:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
