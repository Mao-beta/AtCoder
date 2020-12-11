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


def next_SW(now, prev, sn):
    notSW = {"S": "W", "W": "S"}
    if now == "S" and sn:
        return prev
    if now == "S" and 1-sn:
        return notSW[prev]
    if now == "W" and sn:
        return notSW[prev]
    if now == "W" and 1-sn:
        return prev


def main():
    N = NI()
    S = SI()
    D = {"o": 1, "x": 0}
    SorW = ["S", "W"]
    S = [D[s] for s in S]
    case = ["SS", "SW", "WS", "WW"]
    for T in case:
        for i in range(1, N):
            now, prev = T[i], T[i-1]
            sn, sp = S[i], S[i-1]
            T += next_SW(now, prev, sn)
        if next_SW(T[0], T[-1], S[0]) == T[1] and T[0] == T[-1]:
            print(T[:-1])
            exit()
    print(-1)





if __name__ == "__main__":
    main()