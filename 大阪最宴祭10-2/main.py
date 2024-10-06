import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

import pandas as pd

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


def compress(S):
    """ 座標圧縮 """

    S = set(S)
    zipped, unzipped = {}, {}
    for i, a in enumerate(sorted(S)):
        zipped[a] = i
        unzipped[i] = a
    return zipped, unzipped


def main():
    df = pd.read_csv("./table.csv")
    df = df.loc[df["完売"]==0].reset_index(drop=True)
    df["回ID"] = df.index
    print(df)

    # S: 公演の最大種類数
    S = len(set(df["公演ID"]))
    # 時刻の座標圧縮
    times = set(df["開始時刻(分)"]) | set(df["終了時刻(分)"])
    Z, UZ = compress(times)
    T = len(Z)
    # 公演IDごとの開始/終了時間のリスト
    sID2start = {sID: sorted(list(sub_df.values)) for sID, sub_df in df.groupby("公演ID")["開始時刻(分)"]}
    sID2end = {sID: sorted(list(sub_df.values)) for sID, sub_df in df.groupby("公演ID")["終了時刻(分)"]}
    print(sID2start)

    df = df.sort_values("終了時刻(分)")

    print(f"{S=} {T=} {Z=}")

    # 直前の終了時刻がztで、回った公演の集合がs
    dp = [[0]*(1<<S) for _ in range(T)]
    dp[0][0] = 1
    # 直前の回ID
    prev = [[-1]*(1<<S) for _ in range(T)]

    for s in range(1<<S):
        for zt in range(T):
            if dp[zt][s] == 0:
                continue
            print(zt, bin(s)[2:], bin(s)[2:].count("1"))
            t = UZ[zt]
            for sID in range(S):
                if (s >> sID) & 1:
                    continue
                starts = sID2start[sID]
                ends = sID2end[sID]
                nt = -1
                for i in range(len(starts)):
                    start, end = starts[i], ends[i]
                    if t <= start:
                        nt = end
                        break
                if nt < 0:
                    continue
                nzt = Z[nt]
                dp[nzt][s|(1<<sID)] = 1

    for s in range((1<<S)-1, -1, -1):
        for zt in range(T-1, -1, -1):
            if dp[zt][s]:
                print(zt, bin(s)[2:], bin(s)[2:].count("1"))
                break



if __name__ == "__main__":
    main()
