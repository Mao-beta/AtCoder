import sys

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def cum_2D(A):
    """
    2次元リストAの累積和
    """
    H = len(A)
    W = len(A[0])
    for h in range(H):
        for w in range(W-1):
            A[h][w+1] += A[h][w]
    for w in range(W):
        for h in range(H-1):
            A[h+1][w] += A[h][w]

    return A


def area_sum(cum, hl, hr, wl, wr):
    """
    2次元累積和の行列cum（左と上は0）から、元の行列の[hl:hr, wl:wr]の範囲で和をとる
    """
    return cum[hr][wr] - cum[hl][wr] - cum[hr][wl] + cum[hl][wl]



def main():
    # 中央値がx以下である→上から K**2//2+1 番目の値がx以下
    # →xより大きい値が K**2//2 個以下

    N, K = NMI()
    grid = [NLI() for _ in range(N)]


    def judge(x):
        G = []
        G.append([0]*(N+1))
        for row in grid:
            G.append([0]+[1 if a > x else 0 for a in row])

        cum = cum_2D(G)
        for h in range(N-K+1):
            for w in range(N-K+1):
                cnt = area_sum(cum, h, h+K, w, w+K)
                if cnt <= K**2//2:
                    return True

        return False


    ok = 10**9
    ng = -1
    for _ in range(30):
        mid = (ok+ng) // 2
        if judge(mid):
            ok = mid
        else:
            ng = mid

    print(ok)


if __name__ == "__main__":
    main()
