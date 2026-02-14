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
    ans = [0] * (N+1)
    for y in range(2, 3200):
        for x in range(1, y):
            n = x**2 + y**2
            if n <= N:
                ans[n] += 1
    ans = [i for i in range(1, N+1) if ans[i] == 1]
    print(len(ans))
    print(*ans)


if __name__ == "__main__":
    main()
