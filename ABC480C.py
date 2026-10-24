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

# ライブラリ https://github.com/Mao-beta/AtCoder


def main():
    N, K, T = NMI()
    A = sorted(NLI() + [T])
    now = 0
    ans = 0
    for a in A:
        if a <= now:
            now = max(now, a+K)
        else:
            x = (a - now + K-1) // K
            ans += x
            now = max(now + x*K, a+K)
        # print(now)
        if now >= T:
            break
    print(ans)


if __name__ == "__main__":
    main()
