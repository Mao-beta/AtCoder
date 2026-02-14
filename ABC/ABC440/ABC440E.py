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
    N, K, X = NMI()
    A = NLI()
    A.sort(reverse=True)
    ans = []
    hq = [[0]*(K+1)]
    hq[0][0] = -A[0] * K
    hq[0][1] = K
    l = 0
    S = set()
    while hq:
        now, *C = heappop(hq)
        now *= -1
        ans.append(now)
        # print(now, C, ans, K)
        l += 1
        if l == X:
            break
        for i, a in enumerate(A):
            if i < N-1 and C[i] > 0:
                C[i] -= 1
                C[i+1] += 1
                heappush(hq, [-(now-A[i]+A[i+1]), *C])
                C[i] += 1
                C[i+1] -= 1
    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
