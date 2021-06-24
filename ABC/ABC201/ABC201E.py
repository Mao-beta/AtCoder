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


def main():
    N = NI()
    edges = [NLI() for _ in range(N-1)]
    graph = [[] for _ in range(N)]

    for u, v, w in edges:
        u, v = u-1, v-1
        graph[u].append([v, w])
        graph[v].append([u, w])

    stack = deque()
    stack.append(0)
    X = [-1] * N
    X[0] = 0

    while stack:
        now = stack.pop()
        nowx = X[now]
        for goto, w in graph[now]:
            if X[goto] != -1: continue
            X[goto] = nowx ^ w
            stack.append(goto)

    C = [[0]*2 for _ in range(61)]
    for k, x in enumerate(X):
        for i in range(61):
            if (x>>i) & 1:
                C[i][1] += 1
            else:
                C[i][0] += 1

    ans = 0
    for i in range(61):
        y = C[i][1] * C[i][0]
        ans = (ans + y * pow(2, i, MOD)) % MOD

    print(ans)


if __name__ == "__main__":
    main()
