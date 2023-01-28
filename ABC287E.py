import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations

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
    S = [[SI(), i] for i in range(N)]
    S.sort()
    
    def lcp(s, t):
        res = 0
        for ss, tt in zip(s, t):
            if ss == tt:
                res += 1
            else:
                break
        return res
    
    ans = [0] * N
    for i in range(N-1):
        s, si = S[i]
        t, ti = S[i+1]
        l = lcp(s, t)
        ans[si] = max(ans[si], l)
        ans[ti] = max(ans[ti], l)

    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
