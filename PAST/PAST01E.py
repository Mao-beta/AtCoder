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


def main():
    N, Q = NMI()
    ans = [["N"]*N for _ in range(N)]

    for _ in range(Q):
        q, *x = NLI()
        # print(q, x)
        if q == 1:
            a, b = x
            a, b = a-1, b-1
            ans[a][b] = "Y"
            # print(a, b)

        elif q == 2:
            a = x[0] - 1
            for b in range(N):
                if ans[b][a] == "Y":
                    ans[a][b] = "Y"
                    # print(a, b)

        else:
            a = x[0] - 1
            F = ans[a][:]
            for i, x in enumerate(F):
                if x == "N": continue
                for b in range(N):
                    if b == a: continue
                    if ans[i][b] == "Y":
                        ans[a][b] = "Y"
                        # print(a, b)

    for row in ans:
        print("".join(row))


if __name__ == "__main__":
    main()
