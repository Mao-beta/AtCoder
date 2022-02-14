import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations
from pathlib import Path
import random
from enum import Enum

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


try:
    import numpy
    IS_LOCAL = True
except:
    IS_LOCAL = False


# 方向差分定義
DXY = {"U": (-1, 0), "D": (1, 0), "R": (0, 1), "L": (0, -1)}

def newXY(x, y, d):
    dx, dy = DXY[d]
    nx, ny = x + dx, y + dy
    return nx, ny


# 駒の種類定義
class AgentType(Enum):
    COW = 1
    PIG = 2
    RABBIT = 3
    DOG = 4
    CAT = 5
    HUMAN = 6


# 駒の定義
class Agent:
    def __init__(self, x:int, y:int, species: AgentType, ID:int):
        self.x = x
        self.y = y
        self.spec = species
        self.ID = ID

    def move(self, d:str):
        assert d in "URDL"
        assert len(d) == 1
        self.x, self.y = newXY(self.x, self.y, d)

    def __hash__(self):
        return self.spec.value * 100 + self.ID

    def __repr__(self):
        return f"#x: {self.x}\ty: {self.y}\ttype: {self.spec.name}"


# ボードの状態
class Board:
    def __init__(self, X=30, Y=30):
        # Boardの縦横
        self.X = X
        self.Y = Y
        # ある座標にいるAgentの情報
        self.agents = [[set() for _ in range(Y)] for _ in range(X)]
        # ある座標が通行止めかどうか
        self.blocked = [[0]*Y for _ in range(X)]

    # 状態判定系
    def is_valid_xy(self, x, y):
        return 0 <= x < self.X and 0 <= y < self.Y

    def is_blocked(self, x, y):
        return self.blocked[x][y]

    def is_agent(self, x, y):
        return len(self.agents[x][y]) > 0

    def is_available(self, x, y):
        return self.is_valid_xy(x, y) and not self.is_blocked(x, y)

    def count_agents(self):
        res = 0
        for x in range(self.X):
            for y in range(self.Y):
                res += len(self.agents[x][y])
        return res

    def count_human(self, x, y):
        res = 0
        for agent in self.agents[x][y]:
            if agent.spec == AgentType.HUMAN:
                res += 1
        return res

    # 動作判定系
    def is_blockable(self, agent: Agent, d):
        d = d.upper()
        x, y = agent.x, agent.y
        tx, ty = newXY(x, y, d)

        if self.is_agent(tx, ty) or self.is_blocked(tx, ty):
            return False

        res = True
        for nd in "URLD":
            nx, ny = newXY(tx, ty, nd)
            if not self.is_valid_xy(nx, ny) or not self.is_agent(nx, ny):
                continue
            for agent in self.agents[nx][ny]:
                print(f"# {agent}")
                if agent.spec != AgentType.HUMAN:
                    res = False
                    break

            if not res: break

        return res

    def is_movable(self, agent: Agent, d):
        nx, ny = newXY(agent.x, agent.y, d)
        return self.is_available(nx, ny)

    # move関連
    def set_agent(self, agent: Agent):
        self.agents[agent.x][agent.y].add(agent)

    def delete_agent(self, agent: Agent):
        self.agents[agent.x][agent.y].discard(agent)

    def move_agent(self, agent:Agent, d):
        if self.is_movable(agent, d):
            self.delete_agent(agent)
            agent.move(d)
            self.set_agent(agent)
            return True
        else:
            return False

    # block関連
    def block(self, agent: Agent, d):
        assert self.is_blockable(agent, d)
        nx, ny = newXY(agent.x, agent.y, d)
        self.blocked[nx][ny] = 1

    # デバッグ用
    def __repr__(self):
        res = ["### BOARD"]
        res += ["# " + " ".join(map(str, row)) for row in self.blocked]
        return "\n".join(res)


