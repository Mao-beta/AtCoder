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
    N, K = NMI()
    A = sorted(NLI())
    B = sorted(NLI())
    C = sorted(NLI())

    def f(i, j, k):
        return A[i] * B[j] + B[j] * C[k] + C[k] * A[i]

    def sf(i, j, k):
        return i*N*N + j*N + k

    def sinv(ijk):
        ij, k = divmod(ijk, N)
        i, j = divmod(ij, N)
        return i, j, k


    hq = [[-f(N-1, N-1, N-1), sf(N-1, N-1, N-1)]]
    ans = []
    S = set()
    cnt = 0
    while hq:
        x, ijk = heappop(hq)
        i, j, k = sinv(ijk)
        ans.append(-x)
        cnt += 1
        # print(cnt, i, j, k, ans)
        if cnt == K:
            print(-x)
            return
        if i > 0 and sf(i-1, j, k) not in S:
            heappush(hq, [-f(i-1, j, k), sf(i-1, j, k)])
            S.add(sf(i-1, j, k))
        if j > 0 and sf(i, j-1, k) not in S:
            heappush(hq, [-f(i, j-1, k), sf(i, j-1, k)])
            S.add(sf(i, j-1, k))
        if k > 0 and sf(i, j, k-1) not in S:
            heappush(hq, [-f(i, j, k-1), sf(i, j, k-1)])
            S.add(sf(i, j, k-1))


if __name__ == "__main__":
    main()
