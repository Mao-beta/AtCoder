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


def str_to_01(S):
    res = []
    for row in S:
        nrow = []
        for s in row:
            if s == "#":
                nrow.append(1)
            else:
                nrow.append(0)
        res.append(nrow)
    return res


def pick_1_hw(S):
    N = len(S)
    res = []
    for h in range(N):
        for w in range(N):
            if S[h][w]:
                res.append((h, w))
    return res


def rotate(hws, N):
    res = []
    for h, w in hws:
        res.append((w, N-1-h))
    res.sort(key=lambda x: (x[0], x[1]))
    return res


def shift(hws, dh, dw):
    res = []
    for h, w in hws:
        res.append((h+dh, w+dw))
    return res


def check(S, T):
    for s, t in zip(S, T):
        if s[0] != t[0] or s[1] != t[1]:
            return False
    return True


def main():
    N = NI()
    S = [SI() for _ in range(N)]
    T = [SI() for _ in range(N)]
    S = str_to_01(S)
    T = str_to_01(T)

    S_hws = pick_1_hw(S)
    T_hws = pick_1_hw(T)

    if len(S_hws) != len(T_hws):
        print("No")
        exit()

    T_hws.sort(key=lambda x: (x[0], x[1]))
    for i in range(4):
        S_hws = rotate(S_hws, N)

        dh = T_hws[0][0] - S_hws[0][0]
        dw = T_hws[0][1] - S_hws[0][1]
        SS = shift(S_hws, dh, dw)
        if check(SS, T_hws):
            print("Yes")
            exit()

    print("No")


if __name__ == "__main__":
    main()
