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
        N, X = NMI()
        A = NLI()
        C = []
        heappush(C, (-(X+1), 1))
        ma = 10**18+1
        for a in A:
            if a >= ma:
                continue
            ma = a
            while C and -C[0][0] > a:
                v, k = heappop(C)
                v = -v
                while C and -C[0][0] == v:
                    k += heappop(C)[1]

                l, r = divmod(v, a)
                heappush(C, (-a, l*k))
                if r > 0:
                    heappush(C, (-r, k))

            # print(X, a, C)
        ans = -1
        while C:
            v, k = heappop(C)
            ans += k
        print(ans)


if __name__ == "__main__":
    main()
