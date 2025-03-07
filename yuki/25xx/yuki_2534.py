import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.set_int_max_str_digits(10 ** 6)
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
    ans = 1
    while ans <= 51:
        ans += 1
        if N == 1:
            break
        ans += 1
        if N % 2:
            N = 3 * N + 1
        else:
            N //= 2
    if ans <= 50:
        print("Yes")
        print(ans)
    else:
        print("No")


if __name__ == "__main__":
    main()
