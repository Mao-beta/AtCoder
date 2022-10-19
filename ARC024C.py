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


def main():
    N, K = NMI()
    S = SI()
    S = [ord(s) - ord("a") for s in S]

    def make_hash(b, m):
        P = [pow(b, i, m) for i in range(26)]
        H = []
        nums = [0] * 26
        D = deque()
        for s in S:
            D.append(s)
            nums[s] += 1
            while len(D) > K:
                x = D.popleft()
                nums[x] -= 1

            if len(D) < K:
                continue
            # print(D)
            h = 0
            for i in range(26):
                h += nums[i] * P[i] % m
                h %= m
            H.append(h)
        return H


    H1 = make_hash(37, MOD99)
    H2 = make_hash(41, MOD)

    use = set()
    for i in range(K, len(H1)):
        use.add((H1[i-K], H2[i-K]))
        if (H1[i], H2[i]) in use:
            print("YES")
            exit()

    print("NO")





if __name__ == "__main__":
    main()
