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
    N, K = NMI()
    ABC = deque(EI(N))
    R = [[0, 0]]
    total = 0
    now = 0
    while R or ABC:
        while ABC and total + ABC[0][2] <= K:
            a, b, c = ABC.popleft()
            now = max(now, a)
            # print(now, "in", a, b, c)
            # print(now, total, R, ABC)
            print(now)
            total += c
            heappush(R, [now+b, c])
        t, k = heappop(R)
        total -= k
        now = max(now, t)
        # print(now, total, R, ABC)


if __name__ == "__main__":
    main()
