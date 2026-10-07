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
    N, M, K = NMI()
    X, Y = NMI()
    A = sorted(NLI())
    B = sorted(NLI())
    ans = 0
    CA = list(accumulate([0]+A))

    usedk = 0
    change = 0

    ai = bisect.bisect_right(CA, X+Y*K)
    ans = max(ans, ai-1)

    for bi in range(M):
        k = (B[bi]+K-1) // K
        usedk += k
        change += K*k - B[bi]
        if usedk > Y:
            break
        ai = bisect.bisect_right(CA, X+change+(Y-usedk)*K)
        # print(ai, bi+1, change, usedk, (Y-usedk))
        ans = max(ans, bi + ai)

    # print(CA)
    # print(B)
    print(ans)


if __name__ == "__main__":
    main()
