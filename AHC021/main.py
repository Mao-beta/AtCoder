import sys
import math
import bisect
import time
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
EI = lambda m: [NLI() for _ in range(m)]


def dist(x1, y1, x2, y2):
    # p1->p2の距離
    x = x2 - x1
    y = y2 - y1
    if x * y >= 0:
        return max(abs(x), abs(y))
    else:
        if y < 0:
            x, y = -x, -y
        y += abs(x)
        return y


def move(x1, y1, x2, y2):
    # 上方向になるべく無駄なく移動
    res = []
    l = x1 - x2
    x, y = x1, y1

    if l == 0:
        k = abs(y1 - y2)
        if y1 > y2:
            for _ in range(k):
                res.append((x, y, x, y - 1))
                y -= 1

        else:
            for _ in range(k):
                res.append((x, y, x, y + 1))
                y += 1

    elif y2 < y1 - l:
        left = y1 - l - y2
        for _ in range(l - 1):
            res.append((x, y, x - 1, y - 1))
            x -= 1
            y -= 1
        for _ in range(left):
            res.append((x, y, x, y - 1))
            y -= 1
        res.append((x, y, x - 1, y - 1))
        x -= 1
        y -= 1

    elif y1 < y2:
        right = y2 - y1
        for _ in range(l - 1):
            res.append((x, y, x - 1, y))
            x -= 1
        for _ in range(right):
            res.append((x, y, x, y + 1))
            y += 1
        res.append((x, y, x - 1, y))
        x -= 1

    else:
        while y > y2:
            res.append((x, y, x - 1, y - 1))
            x -= 1
            y -= 1
        while x > x2:
            res.append((x, y, x - 1, y))
            x -= 1

    assert x == x2
    assert y == y2

    return res


def act(_B, _D, moves):
    for x1, y1, x2, y2 in moves:
        b1, b2 = _B[x1][y1], _B[x2][y2]
        _D[b1], _D[b2] = (x2, y2), (x1, y1)
        _B[x1][y1], _B[x2][y2] = b2, b1


def make_D(N, B):
    D = {}
    for x in range(N):
        for y in range(x + 1):
            D[B[x][y]] = (x, y)
    return D


def solve(N, _B):
    """
    [0], [1, 2], [3, 4, 5], ...
    にする
    """
    B = [row[:] for row in _B]
    ans = []

    D = make_D(N, B)

    for x in range(N-1):
        start = x * (x+1) // 2
        targets = list(range(start, start+x+1))
        holders = [(x, y) for y in range(x+1)]
        for y, t in enumerate(targets):
            res = move(*D[t], *holders[y])
            act(B, D, res)

            ans += res

    return ans


import random

def solve_random_sub(N, _B):
    """
    [0], [1, 2], [3, 4, 5], ...
    にする
    同じ段ではシャッフルして入れる
    """
    B = [row[:] for row in _B]
    ans = []

    D = make_D(N, B)

    for x in range(N-1):
        start = x * (x+1) // 2
        targets = list(range(start, start+x+1))
        holders = [(x, y) for y in range(x+1)]
        random.shuffle(targets)
        # print(holders)
        for i, t in enumerate(targets):
            # print(x, i, t, *D[t], *holders[i])
            res = move(*D[t], *holders[i])
            act(B, D, res)
            ans += res

    return ans

N = 30
def calc_score(ans, B):
    E = 0
    for x in range(N-1):
        for y in range(x+1):
            for dy in [0, 1]:
                if y+dy >= x:
                    continue
                if B[x][y] > B[x+1][y+dy]:
                    E += 1

    if E == 0:
        return 100000 - 5 * len(ans)
    else:
        return 50000 - 50 * E


def solve_random(N, B):
    START_TIME = time.time()
    random.seed(42)
    best_score = 0
    best_ans = []

    while time.time() - START_TIME < 1.75:
        ans = solve_random_sub(N, B)
        score = calc_score(ans, B)
        if score > best_score:
            best_score = score
            best_ans = ans

        print(best_score, score)

    return best_ans


def solve_climb_sub(N, _B, _targets):
    """
    [0], [1, 2], [3, 4, 5], ...
    にする
    同じ段での順番は山登りする
    """
    B = [row[:] for row in _B]
    ans = []

    D = make_D(N, B)

    for x in range(N-1):
        start = x * (x+1) // 2
        targets = _targets[start: start+x+1]
        holders = [(x, y) for y in range(x+1)]
        # print(holders)
        for i, t in enumerate(targets):
            # print(x, i, t, *D[t], *holders[i])
            res = move(*D[t], *holders[i])
            act(B, D, res)
            ans += res

    return ans, B


def solve_climb(N, B):
    START_TIME = time.time()
    random.seed(42)
    best_score = 0
    best_ans = []

    X = [N-1] * 465

    targets = list(range(465))
    # for x in range(N-1):
    #     start = x * (x+1) // 2
    #     base = targets[start: start+x+1]
    #     for t in base:
    #         X[t] = x
    #     random.shuffle(base)
    #     targets[start: start + x + 1] = base[:]
    #
    # best_ans, lastB = solve_climb_sub(N, B, targets)
    # best_score = calc_score(best_ans, lastB)
    cnt = 0

    while time.time() - START_TIME < 1.75:
        cnt += 1
        old_targets = targets[:]

        # 遷移
        # 1割くらいswap
        for _ in range(0):
            a = random.randint(0, 464)
            b = random.randint(0, 464)
            targets[a], targets[b] = targets[b], targets[a]

        ans, lastB = solve_climb_sub(N, B, targets)
        score = calc_score(ans, lastB)

        if score > best_score:
            best_score = score
            best_ans = ans
        else:
            targets = old_targets[:]

        print(cnt, best_score, score)

    return best_ans



def main():
    B = []
    N = 30
    for _ in range(N):
        B.append(NLI())

    DH = [-1, -1, 0, 0, 1, 1]
    DW = [-1, 0, -1, 1, 0, 1]

    ans = solve_climb(N, B)

    # print(len(ans))
    # for row in ans:
    #     print(*row)



if __name__ == "__main__":
    main()
