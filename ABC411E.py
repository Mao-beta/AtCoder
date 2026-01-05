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
    A = EI(N)
    B = defaultdict(list)
    for i in range(N):
        for j in range(6):
            B[A[i][j]].append(i)
    Less = [0] * N
    ans = 0
    now = 0
    prev = 0
    zero = set(i for i in range(N))
    S = sorted(list(B.keys()))
    for a in S:
        L = B[a]
        for i in L:
            Less[i] += 1
            if Less[i] == 1:
                zero.discard(i)
                if len(zero) == 0:
                    now = 1
                    for k in Less:
                        now = now * k % MOD99
            else:
                now *= pow(Less[i]-1, MOD99-2, MOD99)
                now *= Less[i]
                now %= MOD99
        ans += a * (now - prev)
        ans %= MOD99
        prev = now
    inv6 = pow(6, MOD99-2, MOD99)
    ans *= pow(inv6, N, MOD99)
    print(ans % MOD99)


if __name__ == "__main__":
    main()
