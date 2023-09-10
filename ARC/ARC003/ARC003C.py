import sys
from heapq import heappop, heappush

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    N, M = NMI()
    C = [list(SI()) for _ in range(N)]

    INF = 10**12
    L = [[i * INF] for i in range(10)]
    for i in range(10):
        for j in range(N*M+1):
            L[i].append(L[i][-1] * 99 // 100)

    S = [0, 0]
    T = [0, 0]
    for i in range(N):
        for j in range(M):
            c = C[i][j]
            if c == "s":
                S = [i, j]
            elif c == "g":
                T = [i, j]


    DH = [0, 0, 1, -1]
    DW = [1, -1, 0, 0]

    def f(t, h, w):
        return t * 500**2 + h * 500 + w

    def g(thw):
        t, hw = divmod(thw, 500**2)
        h, w = divmod(hw, 500)
        return t, h, w


    def check(X):
        # X以上の道のみ通ってgにたどり着けるか
        D = [[INF] * M for _ in range(N)]
        hq = []
        heappush(hq, f(0, S[0], S[1]))
        D[S[0]][S[1]] = 0

        while hq:
            t, h, w = g(heappop(hq))
            if t > D[h][w]:
                continue

            # print(t, h, w)
            if C[h][w] == "g":
                return True

            for dh, dw in zip(DH, DW):
                nh, nw = h+dh, w+dw
                if nh < 0 or N <= nh or nw < 0 or M <= nw:
                    continue
                if C[nh][nw] == "#":
                    continue

                if C[nh][nw] == "g":
                    l = L[int(C[h][w])][t]
                elif C[nh][nw] == "s":
                    continue
                else:
                    c = int(C[nh][nw])
                    l = L[c][t+1]

                # print(nh, nw, c, l)

                if l < X:
                    continue

                if D[nh][nw] > t+1:
                    heappush(hq, f(t+1, nh, nw))
                    D[nh][nw] = t+1

        return False


    ok = -1
    ng = INF**2
    while abs(ok - ng) > 1:
        X = (ok + ng) // 2
        # print(X)
        if check(X):
            ok = X
        else:
            ng = X

    print(-1 if ok == -1 else ok / INF)


if __name__ == "__main__":
    main()
