import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache, cmp_to_key
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


def comp(x, y):
    xy, yx = x+y, y+x
    if xy == yx:
        return 0
    elif xy < yx:
        return 1
    else:
        return -1


def main():
    N, K = NMI()
    S = [SI() for _ in range(N)]
    S = sorted(S, key=lambda x: (len(x), int(x)), reverse=True)
    m = max(S[K-1:], key=lambda x: int(x))
    ans1 = "".join(sorted(S[:K], key=cmp_to_key(comp)))
    ans2 = "".join(sorted([m] + S[:K-1], key=cmp_to_key(comp)))
    ans = max(int(ans1), int(ans2))
    # print(S)
    # print(ans1, ans2)
    print(ans)


if __name__ == "__main__":
    main()
