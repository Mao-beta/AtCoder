import sys
import math
from collections import deque
from collections import defaultdict
from itertools import permutations

sys.setrecursionlimit(100000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def adjlist_nond_1to0(n, edges):
    res = [[] for _ in range(n+1)]
    for a, b in edges:
        res[a].append(b)
        res[b].append(a)
    return res


def main():
    M = NI()
    edges = [NLI() for _ in range(M)]
    P = NLI()
    graph = adjlist_nond_1to0(9, edges)

    que = deque()
    start = [9] * 10
    start[0] = 0
    for i, p in enumerate(P, start=1):
        start[p] = i

    ideal = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
    seen = defaultdict(int)

    if tuple(start) == ideal:
        print(0)
        exit()

    que.append((start, 0))
    while que:
        now, step = que.popleft()
        empty = now.index(9)
        for goto in graph[empty]:
            goto_state = now.copy()
            goto_state[empty], goto_state[goto] = goto_state[goto], goto_state[empty]
            if seen[tuple(goto_state)]:
                continue
            seen[tuple(goto_state)] = 1
            if tuple(goto_state) == ideal:
                print(step+1)
                exit()

            que.append((goto_state, step+1))

    print(-1)


if __name__ == "__main__":
    main()
