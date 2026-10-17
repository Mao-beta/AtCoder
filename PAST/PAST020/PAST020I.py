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
    A = NLI() + NLI()
    A = [x-1 for x in A]

    D = {P:i for i, P in enumerate(permutations(list(range(8))))}
    # h1*4+w1, h2*4+w2
    Swap = [[0,1], [1,2], [2,3], [4,5], [5,6], [6,7], [0,4], [1,5], [2,6], [3,7]]

    que = deque()
    steps = defaultdict(lambda: -1)
    steps[tuple(range(8))] = 0
    que.append(list(range(8)))
    while que:
        X = que.popleft()
        step = steps[tuple(X)]
        if X == A:
            print(step)
            return
        for hw1, hw2 in Swap:
            Y = X[:]
            Y[hw1], Y[hw2] = Y[hw2], Y[hw1]
            if steps[tuple(Y)] == -1:
                steps[tuple(Y)] = step+1
                que.append(Y)


if __name__ == "__main__":
    main()
