import random
import sys
import math
import bisect
import time
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations


try:
    import numpy
    IS_LOCAL = True
except:
    IS_LOCAL = False

input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()
SMI = lambda: input().split()
SLI = lambda: list(SMI())


INF = 10**9-1
BOX = 10**4 + 100


def hline(y):
    return [-BOX, y, BOX, y]

def vline(x):
    return [x, -BOX, x, BOX]


def output(ans):
    print(len(ans))
    for row in ans:
        print(*row)


def calc_score(A, XY, ans):
    N = len(XY)
    pieces = [list(range(N))]
    for px, py, qx, qy in ans:
        new_pieces = []
        for piece in pieces:
            left = []
            right = []
            for j in piece:
                x, y = XY[j]
                side = (qx - px) * (y - py) - (qy - py) * (x - px)
                if side > 0:
                    left.append(j)
                elif side < 0:
                    right.append(j)

            if left:
                new_pieces.append(left)
            if right:
                new_pieces.append(right)
        pieces = new_pieces

    b = [0] * 10
    for piece in pieces:
        if len(piece) <= 10:
            b[len(piece)-1] += 1

    num = 0
    den = 0
    for d in range(10):
        num += min(A[d], b[d])
        den += A[d]
    score = round(1e6 * num / den)
    return score


def pick_ij(n):
    nbi = random.randint(0, n - 1)
    while True:
        nbj = random.randint(0, n - 1)
        if nbi != nbj:
            break
    return nbi, nbj


def main(N, K, A, XY):
    start_time = time.time()

    BN = 8 * BOX
    BX = list(range(-BOX, BOX+1)) * 2 + [-BOX] * (2*BOX-1) + [BOX] * (2*BOX-1)
    BY = [-BOX] * (2*BOX+1) + [BOX] * (2*BOX+1) + list(range(-BOX+1, BOX)) * 2

    ans = []
    gap = 800

    k = 10 ** 4 // gap + 1
    for i in range(-k, k + 1):
        ans.append(hline(0 + gap * i))
        ans.append(vline(0 + gap * i))

    for i in range(K - len(ans)):
        ans.append(hline(BOX))

    score = calc_score(A, XY, ans)

    while time.time() - start_time < 2.7:
        idxes = []
        pqs = []

        for i in range(10):
            idx = random.randint(K-40, K-1)
            idxes.append(idx)

            pqs.append(ans[idx])

            nbi, nbj = pick_ij(BN)

            npx, npy = BX[nbi], BY[nbi]
            nqx, nqy = BX[nbj], BY[nbj]

            ans[idx] = [npx, npy, nqx, nqy]

        tmp_score = calc_score(A, XY, ans)

        if tmp_score > score:
            score = tmp_score

        else:
            for idx, pq in zip(idxes, pqs):
                ans[idx] = pq


    if not IS_LOCAL:
        output(ans)
    else:
        print(score)


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
