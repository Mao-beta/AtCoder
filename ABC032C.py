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


def main():
    N, K = NMI()
    S = []
    for i in range(N):
        s = NI()
        if s == 0:
            print(N)
            exit()
        S.append(s)

    print(syakutori(S, K))

def syakutori(array, K):
    n = len(array)
    l, r = 0, 0
    mul = 1
    res = 0
    for l in range(n):
        while r < n and mul * array[r] <= K:
            mul *= array[r]
            r += 1
        res = max(res, r-l)
        if l == r:
            r += 1
        else:
            mul = mul // array[l]
    return res


if __name__ == "__main__":
    main()