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
    Q = NI()
    D = deque()
    for _ in range(Q):
        q, *X = NMI()
        if q == 1:
            c, x = X
            D.append([c, x])
        else:
            k = X[0]
            ans = 0
            while k > 0:
                c, x = D.popleft()
                mck = min(c, k)
                ans += x * mck
                k -= mck
                c -= mck
                if c > 0:
                    D.appendleft([c, x])
            print(ans)
        # print(D)


if __name__ == "__main__":
    main()
