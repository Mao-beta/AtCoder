import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.set_int_max_str_digits(10 ** 6)
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


def _main():
    N, M, K = NMI()
    A = EI(N)
    S = []
    for _ in range(M):
        s = EI(3)
        S.append(s)

    ans = []

    # 左上から決定
    # 右端と下端は3個ずつ考慮
    for i in range(N-2):
        for j in range(N-2):
            if i < N-3 and j < N-3:
                # 右端と下端以外
                a = A[i][j]
                ti = -1
                ma = a
                for m in range(M):
                    stamp = S[m]
                    na = (a + stamp[0][0]) % MOD99
                    if na > ma:
                        ti = m
                        ma = na
                if ti >= 0:
                    ans.append([ti, i, j])
                    for si in range(3):
                        for sj in range(3):
                            A[i+si][j+sj] = (A[i+si][j+sj] + S[ti][si][sj]) % MOD99

            elif i < N-3:
                # 下端でなく右端は3個考慮
                a = A[i][6] + A[i][7] + A[i][8]
                ti = -1
                ma = a
                for m in range(M):
                    stamp = S[m]
                    na = (A[i][6] + stamp[0][0]) % MOD99 + (A[i][7] + stamp[0][1]) % MOD99 + (A[i][8] + stamp[0][2]) % MOD99
                    if na > ma:
                        ti = m
                        ma = na
                if ti >= 0:
                    ans.append([ti, i, j])
                    for si in range(3):
                        for sj in range(3):
                            A[i + si][j + sj] = (A[i + si][j + sj] + S[ti][si][sj]) % MOD99

            elif j < N-3:
                # 右端でなく下端は3個考慮
                a = A[6][j] + A[7][j] + A[8][j]
                ti = -1
                ma = a
                for m in range(M):
                    stamp = S[m]
                    na = (A[6][j] + stamp[0][0]) % MOD99 + (A[7][j] + stamp[1][0]) % MOD99 + (
                                A[8][j] + stamp[2][0]) % MOD99
                    if na > ma:
                        ti = m
                        ma = na
                if ti >= 0:
                    ans.append([ti, i, j])
                    for si in range(3):
                        for sj in range(3):
                            A[i + si][j + sj] = (A[i + si][j + sj] + S[ti][si][sj]) % MOD99

            else:
                # 右端かつ下端は9個考慮
                a = 0
                for si in range(3):
                    for sj in range(3):
                        a += A[i+si][j+sj]
                ti = -1
                ma = a
                for m in range(M):
                    stamp = S[m]
                    na = 0
                    for si in range(3):
                        for sj in range(3):
                            na += (A[i + si][j + sj] + stamp[si][sj]) % MOD99
                    if na > ma:
                        ti = m
                        ma = na
                if ti >= 0:
                    ans.append([ti, i, j])
                    for si in range(3):
                        for sj in range(3):
                            A[i + si][j + sj] = (A[i + si][j + sj] + S[ti][si][sj]) % MOD99

    # # 右下から上へ
    # for i in range(N-3, -1, -1):
    #     j = N-3
    #     if i > 0:
    #         # 上端でなく右端は下3個考慮
    #         a = A[i+2][6] + A[i+2][7] + A[i+2][8]
    #         ti = -1
    #         ma = a
    #         for m in range(M):
    #             stamp = S[m]
    #             na = (A[i+2][6] + stamp[2][0]) % MOD99 + (A[i+2][7] + stamp[2][1]) % MOD99 + (A[i+2][8] + stamp[2][2]) % MOD99
    #             if na > ma:
    #                 ti = m
    #                 ma = na
    #         if ti >= 0:
    #             ans.append([ti, i, j])
    #             for si in range(3):
    #                 for sj in range(3):
    #                     A[i + si][j + sj] = (A[i + si][j + sj] + S[ti][si][sj]) % MOD99
    #
    #     else:
    #         # 右端かつ下端は9個考慮
    #         a = 0
    #         for si in range(3):
    #             for sj in range(3):
    #                 a += A[i+si][j+sj]
    #         ti = -1
    #         ma = a
    #         for m in range(M):
    #             stamp = S[m]
    #             na = 0
    #             for si in range(3):
    #                 for sj in range(3):
    #                     na += (A[i + si][j + sj] + stamp[si][sj]) % MOD99
    #             if na > ma:
    #                 ti = m
    #                 ma = na
    #         if ti >= 0:
    #             ans.append([ti, i, j])
    #             for si in range(3):
    #                 for sj in range(3):
    #                     A[i + si][j + sj] = (A[i + si][j + sj] + S[ti][si][sj]) % MOD99
    #
    # # 右下から左へ
    # for j in range(N-3, -1, -1):
    #     i = N-3
    #     if j > 0:
    #         # 左端でなく下端は右3個考慮
    #         a = A[6][j+2] + A[7][j+2] + A[8][j+2]
    #         ti = -1
    #         ma = a
    #         for m in range(M):
    #             stamp = S[m]
    #             na = (A[6][j+2] + stamp[0][2]) % MOD99 + (A[7][j+2] + stamp[1][2]) % MOD99 + (A[8][j+2] + stamp[2][2]) % MOD99
    #             if na > ma:
    #                 ti = m
    #                 ma = na
    #         if ti >= 0:
    #             ans.append([ti, i, j])
    #             for si in range(3):
    #                 for sj in range(3):
    #                     A[i + si][j + sj] = (A[i + si][j + sj] + S[ti][si][sj]) % MOD99
    #
    #     else:
    #         # 右端かつ下端は9個考慮
    #         a = 0
    #         for si in range(3):
    #             for sj in range(3):
    #                 a += A[i+si][j+sj]
    #         ti = -1
    #         ma = a
    #         for m in range(M):
    #             stamp = S[m]
    #             na = 0
    #             for si in range(3):
    #                 for sj in range(3):
    #                     na += (A[i + si][j + sj] + stamp[si][sj]) % MOD99
    #             if na > ma:
    #                 ti = m
    #                 ma = na
    #         if ti >= 0:
    #             ans.append([ti, i, j])
    #             for si in range(3):
    #                 for sj in range(3):
    #                     A[i + si][j + sj] = (A[i + si][j + sj] + S[ti][si][sj]) % MOD99




    ans = ans[:K]
    print(len(ans))
    for row in ans:
        print(*row)


