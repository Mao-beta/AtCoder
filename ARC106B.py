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

#隣接リスト 1-index
def make_adjlist_nond(n, edges):
    res = [[] for _ in range(n+1)]
    for edge in edges:
        res[edge[0]].append(edge[1])
        res[edge[1]].append(edge[0])
    return res


def main():
    N, M = NMI()
    A = NLI()
    B = NLI()
    edges = [NLI() for _ in range(M)]
    graph = make_adjlist_nond(N, edges)
    #print(graph)
    seen = [10**20] * (N + 1)
    for start in range(1, N+1):
        if seen[start] != 10**20:
            continue

        stack = deque()
        stack.append(start)

        seen[start] = start
        while stack:
            now = stack.pop()

            for goto in graph[now]:
                if seen[goto] != 10**20:
                    continue
                stack.append(goto)
                seen[goto] = -seen[now]
        #print(seen)

    ab_gaps = [0] + [a-b for a, b in zip(A, B)]
    #print(ab_gaps)
    case = [0] * (N+1)
    sums = [0] * (N+1)
    for i, s in enumerate(seen):
        if s == 10**20:
            continue
        if s > 0:
            case[s] += ab_gaps[i]
        else:
            case[-s] += ab_gaps[i]

    for c in case:
        if c != 0:
            print("No")
            exit()
    print("Yes")


if __name__ == "__main__":
    main()
