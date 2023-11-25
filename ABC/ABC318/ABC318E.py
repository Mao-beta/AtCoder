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
    R = Counter(A)
    L = Counter()
    R[A[0]] -= 1
    same = 0
    ans = 0
    for i in range(N-1):
        # print(i, ans, same, L, R)
        ans += same
        a = A[i]
        b = A[i+1]
        same += R[a]
        L[a] += 1
        same -= L[b]
        R[b] -= 1

    L[A[-1]] += 1
    for x, k in L.items():
        ans -= k * (k-1) * (k-2) // 6
    print(ans)


if __name__ == "__main__":
    main()
