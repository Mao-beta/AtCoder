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
    N, M = NMI()
    X = NLI()
    Y = NLI()
    X = [X[i+1] - X[i] for i in range(N-1)]
    Y = [Y[i+1] - Y[i] for i in range(M-1)]
    XS = 0
    YS = 0
    for i, x in enumerate(X):
        k = (i+1) * (N-1-i)
        XS += x * k
    for i, y in enumerate(Y):
        k = (i+1) * (M-1-i)
        YS += y * k
    print(XS*YS%MOD)

if __name__ == "__main__":
    main()
