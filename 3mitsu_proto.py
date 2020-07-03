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


def make_grid(h, w, num): return [[int(num)] * w for _ in range(h)]


def main():
    total_round = 9
    span = 3
    player_num = 3
    card_his = make_grid(player_num, total_round+2, -1)
    infection_his = [[False] * (total_round+2) for _ in range(player_num)]
    score_his = make_grid(player_num, total_round+2, 0)

    for rnd in range(1, total_round+1):
        sanmitsu_flag = False
        pandemic_flag = False
        cards = NLI()

        for i, h in enumerate(cards):
            card_his[i][rnd] = h

        # 場が三密であるフラグ
        if sum(cards) >= 3:
            sanmitsu_flag = True
        # 職場に感染者が来てるフラグ
        for i in range(player_num):
            if cards[i] > 0 and infection_his[i][rnd]:
                pandemic_flag = True

        # 次回感染する
        for i, h in enumerate(cards):
            if sanmitsu_flag or pandemic_flag:
                if h > 0 and not infection_his[i][rnd]:
                    infection_his[i][rnd+1] = True

        # 点数計算
        for i, h in enumerate(cards):
            f = -1 if infection_his[i][rnd] else 1
            score_his[i][rnd] = score_his[i][rnd-1] + card_his[i][rnd] * f

        # roundごとの出力
        output(player_num, rnd, card_his, infection_his, score_his)





def output(player_num, rnd, card_his, infection_his, score_his):
    print("今回のラウンド：", rnd)
    print("今回出した手：　", end="")
    for i in range(player_num):
        print(card_his[i][rnd], end=" ")
    print()
    print("今回の感染状態：", end="")
    for i in range(player_num):
        print(infection_his[i][rnd], end=" ")
    print()
    print("次回の感染状態：", end="")
    for i in range(player_num):
        print(infection_his[i][rnd + 1], end=" ")
    print()
    print("現在の回転数：　", end="")
    for i in range(player_num):
        print(score_his[i][rnd], end=" ")
    print()


if __name__ == "__main__":
    main()