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


def make_adjlist_d(n, edges):
    res = [[] for _ in range(n+1)]
    for edge in edges:
        res[edge[0]].append(edge[1])
    return res


def main():
    N, M = NMI()
    edges = [NLI() for _ in range(M)]
    S, T = NMI()

    tree = [[] for _ in range(3*N+1)]
    for e in edges:
        tree[e[0]].append(e[1]+N)
        tree[e[0]+N].append(e[1]+2*N)
        tree[e[0]+2*N].append(e[1])

    stack = deque()
    stack.append(S)
    seen = [-1] * (3*N+1)
    seen[S] = 0
    while stack:
        now = stack.popleft()
        now_step = seen[now]
        for goto in tree[now]:
            if seen[goto] >= 0:
                continue

            stack.append(goto)
            seen[goto] = now_step + 1

    print(seen[T]//3)



if __name__ == "__main__":
    main()