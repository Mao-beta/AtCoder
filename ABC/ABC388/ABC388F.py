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
    N, M, A, B = NMI()
    LR = EI(M)

    if A == B:
        if (N-1) % A != 0:
            print("No")
            return
        for l, r in LR:
            l -= 1
            r -= 1
            if l % A == 0 or r % A == 0 or l // A != r // A:
                print("No")
                return
        print("Yes")
        return

    LR.append([N, N])
    buffer = 0
    S = []
    pl, pr = 1, 1
    for l, r in LR:
        l -= buffer
        r -= buffer
        if r-l+1 >= B:
            print("No")
            return
        if pr + 500 < l:
            buffer += l - (pr + 500)
            r -= l - (pr + 500)
            l -= l - (pr + 500)
        S.append([l, r])
        pl, pr = l, r
    N -= buffer
    S.pop()
    # print(S, buffer, N)
    dp = [0] * (N+1)
    dp[1] = 1
    for l, r in S:
        for i in range(l, r+1):
            dp[i] = -1
    for i in range(1, N):
        if dp[i] != 1:
            continue
        for x in range(A, B+1):
            if i+x <= N and dp[i+x] != -1:
                dp[i+x] = 1
    if dp[N] == 1:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
