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
    N = NI()
    A = NLI()
    M = max(A)

    def judge(X, a):
        return M*(2*X-1) <= 2*10**9 * a

    ans = []
    for a in A:
        ok = 1
        ng = 10**19
        while abs(ok - ng) > 1:
            X = (ok + ng) // 2
            if judge(X, a):
                ok = X
            else:
                ng = X

        ans.append(ok)
    print(*ans)


if __name__ == "__main__":
    main()
