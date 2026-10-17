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


def get_y(x, x1, y1, x2, y2):
    """ (x1,y1) と (x2,y2) を結ぶ線分の、x1<=x<=x2 である x の時の y 座標 """
    assert x1 - 1e-6 <= x <= x2 + 1e-6
    dx = x2 - x1
    if dx == 0:
        return y2
    return (y1 * (x2 - x) + y2 * (x - x1)) / dx


def cross_point(x0, y0, x1, y1, x2, y2, x3, y3):
    a0 = x1 - x0
    b0 = y1 - y0
    a2 = x3 - x2
    b2 = y3 - y2

    d = a0 * b2 - a2 * b0
    if d == 0:
        return None

    sn = b2 * (x2 - x0) - a2 * (y2 - y0)
    if not (0 <= sn <= d or d <= sn <= 0):
        return None

    rn = b0 * (x2 - x0) - a0 * (y2 - y0)
    if not (0 <= rn <= d or d <= rn <= 0):
        return None

    return x0 + a0 * sn / d, y0 + b0 * sn / d


def push_rrr(cp, rrr):
    """ 昇順にソートされていて、末尾数項のみが追加点cpと比較して大きい可能性があるrrrに、cpを追加する """
    if rrr:
        if rrr[-1] < cp:
            rrr.append(cp)
        elif rrr[-1] > cp:
            i = len(rrr) - 2
            while i >= 0 and rrr[i] >= cp:
                i -= 1
            if rrr[i + 1] > cp:
                rrr.insert(i + 1, cp)
    else:
        rrr.append(cp)


def add_next_cross(is_hi, ai, bli, bhi, aaa, bbb, n, m, rlo, rhi):
    if bli == bhi == -1:
        return

    x0, y0 = aaa[ai]
    if is_hi:
        x1, y1 = aaa[(ai - 1) % n]
    else:
        x1, y1 = aaa[(ai + 1) % n]
    x2, y2 = bbb[bli]
    x3, y3 = bbb[(bli + 1) % m]
    cp = cross_point(x0, y0, x1, y1, x2, y2, x3, y3)
    # print(f'{x0},{y0},{x1},{y1},{x2},{y2},{x3},{y3},{cp}')
    if cp is not None:
        push_rrr(cp, rlo)
        if is_hi:
            push_rrr(cp, rhi)

    x2, y2 = bbb[bhi]
    x3, y3 = bbb[(bhi - 1) % m]
    cp = cross_point(x0, y0, x1, y1, x2, y2, x3, y3)
    # print(f'{x0},{y0},{x1},{y1},{x2},{y2},{x3},{y3},{cp}')
    if cp is not None:
        push_rrr(cp, rhi)
        if not is_hi:
            push_rrr(cp, rlo)


def add_corner(x, y, bli, bhi, bbb, m, rrr, rrr2=None):
    if bli == bhi == -1:
        return
    if rrr and rrr[-1] == (x, y):
        return
    aly = get_y(x, *bbb[bli], *bbb[(bli + 1) % m])
    ahy = get_y(x, *bbb[bhi], *bbb[(bhi - 1) % m])
    if aly <= y <= ahy:
        push_rrr((x, y), rrr)
        if rrr2 is not None:
            push_rrr((x, y), rrr2)


def get_intersection(ppp, qqq):
    """
    凸多角形ppp, qqq(頂点のリスト)の共通部分の頂点群を返す
    """
    n = len(ppp)
    m = len(qqq)
    ppp_events = [(x, y, 0, i) for i, (x, y) in enumerate(ppp)]
    qqq_events = [(x, y, 1, i) for i, (x, y) in enumerate(qqq)]

    pi_min = min(ppp_events)[3]
    pi_max = max(ppp_events)[3]
    qi_min = min(qqq_events)[3]
    qi_max = max(qqq_events)[3]

    events = ppp_events + qqq_events
    events.sort()

    pli = phi = qli = qhi = -1
    rlo = []
    rhi = []

    for x, y, pq, i in events:

        if pq == 0 and i == pi_min:
            pli = phi = i
            add_next_cross(True, pli, qli, qhi, ppp, qqq, n, m, rlo, rhi)
            add_next_cross(False, phi, qli, qhi, ppp, qqq, n, m, rlo, rhi)
            add_corner(x, y, qli, qhi, qqq, m, rlo, rhi)
            continue
        if pq == 1 and i == qi_min:
            qli = qhi = i
            add_next_cross(True, qli, pli, phi, qqq, ppp, m, n, rlo, rhi)
            add_next_cross(False, qhi, pli, phi, qqq, ppp, m, n, rlo, rhi)
            add_corner(x, y, pli, phi, ppp, n, rlo, rhi)
            continue

        if pq == 0:
            if i == (pli + 1) % n:
                add_corner(x, y, qli, qhi, qqq, m, rlo)
                pli = i
                if pli != pi_max:
                    add_next_cross(False, pli, qli, qhi, ppp, qqq, n, m, rlo, rhi)
            if i == (phi - 1) % n:
                add_corner(x, y, qli, qhi, qqq, m, rhi)
                phi = i
                if phi != pi_max:
                    add_next_cross(True, phi, qli, qhi, ppp, qqq, n, m, rlo, rhi)
        else:
            if i == (qli + 1) % m:
                add_corner(x, y, pli, phi, ppp, n, rlo)
                qli = i
                if qli != qi_max:
                    add_next_cross(False, qli, pli, phi, qqq, ppp, m, n, rlo, rhi)
            if i == (qhi - 1) % m:
                add_corner(x, y, pli, phi, ppp, n, rhi)
                qhi = i
                if qhi != qi_max:
                    add_next_cross(True, qhi, pli, phi, qqq, ppp, m, n, rlo, rhi)

        if pli == phi == pi_max or qli == qhi == qi_max:
            break

    if len(rlo) == len(rhi) == 0:
        return []

    assert len(rlo) > 0 and len(rhi) > 0
    assert rlo[0] == rhi[0]
    assert rlo[-1] == rhi[-1]

    if len(rlo) + len(rhi) <= 4:
        return []

    rlo.extend(rhi[-2:0:-1])
    return rlo


def polygon_area(N, P):
    return abs(sum(P[i][0]*P[i-1][1] - P[i][1]*P[i-1][0] for i in range(N))) / 2.


def main():
    N, M = NMI()
    S = EI(N)
    T = EI(M)

    P = get_intersection(S, T)

    if len(P) < 3:
        print(0)
        return

    print(polygon_area(len(P), P))


if __name__ == "__main__":
    main()
