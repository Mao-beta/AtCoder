import sys
import math
import bisect
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


def main():
    Q = NI()
    querys = [SLI() for _ in range(Q)]

    G = [[] for _ in range(Q+1)]
    Y2V = defaultdict(int)
    V2Q = [[] for _ in range(Q+1)]
    now = 0
    newV = 1
    for qi, query in enumerate(querys):
        q = query[0]
        if q == "DELETE":
            G[now].append([newV, q, -1])
            now = newV
            newV += 1

        else:
            x = int(query[1])
            if q[0] == "A":
                G[now].append([newV, q, x])
                now = newV
                newV += 1
            elif q[0] == "S":
                Y2V[x] = now
            else:
                now = Y2V[x]

        V2Q[now].append(qi)

    # print(G)
    # print(V2Q)
    A = []
    ans = [-1] * Q

    def dfs(now):
        # print(now, V2Q[now], A)
        for qi in V2Q[now]:
            # print(qi)
            if A:
                ans[qi] = A[-1]

        for goto, q, x in G[now]:
            if q[0] == "A":
                A.append(x)
            else:
                if A:
                    x = A.pop()

            dfs(goto)

            if q[0] == "A":
                A.pop()
            else:
                if x != -1:
                    A.append(x)

    dfs(0)
    ans = map(str, ans)
    print(" ".join(ans))


if __name__ == "__main__":
    main()
