import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
MOD99 = 998244353

input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()
SMI = lambda: input().split()
SLI = lambda: list(SMI())
EI = lambda m: [NLI() for _ in range(m)]


def main():
    N, A, B, C = NMI()
    P = [A, B, C]
    D = {"A": 0, "B": 1, "C": 2}
    S = [SI() for _ in range(N)]
    ans = []
    for x, y in S:
        xi, yi = D[x], D[y]
        zi = xi ^ yi ^ 3
        if P[xi] == P[yi] == 0:
            print("No")
            exit()

        if P[xi] >= P[yi]:
            ans.append(y)
            P[yi] += 1
            P[xi] -= 1

        else:
            ans.append(x)
            P[xi] += 1
            P[yi] -= 1

    print("Yes")
    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
