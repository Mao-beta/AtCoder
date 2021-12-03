import sys
from itertools import permutations

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    N = NI()
    A = [NLI() for _ in range(N)]
    M = NI()
    XY = [NLI() for _ in range(M)]
    B = [[0]*N for _ in range(N)]

    for x, y in XY:
        B[x-1][y-1] = 1
        B[y-1][x-1] = 1

    P = permutations(range(N), N)

    if N == 1:
        print(A[0][0])
        exit()

    INF = 10**10
    ans = INF

    for case in P:
        is_bad = False
        for i in range(N-1):
            x, y = case[i], case[i+1]
            if B[x][y]:
                is_bad = True

        if is_bad:
            continue

        tmp = 0
        for i, x in enumerate(case):
            tmp += A[x][i]
        ans = min(ans, tmp)

    print(ans if ans != INF else -1)


if __name__ == "__main__":
    main()
