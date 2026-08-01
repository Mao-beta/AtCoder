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
    ADB = EI(N)
    C = Counter([a for a, d, b in ADB])
    DB = defaultdict(list)
    for a, d, b in ADB:
        DB[d].append([a, b])
    ans = len(C)
    for j in range(1, M+1):
        for a, b in DB[j]:
            C[a] -= 1
            if C[a] == 0:
                ans -= 1
            if C[b] == 0:
                ans += 1
            C[b] += 1
        print(ans)


if __name__ == "__main__":
    main()
