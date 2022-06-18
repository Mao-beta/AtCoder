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
    N = NI()
    X = NLI()
    C = NLI()
    X = [x-1 for x in X]

    seen = [0] * N
    ans = 0
    for start in range(N):
        if seen[start]:
            continue

        # print(start, seen)
        now = start
        L = [start]
        seen[start] = 1
        while True:
            if seen[X[now]]:
                # print(X[now])
                if X[now] not in L:
                    break
                idx = L.index(X[now])
                c = 10**10
                for i in range(idx, len(L)):
                    # print(C[L[i]])
                    c = min(c, C[L[i]])
                ans += c
                # print(c)
                break
            now = X[now]
            L.append(now)
            seen[now] = 1

        # print(L)

    print(ans)


if __name__ == "__main__":
    main()
