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
    ans = [0]

    def rec(case):
        if case == (1<<(3*N))-1:
            ans[0] += 1
            return

        for i in range(3*N):
            if (case >> i) & 1:
                continue
            for j in range(i+1, 3*N):
                if (case >> j) & 1:
                    continue
                for k in range(j+1, 3*N):
                    if (case >> k) & 1:
                        continue
                    ai, aj, ak = A[i], A[j], A[k]
                    if abs(ai-aj) < ak < ai+aj:
                        rec(case | (1<<i) | (1<<j) | (1<<k))
            break

    rec(0)
    print(ans[0])


if __name__ == "__main__":
    main()
