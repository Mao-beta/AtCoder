import sys
import heapq

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    N = NI()
    P = [NLI() for _ in range(N)]

    if N <= 3:
        hq = []
        heapq.heapify(hq)
        for i in range(N):
            for j in range(i+1, N):
                xi, yi = P[i]
                xj, yj = P[j]
                d = max(abs(xi-xj), abs(yi-yj))
                heapq.heappush(hq, -d)
        _ = heapq.heappop(hq)
        ans = heapq.heappop(hq)
        print(-ans)
        exit()

    X = [(x, i) for i, (x, y) in enumerate(P)]
    Y = [(y, i) for i, (x, y) in enumerate(P)]

    X.sort()
    Y.sort()

    def dist(i, j):
        xi, yi = P[i]
        xj, yj = P[j]
        d = max(abs(xi - xj), abs(yi - yj))
        return d

    idx = [(X[-1][1], X[0][1]), (X[-2][1], X[0][1]), (X[-1][1], X[1][1]),
           (Y[-1][1], Y[0][1]), (Y[-2][1], Y[0][1]), (Y[-1][1], Y[1][1])]

    idx = list(map(tuple, (map(sorted, idx))))
    idx = set(idx)

    L = [dist(i, j) for i, j in idx]

    L.sort()
    print(L[-2])


if __name__ == "__main__":
    main()
