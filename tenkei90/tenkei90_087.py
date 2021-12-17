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
    N, P, K = NMI()
    A = [NLI() for _ in range(N)]

    def calc(X):
        AA = [[X]*N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if A[i][j] != -1:
                    AA[i][j] = A[i][j]

        for k in range(N):
            for i in range(N):
                for j in range(N):
                    AA[i][j] = min(AA[i][j], AA[i][k] + AA[k][j])

        num = 0
        for i in range(N):
            for j in range(i+1, N):
                if AA[i][j] <= P:
                    num += 1

        return num


    # K個ある区間の下端を求める
    # 「K個以下か？」についてng=1, ok=10**20
    ok = 10**20
    ng = 0
    while abs(ok-ng) > 1:
        X = (ok + ng) // 2
        if calc(X) <= K:
            ok = X
        else:
            ng = X

    L = ok

    # K個ある区間の上端(の次)を求める
    # 「K-1個以下か？」についてng=1, ok=10**20
    ok = 10**20
    ng = 0
    while abs(ok-ng) > 1:
        X = (ok + ng) // 2
        if calc(X) <= K-1:
            ok = X
        else:
            ng = X

    R = ok
    if R - L >= 10**15:
        print("Infinity")
    else:
        print(R-L)


if __name__ == "__main__":
    main()
