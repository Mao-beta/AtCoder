import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations
# import matplotlib.pyplot as plt

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
MOD99 = 998244353

input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()
SMI = lambda: input().split()
SLI = lambda: list(SMI())


def main():
    p = (37, 0)
    q = (123, 123)
    r = (0, 31)
    X = []
    Y = []
    for i in range(10):
        for j in range(10):
            for k in range(10):
                x = i * p[0] + j * q[0] + k * r[0]
                y = i * p[1] + j * q[1] + k * r[1]
                X.append(x)
                Y.append(y)

    print(1000)
    for x, y in zip(X, Y):
        print(x, y)


def judge(PX, PY):
    X = set()
    Y = set()
    D = set()
    S = set()

    for x, y in zip(PX, PY):
        X.add(x)
        Y.add(y)
        D.add(y-x)
        S.add(x+y)

    a, b, c, d = len(Y), len(D), len(X), len(S)
    M = max(a, b, c)
    print(a, b, c, d)


def plot():
    p = (37, 0)
    q = (123, 123)
    r = (0, 31)
    X = []
    Y = []
    for i in range(10):
        for j in range(10):
            for k in range(10):
                x = i * p[0] + j * q[0] + k * r[0]
                y = i * p[1] + j * q[1] + k * r[1]
                X.append(x)
                Y.append(y)

    judge(X, Y)

    plt.scatter(X, Y, s=10)
    plt.show()


if __name__ == "__main__":

    main()
