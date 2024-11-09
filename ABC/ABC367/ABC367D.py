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
    N, M = NMI()
    A = NLI()
    D = list(accumulate([0]+A*3))
    S = sum(A)
    l, r = 0, 0
    C = Counter()
    ans = 0
    for now in range(N, 2*N):
        nl = bisect.bisect_left(D, D[now])
        nr = bisect.bisect_left(D, D[now] + S)
        while r < nr:
            C[D[r] % M] += 1
            r += 1
        while l < nl:
            C[D[l] % M] -= 1
            l += 1
        ans += C[D[now] % M] - 1

    print(ans)


if __name__ == "__main__":
    main()
