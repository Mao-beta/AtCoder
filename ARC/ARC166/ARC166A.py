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
EI = lambda m: [NLI() for _ in range(m)]


def solve(N, X, Y):
    X += "C"
    Y += "C"

    words = []
    now_x = []
    now_y = []
    for xx, yy in zip(X, Y):
        if yy == "C":
            if xx != "C":
                return False
            else:
                words.append([now_x[:], now_y[:]])
                now_x = []
                now_y = []

        else:
            now_x.append(xx)
            now_y.append(yy)

    for wx, wy in words:
        ya = wy.count("A")
        yb = wy.count("B")
        xa = wx.count("A")
        xb = wx.count("B")
        xc = wx.count("C")
        ctoa = ya - xa
        ctob = yb - xb
        if ctoa < 0 or ctob < 0 or ctoa + ctob != xc:
            return False

        for i in range(len(wx)):
            if wx[i] == "C":
                if ctoa > 0:
                    wx[i] = "A"
                    ctoa -= 1
                else:
                    wx[i] = "B"

        num = 0
        for x, y in zip(wx, wy):
            if x == "A" and y == "B":
                num += 1
            elif x == "B" and y == "A":
                num -= 1
            if num < 0:
                return False
    
    return True


def main():
    T = NI()
    for _ in range(T):
        N, X, Y = SMI()
        N = int(N)
        ans = solve(N, X, Y)
        if ans:
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    main()
