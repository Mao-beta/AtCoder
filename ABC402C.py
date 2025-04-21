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
    A2I = [[] for _ in range(N+1)]
    As = []
    for i in range(M):
        k, *A = NMI()
        As.append(set(A))
        for a in A:
            A2I[a].append(i)
    B = NLI()
    ans = 0
    for b in B:
        for i in A2I[b]:
            if len(As[i]) == 1:
                ans += 1
            As[i].discard(b)
        print(ans)


if __name__ == "__main__":
    main()
