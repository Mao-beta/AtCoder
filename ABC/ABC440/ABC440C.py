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
        N, W = NMI()
        C = NLI() * 2
        cum = list(accumulate([0]+C))
        ans = 10**60
        for x in range(2*W):
            tmp = 0
            for l in range(x-2*W, N, 2*W):
                r = l + W
                l = max(l, 0)
                r = min(r, N)
                if l >= r:
                    continue
                tmp += cum[r] - cum[l]
                # print(x, l, r)
            ans = min(ans, tmp)
            # print(x, tmp)
        print(ans)



if __name__ == "__main__":
    main()
