import sys
import math
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
    items = [[0,0]] + [NLI() for _ in range(N)]
    Q = NI()
    querys = [NLI() for _ in range(Q)]

    # 半分全列挙
    # dp[x][l]: 頂点xから根までで重さl以下の最大価値
    X = 1<<10
    maxL = max([l for v, l in querys])
    M = maxL + 1
    dp = [[-1]*M for _ in range(X)]

    for l in range(M):
        v, w = items[1]
        if l >= w:
            dp[1][l] = v
        else:
            dp[1][l] = 0

    for x in range(1, X):
        px = x // 2

        if x > N: break
        vx, wx = items[x]

        for l in range(M):
            dp[x][l] = max(dp[x][l], dp[px][l])

            if l >= wx:
                dp[x][l] = max(dp[x][l], dp[px][l-wx] + vx)

    for v, l in querys:
        if v < X:
            print(dp[v][l])
            continue

        VW = [(0, 0)]
        while v >= X:
            tmp = []
            vx, wx = items[v]
            for val, w in VW:
                if w+wx <= l:
                    tmp.append((val+vx, w+wx))
            VW += tmp
            v //= 2

        ans = 0
        for val, w in VW:
            ans = max(ans, dp[v][l-w] + w)
        print(ans)


if __name__ == "__main__":
    main()