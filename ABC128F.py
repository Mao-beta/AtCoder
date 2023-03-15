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


# 約数列挙（単体）
def divisors(x):
    res = set()
    for i in range(1, int(x**0.5) + 2):
        if x % i == 0:
            res.add(i)
            res.add(x//i)
    return res


def main():
    N = NI()
    S = NLI()
    
    # C[d][k]: 前からdずつk回飛んだ時の総和
    C = [[0] for _ in range(N)]
    # R[d][k]: 後ろからdずつk回飛んだ時の総和
    R = [[0] for _ in range(N)]

    # Σ(N//d)は調和級数O(NlogN)
    for d in range(1, N):
        for i in range(d, N, d):
            C[d].append(C[d][-1] + S[i])
        for i in range(N-1-d, -1, -d):
            R[d].append(R[d][-1] + S[i])

    ans = 0 # A == N-1は自明
    for A in range(N-1):
        # 一回の約数列挙にO(√N)なので計O(N√N)
        D = divisors(N-1-A)
        # 約数の個数は多くても30個くらい
        for d in D:
            # d == A - B
            # 踏む地点は最終的に
            # 0, d, 2d, ..., kd, A, A+d, ..., A+kd(=N-1)
            # つまり C[d][k]+R[d][k]
            B = A - d
            if B <= 0 or B >= A:
                continue
            # dずつ前から飛んでN-1より先に座標Aに着くようなケースはダメ
            if A % d == 0 and N-1 >= 2*A:
                continue
            k = (N-1-A) // d
            ans = max(ans, C[d][k] + R[d][k])

    print(ans)


if __name__ == "__main__":
    main()
