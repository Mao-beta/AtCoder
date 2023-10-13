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
    while True:
        N, M, P, Q = NMI()
        if N == 0:
            exit()
        P, Q = P-1, Q-1
        X = NLI()
        Y = []
        Y.append(list(range(N)))
        for x in X[::-1]:
            Z = Y[-1][:]
            Z[x], Z[x-1] = Z[x-1], Z[x]
            Y.append(Z[:])
        
        Y = Y[::-1]
        if Y[0][P] == Q:
            print("OK")
            continue

        ans = [-1, -1]
        now = P
        for i, x in enumerate(X):
            t = Y[i].index(Q)
            if now-1 == t:
                ans = [t+1, i]
                break
            elif now+1 == t:
                ans = [now+1, i]
                break
            if now == x-1:
                now += 1
            elif now == x:
                now -= 1

        if ans[0] < 0:
            i = M
            t = Y[-1].index(Q)
            if now - 1 == t:
                ans = [t + 1, i]
            elif now + 1 == t:
                ans = [now+1, i]

        if ans[0] < 0:
            print("NG")
        else:
            print(*ans)


if __name__ == "__main__":
    main()
