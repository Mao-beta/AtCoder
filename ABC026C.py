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
    Boss = [0]*(N+1)
    Buka = [[] for _ in range(N+1)]
    for i in range(2, N+1):
        Boss[i] = NI()
        Buka[Boss[i]].append(i)

    print(dfs(1, Buka))


def dfs(boss, Buka):
    maxM = 0
    minM = float("inf")

    if Buka[boss]:
        for buka in Buka[boss]:
            tmp = dfs(buka, Buka)
            maxM = max(maxM, tmp)
            minM = min(minM, tmp)

        return maxM + minM + 1

    else:
        return 1


if __name__ == "__main__":
    main()