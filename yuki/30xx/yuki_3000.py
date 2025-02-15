import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.set_int_max_str_digits(10 ** 6)
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
    S = SI()
    D = {}
    alphabets = set("abcdefghijklmnopqrstuvwxyz")
    for s, t in zip("pfnovu", "orange"):
        D[s] = t
        alphabets.discard(t)
    for s, t in zip("axqwuf", "cipher"):
        D[s] = t
        alphabets.discard(t)
    for s, t in zip("mbgrihcdejkolsty", "bqsuftlmdxynzvwj"):
        D[s] = t
        alphabets.discard(t)
    D["z"] = alphabets.pop()
    T = [D[s] for s in S]
    print("".join(T))


if __name__ == "__main__":
    main()
