import sys


sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def make_adjlist_nond(n, edges):
    res = [[] for _ in range(n)]
    for a, b, c in edges:
        a, b = a-1, b-1
        res[a].append([b, c])
        res[b].append([a, c])
    return res


def main():
    N, M = NMI()
    edges = [NLI() for _ in range(M)]
    INF = 10**10
    costs = [[INF] * N for _ in range(N)]
    for i in range(N):
        costs[i][i] = 0

    for a, b, c in edges:
        a, b = a-1, b-1
        costs[a][b] = c
        costs[b][a] = c

    for k in range(N):
        for i in range(N):
            for j in range(N):
                costs[i][j] = min(costs[i][j], costs[i][k] + costs[k][j])

    ans = 0
    for a, b, c in edges:
        a, b = a-1, b-1
        if costs[a][b] < c:
            ans += 1

    print(ans)



if __name__ == "__main__":
    main()
