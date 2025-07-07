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
    N, M = NMI()
    A = [NLI() for _ in range(N)]
    L = [[] for _ in range(N)]
    R = [[] for _ in range(N)]
    for case in range(1<<(N-1)):
        now = A[0][0]
        h, w = 0, 0
        for i in range(N-1):
            now = now * 10 % M
            if (case >> i) & 1:
                w += 1
            else:
                h += 1
            now += A[h][w]
        L[w].append(now * pow(10, N-1, M) % M)
    # print(L)

    for case in range(1<<(N-1)):
        h, w = N-1, N-1
        now = 0
        for i in range(N-1):
            now += A[h][w] * pow(10, i, M)
            now %= M
            if (case >> i) & 1:
                w -= 1
            else:
                h -= 1
        R[w].append(now % M)
    ans = 0
    for w in range(N):
        L[w].sort()
        for r in R[w]:
            idx = bisect.bisect_right(L[w], M-r-1)
            s = L[w][idx-1] + r
            ans = max(ans, s % M)
    print(ans)


if __name__ == "__main__":
    main()
