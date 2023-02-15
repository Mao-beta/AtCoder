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


def main():
    B = [SI() for _ in range(19)]
    black = 0
    white = 0
    for row in B:
        black += row.count("o")
        white += row.count("x")
    
    if white + 1 < black or black < white:
        print("NO")
        exit()
    
    if black == white:
        last = "white"
    else:
        last = "black"
    
    N = 19
    DH = [1, 1, 1, 0]
    DW = [-1, 0, 1, 1]
    
    res = [[0]*N for _ in range(N)]
    
    def check(h, w, dh, dw, t):
        nt = 0
        for i in range(5):
            nh = h + dh * i
            nw = w + dw * i
            if nh < 0 or nh >= N or nw < 0 or nw >= N:
                return False
            if B[nh][nw] == t:
                nt += 1
        
        if nt < 5:
            return False
        
        for i in range(5):
            nh = h + dh * i
            nw = w + dw * i
            res[nh][nw] += 1
        
        return True
        
    bline = 0
    wline = 0
    for h in range(N):
        for w in range(N):
            for dh, dw in zip(DH, DW):
                bline += int(check(h, w, dh, dw, "o"))
                wline += int(check(h, w, dh, dw, "x"))

    if last == "white" and bline > 0:
        print("NO")
        exit()
    if last == "black" and wline > 0:
        print("NO")
        exit()
    if bline == 0 and wline == 0:
        print("YES")
        exit()

    M = 0
    for row in res:
        M = max(M, max(row))

    if M == max(bline, wline):
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
