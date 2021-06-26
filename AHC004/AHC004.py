import sys
import math
from collections import deque
import random

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    N, M = NMI()
    S = [SI() for _ in range(M)]
    S.sort(key=lambda x: len(x))
    letters = "ABCDEF"
    ans = [["."]*N for _ in range(N)]

    s_idx = 0
    for h in range(N):
        for w in range(N):
            if ans[h][w] != ".":
                continue
            s = S[s_idx]
            if w + len(s) >= N:
                break
            for i, ss in enumerate(s):
                ans[h][w+i] = ss
            s_idx += 1


    for row in ans:
        print("".join(row))


if __name__ == "__main__":
    main()
