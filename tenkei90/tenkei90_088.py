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


def adjlist_d_1to0(n, edges):
    res = [[] for _ in range(n)]
    for a, b in edges:
        a, b = a-1, b-1
        res[a].append(b)
    return res


def main():
    N, Q = NMI()
    A = NLI()
    XY = [NLI() for _ in range(Q)]
    graph = adjlist_d_1to0(N, XY)

    D = [None] * 9000
    S = set()
    cnts = [0] * N


    def dfs(i, total):

        if i == N:
            if D[total]:
                print(len(D[total]))
                print(*D[total])
                print(len(S))
                print(*tuple(S))
                exit()
            D[total] = tuple(S)
            return

        a = A[i]

        # えらばない
        dfs(i+1, total)

        # えらぶ
        if cnts[i]:
            return

        for goto in graph[i]:
            cnts[goto] += 1

        S.add(i+1)
        dfs(i+1, total+a)
        S.discard(i+1)

        for goto in graph[i]:
            cnts[goto] -= 1


    dfs(0, 0)


if __name__ == "__main__":
    main()
