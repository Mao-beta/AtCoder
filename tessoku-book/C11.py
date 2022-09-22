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
    N, K = NMI()
    A = NLI()

    def judge(X):
        res = 0
        for a in A:
            res += int(a / X)
        return res <= K

    ok = 10**9
    ng = 1
    for i in range(50):
        X = (ok + ng) / 2
        if judge(X):
            ok = X
        else:
            ng = X

    ans = [int(a / ok) for a in A]
    print(*ans)


if __name__ == "__main__":
    main()
