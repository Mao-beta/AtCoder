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
    N = NI()
    S = SI()
    A = NLI()

    L = [0]*(N+1)
    R = [0]*(N+1)
    for i in range(N):
        if S[i] == "<":
            L[i+1] = L[i] + 1
    T = S[::-1]
    for i in range(N):
        if T[i] == ">":
            R[i+1] = R[i] + 1
    R = R[::-1]
    #print(L, R)
    base = [max(l, r) for l, r in zip(L, R)]

    k = 1
    flag = False
    while True:
        rem = [a - b*(k-1) for a, b in zip(A, base)]
        if min(rem) < 0: break
        for i, s in enumerate(S):
            if s == "<" and rem[i] < rem[i+1]:
                pass
            elif s == ">" and rem[i] > rem[i+1]:
                pass
            else:
                flag = True
        if flag:
            break
        k += 1

    print(k-1)
    for i in range(k-2):
        print(*base)
    rem = [a - b * (k - 2) for a, b in zip(A, base)]
    print(*rem)


if __name__ == "__main__":
    main()
