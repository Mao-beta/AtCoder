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


def main():
    N, M = NMI()
    A = NLI()
    A.sort(key=lambda x: x % M)

    res = []
    tmp = []
    for a in A:
        if not tmp:
            tmp.append(a)
        else:
            if a % M - tmp[-1] % M <= 1:
                tmp.append(a)
            else:
                res.append(tmp[:])
                tmp = [a]

    if tmp:
        if tmp[-1] % M == M-1 and res and res[0][0] % M == 0:
            res[0] += tmp[:]
        else:
            res.append(tmp[:])

    total = sum(A)
    ans = total
    for L in res:
        ans = min(ans, total - sum(L))
    print(ans)


if __name__ == "__main__":
    main()
