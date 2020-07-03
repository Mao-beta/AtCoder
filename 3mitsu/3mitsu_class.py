import sys
import math
from collections import deque
#from components import Player, Card


class Player:
    def __init__(self, max_round, p_id, name):
        self.p_id = p_id
        self.name = name
        self.card_his = [99] * (max_round + 1)
        self.infection_his = [False] * (max_round + 1)
        self.score_his = [0] * (max_round + 1)


class WorkCard:
    def __init__(self, data):
        self.c_id = data["c_id"]
        self.name = data["name"]
        self.condense = data["condense"]
        self.turn = data["turn"]

    def get_id(self):
        return self.c_id

    def get_name(self):
        return self.name

    def get_condense(self):
        return self.condense

    def get_turn(self):
        return self.turn


class Gameboard:

    def __init__(self, max_round, total_player_num, player_data, card_data):
        self.now_round = 1
        self.max_round = max_round
        self.total_player_num = total_player_num
        self.Players = [Player(max_round=max_round, p_id=i, name=player_data[i]) for i in range(total_player_num)]
        self.field = [9]*(self.max_round + 1)
        self.card_data = card_data

    # 各フェイズ処理
    def working_phase(self, Cards):
        rnd = self.now_round

        # カード使用履歴更新
        self.update_card_his(Cards)
        # 場の密度を更新
        self.update_field(Cards)
        # 感染状況を更新
        self.update_infection_his(rnd, Cards)
        # 点数を更新
        self.update_scores(rnd, Cards)

    # update系統
    def update_card_his(self, Cards):
        for p_id, card in enumerate(Cards):
            self.use_workcard(p_id, card)

    def update_field(self, Cards):
        rnd = self.get_round()
        self.field[rnd] = 0
        for p_id, card in enumerate(Cards):
            self.field[rnd] += card.get_condense()

    def update_infection_his(self, rnd, Cards):
        # 三密時の処理
        if self.get_field(rnd) >= 3:
            for p_id, card in enumerate(Cards):
                # 職場に来てたら次ラウンド感染 最終ラウンドは無視
                if card.get_id() in [1, 2] and not self.is_final_round():
                    self.set_infection(p_id, rnd + 1)

        # pandemic時
        if self.is_pandemic(rnd):
            for p_id, card in enumerate(Cards):
                # 職場に来てたら次ラウンド感染 最終ラウンドは無視
                if card.get_id() in [1, 2] and not self.is_final_round():
                    self.set_infection(p_id, rnd + 1)

        # 感染してた人は次ラウンドで戻る
        for p_id in range(self.total_player_num):
            if self.is_infected(p_id, rnd) and not self.is_final_round():
                self.solve_infection(p_id, rnd + 1)

    def update_scores(self, rnd, Cards):
        for p_id, card in enumerate(Cards):
            self.set_score(p_id, rnd, self.get_score_his(p_id, rnd-1))
            if self.is_infected(p_id, rnd):
                self.add_score(p_id, rnd, card.get_turn() * (-1))
            else:
                self.add_score(p_id, rnd, card.get_turn())

    # get系統
    def get_field(self, rnd=-1):
        if rnd != -1:
            return self.field[rnd]
        else:
            return self.field

    def get_round(self):
        return self.now_round

    def get_card_his(self, p_id, rnd=-1):
        if rnd != -1:
            return self.Players[p_id].card_his[rnd]
        else:
            return self.Players[p_id].card_his

    def get_infection_his(self, p_id, rnd=-1):
        if rnd != -1:
            return self.Players[p_id].infection_his[rnd]
        else:
            return self.Players[p_id].infection_his

    def get_score_his(self, p_id, rnd=-1):
        if rnd != -1:
            return self.Players[p_id].score_his[rnd]
        else:
            return self.Players[p_id].score_his

    # 処理系統
    def use_workcard(self, p_id, card):
        self.Players[p_id].card_his[self.now_round] = card.get_id()

    def add_round(self):
        self.now_round += 1

    def set_infection(self, p_id, rnd):
        if not self.is_infected(p_id, rnd):
            self.Players[p_id].infection_his[rnd] = True

    def solve_infection(self, p_id, rnd):
        if self.is_infected(p_id, rnd):
            self.Players[p_id].infection_his[rnd] = False

    def set_score(self, p_id, rnd, score):
        self.Players[p_id].score_his[rnd] = score

    def add_score(self, p_id, rnd, turn):
        self.Players[p_id].score_his[rnd] += turn

    def set_round(self, rnd):
        self.now_round = rnd

    # 出力系統
    def output_all_card_his(self):
        for p_id in range(self.total_player_num):
            res = [self.card_data[h]["name"] for h in self.get_card_his(p_id)]
            print(res[1:])

    def output_all_infection_his(self):
        for p_id in range(self.total_player_num):
            print(self.get_infection_his(p_id)[1:])

    def output_all_score_his(self):
        for p_id in range(self.total_player_num):
            print(self.get_score_his(p_id)[1:])

    def debug_output(self):
        self.output_all_card_his()
        print(self.get_field()[1:])
        self.output_all_infection_his()
        self.output_all_score_his()
        print()

    # 判定系統
    def is_gameover(self):
        return self.now_round > self.max_round

    def is_final_round(self):
        return self.get_round() == self.max_round

    def is_infected(self, p_id, rnd):
        return self.get_infection_his(p_id, rnd)

    def is_pandemic(self, rnd):
        # 感染者が来てる
        flag = False
        Mitsu_cards = [1, 2]
        for p_id in range(self.total_player_num):
            infected_flag = self.get_infection_his(p_id, rnd)
            working_flag = self.get_card_his(p_id, rnd) in Mitsu_cards
            flag |= infected_flag and working_flag
        return flag