# システム全体
class Game:
    def __init__(self, N, M, P, H, X=30, Y=30):
        self.N = N
        self.M = M
        self.board = Board(X, Y)
        self.pets = [Agent(x-1, y-1, ID=100+i, species=AgentType(t)) for i, (x, y, t) in enumerate(P)]
        self.humans = [Agent(x-1, y-1, ID=i, species=AgentType.HUMAN) for i, (x, y) in enumerate(H)]

        for pet in self.pets:
            self.board.set_agent(pet)

        for human in self.humans:
            self.board.set_agent(human)

        assert self.board.count_agents() == N + M


    def move(self, agent: Agent, d: str):
        if self.board.is_movable(agent, d):
            self.board.move_agent(agent, d)
            return True
        else:
            return False

    def block(self, agent: Agent, d: str):
        d = d.upper()
        if self.board.is_blockable(agent, d):
            self.board.block(agent, d)
            return True
        else:
            return False


    def conduct_human(self, querys: str):
        for human, d in zip(self.humans, querys):
            if d == ".": continue
            elif d.islower():
                self.block(human, d)
            else:
                self.move(human, d)
        print(querys)
        sys.stdout.flush()


    def conduct_pets(self):
        querys = SLI()
        for pet, query in zip(self.pets, querys):
            for d in query:
                self.move(pet, d)

    def conduct(self, querys):
        self.conduct_human(querys)
        self.conduct_pets()


def solve(values, out_path=None):
    N, P, M, H = values

    T = 300
    game = Game(N, M, P, H)
    print(*game.pets, sep="\n")

    for turn in range(T):
        if MOVED is None:
            querys = strategy(game, 15, 1, "R")
        else:
            if MOVED == "d":
                querys = strategy2(game, 13, 15, "U", 0, 15)
            else:
                querys = strategy2(game, 17, 15, "D", 16, 30)
        game.conduct(querys)
        # print(*game.pets, sep="\n")


PHASE = 0
MOVED = None
PHASE2 = 0

def strategy(game, sx, sy, sd):
    if sd == "R":
        rd = "L"
        side = "UD"
    elif sd == "D":
        rd = "U"
        side = "LR"

    global PHASE
    querys = ["."] * game.M

    if PHASE == 0 and game.board.count_human(sx, sy) == game.M - 1:
        PHASE = 1
        print("# PHASE 1")
        sys.stdout.flush()

    if PHASE == 0:
        # (sx, sy)を目指す
        for human in game.humans:
            if human.ID == game.M - 1:
                if human.x < 15 and human.y < 15:
                    sx = 0
                    sy = 0
                elif human.x >= 15 and human.y < 15:
                    sx = 29
                    sy = 0
                elif human.x < 15 and human.y >= 15:
                    sx = 0
                    sy = 29
                else:
                    sx = 29
                    sy = 29

            if human.x > sx:
                querys[human.ID] = "U"
            elif human.x < sx:
                querys[human.ID] = "D"
            elif human.y > sy:
                querys[human.ID] = "L"
            elif human.y < sy:
                querys[human.ID] = "R"

    elif PHASE == 1:
        human = game.humans[0]
        print(f"# now x: {human.x}, y: {human.y}")
        sys.stdout.flush()
        # 左が移動可能でなく右が移動可能なら移動
        if not game.board.is_movable(human, rd):
            if game.board.is_movable(human, sd):
                querys = [sd] * game.M
                querys[-1] = "."
            else:
                # 右端についた
                print("# PHASE 2")
                sys.stdout.flush()
                PHASE = 2

        # 左が移動可能だがBlockできなければ待機
        elif not game.board.is_blockable(human, rd):
            pass

        # そうでなければ左をBlock
        else:
            querys[0] = rd.lower()


    elif PHASE == 2:
        upper = 0
        for x in range(15):
            for y in range(30):
                upper += len(game.board.agents[x][y])
        lower = game.N - upper

        if upper <= lower:
            querys = ["U"] * game.M
        else:
            querys = ["D"] * game.M

        querys[-1] = "."

        print("# PHASE 3")
        sys.stdout.flush()
        PHASE = 3

    elif PHASE == 3:
        human = game.humans[0]
        if human.x < 15:
            D = "d"
        else:
            D = "u"

        if game.board.is_blockable(human, D):
            querys[0] = D
            global MOVED
            MOVED = D

    return "".join(querys)


