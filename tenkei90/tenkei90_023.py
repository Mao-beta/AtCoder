import sys
from collections import defaultdict


sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def solve(H, W, C):
    # 左上から1マスずつ決めていく
    # 直前のW+1マスの状態を保持
    # dp[i][state]: i個のマスを見終わり、W+1マスの状態がstateのときの場合の数
    # →マスi(0-index)に置こうとしている

    def hw2i(h, w):
        return h * W + w

    def in_grid(h, w):
        return 0 <= h < H and 0 <= w < W

    DH = [-1, -1, -1,  0]
    DW = [-1,  0,  1, -1]
    DK = [W, W-1, W-2, 0]
    ZD = list(zip(DH, DW, DK))

    M = H * W
    dp = [defaultdict(int) for _ in range(M+1)]
    dp[0][0] = 1

    MASK = (1<<(W+1)) - 1


    for h in range(H):
        for w in range(W):
            i = hw2i(h, w)

            for state in dp[i].keys():
                if not dp[i][state]: continue

                can = True
                for dh, dw, dk in ZD:
                    nh, nw = h+dh, w+dw
                    if nh < 0 or H <= nh or nw < 0 or W <= nw:
                        continue
                    if (state>>dk) & 1:
                        can = False

                # 置かない
                ns = (state << 1) & MASK
                dp[i+1][ns] += dp[i][state]
                dp[i+1][ns] %= MOD

                # 置く
                if can and C[h][w] != "#":
                    ns = (state << 1) & MASK
                    ns |= 1
                    dp[i+1][ns] += dp[i][state]
                    dp[i+1][ns] %= MOD

    ans = 0
    #print(*dp.values(), sep="\n")
    for d in dp[M].values():
        ans += d
        ans %= MOD
    print(ans)


def main():
    H, W = NMI()
    C = [SI() for _ in range(H)]

    solve(H, W, C)


if __name__ == "__main__":
    main()
