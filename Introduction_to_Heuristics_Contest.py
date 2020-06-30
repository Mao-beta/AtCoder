import sys
import math
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def make_grid(h, w, num): return [[int(num)] * w for _ in range(h)]


def main():
    D = NI()
    C = NLI()
    S = [NLI() for _ in range(D)]
    #T = [NI() - 1 for _ in range(D)]
    T = []
    last = [0]*26
    conf = 0
    for i in range(D):
        idx, s = argmax(S[i])
        T.append(idx)
        conf += s
        last[idx] = i+1
        for a in range(26):
            conf -= C[a] * (i+1 - last[a])
        print(idx)


def argmax(A):
    A = [[i, a] for i, a in enumerate(A)]
    A.sort(key=lambda x: x[1], reverse=True)
    return A[0]


if __name__ == "__main__":
    main()