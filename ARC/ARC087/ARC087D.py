import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations

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


from typing import List
from itertools import groupby

def runLengthEncode(S: str) -> "List[tuple[str, int]]":
    grouped = groupby(S)
    res = []
    for k, v in grouped:
        res.append((k, int(len(list(v)))))
    return res


def main():
    S = SI()
    X, Y = NMI()
    RS = runLengthEncode(S)

    LR = []
    UD = []
    is_lr = True
    for s, k in RS:
        if s == "T" and k % 2:
            is_lr = not is_lr

        elif s == "F":
            if is_lr:
                X += k
                LR.append(2*k)
            else:
                Y += k
                UD.append(2*k)

    if S[0] == "F":
        X -= LR[0]
        del LR[0]

    if not LR:
        if X != 0:
            print("No")
            exit()

    else:
        M = sum(LR)
        if M < X or X < 0:
            print("No")
            exit()

        dp = [[0]*(M+1) for _ in range(len(LR)+1)]
        dp[0][0] = 1
        for i, k in enumerate(LR):
            for j in range(M):
                dp[i+1][j] |= dp[i][j]
                if j+k <= M:
                    dp[i+1][j+k] |= dp[i][j]

        if dp[-1][X] == 0:
            print("No")
            exit()

    if not UD:
        if Y != 0:
            print("No")
            exit()

    else:
        M = sum(UD)
        if M < Y or Y < 0:
            print("No")
            exit()

        dp = [[0] * (M+1) for _ in range(len(UD)+1)]
        dp[0][0] = 1
        for i, k in enumerate(UD):
            for j in range(M):
                dp[i + 1][j] |= dp[i][j]
                if j + k <= M:
                    dp[i + 1][j + k] |= dp[i][j]

        if dp[-1][Y] == 0:
            print("No")
            exit()

    print("Yes")


if __name__ == "__main__":
    main()
