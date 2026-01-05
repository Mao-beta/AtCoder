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
    N = NI()
    A = NLI()
    ans = []
    base = 0
    for i in range(29, -1, -1):
        idx = bisect.bisect_left(A, base + (1<<i))
        if idx > 0:
            ans.append([1, idx, 1<<i])
            for j in range(idx):
                A[j] += 1<<i
        A.sort()
        base += 1<<i
    # print(A)
    print(len(ans))
    for a in ans:
        print(*a)


if __name__ == "__main__":
    main()
