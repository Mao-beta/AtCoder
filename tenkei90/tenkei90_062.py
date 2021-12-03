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
    AB = [NLI() for _ in range(N)]
    graph = [[] for _ in range(N+1)]
    que = deque()
    seen = [0] * (N+1)
    for i, (a, b) in enumerate(AB, start=1):
        graph[a].append(i)
        graph[b].append(i)
        if a == i or b == i:
            que.append(i)
            seen[i] = 1


    ans = []
    while que:
        now = que.popleft()
        ans.append(now)
        for goto in graph[now]:
            if seen[goto]:
                continue
            que.append(goto)
            seen[goto] = 1

    ans = ans[::-1]
    if len(ans) != N:
        print(-1)
        exit()

    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
