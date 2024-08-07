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
    A = SLI()
    D = [pow(10, len(a), MOD99) for a in A]
    c = 0
    ans = 0
    for i in range(N-1, -1, -1):
        A[i] = int(A[i])
        ans += c * A[i] % MOD99
        ans += i * A[i] % MOD99
        c += D[i]
        ans %= MOD99
        c %= MOD99
    print(ans)


if __name__ == "__main__":
    main()
