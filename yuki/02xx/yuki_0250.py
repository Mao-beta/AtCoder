import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.set_int_max_str_digits(10 ** 6)
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
    for _ in range(Q):
        d, x, t = NMI()
        if d == 1:
            print("AC" if t >= 1 else "ZETUBOU")
            continue

        # x+d-1 C d-1
        n = x+d-1
        r = d-1
        if n-r < r:
            r = n-r
        ans = 1
        for i in range(r):
            ans *= n-i
            ans //= i+1
            if ans > t:
                break
        # print(d, x, t, ans)
        print("AC" if ans <= t else "ZETUBOU")


if __name__ == "__main__":
    main()
