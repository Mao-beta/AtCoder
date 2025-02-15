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


def main(N, M, _S, _T):
    S = _S[:]
    T = _T[:]
    D = [[] for _ in range(10)]
    for i, t in enumerate(T):
        D[int(t)].append(i)
    for i in range(10):
        D[i].sort()
    t = 9
    max_ti = -1
    for i in range(N):
        s = int(S[i])
        while t > 0 and len(D[t]) == 0:
            t -= 1
        if t == 0:
            break
        if s >= t:
            continue
        ti = D[t].pop()
        max_ti = max(max_ti, ti)
        S[i] = str(t)
    if max_ti < M-1:
        x = T[-1]
        if x not in S:
            S[-1] = x
    return "".join(S)


def guchoku(N, M, _S, _T):
    S = _S[:]
    T = _T[:]
    ans = 0
    case = None
    for P in product(range(N), repeat=M):
        tmp = S[:]
        for k, i in enumerate(P):
            tmp[i] = T[k]
        if ans >= int("".join(tmp)):
            continue
        ans = max(ans, int("".join(tmp)))
        case = P
    return str(ans), case


if __name__ == "__main__":
    N, M = NMI()
    S = list(SI())
    T = list(SI())
    ans = main(N, M, S[:], T[:])
    print(ans)
    # N = 4
    # M = 4
    # from random import randint
    # for _ in range(100):
    #     S = [str(randint(1, 9)) for _ in range(N)]
    #     T = [str(randint(1, 9)) for _ in range(M)]
    #     ans = main(N, M, S[:], T[:])
    #     gu, case = guchoku(N, M, S[:], T[:])
    #     print(S, T, ans, gu, case)
    #     assert ans == gu