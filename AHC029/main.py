import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product
from typing import List

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

IS_LOCAL = True
try:
    import seaborn
except:
    IS_LOCAL = False


from enum import Enum

class CardType(Enum):
    NORMAL = 0
    FULLPW = 1
    CANCEL = 2
    CHANGE = 3
    EXPAND = 4
    BLANKS = 9


class Card:
    def __init__(self, t: int, w: int, p: int):
        self.t = t
        self.type = CardType(t)
        self.w = w
        self.p = p

    def power(self, L):
        return Card(self.t, self.w * 2**L, self.p * 2**L)

    def __repr__(self):
        return f"Card(t={self.type}, w={self.w}, p={self.p})"

    @staticmethod
    def blank():
        return Card(9, 0, 0)

    def is_blank(self):
        return self.type == CardType.BLANKS


class Project:
    def __init__(self, h: int, v: int):
        self.h = h
        self.v = v

    def power(self, L):
        return Project(self.h * 2**L, self.v * 2**L)

    def work(self, w):
        self.h -= w
        if self.is_done():
            return self.v
        else:
            return 0

    def cancel(self):
        self.h = -1
        self.w = -1

    @staticmethod
    def blank():
        return Project(-1, -1)

    def is_blank(self):
        return self.v < 0

    def is_done(self):
        return self.h <= 0 and self.v > 0

    def is_changeable(self):
        return self.is_blank() or self.is_done()

    def __repr__(self):
        return f"Project(h={self.h}, v={self.v})"


class Input:
    def __init__(self):
        if IS_LOCAL:
            self.N, self.M, self.K, self.T = NMI()

            self.projects = []
            for _ in range(self.M + self.T * self.M):
                h, v = NMI()
                self.projects.append(Project(h, v))

            self.cards = []
            for _ in range(self.N):
                t, w = NMI()
                self.cards.append(Card(t, w, 0))
            for _ in range(self.T * self.K):
                t, w, p = NMI()
                self.cards.append(Card(t, w, p))

        else:
            self.N, self.M, self.K, self.T = NMI()

            self.cards = []
            for _ in range(self.N):
                t, w = NMI()
                self.cards.append(Card(t, w, 0))

            self.projects = []
            for _ in range(self.M):
                h, v = NMI()
                self.projects.append(Project(h, v))


class SaveData:
    def __init__(self, projects, project_idx, hands, money, L, turn):
        self.projects = projects
        self.project_idx = project_idx
        self.hands = hands
        self.money = money
        self.L = L
        self.turn = turn


class DebugStrategy:
    def __init__(self):
        pass

    def decide_use(self):
        c, m = NMI()
        return c, m

    def decide_choose(self):
        r = NI()
        return r


class AllZeroStrategy:
    def __init__(self):
        pass

    def decide_use(self, projects: List[Project], hands: List[Card]):
        return 0, 0

    def decide_choose(self, choices: List[Card], money: int, turn: int):
        return 0


class Strategy:
    def __init__(self):
        pass

    def decide_use(self, projects: List[Project], hands: List[Card]):
        """
        EXPANDがあれば使う
        FULLPWがあれば使う
        コスパの良いProjectを選ぶ
        NORMALは最も無駄にしないように使う
        :return: c, m
        """
        for c, card in enumerate(hands):
            if card.type == CardType.EXPAND:
                return c, 0

        for c, card in enumerate(hands):
            if card.type == CardType.FULLPW:
                return c, 0

        m = 0
        vperh = 0
        for mi, project in enumerate(projects):
            if project.v / project.h > vperh:
                m = mi
                vperh = project.v / project.h

        project = projects[m]
        c = 0
        w = 0
        for ci, card in enumerate(hands):
            if card.type == CardType.NORMAL:
                if card.w > project.h * 1.2:
                    continue
                if card.w > w:
                    c = ci
                    w = card.w

        card = hands[c]
        if card.type in [CardType.FULLPW, CardType.EXPAND, CardType.CHANGE]:
            m = 0
        return c, m

    def decide_choose(self, choices: List[Card], money: int, turn: int):
        """
        turn < 900で、
            EXPANDを買えるなら買う
        NORMALとFULLPWはコスパ1倍以上のものを買う
        両方あればFULLPW優先気味で買う
        何もなければr=0でお茶を濁す
        """
        if turn < 900:
            for r, card in enumerate(choices):
                if card.type == CardType.EXPAND and money >= card.p:
                    return r

        for r, card in enumerate(choices):
            if card.type == CardType.FULLPW and money >= card.p and card.w >= card.p * 0.9:
                return r

        for r, card in enumerate(choices):
            if card.type == CardType.NORMAL and money >= card.p and card.w >= card.p * 0.9:
                return r

        r = 0
        return r



import random
from random import randint, uniform, gauss

