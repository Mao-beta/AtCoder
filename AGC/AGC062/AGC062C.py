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
    N, K = NMI()
    A = NLI()
    A.sort()
    A.append(10**20)

    cutoff = 20

    if N <= cutoff:
        S = set()
        S.add(0)

        for a in A:
            T = set()
            for s in S:
                T.add(s)
                T.add(s+a)
            S = T

        ans = []
        for i in range(1, 10**7):
            if i not in S:
                ans.append(i)
            if len(ans) >= K:
                break

        print(*ans[:K])

    else:
        S = set()
        S.add(0)

        for a in A[:cutoff]:
            T = set()
            for s in S:
                T.add(s)
                T.add(s + a)
            S = T

        M = max(S)
        # print(S)

        B = set()
        for i in range(1, M+1):
            if i not in S:
                B.add(i)

        for a in A[cutoff:]:
            # print(a, M, B)
            if a >= M:
                if a > M + K:
                    for x in range(M+1, M+1+K):
                        B.add(x)
                    break

                for x in range(M+1, a):
                    B.add(x)

                for b in list(B):
                    B.add(b+a)

            else:
                C = set()
                for b in list(B):
                    C.add(b)
                    if b >= a and b-a not in B:
                        C.discard(b)

                for b in list(B):
                    x = b + a
                    if x <= M and x not in C:
                        continue
                    else:
                        C.add(x)

                B = C
            # print(sorted(list(B)))
            M += a
            if len(B) >= 10**6:
                break

        if len(B) < K:
            for i in range(max(A)+1, max(A)+K+1):
                B.add(i)

        ans = sorted(list(B))

        print(*ans[:K])



if __name__ == "__main__":
    main()
