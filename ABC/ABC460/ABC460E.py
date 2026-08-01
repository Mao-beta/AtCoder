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
    nines = [0]+[10**i-1 for i in range(1, 20)]
    # print(nines)
    for _ in range(T):
        N, M = NMI()
        ans = 0
        for i in range(1, 20):
            l, r = nines[i-1]+1, nines[i]
            if N < l:
                break
            g = math.gcd(M, r)
            mod = M // g
            yc = r-l+1 if N >= r else N-l+1
            # N以下のxのうち、modの倍数は？
            ans += (N // mod) * yc
            ans %= MOD99
        print(ans)


if __name__ == "__main__":
    main()
