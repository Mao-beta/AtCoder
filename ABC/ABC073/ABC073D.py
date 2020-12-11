import sys
import math
from collections import defaultdict
from collections import deque
from itertools import permutations

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    N, M, R = NMI()
    targets = NLI()
    targets = [t-1 for t in targets]
    dist = [[10**9] * N for _ in range(N)]
    for _ in range(M):
        a, b, c = NMI()
        dist[a-1][b-1] = c
        dist[b-1][a-1] = c
    for i in range(N):
        dist[i][i] = 0

    for k in range(N):
        for i in range(N):
            for j in range(N):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    ans = 10**9
    for case in permutations(targets, R):
        now = case[0]
        cost = 0
        for goto in case[1:]:
            cost += dist[now][goto]
            now = goto
        ans = min(ans, cost)
    print(ans)

if __name__ == "__main__":
    main()