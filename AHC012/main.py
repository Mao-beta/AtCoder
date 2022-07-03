import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations


try:
    import numpy
    IS_LOCAL = True
except:
    IS_LOCAL = False


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


INF = 10**9-1

def hline(y):
    return [-INF, y-1, INF, y]

def vline(x):
    return [x-1, -INF, x, INF]


def ruline(x):
    return [x, 0, x+1, 1]

def luline(x):
    return [x, 0, x-1, 1]


def output(ans):
    print(len(ans))
    for row in ans:
        print(*row)


def count_from_gap(gap, XY):
    D = [(x // gap, y // gap) for x, y in XY]
    C = Counter(Counter(D).values())
    return [C[i] for i in range(1, 11)]


def count_from_gap_tilt(gap, XY):
    D = [((y+x) // gap, (y-x) // gap) for x, y in XY if (y+x) % gap and (y-x) % gap]
    C = Counter(Counter(D).values())
    return [C[i] for i in range(1, 11)]


def calc_score(A, B):
    S = [min(a, b) for a, b in zip(A, B)]
    res = round(10**6 * sum(S) / sum(A))
    return res


def main(N, K, A, XY):

    ans = []
    score = 0
    gap = 0
    for tmp_gap in range(500, 1001):
        B = count_from_gap(tmp_gap, XY)
        tmp_score = calc_score(A, B)
        if tmp_score > score:
            score = tmp_score
            gap = tmp_gap

    is_tilt = False

    for tmp_gap in range(700, 1500):
        B = count_from_gap_tilt(tmp_gap, XY)
        tmp_score = calc_score(A, B)
        if tmp_score > score:
            score = tmp_score
            gap = tmp_gap
            is_tilt = True


    if not is_tilt:
        k = 10**4 // gap + 1
        for i in range(-k, k+1):
            ans.append(hline(0 + gap * i))
            ans.append(vline(0 + gap * i))

    else:
        k = 10 ** 4 * 16 // gap // 10 + 1
        for i in range(-k, k + 1):
            ans.append(ruline(0 + gap * i))
            ans.append(luline(0 + gap * i))

    if not IS_LOCAL:
        output(ans)
    else:
        print(gap, is_tilt, score)


def take_input(path=None):
    if path:
        with open(path, mode="r") as f:
            inputs = f.readlines()
            N, K = map(int, inputs[0].split())
            A = list(map(int, inputs[1].split()))
            XY = []
            for i in range(N):
                xy = list(map(int, inputs[2+i].split()))
                XY.append(xy)

    else:
        N, K = NMI()
        A = NLI()
        XY = [NLI() for _ in range(N)]

    return N, K, A, XY


# IS_LOCAL = False

if __name__ == "__main__":
    if IS_LOCAL:
        for i in range(100):
            path = f"./in/{str(i).zfill(4)}.txt"
            main(*take_input(path))

    else:
        main(*take_input())
