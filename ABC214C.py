import sys
import math
from collections import deque
from itertools import accumulate

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    N = NI()
    S = NLI()
    T = NLI()

    X = [10**10] * N
    for i in range(2*N+1):
        j = i-1
        i %= N
        j %= N
        X[i] = min(X[i], T[i], X[j]+S[j])

    print(*X, sep="\n")



if __name__ == "__main__":
    main()
