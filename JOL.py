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


def main():
    S = ["aa", "aa luaa", "aa mea", "aauu asi", "bini vaa", "keel",
         "keel maa", "laavang", "laavang asi", "laavang ila", "laavang vaa",
         "mooi", "mooi maa", "mooi silba", "silba", "vate", "vate ila", "vate luaa"]

    W = []
    for s in S:
        for ss in s.split():
            W.append(ss)

    C = Counter(W)
    for key, k in C.most_common():
        print(key, k)



if __name__ == "__main__":
    main()
