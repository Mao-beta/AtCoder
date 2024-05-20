import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

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
    S = SI()
    K = NI()
    N = len(S)
    S = [int(s == ".") for s in S]
    r = 0
    D = deque()
    dot = 0
    ans = 0
    for l in range(N):
        while r <= N-1 and dot + S[r] <= K:
            dot += S[r]
            D.append(S[r])
            r += 1
        # print(D, l, r)
        ans = max(ans, len(D))
        if len(D) > 0:
            x = D.popleft()
            dot -= x
        if r <= l:
            r = l+1
    print(ans)


if __name__ == "__main__":
    main()
