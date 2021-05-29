import sys
import heapq

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def calc_path_len(S, T, path, Hs, Vs):
    res = 0
    h, w = S
    for dir in path:
        if dir == "U":
            res += Vs[h-1][w]
            h -= 1
        elif dir == "D":
            res += Vs[h][w]
            h += 1
        elif dir == "L":
            res += Hs[h][w-1]
            w -= 1
        elif dir == "R":
            res += Hs[h][w]
            w += 1
        else:
            print("invalid path")

    if (h, w) != T:
        print("goal is not T")

    return res


def first_choice(w_move, h_move, w_prior=True):
    path = []

    if w_prior:
        # 全力横移動
        if w_move > 0:
            path += ["R"] * abs(w_move)
        else:
            path += ["L"] * abs(w_move)
        # 全力縦移動
        if h_move > 0:
            path += ["D"] * abs(h_move)
        else:
            path += ["U"] * abs(h_move)
    else:
        # 全力縦移動
        if h_move > 0:
            path += ["D"] * abs(h_move)
        else:
            path += ["U"] * abs(h_move)
        # 全力横移動
        if w_move > 0:
            path += ["R"] * abs(w_move)
        else:
            path += ["L"] * abs(w_move)

    return path


def prior_vertical(S, T, w):
    # 指定のwまで移動し、そこを縦に突っ切る
    w_move = w - S[1]
    h_move = T[0] - S[0]
    path = first_choice(w_move, h_move, True)

    w_move = T[1] - w
    if w_move > 0:
        path += ["R"] * abs(w_move)
    else:
        path += ["L"] * abs(w_move)

    return path


def prior_horizontal(S, T, h):
    # 指定のhまで移動し、そこを横に突っ切る
    w_move = T[1] - S[1]
    h_move = h - S[0]
    path = first_choice(w_move, h_move, False)
    h_move = T[0] - h
    if h_move > 0:
        path += ["D"] * abs(h_move)
    else:
        path += ["U"] * abs(h_move)

    return path



def main():
    LOCAL_TEST = False

    if LOCAL_TEST:
        Hs = [NLI() for _ in range(30)]
        Vs = [NLI() for _ in range(29)]

    score = 0.0

    # 移動の期待値
    INF = 10**10
    EH = [INF] * 30
    EV = [INF] * 30

    good_h = [0] * 30
    good_w = [0] * 30

    for k in range(1000):
        # 入力
        if LOCAL_TEST:
            si, sj, ti, tj, a, e = SI().split()
            si, sj, ti, tj, a = map(int, [si, sj, ti, tj, a])
            e = float(e)
        else:
            si, sj, ti, tj = NMI()

        S = (si, sj)
        T = (ti, tj)


        # solve
        if LOCAL_TEST:
            print(S, T)

        if max(good_h[S[0]], good_h[T[0]], good_w[S[1]], good_w[T[1]]) < 5:
            FIRST_CHOICE = True
        else:
            FIRST_CHOICE = False

        if FIRST_CHOICE:
            w_move = T[1] - S[1]
            h_move = T[0] - S[0]
            ans = first_choice(w_move, h_move)

        else:
            max_case = max(good_h[S[0]], good_h[T[0]], good_w[S[1]], good_w[T[1]])
            if max_case == good_h[S[0]]:
                ans = prior_horizontal(S, T, S[0])
            elif max_case == good_h[T[0]]:
                ans = prior_horizontal(S, T, T[0])
            elif max_case == good_w[S[1]]:
                ans = prior_vertical(S, T, S[1])
            elif max_case == good_w[T[1]]:
                ans = prior_vertical(S, T, T[1])

        print("".join(ans))
        sys.stdout.flush()

        prev_res = 10**10
        # スコア計算処理
        if LOCAL_TEST:
            b = calc_path_len(S, T, ans, Hs, Vs)
            score = score * 0.998 + a / b
            prev_res = round(b * e)
            print(S, T, prev_res)

        else:
            prev_res = NI()

        mean_cost = prev_res / (abs(h_move) + abs(w_move))

        if FIRST_CHOICE and mean_cost < 5000:
            good_h[S[0]] += 1
            good_w[T[1]] += 1

        elif mean_cost < 5000:
            if max_case == good_h[S[0]]:
                good_h[S[0]] += 1
            elif max_case == good_h[T[0]]:
                good_h[T[0]] += 1
            elif max_case == good_w[S[1]]:
                good_w[S[1]] += 1
            elif max_case == good_w[T[1]]:
                good_w[T[1]] += 1


    if LOCAL_TEST:
        print(round(2312311 * score))

        print(sum(good_w))
        print(sum(good_h))


if __name__ == "__main__":
    main()
