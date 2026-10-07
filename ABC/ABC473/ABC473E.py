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
    A = NLI()
    C = list(accumulate([0]+A))
    D = defaultdict(list)
    for i, c in enumerate(C):
        D[c%K].append(i)
    LR = []
    for c, L in D.items():
        for i in range(len(L)-1):
            LR.append([L[i], L[i+1]])
    LR.sort(key=lambda x: x[1])
    ans = 0
    now = 0
    # print(D)
    # print(LR)
    for l, r in LR:
        if l < now:
            continue
        ans += 1
        now = r
    print(ans)


if __name__ == "__main__":
    main()
