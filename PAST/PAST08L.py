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


def main():
    N, K = NMI()
    A = NLI()
    B = list(accumulate([0] + A))
    B.sort()

    # 答えを二分探索
    # X以下の値がK個以上あるようなXの最小値
    def judge(X):
        # 総和の絶対値 = abs(Bi-Bj) がX以下のペアがK個以上あるか？
        # sortしたBについてあるBiをとり、|Bi-Bj|<=Xなるjの個数
        # Bi-X <= Bj <= Bi+X なるjの個数は尺取りでもとまる
        # ただし、j=iなるjがあるので1個引く
        # かつ、(i, j), (j, i)を重複しているので2で割る
        res = 0
        l, r = 0, 0
        for b in B:
            while r < len(B) and B[r] <= b+X:
                r += 1
            while l < len(B) and B[l] < b-X:
                l += 1
            res += max(0, r-l-1)
        res //= 2
        return res >= K

    ok = 10**15
    ng = -1
    while abs(ok - ng) > 1:
        X = (ok + ng) // 2
        if judge(X):
            ok = X
        else:
            ng = X

    print(ok)



if __name__ == "__main__":
    main()
