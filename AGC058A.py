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


def solve(N, PP):
    P = PP.copy()

    ans = []
    for i in range(2*N-1):
        x, y = P[i], P[i+1]
        if i % 2 == 0 and x > y:
            ans.append(i+1)
            P[i], P[i+1] = P[i+1], P[i]
        elif i % 2 == 1 and x < y:
            ans.append(i+1)
            P[i], P[i+1] = P[i+1], P[i]

    if len(ans) <= N:
        # print(PP)
        # print(P)
        print(len(ans))
        print(*ans)
        exit()

    ans = [i for i in range(1, 2*N, 2)]
    print(len(ans))
    print(*ans)



if __name__ == "__main__":
    # N = 2
    # for PP in permutations(range(1, 2*N+1), 2*N):
    #     solve(N, list(PP))
    N = NI()
    PP = NLI()
    solve(N, PP)