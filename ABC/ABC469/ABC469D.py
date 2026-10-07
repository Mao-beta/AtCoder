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
    AB = EI(M)

    ans = set()

    x = AB[0][0]
    rem = 0
    C = Counter()
    for a, b in AB:
        if a != x and b != x:
            C[a] += 1
            C[b] += 1
        else:
            rem += 1
    for i in range(1, N+1):
        if i != x and C[i] + rem == M:
            ans.add((min(x, i), max(x, i)))

    x = AB[0][1]
    rem = 0
    C = Counter()
    for a, b in AB:
        if a != x and b != x:
            C[a] += 1
            C[b] += 1
        else:
            rem += 1
    for i in range(1, N + 1):
        if i != x and C[i] + rem == M:
            ans.add((min(x, i), max(x, i)))

    print(len(ans))


if __name__ == "__main__":
    main()
