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
    # X[i]: i回以上割り切れるペアの数
    X = [0] * 33
    X[0] = N * (N-1) // 2
    for k in range(1, 33):
        b = 1<<k
        C = Counter([a % b for a in A])
        for a in A:
            a = a % b
            if (b-a) % b == a:
                X[k] += C[(b-a)%b]-1
            else:
                X[k] += C[(b-a)%b]
        X[k] //= 2
    ans = 0
    for k in range(31):
        ans += (X[k] - X[k+1]) * k
    print(ans)


if __name__ == "__main__":
    main()
