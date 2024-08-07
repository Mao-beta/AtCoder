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
    B = NLI()
    ans = 0
    for k in range(30):
        # 下からk-bit目について考える
        MASK = (1<<(k+1))-1
        Ak = [a & MASK for a in A]
        Ak.sort()
        Bk = [b & MASK for b in B]
        Bk.sort()
        c = 0
        # print(Ak)
        for a in Ak:
            # ちょうど100..0になるb
            l = ((1<<(k+1)) + (1 << k) - a) & MASK
            # ちょうど000..0になるb
            r = ((1<<(k+1)) -a) & MASK
            if l < r:
                m = bisect.bisect_left(Bk, r) - bisect.bisect_left(Bk, l)
            else:
                m = N - (bisect.bisect_left(Bk, l) - bisect.bisect_left(Bk, r))
            c += m
        #     print(a, Bk, l, r, m)
        # print(k, c)
        if c % 2:
            ans |= 1<<k
    print(ans)


if __name__ == "__main__":
    main()
