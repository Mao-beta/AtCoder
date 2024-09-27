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
    AB = EI(N)
    L = [0] * (N+1)
    R = [0] * (N+1)
    ML = [0] * (N+1)
    MR = [0] * (N+1)
    for i, (a, b) in enumerate(AB):
        L[i+1] = L[i] + a / b
        ML[i+1] = ML[i] + a
    for i, (a, b) in enumerate(AB[::-1]):
        R[N-i-1] = R[N-i] + a / b
        MR[N-i-1] = MR[N-i] + a
    R = R[::-1]

    def judge(X):
        # X秒時点ですでに交差しているか
        li = bisect.bisect_left(L, X) - 1
        ri = bisect.bisect_left(R, X) - 1
        if N-ri <= li:
            return True
        if N-ri - li >= 2:
            return False
        a, b = AB[li]
        rem = (X - L[li]) * b + (X - R[ri]) * b
        return rem >= a

    ok = 10**10
    ng = 0
    for _ in range(100):
        X = (ok + ng) / 2
        if judge(X):
            ok = X
        else:
            ng = X

    X = ok
    li = bisect.bisect_left(L, X) - 1
    ri = bisect.bisect_left(R, X) - 1
    a, b = AB[li]
    ans = ML[li] + (X - L[li]) * b
    print(ans)


if __name__ == "__main__":
    main()
