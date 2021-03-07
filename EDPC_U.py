import sys
import math
from collections import defaultdict
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    N = NI()
    A = [NLI() for _ in range(N)]

    # dp[S]は集合Sを任意にグループ分けしたときの最大得点
    dp = [0]*(1<<N)
    # score[S]は集合Sが同一グループのときのスコア
    score = [0]*(1<<N)

    # 各caseの部分集合のみを探索することでO(3^N)
    for case in range(1<<N):

        # 今回のcaseが全員同じグループのときのスコアを計算
        for i in range(N):
            for j in range(i+1, N):
                if (case>>i) & (case>>j) & 1:
                    score[case] += A[i][j]

        # caseの部分集合subを全探索
        # 1を引いてcaseでマスクすると一つ下の部分集合に遷移できる
        # subを1グループとして切り分けて離脱させるイメージ
        sub = case
        while sub > 0:
            dp[case] = max(dp[case], score[sub]+dp[sub^case])
            sub = (sub - 1) & case

    print(dp[-1])


if __name__ == "__main__":
    main()
