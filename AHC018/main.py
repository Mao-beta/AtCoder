import sys
from enum import Enum
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations
from typing import List, Tuple
from pathlib import Path

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


IS_LOCAL = False
try:
    import matplotlib.pyplot as plt
    IS_LOCAL = True
except:
    pass


class Pos:
    def __init__(self, y: int, x: int):
        self.y = y
        self.x = x

    def __str__(self):
        return f"y: {self.y}, x: {self.x}"


class Response(Enum):
    NOT_BROKEN = 0
    BROKEN = 1
    FINISH = 2
    INVALID = -1


class Field:
    def __init__(self, N: int, C: int, S=None):
        self.C = C
        self.is_broken = [[False] * N for _ in range(N)]
        self.total_cost = 0
        self.S = S

    def judge(self, y: int, x: int, power: int):
        if self.S[y][x] > power:
            self.S[y][x] -= power
            return 0
        else:
            self.S[y][x] = 0
            return 1

    def query(self, y: int, x: int, power: int) -> Tuple[Response, List]:
        self.total_cost += power + self.C
        print(f"{y} {x} {power}", flush=True)
        q = [y, x, power]

        if IS_LOCAL:
            res = Response(self.judge(y, x, power))
        else:
            res = Response(int(input()))

        if res in (Response.BROKEN, Response.FINISH):
            self.is_broken[y][x] = True
        return res, q


class Ans:
    def __init__(self):
        self.ans = []

    def append(self, ans_q):
        self.ans.append(ans_q)

    def output(self, dst_path=None):
        if dst_path is None:
            return

        with open(dst_path, mode="w") as f:
            for y, x, p in self.ans:
                f.write(f"{y} {x} {p}\n")


class Solver:
    def __init__(self, N: int, source_pos: List[Pos], house_pos: List[Pos], C: int, S=None, dst_path=None):
        self.N = N
        self.source_pos = source_pos
        self.house_pos = house_pos
        self.house_connected = {(yx.y, yx.x): 0 for i, yx in enumerate(house_pos)}
        self.C = C
        self.field = Field(N, C, S)
        self.ans = Ans()
        self.dst_path = dst_path

    def solve_carpet(self, power):
        for y in range(self.N):
            for x in range(self.N):
                result, ans_q = self.field.query(y, x, power)
                self.ans.append(ans_q)

                if result == Response.FINISH:
                    print(f"total_cost={self.field.total_cost}", file=sys.stderr)
                    self.ans.output(self.dst_path)
                    sys.exit(0)
                elif result == Response.INVALID:
                    print(f"invalid: y={y} x={x}", file=sys.stderr)
                    sys.exit(1)

        self.ans.output(self.dst_path)


    def solve_sample(self):
        # from each house, go straight to the first source
        for house in self.house_pos:
            self.move_sample(house, self.source_pos[0])

        # should receive Response.FINISH and exit before entering here
        raise AssertionError()

    def move_sample(self, start: Pos, goal: Pos):
        # you can output comment
        print(f"# move from ({start.y},{start.x}) to ({goal.y},{goal.x})")

        # down/up
        if start.y < goal.y:
            for y in range(start.y, goal.y, 1):
                self.destruct_sample(y, start.x)
        else:
            for y in range(start.y, goal.y, -1):
                self.destruct_sample(y, start.x)

        # right/left
        if start.x < goal.x:
            for x in range(start.x, goal.x + 1, 1):
                self.destruct_sample(goal.y, x)
        else:
            for x in range(start.x, goal.x - 1, -1):
                self.destruct_sample(goal.y, x)

    def destruct_sample(self, y: int, x: int):
        # excavate (y, x) with fixed power until destruction
        power = 100
        while not self.field.is_broken[y][x]:
            result, ans_q = self.field.query(y, x, power)
            self.ans.append(ans_q)

            if result == Response.BROKEN and (y, x) in self.source_pos:
                self.house_connected[(y, x)] = 1
                if sum(self.house_connected.values()) == len(self.house_pos):
                    result = Response.FINISH

            print(f"# {self.house_connected}")

            if result == Response.FINISH:
                print(f"total_cost={self.field.total_cost}", file=sys.stderr)
                self.ans.output(self.dst_path)
                sys.exit(0)
            elif result == Response.INVALID:
                print(f"invalid: y={y} x={x}", file=sys.stderr)
                sys.exit(1)


def visualize(S, dst_path):
    from itertools import chain
    X = list(chain.from_iterable(S))
    step = 100
    X = [x // step * step for x in X]
    C = Counter(X)
    print(C)
    H = [C[i] for i in range(0, 5001, step)]
    print(H)
    cum = list(accumulate(H))

    plt.bar(range(0, 5001, step), cum, width=100)
    plt.gca().set_ylim([0, 40000])
    plt.savefig(dst_path, dpi=150, bbox_inches="tight")
    plt.close()


def main():
    if IS_LOCAL:
        for fi in range(1):
            filename = f"{str(fi).zfill(4)}.txt"
            src_path = Path(f"./in/{filename}")

            source_pos = []
            house_pos = []

            with open(src_path, mode="r") as f:
                f = f.readlines()
                N, W, K, C = map(int, f[0].split(" "))
                S = []
                for i in range(1, N+1):
                    S.append(list(map(int, f[i].split())))

                for i in range(W):
                    y, x = (int(v) for v in f[N+1+i].split(" "))
                    source_pos.append(Pos(y, x))
                for i in range(K):
                    y, x = (int(v) for v in f[N+1+W+i].split(" "))
                    house_pos.append(Pos(y, x))

            # visualize(S, Path(f"./vis/{str(fi).zfill(4)}.png"))

            dst_path = Path(f"./out/{filename}")
            print(f"# {N} {W} {K} {C}")
            solver = Solver(N, source_pos, house_pos, C, S, dst_path)
            solver.solve_carpet(3000)
            return

    else:
        N, W, K, C = [int(v) for v in input().split(" ")]
        S = None
        dst_path = None

        source_pos = []
        house_pos = []
        for _ in range(W):
            y, x = (int(v) for v in input().split(" "))
            source_pos.append(Pos(y, x))
        for _ in range(K):
            y, x = (int(v) for v in input().split(" "))
            house_pos.append(Pos(y, x))

        solver = Solver(N, source_pos, house_pos, C, S, dst_path)
        solver.solve_carpet(3000)



if __name__ == "__main__":
    main()


