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
    ST = EI(N)
    M = 200000
    S = [[] for i in range(M+1)]
    T = [[] for i in range(M+1)]
    for i, (s, t) in enumerate(ST):
        S[s].append(i)
        T[t].append(i)
    done = 0
    yet = N
    ans = [N-1] * N
    for i in range(M+1):
        for s in S[i]:
            ans[s] -= done
            yet -= 1
        for t in T[i]:
            ans[t] -= yet
            done += 1
    print(*ans)


if __name__ == "__main__":
    main()
