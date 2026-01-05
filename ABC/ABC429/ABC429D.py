import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.set_int_max_str_digits(10**6)
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
    N, M, C = NMI()
    A = NLI()
    A = [(a+M-1)%M+1 for a in A] + [(a+M-1)%M+M+1 for a in A]
    A.sort()
    # print(A)
    ans = 0
    prev = 0
    for i in range(N):
        a = A[i]
        t = A[i+C-1]
        idx = bisect.bisect_right(A, t)
        # print(idx, i, a, prev)
        ans += (idx - i) * (a - prev)
        prev = a
    a = M
    t = A[N + C - 1]
    idx = bisect.bisect_right(A, t)
    # print(idx, i, a, prev)
    ans += (idx - N) * (a - prev)
    print(ans)


if __name__ == "__main__":
    main()
