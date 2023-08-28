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
    N, *A = NMI()
    # 最大61桁あるとする
    B = 61

    # 上からi桁決めた 未満フラグがj(000~111) 余りがk, l, m
    dp = [[[[[0]*A[2] for _ in range(A[1])] for _ in range(A[0])]
           for _ in range(8)] for _ in range(B+1)]
    dp[0][0][0][0][0] = 1

    for i in range(B):
        # 次は下からt-bit(0-index)めをみる
        # i=0 -> t=B-1
        # i=B-1 -> t=0
        t = B-1 - i
        x = (N >> t) & 1

        # そもそも無理な桁はとばす
        if (1 << t) > N:
            dp[i+1][0][0][0][0] += dp[i][0][0][0][0]
            continue

        # その桁のbitを立てたときの、あまりへの寄与
        dk = (1 << t) % A[0]
        dl = (1 << t) % A[1]
        dm = (1 << t) % A[2]

        for j in range(8):
            # 現状のjで、その桁のbitを立てられるか？
            # N未満確定なら1をとれる、そうでないならN(その桁のbitはx)依存
            x0max = 1 if (j >> 0) & 1 else x
            x1max = 1 if (j >> 1) & 1 else x
            x2max = 1 if (j >> 2) & 1 else x

            for x0 in range(x0max+1):
                for x1 in range(x1max+1):
                    # x0とx1がきまればx2は自動できまる
                    x2 = x0 ^ x1
                    # 上限オーバーなら諦める
                    if x2 > x2max:
                        continue

                    # 遷移先の未満フラグ
                    # もともと未満フラグがなく、かつ次も追従なら0にする
                    nj = (1<<3) - 1
                    if (j >> 0) & 1 == 0 and x0 == x0max:
                        nj ^= 1 << 0
                    if (j >> 1) & 1 == 0 and x1 == x1max:
                        nj ^= 1 << 1
                    if (j >> 2) & 1 == 0 and x2 == x2max:
                        nj ^= 1 << 2

                    for k in range(A[0]):
                        for l in range(A[1]):
                            for m in range(A[2]):
                                if dp[i][j][k][l][m] == 0:
                                    continue

                                # 遷移先のあまりが確定
                                # bitを立てる予定ならd*を足す
                                nk = (k + dk * x0) % A[0]
                                nl = (l + dl * x1) % A[1]
                                nm = (m + dm * x2) % A[2]
                                dp[i+1][nj][nk][nl][nm] += dp[i][j][k][l][m]
                                dp[i+1][nj][nk][nl][nm] %= MOD99

    ans = 0
    for j in range(8):
        # print(dp[B][j][0][0][0])
        ans += dp[B][j][0][0][0]

    # 現在のansは
    # 0以上N以下のXi, XiはそれぞれAiの倍数、累積xorが0
    # なる(X0, X1, X2)の個数

    # なので、0が1個だけまたは3個であるケースを含んでいる

    # Xi == 0, それ以外は正　のケースをそれぞれ引く
    # X0 == 0 のとき X1 == X2 かつ X1 % A[1] == 0 かつ X2 % A[2] == 0
    # よって X1 == X2 は A[1]とA[2]の公倍数で1以上N以下のもの
    for i in range(3):
        a, b = A[i], A[(i+1)%3]
        g = math.gcd(a, b)
        lcm = a * b // g
        # print(N, lcm)
        ans -= N // lcm

    # 3つ0のパターンを引く
    ans -= 1

    print(ans % MOD99)


if __name__ == "__main__":
    main()
