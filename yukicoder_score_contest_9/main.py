import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

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


def score(a, b, x):
    v1 = abs(5 * 10**17 - a)
    v2 = abs(5 * 10**17 - b)
    if max(v1, v2) > 0:
        return int(2000000 - 100000 * math.log10(max(v1, v2)+1))
    else:
        return 2000050 - x


def answer(ans):
    print(len(ans))
    for i, j in ans:
        print(i+1, j+1)


def greedy():
    N = NI()
    AB = EI(N)

    ans = []
    # 0と何かだけで貪欲
    for qi in range(50):
        a0, b0 = AB[0]
        s = score(a0, b0, qi)
        best_s = s
        best_v = 1
        for v in range(1, N):
            av, bv = AB[v]
            na, nb = (a0+av) // 2, (b0+bv) // 2
            ns = score(na, nb, qi+1)

            if ns > best_s:
                best_s = ns
                best_v = v

        if best_s > s:
            av, bv = AB[best_v]
            na, nb = (a0 + av) // 2, (b0 + bv) // 2
            AB[0] = [na, nb]
            AB[best_v] = [na, nb]
            ans.append([0, best_v])
        else:
            break

    answer(ans)


def means(AB, i, j):
    ai, bi = AB[i]
    aj, bj = AB[j]
    na, nb = (ai + aj) // 2, (bi + bj) // 2
    return na, nb


def query(AB, i, j):
    na, nb = means(AB, i, j)
    AB[i] = [na, nb]
    AB[j] = [na, nb]


def total_score(AB):
    res = 0
    for a, b in AB:
        res += score(a, b, 0)
    return res


def calc_gap(AB, i, j):
    # ABについてi, jを操作したときのスコアの差分
    na, nb = means(AB, i, j)
    after = score(na, nb, 0) * 2
    before = score(AB[i][0], AB[i][1], 0) + score(AB[j][0], AB[j][1], 0)
    return after - before


def _main():
    N = NI()
    AB = EI(N)

    total = total_score(AB)
    # print(total)
    ans = []

    # totalが改善するように山登り
    for qi in range(50):

        max_gap = 0
        best_ij = [0, 1]
        for i in range(N):
            if qi == 49 and i > 0:
                break
            for j in range(i+1, N):
                gap = calc_gap(AB, i, j)
                if gap > max_gap:
                    max_gap = gap
                    best_ij = [i, j]
        if max_gap > 0:
            total += max_gap
            query(AB, *best_ij)
            ans.append(best_ij)
            # print(total, score(AB[0][0], AB[0][1], qi))
        else:
            break

    answer(ans)


def manhattan(a, b, ta, tb):
    v1 = abs(ta - a)
    v2 = abs(tb - b)
    return v1 + v2

def chebyshev(a, b, ta, tb):
    v1 = abs(ta - a)
    v2 = abs(tb - b)
    return max(v1, v2)

def twobytwo():
    N = NI()
    AB = EI(N)

    ans = []

    CENTER = 5 * 10**17

    # 二次元平面上で考える
    # 操作は「2点選んで中点につぶす」
    # AB[0]の反対側になるべく近いところになるように2点全探索
    # →そことAB[0]を選ぶ　を繰り返す？

    prev_ij = [0, 1]

    for qi in range(50):
        if qi % 2 == 0:
            a0, b0 = AB[0]
            ta = CENTER * 2 - a0
            tb = CENTER * 2 - b0

            minm = CENTER * 2
            best_ij = [0, 1]
            for i in range(1, N):
                for j in range(i + 1, N):
                    na, nb = means(AB, i, j)
                    m = manhattan(na, nb, ta, tb)
                    if m < minm:
                        best_ij = [i, j]
                        minm = m

            if minm < CENTER * 2:
                query(AB, *best_ij)
                ans.append(best_ij)
                prev_ij = best_ij

        else:
            j = prev_ij[1]
            query(AB, 0, j)
            ans.append([0, j])

        # print(score(*AB[0], 0))

    answer(ans)


def main():
    N = NI()
    AB = EI(N)

    ans = []

    CENTER = 5 * 10**17

    # 二次元平面上で考える
    # 操作は「2点選んで中点につぶす」
    # 4点→2点→1点にした点がAB[0]と反対側ならOK

    # AB[0]が端の場合無理なのでまず1回やる
    minm = CENTER * 2
    nj = 1
    for j in range(1, N):
        m = manhattan(*AB[0], *AB[j])
        if m < minm:
            nj = j
            minm = m
    query(AB, 0, nj)
    ans.append([0, nj])

    for _ in range(3):

        # 0以外の4点を全探索
        a0, b0 = AB[0]
        ta, tb = CENTER*2 - a0, CENTER*2 - b0

        minm = CENTER * 2
        bestP = []
        for P in permutations(range(1, N), 4):
            p1, p2, p3, p4 = P
            na1, nb1 = means(AB, p1, p2)
            na2, nb2 = means(AB, p3, p4)
            na, nb = (na1+na2) // 2, (nb1+nb2) // 2
            m = manhattan(ta, tb, na, nb)
            if m < minm:
                minm = m
                bestP = list(P)

        for P in permutations(range(1, N), 3):
            p1, p2, p3 = P
            na1, nb1 = means(AB, p1, p2)
            na2, nb2 = AB[p3]
            na, nb = (na1+na2) // 2, (nb1+nb2) // 2
            m = manhattan(ta, tb, na, nb)
            if m < minm:
                minm = m
                bestP = list(P)

        # print(score(*AB[0], 0))

        if len(bestP) == 3:
            p1, p2, p3 = bestP
            query(AB, p1, p2)
            ans.append([p1, p2])
            query(AB, p2, p3)
            ans.append([p2, p3])
            query(AB, p3, 0)
            ans.append([p3, 0])

        elif len(bestP) == 4:
            p1, p2, p3, p4 = bestP
            query(AB, p1, p2)
            ans.append([p1, p2])
            query(AB, p3, p4)
            ans.append([p3, p4])
            query(AB, p2, p4)
            ans.append([p2, p4])
            query(AB, 0, p4)
            ans.append([0, p4])

    answer(ans)
    # print(score(*AB[0], 1))
    # print(AB[0])


def sort_ABs():
    # いまいち
    N = NI()
    AB = EI(N)

    ans = []

    ABI = [[a, b, i] for i, (a, b) in enumerate(AB)]
    ABI.sort()
    for si in range(N//2):
        i, j = ABI[si][2], ABI[N-1-si][2]
        query(AB, i, j)
        ans.append([i, j])
    ABI = [[a, b, i] for i, (a, b) in enumerate(AB)]
    AB.sort(key=lambda x: x[1])
    for si in range(N // 2):
        i, j = ABI[si][2], ABI[N - 1 - si][2]
        query(AB, i, j)
        ans.append([i, j])

    CENTER = 5 * 10**17
    a0, b0 = AB[0]
    ta = CENTER * 2 - a0
    tb = CENTER * 2 - b0

    minm = CENTER * 2
    best_ij = [0, 1]
    for i in range(1, N):
        for j in range(i + 1, N):
            na, nb = means(AB, i, j)
            m = manhattan(na, nb, ta, tb)
            if m < minm:
                best_ij = [i, j]
                minm = m

    query(AB, *best_ij)
    ans.append(best_ij)

    j = best_ij[1]
    query(AB, 0, j)
    ans.append([0, j])

    answer(ans)


if __name__ == "__main__":
    main()
