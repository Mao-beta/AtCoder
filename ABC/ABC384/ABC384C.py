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
    P = NLI()
    ans = []
    for case in range(1, 32):
        tmp = 0
        name = []
        for i in range(5):
            if (case >> i) & 1:
                name.append("ABCDE"[i])
                tmp += P[i]
        ans.append([tmp, "".join(name)])
    ans.sort(key=lambda x: (-x[0], x[1]))
    for p, name in ans:
        print(name)


if __name__ == "__main__":
    main()
