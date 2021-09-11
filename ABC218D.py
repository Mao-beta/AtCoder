import sys
import math
from collections import defaultdict

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

    S = defaultdict(int)
    Ys = defaultdict(list)
    P.sort()

    for x, y in P:
        Ys[x].append(y)

    ans = 0
    YI = sorted(Ys.items())
    for x, Y in YI:
        if len(Y) <= 1: continue
        k = len(Y)
        for i in range(k):
            for j in range(i+1, k):
                yi = Y[i]
                yj = Y[j]
                ans += S[(yi, yj)]
                S[(yi, yj)] += 1

    print(ans)


if __name__ == "__main__":
    main()