def main():
    # 6x6を先にやる
    # 残り3x3x5の領域は5個以内の合成スタンプで頑張る
    N, M, K = NMI()
    A = EI(N)
    S = []
    for _ in range(M):
        s = EI(3)
        S.append(s)

    ans = []

    # 左上から決定　6x6
    for i in range(N-3):
        for j in range(N-3):
            if i < N-3 and j < N-3:
                # 右端と下端以外
                a = A[i][j]
                ti = -1
                ma = a
                for m in range(M):
                    stamp = S[m]
                    na = (a + stamp[0][0]) % MOD99
                    if na > ma:
                        ti = m
                        ma = na
                if ti >= 0:
                    ans.append([ti, i, j])
                    for si in range(3):
                        for sj in range(3):
                            A[i+si][j+sj] = (A[i+si][j+sj] + S[ti][si][sj]) % MOD99

    T = []
    for num in range(1, 6):
        for P in combinations(range(M), num):
            P = list(P)
            t = [[0]*3 for _ in range(3)]
            for si in P:
                for i in range(3):
                    for j in range(3):
                        t[i][j] += S[si][i][j]
            T.append([t, P])


    def stamp(i, j):
        a = 0
        for si in range(3):
            for sj in range(3):
                a += A[i + si][j + sj]
        mp = []
        ma = a
        for stamp, P in T:
            na = 0
            for si in range(3):
                for sj in range(3):
                    na += (A[i + si][j + sj] + stamp[si][sj]) % MOD99
            if na > ma:
                mp = P
                ma = na
        if mp and len(mp) + len(ans) <= K:
            for ti in mp:
                ans.append([ti, i, j])
                for si in range(3):
                    for sj in range(3):
                        A[i + si][j + sj] = (A[i + si][j + sj] + S[ti][si][sj]) % MOD99

    stamp(6, 0)
    stamp(6, 3)
    stamp(6, 6)
    stamp(0, 6)
    stamp(3, 6)

    ans = ans[:K]
    print(len(ans))
    for row in ans:
        print(*row)


if __name__ == "__main__":
    main()