def strategy2(game, sx, sy, sd, mx, Mx):
    if sd == "R":
        rd = "L"
        side = "UD"
    elif sd == "U":
        rd = "D"
        side = "LR"
    elif sd == "D":
        rd = "U"

    global PHASE2
    querys = ["."] * game.M

    if PHASE2 == 0 and game.board.count_human(sx, sy) == game.M - 1:
        PHASE2 = 1
        print("# PHASE2 1")
        sys.stdout.flush()

    if PHASE2 == 0:
        # (sx, sy)を目指す
        for human in game.humans:
            if human.x > sx:
                querys[human.ID] = "U"
            elif human.x < sx:
                querys[human.ID] = "D"
            elif human.y > sy:
                querys[human.ID] = "L"
            elif human.y < sy:
                querys[human.ID] = "R"

    elif PHASE2 == 1:
        human = game.humans[0]
        print(f"# now x: {human.x}, y: {human.y}")
        sys.stdout.flush()
        # 左が移動可能でなく右が移動可能なら移動
        if not game.board.is_movable(human, rd):
            if game.board.is_movable(human, sd):
                querys = [sd] * game.M
            else:
                # 右端についた
                print("# PHASE 2")
                sys.stdout.flush()
                PHASE2 = 2

        # 左が移動可能だがBlockできなければ待機
        elif not game.board.is_blockable(human, rd):
            pass

        # そうでなければ左をBlock
        else:
            querys[0] = rd.lower()


    elif PHASE2 == 2:
        upper = 0
        lower = 0
        for x in range(mx, Mx):
            for y in range(30):
                if y < 15:
                    upper += len(game.board.agents[x][y]) - game.board.count_human(x, y)
                else:
                    lower += len(game.board.agents[x][y]) - game.board.count_human(x, y)

        print(f"# left: {upper}, right: {lower}")

        if upper <= lower:
            querys = ["L"] * game.M
        else:
            querys = ["R"] * game.M

        print("# PHASE 3")
        sys.stdout.flush()
        PHASE2 = 3

    elif PHASE2 == 3:
        human = game.humans[0]
        if human.y < 15:
            D = "r"
        else:
            D = "l"

        if game.board.is_blockable(human, D):
            querys[0] = D

    querys[-1] = "."
    return "".join(querys)


def output_ans(ans, path=None):
    if path:
        with open(path, "w") as f:
            for row in ans:
                f.write(str(row) + "\n")
    else:
        for row in ans:
            pass
            #print(*row, sep="")


def input_values(path=None):
    if path:
        P = []
        H = []
        with open(path, mode="r") as f:
            inputs = f.readlines()
            # 0
            N = int(inputs[0])
            # 1-N
            for i in range(N):
                x, y, t = map(int, inputs[1+i].split())
                P.append([x, y, t])
            # N+1
            M = int(inputs[N+1])
            # N+2 - N+M+1
            for i in range(M):
                x, y = map(int, inputs[N+2+i].split())
                H.append([x, y])

    else:
        N = NI()
        P = [NLI() for _ in range(N)]
        M = NI()
        H = [NLI() for _ in range(M)]

    return N, P, M, H


def main(file=None):
    in_path = None
    out_path = None

    if file:
        in_filename = file + ".in"
        in_path = Path("./in/") / in_filename
        out_filename = file + ".out"
        out_path = Path("./out/") / out_filename
        Path("./out/").mkdir(exist_ok=True)

    values = input_values(in_path)
    solve(values, out_path)
    exit()


if __name__ == "__main__":
    IS_LOCAL = False
    if IS_LOCAL:
        for i in range(0, 1):
            random.seed(i)
            main(str(i).zfill(3))
    else:
        main()


if __name__ == "__main__":
    main()
