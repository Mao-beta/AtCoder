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
    N, A, B = NMI()
    P, Q, R, S = NMI()

    ans = [["."]*(S-R+1) for _ in range(P, Q+1)]

    for h in range(P, Q+1):
        for w in range(R, S+1):
            if abs(h - A) == abs(w - B):
                ans[h-P][w-R] = "#"

    for row in ans:
        print("".join(row))


if __name__ == "__main__":
    main()
