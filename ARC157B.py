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


def main(N, K, S):
    X = S.count("X")
    Y = N - X

    if N == 1:
        return 0

    if X == 0:
        return max(0, N-1 - K)

    if K <= X:
        ans = 0
        R = runLengthEncode(S)
        # print(R)
        Xs = []
        edges = []
        L = len(R)
        for i, (xy, k) in enumerate(R):
            if xy == "Y":
                ans += k-1
                continue

            if 0 < i < L-1:
                Xs.append(k)
            else:
                edges.append(k)

        Xs.sort()
        rem = K
        for x in Xs:
            if rem >= x:
                rem -= x
                ans += x+1
            else:
                ans += rem
                rem = 0

        if rem > 0:
            return Y + K - 1
        else:
            return ans

    else:
        ans = N-1
        R = runLengthEncode(S)
        # print(R)
        Ys = []
        edges = []
        L = len(R)
        for i, (xy, k) in enumerate(R):
            if xy == "X":
                continue

            if 0 < i < L - 1:
                Ys.append(k)
            else:
                edges.append(k)

        rem = K - X
        for y in edges:
            if rem >= y:
                rem -= y
                ans -= y
            else:
                ans -= rem
                rem = 0

        if rem == 0:
            return ans

        # print(Ys, ans)
        Ys.sort(reverse=True)
        for y in Ys:
            if rem >= y:
                ans -= y+1
                rem -= y
            else:
                ans -= rem+1
                rem = 0

            if rem <= 0:
                break

        return ans


def guchoku(N, K, S):
    S = list(S)
    ans = 0
    for P in combinations(range(N), K):
        tmp = 0
        SS = S.copy()
        for p in P:
            if SS[p] == "X":
                SS[p] = "Y"
            else:
                SS[p] = "X"

        R = runLengthEncode(SS)
        for x, k in R:
            if x == "Y":
                tmp += k-1

        ans = max(ans, tmp)

    return ans


if __name__ == "__main__":
    N, K = NMI()
    S = SI()
    print(main(N, K, S))
    # for N in range(1, 6):
    #     for K in range(0, N+1):
    #         for S in product("XY", repeat=N):
    #             print(S)
    #             ans = main(N, K, S)
    #             gu = guchoku(N, K, S)
    #             assert ans == gu, [N, K, S, ans, gu]
