import sys
import math
from collections import defaultdict
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    H, W = NMI()
    C = NLI()
    D = NLI()
    C = [x-1 for x in C]
    D = [x-1 for x in D]
    grid = [SI() for _ in range(H)]

    que = deque()
    cost = [[10**10]*W for _ in range(H)]
    cost[C[0]][C[1]] = 0
    que.append(C)
    while que:
        now = que.popleft()
        now_cost = cost[now[0]][now[1]]

        for i in range(-2, 3):
            if now[0] + i < 0 or now[0] + i >= H:
                continue
            for j in range(-2, 3):
                if now[1]+j < 0 or now[1]+j >= W:
                    continue
                if i == j == 0:
                    continue
                goto = [now[0]+i, now[1]+j]
                goto_cost = cost[goto[0]][goto[1]]
                if grid[goto[0]][goto[1]] == "#":
                    continue

                dist = abs(goto[0]-now[0]) + abs(goto[1]-now[1])
                if dist == 1:
                    if now_cost < goto_cost:
                        cost[goto[0]][goto[1]] = now_cost
                        que.appendleft(goto)
                else:
                    if now_cost + 1 < goto_cost:
                        cost[goto[0]][goto[1]] = now_cost + 1
                        que.append(goto)

    ans = cost[D[0]][D[1]]
    print(ans if ans < 10**10 else -1)


if __name__ == "__main__":
    main()