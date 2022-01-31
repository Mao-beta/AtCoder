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


def cum_2D(A):
    """
    2次元リストAの累積和
    """
    H = len(A)
    W = len(A[0])
    C = [[0]*W for _ in range(H)]

    for h in range(H):
        cw = 0
        for w in range(W):
            if h == 0 and w == 0:
                C[h][w] = A[h][w]
            elif h == 0:
                C[h][w] = A[h][w] + C[h][w-1]
            elif w == 0:
                C[h][w] = A[h][w] + C[h-1][w]
            else:
                cw += A[h][w]
                C[h][w] = C[h-1][w] + cw

    return C


def area_sum(cum, hl, hr, wl, wr):
    """
    2次元累積和の行列cum（左と上は0）から、元の行列の[hl:hr, wl:wr]の範囲で和をとる
    """
    return cum[hr][wr] - cum[hl][wr] - cum[hr][wl] + cum[hl][wl]


def main():
    H, W = NMI()
    A = [NLI() for _ in range(H)]
    SH = [sum(L) for L in A]

    cum = cum_2D([[0]*(W+1)] + [[0]+row for row in A])
    ans = 0
    CSH = list(accumulate(SH))
    for i, c in enumerate(CSH):
        H_idx = []
        H_idx.append(list(range(i+1)))

        now_idx = i+1
        now = 0
        now_H = []
        is_ok = True

        while now_idx < H:
            if now + SH[now_idx] <= c:
                now += SH[now_idx]
                now_H.append(now_idx)
            else:
                is_ok = False
                break

            if now == c:
                H_idx.append(now_H)
                now_H = []
                now = 0

            now_idx += 1

        if now > 0 or not is_ok:
            continue

        # print("H", H_idx)

        for wr0 in range(1, W+1):
            g = area_sum(cum, H_idx[0][0], H_idx[0][-1]+1, 0, wr0)
            # print(g)
            WW = []
            ans_flag = True
            for j, Hs in enumerate(H_idx):
                wl = wr0
                hl, hr = H_idx[j][0], H_idx[j][-1]+1
                wr = wl+1
                Ws = [[0, wr0]]
                is_ok = True
                while wr <= W:
                    area = area_sum(cum, hl, hr, wl, wr)
                    if area < g:
                        wr += 1
                        is_ok = False
                        continue
                    elif area == g:
                        Ws.append([wl, wr])
                        wl = wr
                        wr = wl+1
                        is_ok = True
                        continue
                    else:
                        is_ok = False
                        break

                if not is_ok:
                    continue

                # print("W", Ws)
                if j == 0:
                    WW = Ws
                elif WW != Ws:
                    ans_flag = False
                    break
                else:
                    # print(WW, Ws)
                    continue

            if ans_flag:
                # print(wr0, Ws, ans)
                if Ws[-1][-1] == W:
                    ans += 1

    print(ans-1)



if __name__ == "__main__":
    main()
