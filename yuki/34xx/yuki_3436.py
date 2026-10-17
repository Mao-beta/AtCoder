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
    Q = NI()
    for _ in range(Q):
        N, M, K, P = NMI()
        T = NLI()
        C = NLI()
        B = NLI()
        D = NLI()
        S = [0] + NLI()
        BD2J = defaultdict(list)
        B2J = defaultdict(list)

        K2B = [[] for _ in range(K+1)]
        for j, (b, d) in enumerate(zip(B, D)):
            K2B[d].append(b)
            BD2J[(b, d)].append(j)
            B2J[b].append(j)
        for k in range(K+1):
            K2B[k].sort()
        SB = sorted(B)

        def judge(X):
            res = 0
            for t, c in zip(T, C):
                res += bisect.bisect_right(SB, X-t)
                res += bisect.bisect_right(K2B[c], X+S[c]-t)
                res -= bisect.bisect_right(K2B[c], X-t)
            return res >= P

        ok = 10**18
        ng = 0
        while abs(ok - ng) > 1:
            X = (ok + ng) // 2
            if judge(X):
                ok = X
            else:
                ng = X

        # print(f"{ok=}")

        for i, (t, c) in enumerate(zip(T, C)):
            # print(t, ok+S[c]-t)
            same = BD2J[(ok+S[c]-t, c)]
            # print(same)
            if same:
                print(i+1, same[0]+1)
                break
            odd = B2J[ok-t]
            flg = False
            for j in odd:
                if D[j] != c:
                    flg = True
                    print(i+1, j+1)
                    break
            if flg:
                break


if __name__ == "__main__":
    main()
