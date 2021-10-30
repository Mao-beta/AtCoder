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
    N, M = NMI()
    B = [NLI() for _ in range(N)]

    for h in range(N):
        for w in range(M):
            B[h][w] -= 1

    for h in range(N):
        for w in range(M):
            if h < N-1 and w < M-1:
                if B[h+1][w] != B[h][w] + 7:
                    print("No")
                    exit()
                elif B[h][w+1] % 7 != B[h][w] % 7 + 1:
                    print("No")
                    exit()

            elif h == N-1 and w < M-1:
                if B[h][w+1] % 7 != B[h][w] % 7 + 1:
                    print("No")
                    exit()

            elif h < N-1 and w == M-1:
                if B[h+1][w] != B[h][w] + 7:
                    print("No")
                    exit()

    print("Yes")


if __name__ == "__main__":
    main()
