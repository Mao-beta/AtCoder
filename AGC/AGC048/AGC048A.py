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
    T = NI()
    for _ in range(T):
        S = SI()
        N = len(S)
        res = 10**10
        if S > "atcoder":
            print(0)
            continue

        for i in range(N):
            for j in range(i+1, N):
                s = S[:i] + S[j] + S[i+1:j] + S[i] + S[j+1:]
                if s > "atcoder":
                    res = min(res, j-i)
        if res == 10**10:
            print(-1)
        else:
            print(res)


if __name__ == "__main__":
    main()
