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
    T = NI()
    for _ in range(T):
        N, S = SMI()
        N = int(N)
        S = int(S.replace(".", ""))
        ans = 0
        for i in range(1, 2001):
            if i > N:
                break
            l = S * i
            r = (S+1) * i - 1
            if r // 1000 * 1000 >= l:
                # print(i, l, r)
                ans += 1
        if N > 2000:
            ans += N - 2000
        print(ans)


if __name__ == "__main__":
    main()
