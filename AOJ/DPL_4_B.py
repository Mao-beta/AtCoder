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


def split_and_list(A):
    """
    半分全列挙して前半と後半の部分和を返す
    O(2^(N//2))
    """
    N = len(A)
    former, latter = A[:N // 2], A[N // 2:]
    fn, ln = len(former), len(latter)
    F = []
    for k in range(fn + 1):
        F += [sum(c) for c in combinations(former, k)]
    L = []
    for k in range(ln + 1):
        L += [sum(c) for c in combinations(latter, k)]
    return F, L


def split_and_list_by_size(A):
    """
    半分全列挙して前半と後半の部分和をサイズごとに分けて返す
    O(2^(N//2))
    """
    N = len(A)
    former, latter = A[:N // 2], A[N // 2:]
    fn, ln = len(former), len(latter)
    F = [[sum(c) for c in combinations(former, k)] for k in range(fn + 1)]
    L = [[sum(c) for c in combinations(latter, k)] for k in range(ln + 1)]
    return F, L


def main():
    N, K, L, R = NMI()
    A = NLI()
    former, latter = split_and_list_by_size(A)
    ans = 0
    for kf in range(K+1):
        kl = K - kf
        if kf >= len(former) or kl >= len(latter):
            continue
        Lk = latter[kl]
        Lk.sort()
        for f in former[kf]:
            ans += bisect.bisect_right(Lk, R-f) - bisect.bisect_left(Lk, L-f)
    print(ans)


if __name__ == "__main__":
    main()
