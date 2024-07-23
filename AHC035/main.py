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


IS_LOCAL = True
try:
    import matplotlib
except:
    IS_LOCAL = False

from random import randint

def main():
    N, M, T = NMI()
    SN = 2 * N * (N-1)

    # 中心から渦巻きの配置
    order = [
        [2, 2], [2, 3], [3, 3], [3, 2], [3, 1], [2, 1],
        [1, 1], [1, 2], [1, 3], [1, 4], [2, 4], [3, 4],
        [4, 4], [4, 3], [4, 2], [4, 1], [4, 0], [3, 0],
        [2, 0], [1, 0], [0, 0], [0, 1], [0, 2], [0, 3],
        [0, 4], [0, 5], [1, 5], [2, 5], [3, 5], [4, 5],
        [5, 5], [5, 4], [5, 3], [5, 2], [5, 1], [5, 0],
    ]

    X = [[NLI(), i] for i in range(SN)]

    Xbests = [[] for _ in range(M)]
    for x, i in X:
        for y in range(M):
            Xbests[y].append(x[y])
    for y in range(M):
        Xbests[y].sort(reverse=True)

    U = []
    V = []
    if IS_LOCAL:
        for _ in range(T):
            UU = [SLI() for _ in range(N)]
            VV = [SLI() for _ in range(N - 1)]
            U.append(UU)
            V.append(VV)


    def simulate(X, RARE):
        # そのパラメータで理論値top2以上の値を持っている種の少なさ(2ならRARE、あとは反比例)
        rarity = [RARE] * M

        def judge_seed(x):
            base = sum(x)
            for l in range(M):
                if x[l] == Xbests[l][0]:
                    base += rarity[l]
                elif x[l] == Xbests[l][1]:
                    base += rarity[l]
            return base

        for t in range(T):
            # 合計値の大きい種を残す Xmaxの要素があると大きく加点
            XS = sorted(X, reverse=True, key=lambda x: judge_seed(x[0]))
            A = [[0] * N for _ in range(N)]
            for i in range(N ** 2):
                x, xi = XS[i]
                A[order[i][0]][order[i][1]] = xi
            # for row in A:
            #     print(*row, flush=True)

            # 次の入力をランダムに決定
            Xn = []
            for h in range(N):
                for w in range(N - 1):
                    L = X[A[h][w]][0]
                    R = X[A[h][w + 1]][0]
                    xn = L[:]
                    for l in range(M):
                        s = str(randint(0, 1))
                        if s == "1":
                            xn[l] = R[l]
                    Xn.append(xn)
            for h in range(N - 1):
                for w in range(N):
                    L = X[A[h][w]][0]
                    R = X[A[h + 1][w]][0]
                    xn = L[:]
                    for l in range(M):
                        s = str(randint(0, 1))
                        if s == "1":
                            xn[l] = R[l]
                    Xn.append(xn)
            X = [[xn, i] for i, xn in enumerate(Xn)]

            # rarity補正
            cnts = [0] * M
            for xn, i in X:
                for l in range(M):
                    if xn[l] >= Xbests[l][1]:
                        cnts[l] += 1
            for l in range(M):
                if cnts[l] == 0:
                    continue
                rarity[l] = int(RARE / cnts[l])
            # print("#", X)

        W = max(sum(x) for x, _ in X)
        score = 10 ** 6 * W / sum(Xbests[i][0] for i in range(M))
        # print("# rare:", RARE)
        # print("# score:", score)
        return score

    trial_res = []
    for RARE in [100, 200, 500, 1000, 1500, 2000, 3000]:
        res = []
        for trial in range(200):
            res.append(simulate(X, RARE))
        trial_res.append([int(sum(res)), RARE])

    print("#", trial_res)
    trial_res.sort(reverse=True)


    # そのパラメータで理論値top2以上の値を持っている種の少なさ(2ならRARE、あとは反比例)
    RARE = trial_res[0][1]
    rarity = [RARE] * M

    def judge_seed(x):
        base = sum(x)
        for l in range(M):
            if x[l] == Xbests[l][0]:
                base += rarity[l]
            elif x[l] == Xbests[l][1]:
                base += rarity[l]
        return base



    for t in range(T):
        # 合計値の大きい種を残す Xmaxの要素があると大きく加点
        XS = sorted(X, reverse=True, key=lambda x: judge_seed(x[0]))
        A = [[0]*N for _ in range(N)]
        for i in range(N**2):
            x, xi = XS[i]
            A[order[i][0]][order[i][1]] = xi
        for row in A:
            print(*row, flush=True)

        # 次の入力
        if IS_LOCAL:
            Ut = U[t]
            Vt = V[t]
            Xn = []
            for h in range(N):
                for w in range(N-1):
                    L = X[A[h][w]][0]
                    R = X[A[h][w+1]][0]
                    xn = L[:]
                    for l, s in enumerate(Ut[h][w]):
                        if s == "1":
                            xn[l] = R[l]
                    Xn.append(xn)
            for h in range(N-1):
                for w in range(N):
                    L = X[A[h][w]][0]
                    R = X[A[h+1][w]][0]
                    xn = L[:]
                    for l, s in enumerate(Vt[h][w]):
                        if s == "1":
                            xn[l] = R[l]
                    Xn.append(xn)
            X = [[xn, i] for i, xn in enumerate(Xn)]
        else:
            X = [[NLI(), i] for i in range(SN)]

        # rarity補正
        cnts = [0] * M
        for xn, i in X:
            for l in range(M):
                if xn[l] >= Xbests[l][1]:
                    cnts[l] += 1
        for l in range(M):
            if cnts[l] == 0:
                continue
            rarity[l] = int(RARE / cnts[l])
        # print("#", X)

    W = max(sum(x) for x, _ in X)
    print("# score:", 10**6 * W / sum(Xbests[i][0] for i in range(M)))


if __name__ == "__main__":
    main()
