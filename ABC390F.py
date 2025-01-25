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
    N = NI()
    A = NLI()
    # 前のaiのidx, ai-1のidx, ai+1のidxを保持
    Is = [[-1, N, N] for _ in range(N+2)]
    ans = 0
    for i, a in enumerate(A):
        prev, m, p = Is[a]
        if m == N and p == N:
            ans += (i - prev) * (N-i)
        elif m == N or p == N:
            ans += (i - min(m, p)) * (N-i)
        else:
            l = min(m, p)
            r = max(m, p)
            ans += (i - r) * (N-i)
            ans -= (l - prev) * (N-i)
        Is[a] = [i, N, N]
        Is[a+1][1] = i
        Is[a-1][2] = i
        # print(i, a, ans, Is)
    print(ans)


if __name__ == "__main__":
    main()
