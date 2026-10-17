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
    N, M = NMI()
    AB = EI(N)
    CD = EI(M)

    def judge(X):
        # 強さXを達成可能か？
        ab = [b - a * X for a, b in AB]
        cd = [d - c * X for c, d in CD]
        ab.sort(reverse=True)
        cd.sort(reverse=True)
        if sum(ab[:5]) >= 0 or sum(ab[:4]) + cd[0] >= 0:
            return True
        else:
            return False

    ok = 0
    ng = 10**6
    for _ in range(50):
        X = (ok + ng) / 2
        if judge(X):
            ok = X
        else:
            ng = X

    print(ok)


if __name__ == "__main__":
    main()