# 入力受付
def command_card(Game):
    total_player_num = Game.total_player_num
    user_input = input("'X X X'の形でカード入力してください: ")
    try:
        res = list(map(int, user_input.split()))
    except:
        print("Error: 'X X X'の形で入力してください")
        return command_card(Game)

    if len(res) == 1 and int(res[0]) < 0:
        return res[0]
    elif len(res) != total_player_num:
        print("Error: 人数は{0}人です".format(total_player_num))
        return command_card(Game)
    elif min(res) < 0 or max(res) > 2:
        print("Error: 入力は0から2までです")
        return command_card(Game)
    else:
        print(res)
        return res


def main():
    # 初期化
    # 定数宣言
    TOTAL_PLAYER_NUM = 3
    MAX_ROUND = 9
    player_data = ["A", "B", "C"]
    # コンポーネント初期化
    card_data = {0: {"c_id": 0, "name": "NO密", "condense": 0, "turn": 0},
                 1: {"c_id": 1, "name": " 密 ", "condense": 1, "turn": 1},
                 2: {"c_id": 2, "name": "濃密", "condense": 2, "turn": 2},
                 99: {"c_id": 99, "name": "    "}} # 無のカード
    Mitsu = [WorkCard(card_data[0]),
             WorkCard(card_data[1]),
             WorkCard(card_data[2])]

    Game = Gameboard(max_round=MAX_ROUND,
                     total_player_num=TOTAL_PLAYER_NUM,
                     player_data=player_data,
                     card_data=card_data)
    # 終了フラグ
    end_flag = False


    # mainloop
    while end_flag == False:
        # 使用するカード入力
        cards_inputs = command_card(Game)

        # -nが入力されたらnラウンド戻す
        if type(cards_inputs) is int:
            print("負の単一数が入力されました、ラウンドを戻します")
            next_round = Game.get_round() + cards_inputs
            if 1 <= next_round <= MAX_ROUND:
                Game.set_round(next_round)
                print("次はラウンド{0}".format(next_round))
            else:
                print("行き先のラウンドは範囲外です")
                print("次はラウンド{0}".format(Game.get_round()))
            continue

        cards = [Mitsu[x] for x in cards_inputs]
        # 仕事フェイズ
        Game.working_phase(cards)
        print("ラウンド：" + str(Game.get_round()))

        # debug用出力処理
        Game.debug_output()

        # ラウンド進行処理
        Game.add_round()
        # ラウンドが一定数超えたら終了
        if Game.is_gameover():
            end_flag = True


if __name__ == "__main__":
    main()