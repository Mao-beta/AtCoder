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
    N, K = NMI()
    A = NLI()
    A = [[a, i] for i, a in enumerate(A)]
    A.sort()
    ans = [K//N] * N
    for i in range(K%N):
        ans[A[i][1]] += 1
    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
