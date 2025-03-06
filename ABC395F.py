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
    N, X = NMI()
    UD = EI(N)
    Us = [u for u, _ in UD]
    hq = [[u, i] for i, (u, _) in enumerate(UD)]
    heapify(hq)
    while hq:
        u, i = heappop(hq)
        if u > Us[i]:
            continue
        if i > 0 and Us[i-1] > u+X:
            Us[i-1] = u+X
            heappush(hq, [u+X, i-1])
        if i < N-1 and Us[i+1] > u+X:
            Us[i+1] = u+X
            heappush(hq, [u+X, i+1])
    Ds = [d for _, d in UD]
    m = min(u+d for u, d in zip(Us, Ds))
    ans = sum(u+d for u, d in UD) - m * N
    print(ans)


if __name__ == "__main__":
    main()
