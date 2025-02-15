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
    B = NLI() * 2
    ans = 3000

    def f(l, k):
        return l * 3000 + k

    for s in range(N):
        hq = [f(a, 0) for a in A]
        heapify(hq)
        M = 0
        for i in range(s, s+N):
            l, k = divmod(heappop(hq), 3000)
            b = B[i]
            heappush(hq, f(l+b//2, k+1))
            M = max(M, k+1)
            if M > ans:
                break
        ans = min(ans, M)
    print(ans)


if __name__ == "__main__":
    main()
