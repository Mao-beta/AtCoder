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
    N = NI()
    S = set(SI() for _ in range(N))

    def check(name):
        if name[-1] not in "aiueo":
            return False
        for i in range(len(name)-1):
            if name[i] in "aiueo":
                continue
            if name[i+1] not in "aiueo":
                return False
        return True

    for P in permutations("inabameguru"):
        if check(P) and "".join(P) not in S:
            print("".join(P))
            return

    print("NO")


if __name__ == "__main__":
    main()
