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


def same_prefix(S, T):
    # SのprefixがTのprefixに何文字一致しているか
    N = len(S)
    si = 0
    for ti, t in enumerate(T):
        if S[si] == t:
            si += 1
        else:
            break
        if si >= N:
            break
    return si


def main():
    N, T = SMI()
    N = int(N)
    S = [SI() for _ in range(N)]
    M = len(T)
    R = T[::-1]
    ans = []
    for i, s in enumerate(S, start=1):
        pre = same_prefix(s, T)
        post = same_prefix(s[::-1], R)
        sn = len(s)
        if sn == M:
            if pre + post >= M-1:
                ans.append(i)
        elif sn == M-1:
            if pre + post >= M-1:
                ans.append(i)
        elif sn == M+1:
            if pre + post >= M:
                ans.append(i)

    print(len(ans))
    print(*ans)



if __name__ == "__main__":
    main()
