import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

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
    N, A, B = NMI()
    S = SI()
    S = [1 if s == "(" else -1 for s in S]
    total = sum(S)

    ans = 0

    if total < 0:
        c = -total
        for i in range(2*N):
            if c > 0 and S[i] == -1:
                c -= 2
                S[i] = 1
                ans += B
    elif total > 0:
        c = total
        for i in range(2*N-1, -1, -1):
            if c > 0 and S[i] == 1:
                c -= 2
                S[i] = -1
                ans += B
    C = list(accumulate([0]+S))

    m = min(C)
    if m < 0:
        ans += (-m+1) // 2 * min(2*B, A)
    print(ans)


if __name__ == "__main__":
    main()
