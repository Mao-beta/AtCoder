import sys
import bisect
from itertools import accumulate

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def split_and_list(A):
    """
    半分全列挙
    :param A: 長さ40以下くらいのList
    :return: 前半と後半それぞれについて、各部分集合の和のList
    """

    def solve_half(A_half):
        n = len(A_half)
        res = []
        for case in range(1<<n):
            now = 0
            for i in range(n):
                if (case >> i) & 1:
                    now += A_half[i]
            res.append(now)
        res.sort()
        return res

    N = len(A)
    return solve_half(A[:N//2]), solve_half(A[N//2:])


def small_N_solve(N, W, Vs, Ws):
    # 半分全列挙
    N1 = N//2
    N2 = N - N1
    Vs1, Vs2 = Vs[:N//2], Vs[N//2:]
    Ws1, Ws2 = Ws[:N//2], Ws[N//2:]

    def get_sorted_WV(n, vs, ws):
        WV = []
        for case in range(1<<n):
            now_v = 0
            now_w = 0
            for i in range(n):
                if (case >> i) & 1:
                    now_v += vs[i]
                    now_w += ws[i]
            WV.append((now_w, now_v))
        WV.sort()
        W_total = [w for w, v in WV]
        V_total = [v for w, v in WV]
        V_total = list(accumulate(V_total, max))

        return W_total, V_total

    W1, V1 = get_sorted_WV(N1, Vs1, Ws1)
    W2, V2 = get_sorted_WV(N2, Vs2, Ws2)

    ans = 0
    for w, v in zip(W1, V1):
        rem_W = W - w
        if rem_W < 0:
            continue
        idx = bisect.bisect_right(W2, rem_W)
        ans = max(ans, v + V2[idx-1])

    print(ans)


def small_V_solve(N, W, Vs, Ws):
    # ありうる価値の値に対して合計重量の最小値をもつDP
    # O(N*sum(Vs)) <= 4*10^7
    V = sum(Vs)
    INF = 10**20
    dp = [[INF]*(V+1) for _ in range(N+1)]
    dp[0][0] = 0
    for i in range(1, N+1):
        for j in range(V+1):
            w = Ws[i-1]
            v = Vs[i-1]
            dp[i][j] = min(dp[i][j], dp[i-1][j])
            if j-v >= 0:
                dp[i][j] = min(dp[i][j], dp[i-1][j-v] + w)

    for i, w in enumerate(dp[N][::-1]):
        if w <= W:
            print(V-i)
            exit()


def small_W_solve(N, W, Vs, Ws):
    # ありうる重量の値に対して合計価値の最大値をもつDP
    # O(N*sum(Ws)) <= 4*10^7
    W = min(W, sum(Ws))
    dp = [[0]*(W+1) for _ in range(N+1)]
    for i in range(1, N+1):
        for j in range(W+1):
            w = Ws[i-1]
            v = Vs[i-1]
            dp[i][j] = max(dp[i][j], dp[i-1][j])
            if j-w >= 0:
                dp[i][j] = max(dp[i][j], dp[i-1][j-w] + v)

    print(max(dp[N]))


def main():
    N, W = NMI()
    Vs = []
    Ws = []
    for _ in range(N):
        v, w = NMI()
        Vs.append(v)
        Ws.append(w)

    if N <= 30:
        small_N_solve(N, W, Vs, Ws)
    elif max(Vs) <= 1000:
        small_V_solve(N, W, Vs, Ws)
    else:
        small_W_solve(N, W, Vs, Ws)


if __name__ == "__main__":
    main()
