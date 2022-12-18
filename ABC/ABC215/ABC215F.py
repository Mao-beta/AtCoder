import sys
from collections import deque

input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()
SMI = lambda: input().split()
SLI = lambda: list(SMI())


def main(N, XY):
    XY.sort()
    INF = 10**15

    def judge(X):
        D = deque()
        ymin, ymax = INF, INF
        for x, y in XY:
            D.append((x, y))

            while D and x - D[0][0] >= X:
                dx, dy = D.popleft()
                if ymin == INF:
                    ymin = dy
                    ymax = dy
                    continue
                ymin = min(ymin, dy)
                ymax = max(ymax, dy)

            # print(D)

            if ymin == INF:
                continue
            if ymin <= y - X or ymax >= y + X:
                # print(x, y, ymin, ymax)
                return True

        return False


    ok = -1
    ng = 10**9+10
    while abs(ok - ng) > 1:
        X = (ok + ng) // 2
        # print(X)
        if judge(X):
            ok = X
        else:
            ng = X

    print(ok)


if __name__ == "__main__":
    N = NI()
    XY = [tuple(NMI()) for _ in range(N)]
    main(N, XY)

