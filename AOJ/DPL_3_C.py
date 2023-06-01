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


def largest_rectangle_in_histogram(_H: list) -> int:
    """
    ヒストグラム内の最大長方形の面積 stack使用でO(N)
    """
    from collections import deque
    H = _H.copy()
    H.append(0)
    res = 0
    D = deque()
    # i, h
    D.append([0, 0])
    for i, h in enumerate(H):
        li = i
        while D[-1][1] > h:
            li, lh = D.pop()
            res = max(res, (i-li)*lh)
        D.append([li, h])

    return res


def main():
    N = NI()
    H = NLI()
    ans = largest_rectangle_in_histogram(H)
    print(ans)


if __name__ == "__main__":
    main()
