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
    T = NI()
    for _ in range(T):
        N, K = NMI()
        A = NLI()
        B = NLI()
        AB = [[a, b] for a, b in zip(A, B)]
        AB.sort()
        hq = []
        bs = 0
        ans = 10**18
        for i in range(N):
            a, b = AB[i]
            if i >= K-1:
                # print(i, a, b, hq, bs, a * (bs+b))
                ans = min(ans, a * (bs+b))
            heappush(hq, -b)
            bs += b
            if len(hq) > K-1:
                x = heappop(hq) * (-1)
                bs -= x
        print(ans)



if __name__ == "__main__":
    main()
