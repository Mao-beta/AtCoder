import sys
import math
from collections import deque

sys.setrecursionlimit(100000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()



def main():
    N, X = NMI()
    ABC = [NLI() for _ in range(N-1)]

    D = [[] for _ in range(N)]
    for a, b, c in ABC:
        a, b = a-1, b-1
        D[a].append([b, c])
        D[b].append([a, c])


    def dfs(start):
        stack = deque([start])
        dist = [-1] * N
        dist[start] = 0

        while stack:
            now = stack.pop()
            now_dist = dist[now]
            for goto, cost in D[now]:
                if dist[goto] >= 0:
                    continue

                dist[goto] = now_dist + cost
                stack.append(goto)

        return dist


    for i in range(N):
        dist = dfs(i)
        if X in dist:
            print("Yes")
            exit()

    print("No")


if __name__ == "__main__":
    main()
