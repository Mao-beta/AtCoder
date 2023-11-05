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
    N, M = NMI()
    B = EI(M)
    ans = []
    nex = [1]


    def sort_column(c):
        res = []
        # c列目をsort
        # ほか9列を使って、大きいものの直上をよけていく
        X = [[] for _ in range(M)]
        X[c] = B[c][:]
        E = sorted(B[c])[-8:][::-1]
        rem = sorted(B[c])[:-8][::-1]

        IDX = []
        for e in E:
            IDX.append(X[c].index(e))
        IDX.sort()
        temae = []
        for idx in IDX:
            if idx < len(X[c])-1:
                temae.append(X[c][idx+1])
        goto = 0
        while temae:
            t = temae.pop()
            if goto == c:
                goto += 1
            res.append([t, goto])
            X[goto] += X[c][X[c].index(t):]
            X[c] = X[c][:X[c].index(t)]
            goto += 1

        if len(X[c]) > 0:
            if goto == c:
                goto += 1
            res.append([X[c][0], goto])
            X[goto] += X[c][:]
            X[c] = []

        for e in E:
            res.append([e, c])
            for t in range(M):
                if t == c:
                    continue
                if e in X[t]:
                    X[t].pop()
                    X[c].append(e)
                    break

        # print(*X, sep="\n")

        # 残りを戻すときは貪欲
        for r in rem:
            # print("#", r)
            for t in range(M):
                if t == c:
                    continue
                if r in X[t]:
                    idx = X[t].index(r)
                    if idx == len(X[t])-1:
                        res.append([r, c])
                        X[t].pop()
                        X[c].append(r)
                    else:
                        goto = 9
                        for g in range(M):
                            if len(X[g]) == 0:
                                goto = g
                                break

                        res.append([X[t][idx+1], goto])
                        X[goto] += X[t][idx+1:]
                        res.append([r, c])
                        X[t] = X[t][:idx]
                    break


        for r in res:
            x, t = r
            print(x, t+1)

        # print(X[c])


    for c in range(M):
        sort_column(c)

    for x in range(1, N+1):
        print(x, 0)


if __name__ == "__main__":
    main()
