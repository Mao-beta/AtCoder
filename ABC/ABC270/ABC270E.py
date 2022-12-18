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
        k = sum(min(a, X) for a in A)
        return k <= K

    ok = -1
    ng = 10**12
    while abs(ok - ng) > 1:
        X = (ok + ng) // 2
        if judge(X):
            ok = X
        else:
            ng = X

    ans = [max(0, a-ok) for a in A]
    K -= sum(min(a, ok) for a in A)
    for i in range(N):
        if K <= 0:
            break
        if ans[i] > 0:
            ans[i] -= 1
            K -= 1

    print(*ans)


if __name__ == "__main__":
    main()
