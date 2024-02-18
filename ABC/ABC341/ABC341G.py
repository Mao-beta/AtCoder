import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

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
    C = list(accumulate([0]+A))

    D = []
    D.append([N, C[N]])
    D.append([N-1, C[N-1]])
    ans = [A[-1]]

    for i in range(N-2, -1, -1):
        x, y = i, C[i]
        while len(D) >= 2:
            # P, P1, P2の順で並ぶ
            # P2P1とP1Pの外積で判定
            x1, y1 = D[-1]
            x2, y2 = D[-2]
            if (x1-x2)*(y-y1) - (y1-y2)*(x-x1) < 0:
                D.pop()
            else:
                break
        D.append([i, C[i]])
        ans.append((D[-2][1]-D[-1][1]) / (D[-2][0]-D[-1][0]))

    print(*ans[::-1], sep="\n")



if __name__ == "__main__":
    main()
