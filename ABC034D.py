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


#隣接リスト 1-order
def make_adjlist_d(n, edges):
    res = [[] for _ in range(n + 1)]
    for edge in edges:
        res[edge[0]].append(edge[1])
        res[edge[1]].append(edge[0])
    return res


def make_adjlist_nond(n, edges):
    res = [[] for _ in range(n + 1)]
    for edge in edges:
        res[edge[0]].append(edge[1])
    return res


#nCr
def cmb(n, r):
    return math.factorial(n) // math.factorial(r) // math.factorial(n - r)


def main():
    N, K = NMI()
    W = []
    P = []
    for i in range(N):
        tmpw, tmpp = NMI()
        W.append(tmpw)
        P.append(tmpp)

    ng = 101
    ok = 0
    for i in range(100):
        mid = (ng + ok) / 2
        Pk = [p-mid for p in P]
        adv = [pk*w for pk, w in zip(Pk, W)]
        adv = sorted(adv, reverse=True)
        con = sum(adv[:K])
        if con >= 0:
            ok = mid
        else:
            ng = mid
    print(ok)


if __name__ == "__main__":
    main()