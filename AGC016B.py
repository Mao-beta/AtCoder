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


def check(N, K, S):
    # N匹いてK色ある、うち単色がS種類の状況があるか？
    if N < K or N < S or K < S: return False
    R = N - S
    RC = K - S
    # R匹のうち単色でないRC色それぞれに2匹以上いなければFalse
    # print(R, RC)

    if R > 0 and RC == 0: return False
    if R < RC * 2: return False
    return True


def main():
    N = NI()
    A = NLI()
    C = Counter(A)

    # 実際はK種類あるとする
    # 1匹のみの色があれば、その色の猫はK-1と言う
    # そうでなければKと言う

    if max(A) - min(A) >= 2:
        print("No")
        exit()

    if max(A) - min(A) == 1:
        K = max(A)
        S = C[K-1]
        if check(N, K, S):
            print("Yes")
        else:
            print("No")
        exit()

    K = max(A)
    S = C[K-1]
    if check(N, K, S):
        print("Yes")
        exit()

    K = max(A) + 1
    S = C[K-1]
    if check(N, K, S):
        print("Yes")
        exit()

    print("No")


if __name__ == "__main__":
    main()
