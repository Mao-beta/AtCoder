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
        F += [[sum(former[cc] for cc in c), tuple(cc+1 for cc in c)] for c in combinations(range(fn), k)]
    L = []
    for k in range(ln + 1):
        L += [[sum(latter[cc] for cc in c), tuple(cc+fn+1 for cc in c)] for c in combinations(range(ln), k)]
    return F, L


def main():
    N, S = NMI()
    P = [NI() for _ in range(N)]
    F, L = split_and_list(P)
    F.sort()
    L.sort()
    FX = []
    FI = []
    LX = []
    LI = []
    for x, i in F:
        FX.append(x)
        FI.append(i)
    for x, i in L:
        LX.append(x)
        LI.append(i)

    ans = []
    for fx, fi in zip(FX, FI):
        if fx > S:
            continue
        lx = S - fx
        bl = bisect.bisect_left(LX, lx)
        br = bisect.bisect_right(LX, lx)
        for bi in range(bl, br):
            ans.append(sorted(list(fi) + list(LI[bi])))

    ans.sort()
    for row in ans:
        print(*row)


if __name__ == "__main__":
    main()
