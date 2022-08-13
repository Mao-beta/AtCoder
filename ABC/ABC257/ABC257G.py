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


# KMP法
# 1対1の検索アルゴリズム。Tが固定のときTableを使いまわせる？
# 前計算O(|T|), 検索O(|S|)
# 事前にTから「j文字目で照合失敗したら次は何文字ずらすか」テーブルを作っておき、
# マッチ位置を試す位置を少なくする。
def make_kmp_table(t):
    """
    tbl[i]: t[:x] == t[i-x:i] となる最大のx
    つまり、tのi文字目からみて後ろ何文字が、tのprefixと一致するか
    """
    i = 2
    j = 0
    m = len(t)
    tbl = [0] * (m + 1)
    tbl[0] = -1
    while i <= m:
        if t[i - 1] == t[j]:
            tbl[i] = j + 1
            i += 1
            j += 1
        elif j > 0:
            j = tbl[j]
        else:
            tbl[i] = 0
            i += 1
    return tbl


def kmp(s, t):
    matched_indices = []
    tbl = make_kmp_table(t)
    i = 0
    j = 0
    n = len(s)
    m = len(t)
    while i + j < n:
        if t[j] == s[i + j]:
            j += 1
            if j == m:
                matched_indices.append(i)
                i += j - tbl[j]
                j = tbl[j]
        else:
            i += j - tbl[j]
            if j > 0:
                j = tbl[j]
    return matched_indices


def main():
    S = SI()
    T = SI()
    N = len(T)
    tbl = make_kmp_table(S+"$"+T)[-N:]
    idx = N
    ans = 0
    # print(tbl)
    while idx != 0 and tbl[idx-1] > 0:
        idx -= tbl[idx-1]
        ans += 1
        # print(idx)
    if idx == 0:
        print(ans)
    else:
        print(-1)


if __name__ == "__main__":
    main()
