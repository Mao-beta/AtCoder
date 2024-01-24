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
    H, W, K = NMI()
    S = [SI() for _ in range(H)]
    INF = 10**7

    def solve(S):
        res = INF
        sh = len(S)
        for h in range(sh):
            D = deque()
            r = 0
            for s in S[h]:
                if s == "x":
                    if len(D) == K:
                        res = min(res, K-r)
                    D = deque()
                    r = 0
                else:
                    D.append(s)
                    if s == "o":
                        r += 1
                    while len(D) > K:
                        sl = D.popleft()
                        if sl == "o":
                            r -= 1
                    if len(D) == K:
                        res = min(res, K-r)
        return res

    ans = INF
    ans = min(ans, solve(S))
    S = [x for x in zip(*S)]
    ans = min(ans, solve(S))
    print(ans if ans < INF else -1)


if __name__ == "__main__":
    main()
