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
    A = NLI()
    ans = [0]
    A.sort()
    idx = 0
    for k in range(max(A)):
        while idx < N and k >= A[idx]:
            idx += 1
        ans[k] += N - idx
        x, r = divmod(ans[k], 10)
        ans.append(x)
        ans[k] = r
    while ans[-1] == 0:
        ans.pop()
    while ans[-1] >= 10:
        x, r = divmod(ans[-1], 10)
        ans[-1] = r
        ans.append(x)
    ans = ans[::-1]
    print(*ans, sep="")


if __name__ == "__main__":
    main()
