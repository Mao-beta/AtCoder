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
    N, L = NMI()
    C = [0] * L
    now = 0
    C[now] += 1
    D = NLI()
    if L % 3:
        print(0)
        return
    for d in D:
        now = (now+d) % L
        C[now] += 1
    ans = 0
    for i in range(L//3):
        ans += C[i] * C[i+L//3] * C[i+L//3*2]
    print(ans)


if __name__ == "__main__":
    main()
