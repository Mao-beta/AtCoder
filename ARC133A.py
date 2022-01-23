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
    A = NLI()
    if len(set(A)) == 1:
        print("")
        exit()

    a0 = A[0]
    for a in A:
        if a >= a0:
            a0 = a
        else:
            break

    ans = []
    for a in A:
        if a != a0:
            ans.append(a)
    print(*ans)


if __name__ == "__main__":
    main()
