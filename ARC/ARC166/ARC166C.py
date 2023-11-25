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


M = 2*10**6 + 100
Fib = [1, 1]
for _ in range(M):
    Fib.append((Fib[-1] + Fib[-2]) % MOD99)

Fib_even = Fib[0::2]
cum = list(accumulate(Fib_even, func=lambda x, y: x * y % MOD99))

def solve(H, W):
    if H > W:
        H, W = W, H

    res = cum[H] * cum[H] % MOD99 * pow(Fib[2*H+1], W-H, MOD99) % MOD99
    return res

def main():
    T = NI()
    for _ in range(T):
        H, W = NMI()
        ans = solve(H, W)
        print(ans)


if __name__ == "__main__":
    main()