class Judge:
    def __init__(self, inputs: Input):
        self.inputs = inputs
        self.projects = [self.inputs.projects[i] for i in range(inputs.M)]
        self.project_idx = inputs.M
        self.hands = [self.inputs.cards[i] for i in range(inputs.N)]
        self.money = 0
        self.L = 0

        self.savedata = SaveData(self.projects, self.project_idx, self.hands, self.money, self.L, turn=0)

    def use_card(self, c, m):
        print(c, m, flush=True)

        if IS_LOCAL:
            card = self.hands[c]
            self.hands[c] = Card.blank()
            # カード効果を適用
            if card.type == CardType.NORMAL:
                self.money += self.projects[m].work(card.w)

            elif card.type == CardType.FULLPW:
                for m in range(self.inputs.M):
                    self.money += self.projects[m].work(card.w)

            elif card.type == CardType.CANCEL:
                self.projects[m].cancel()

            elif card.type == CardType.CHANGE:
                for m in range(self.inputs.M):
                    self.projects[m].cancel()

            elif card.type == CardType.EXPAND:
                self.L += 1
            else:
                raise ValueError

            self.fill_all_projects()

    def get_projects_info(self):
        if IS_LOCAL:
            return self.projects
        else:
            res = []
            for _ in range(self.inputs.M):
                h, v = NMI()
                res.append(Project(h, v))
            self.projects = res[:]
            return self.projects

    def get_money(self):
        if IS_LOCAL:
            return self.money
        else:
            self.money = NI()
            return self.money


    def get_cards_info(self, turn):
        if IS_LOCAL:
            l = self.inputs.N + turn * self.inputs.K
            r = l + self.inputs.K
            return [card.power(self.L) for card in self.inputs.cards[l:r]]
        else:
            return [Card(*NMI()) for _ in range(self.inputs.K)]

    def choose_card(self, r):
        print(r, flush=True)

    def fill_card(self, c: int, card: Card):
        self.hands[c] = card
        self.money -= card.p

    def fill_all_projects(self):
        for m in range(self.inputs.M):
            if self.projects[m].is_changeable():
                self.projects[m] = self.inputs.projects[self.project_idx].power(self.L)
                self.project_idx += 1

    def save(self, turn):
        self.savedata = SaveData(self.projects, self.project_idx, self.hands, self.money, self.L, turn=turn)

    def load(self):
        self.projects = self.savedata.projects
        self.project_idx = self.savedata.project_idx
        self.hands = self.savedata.hands
        self.money = self.savedata.money
        self.L = self.savedata.L
        return self.savedata.turn


class Generators:
    def __init__(self, inputs: Input):
        self.inputs = inputs

    def clamp(self, n, smallest, largest):
        return max(smallest, min(n, largest))

    def generate_project(self, L) -> Project:
        b = uniform(2.0, 8.0)
        h = round(pow(2, b)) * 2**L
        v = round(pow(2, self.clamp(gauss(b, 0.5), 0.0, 10.0))) * 2**L
        return Project(h, v)

    def generate_policy_card(self, X: List[int], L: int) -> Card:
        """
        Generate a policy card based on the given parameters.

        :param x: List of probabilities for card types [x0, x1, x2, x3, x4]
        :param L: The number of times capital increase cards have been used (0 <= L <= 20)
        :return: Tuple of (card type, labor force, cost)
        """
        # Choose card type based on weighted probability
        t = random.choices(range(5), weights=X, k=1)[0]

        # Initialize labor force and cost
        w = 0
        p = 0

        # Calculate labor force and cost based on card type
        if t == 0 or t == 1:
            w = random.randint(1, 50) * (2 ** L)
            w_prime = w / (2 ** L)
            if t == 0:
                p = self.clamp(round(random.gauss(w_prime, w_prime / 3)), 1, 10000) * (2 ** L)
            else:
                p = self.clamp(round(random.gauss(w_prime * self.inputs.M, w_prime * self.inputs.M / 3)), 1, 10000) * (2 ** L)
        elif t == 2 or t == 3:
            p = random.randint(0, 10) * (2 ** L)
        elif t == 4:
            p = random.randint(200, 1000) * (2 ** L)

        return Card(t, w, p)



class Game:
    def __init__(self, inputs: Input):
        self.turn = 0
        self.inputs = inputs
        self.judge = Judge(inputs)
        # self.strategy = AllZeroStrategy()
        self.strategy = Strategy()

    def run(self):
        for turn in range(self.inputs.T):
            self.proceed(turn)

    def proceed(self, turn):
        # 各ターン
        print(f"# TURN {turn}")
        print(f"# CARDS {self.judge.hands}")
        print(f"# PROJECTS {self.judge.projects}")

        # 使用カード出力 >>c m 何番目か、プロジェクト番号
        c, m = self.strategy.decide_use(self.judge.projects, self.judge.hands)
        self.judge.use_card(c, m)

        # カード使用後のProject状況を受け取る
        projects = self.judge.get_projects_info()
        print(f"# PROJECTS {projects}")

        money = self.judge.get_money()
        print(f"# MONEY {money}")

        choices = self.judge.get_cards_info(turn)
        print(f"# CHOOSE {choices}")

        # 何番目を手札に加えるか選択
        r = self.strategy.decide_choose(choices, money, turn)
        self.judge.choose_card(r)
        self.judge.fill_card(c, choices[r])


def main():
    # 入力
    inputs = Input()

    game = Game(inputs)
    game.run()


if __name__ == "__main__":
    main()
