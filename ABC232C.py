import sys
import math
from itertools import permutations

sys.setrecursionlimit(100000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def adjlist_nond_1to0(n, edges):
    res = [[] for _ in range(n)]
    for a, b in edges:
        a, b = a-1, b-1
        res[a].append(b)
        res[b].append(a)
    return res


def main():
    N, M = NMI()
    AB = [NLI() for _ in range(M)]
    CD = set(tuple(NLI()) for _ in range(M))

    for P in permutations(range(1, N+1), N):
        TA = {i: p for i, p in enumerate(P, start=1)}
        ok = True
        for a, b in AB:
            aa, bb = TA[a], TA[b]
            aa, bb = min(aa, bb), max(aa, bb)
            if (aa, bb) not in CD:
                ok = False

        if ok:
            print("Yes")
            exit()
    print("No")



if __name__ == "__main__":
    main()
