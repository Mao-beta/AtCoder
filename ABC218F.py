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
    for i, a, b in edges:
        a, b = a-1, b-1
        res[a].append([i, b])
    return res


def main():
    N, M = NMI()
    ST = [[i] + NLI() for i in range(M)]
    G = adjlist_d_1to0(N, ST)

    que = deque()
    que.append((0, set()))
    seen = [0] * N
    U = set()

    while que:
        now, used = que.popleft()

        if now == N-1:
            U = used
            break

        for i, goto in G[now]:
            if seen[goto]:
                continue
            seen[goto] = 1
            used.add(i)
            que.append((goto, used.copy()))
            used.discard(i)

    shortest = len(U)

    if shortest == 0:
        for i in range(M):
            print(-1)
        exit()


    ans = [10**10] * M
    for i in range(M):
        if i not in U:
            ans[i] = shortest

    for m in U:
        que = deque()
        que.append((0, 0))
        seen = [0] * N

        while que:
            now, step = que.popleft()
            if now == N-1:
                ans[m] = step
                break

            for i, goto in G[now]:
                if seen[goto]:
                    continue
                if i == m:
                    continue
                seen[goto] = 1
                que.append((goto, step+1))

    for a in ans:
        if a == 10**10:
            print(-1)
        else:
            print(a)

if __name__ == "__main__":
    main()
