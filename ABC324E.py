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


def included(T, S):
    # TのprefixがSに（連続とは限らない）部分列として何文字含まれるか
    N = len(T)
    ti = 0
    for si, s in enumerate(S):
        if T[ti] == s:
            ti += 1
        if ti >= N:
            break
    return ti


def main():
    N, T = SMI()
    N = int(N)
    S = [SI() for _ in range(N)]
    P = [included(T, s) for s in S]
    R = T[::-1]
    Q = [included(R, s[::-1]) for s in S]
    M = 5 * 10**5 + 1
    Pn = [0] * M
    Qn = [0] * M
    for p in P:
        Pn[p] += 1
    for q in Q:
        Qn[q] += 1
    Qc = list(accumulate(Qn))
    ans = 0
    Tn = len(T)
    for i in range(Tn+1):
        # 前からi個、後ろからTn-i個以上
        if i <= Tn-1:
            ans += Pn[i] * (Qc[Tn] - Qc[Tn-i-1])
        else:
            ans += Pn[i] * Qc[Tn]

    print(ans)


if __name__ == "__main__":
    main()
