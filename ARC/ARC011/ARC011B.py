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


def main():
    N = NI()
    W = SLI()
    DD = ["zr", "bc", "dw", "tj", "fq", "lv", "sx", "pm", "hk", "ng"]
    D = defaultdict(str)
    for i, S in enumerate(DD):
        for s in S:
            D[s] = str(i)

    ans = []
    for word in W:
        word = word.lower()
        w = []
        for s in word:
            w.append(D[s])
        w = "".join(w)
        if w:
            ans.append(w)

    print(*ans)


if __name__ == "__main__":
    main()
