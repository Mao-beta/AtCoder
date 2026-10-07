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
    N, D = NMI()
    ST = EI(N)
    IN = [[] for _ in range(2*10**6+2)]
    OUT = [[] for _ in range(2*10**6+2)]
    for i, (s, t) in enumerate(ST):
        if t-s < D:
            continue
        IN[s].append(i)
        OUT[t].append(i)
    NOW = set()
    ans = 0
    for x in range(10**6+1):
        for i in IN[x]:
            NOW.add(i)
        for i in OUT[x+D-1]:
            NOW.discard(i)
        k = len(NOW)
        # print(x, k, NOW)
        ans += k * (k-1) // 2
    print(ans)


if __name__ == "__main__":
    main()
