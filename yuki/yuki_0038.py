import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

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
    Kr, Kb = NMI()
    S = SI()

    ans = 0
    for case in range(1<<20):
        T = []
        d = 0
        for s in S:
            if s == "W":
                T.append(s)
            else:
                if (case >> d) & 1:
                    T.append(s)
                d += 1
        ok = True
        M = len(T)

        for i in range(M):
            j = i + Kr
            if j >= M:
                break
            if T[i] == T[j] == "R":
                ok = False

        for i in range(M):
            j = i + Kb
            if j >= M:
                break
            if T[i] == T[j] == "B":
                ok = False

        if ok:
            if M > ans:
                ans = max(ans, M)

    print(ans)


if __name__ == "__main__":
    main()
