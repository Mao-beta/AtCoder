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


def main(N):
    res = 0
    for y in range(1, int(N**0.5) + 5):
        if y ** 2 > N:
            break

        # print("y", y)

        # x=y=z
        if y ** 2 <= N:
            # print(1)
            res += 1

        # x=y<z
        if y ** 2 <= N:
            # y < z <= N//y
            if N // y > y:
                # print((N // y - y) * 3)
                res += (N // y - y) * 3

        # x<y=z
        if y ** 2 <= N:
            # x < y
            # print((y-1) * 3)
            res += (y-1) * 3

        # x < y < z
        if N // y > y:
            # print((N // y - y) * (y-1) * 6)
            res += (N // y - y) * (y-1) * 6

        res %= MOD99

    return res


def guchoku(N):
    res = 0
    for i in range(1, N+1):
        for j in range(1, N + 1):
            for k in range(1, N + 1):
                if i*j <= N and j*k <= N and k*i <= N:
                    print(i, j, k)
                    res += 1
    return res


if __name__ == "__main__":
    T = NI()
    for _ in range(T):
        N = NI()
        ans = main(N)
        print(ans)
        # gu = guchoku(N)
        # print(gu)
