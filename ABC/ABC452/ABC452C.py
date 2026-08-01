import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.set_int_max_str_digits(10**6)
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
    N = NI()
    AB = EI(N)
    M = NI()
    S = [SI() for _ in range(M)]
    # i番目の骨の文字がcであるものが存在するか
    OKs = [[0]*26 for _ in range(N)]
    for i, (a, b) in enumerate(AB):
        for c in range(26):
            for s in S:
                if len(s) == a and ord(s[b-1]) - ord("a") == c:
                    OKs[i][c] = 1
    for s in S:
        if len(s) != N:
            print("No")
            continue
        ok = True
        for i, ss in enumerate(s):
            c = ord(ss) - ord("a")
            if OKs[i][c] == 0:
                ok = False
        if ok:
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    main()
