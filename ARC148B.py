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


from typing import List
from itertools import groupby

# RUN LENGTH ENCODING str -> list(tuple())
# example) "aabbbbaaca" -> [('a', 2), ('b', 4), ('a', 2), ('c', 1), ('a', 1)]
def runLengthEncode(S: str) -> "List[tuple[str, int]]":
    grouped = groupby(S)
    res = []
    for k, v in grouped:
        res.append((k, int(len(list(v)))))
    return res


def main(N, S):

    if len(set(S)) == 1:
        if S[0] == "d":
            return S
        else:
            return "d"*N

    SR = runLengthEncode(S)
    SSR = sorted(SR)
    maxp = SSR[-1][1]

    L = list(S)

    now = 0
    l = 0
    ok = False
    T = [S]
    f = {"d": "p", "p": "d"}

    for s, k in SR:
        if not ok:
            if s == "d":
                pass
            else:
                ok = True
                l = now

        now += k

        if ok:
            tmp = L[:l] + list(map(lambda x: f[x], L[l:now][::-1])) + L[now:]
            T.append("".join(tmp))

    return sorted(T)[0]


def guchoku(N, S):
    L = list(S)
    f = {"d": "p", "p": "d"}
    T = [S]
    for l in range(N):
        for r in range(l, N+1):
            tmp = L[:l] + list(map(lambda x: f[x], L[l:r][::-1])) + L[r:]
            T.append("".join(tmp))
    # print(T)
    return sorted(T)[0]


if __name__ == "__main__":
    N = NI()
    S = SI()
    print(main(N, S))

    # for N in range(1, 9):
    #     print(N)
    #     for S in product("dp", repeat=N):
    #         S = "".join(S)
    #         res = main(N, S)
    #         res_g = guchoku(N, S)
    #         if res != res_g:
    #             print(N, S)
    #             print(res, res_g)
