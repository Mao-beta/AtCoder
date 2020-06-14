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
    N, Q = NMI()
    infants = [[0, 0]]
    inf_to_kind = [0] * (N+1)
    kinder = {}
    for i in range(N):
        a, b = NMI()
        infants.append([a, b])
        inf_to_kind[i+1] = b
        if not b in kinder:
            kinder[b] = {}
        kinder[b][i+1] = a
    querys = [NLI() for _ in range(Q)]

    for infant, next_kind in querys:
        now_kind = inf_to_kind[infant]
        inf_to_kind[infant] = next_kind
        rate = kinder[now_kind][infant]
        del kinder[now_kind][infant]
        if not next_kind in kinder:
            kinder[next_kind] = {}
        kinder[next_kind][infant] = rate
        res = 10**10
        for k in kinder.keys():
            if kinder[k]:
                res = min(res, max(kinder[k].values()))
        print(res)


if __name__ == "__main__":
    main()