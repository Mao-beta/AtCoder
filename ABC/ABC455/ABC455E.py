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
    S = SI()
    AB = Counter()
    BC = Counter()
    CA = Counter()
    ABC = Counter()
    ab, bc, ca, abc = 0, 0, 0, [0, 0]
    AB[0] += 1
    BC[0] += 1
    CA[0] += 1
    ABC[tuple(abc)] += 1
    for s in S:
        if s == "A":
            ab += 1
            ca -= 1
            abc[0] += 1
        elif s == "B":
            ab -= 1
            bc += 1
            abc[1] += 1
        else:
            bc -= 1
            ca += 1
            abc[0] -= 1
            abc[1] -= 1
        AB[ab] += 1
        BC[bc] += 1
        CA[ca] += 1
        ABC[tuple(abc)] += 1
    ans = N*(N+1)//2
    for v in AB.values():
        ans -= v*(v-1)//2
    for v in BC.values():
        ans -= v*(v-1)//2
    for v in CA.values():
        ans -= v*(v-1)//2
    for v in ABC.values():
        ans += v*(v-1)
    print(ans)
    # print(AB, BC, CA, ABC)


if __name__ == "__main__":
    main()
