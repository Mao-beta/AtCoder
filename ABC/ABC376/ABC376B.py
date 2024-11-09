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
    N, Q = NMI()
    HT = [SMI() for _ in range(Q)]
    l, r = 0, 1
    ans = 0
    for h, t in HT:
        t = int(t) - 1
        tmp = 100
        if h == "L":
            for i in range(100):
                if (l+i) % N == r:
                    break
                if (l+i) % N == t:
                    tmp = min(tmp, i)
                    break
            for i in range(100):
                if (l-i) % N == r:
                    break
                if (l-i) % N == t:
                    tmp = min(tmp, i)
                    break
            l = t
        else:
            for i in range(100):
                if (r + i) % N == l:
                    break
                if (r + i) % N == t:
                    tmp = min(tmp, i)
                    break
            for i in range(100):
                if (r - i) % N == l:
                    break
                if (r - i) % N == t:
                    tmp = min(tmp, i)
                    break
            r = t
        ans += tmp
    print(ans)


if __name__ == "__main__":
    main()
