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


def compress(S):
    """ 座標圧縮 """

    S = set(S)
    zipped, unzipped = {}, {}
    for i, a in enumerate(sorted(S)):
        zipped[a] = i
        unzipped[i] = a
    return zipped, unzipped


def main():
    N, X = NMI()
    Y = NLI()
    Z = NLI()
    SY = set(Y)
    Y2i = {y: i for i, y in enumerate(Y)}

    Zip, UZip = compress(Y + Z + [0, X])
    ZN = len(Zip)
    s = Zip[0]
    t = Zip[X]
    INF = 10**15
    # dp[is_r][l][r]: lからrまで到達済みで、is_rはいま右端にいるか（ありうる状態は端だけ）
    dp = [[[INF]*ZN for _ in range(ZN)] for _ in range(2)]

    dp[0][s][s] = 0
    dp[1][s][s] = 0

    def check(l, r, p):
        # 次が壁で今までハンマーを取っていないならだめ
        if p in SY:
            i = Y2i[p]
            z = Zip[Z[i]]
            if z < l or r < z:
                return False

        return True


    for gap in range(1, ZN):
        for l in range(ZN-gap):
            r = l + gap
            for is_r in range(2):
                # l+1, rからの遷移
                now = l
                nowp = UZip[now]
                prev = UZip[r if is_r else l+1]
                if check(l+1, r, nowp):
                    dp[0][l][r] = min(dp[0][l][r], dp[is_r][l+1][r] + abs(nowp - prev))

                # l, r-1からの遷移
                now = r
                nowp = UZip[now]
                prev = UZip[r-1 if is_r else l]
                if check(l, r-1, nowp):
                    dp[1][l][r] = min(dp[1][l][r], dp[is_r][l][r-1] + abs(nowp - prev))

    ans = INF
    s, t = min(s, t), max(s, t)
    for l in range(s+1):
        for r in range(t, ZN):
            for is_r in range(2):
                ans = min(ans, dp[is_r][l][r])

    print(ans if ans < INF else -1)



if __name__ == "__main__":
    main()
