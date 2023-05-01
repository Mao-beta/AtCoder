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


def print_err(*args):
    print(*args, file=sys.stderr)


def main():
    N = NI()
    A = NLI()
    B = NLI()

    if sorted(A) != sorted(B):
        print("No")
        return

    AA = [i for i, a in enumerate(A) if a % 2]
    BB = [i for i, b in enumerate(B) if b % 2]

    GA = []
    GB = []
    for i in range(len(AA)-1):
        GA.append(AA[i+1] - AA[i])
        GB.append(BB[i+1] - BB[i])

    if len(AA) == 0:
        print("Yes")
        return

    if len(AA) == 1 or min(GA) > 2:
        # 移動不可
        if AA != BB:
            print("No")
            return

        idx = 0
        SA = []
        SB = []
        for x in AA + [N]:
            while idx < x:
                SA.append(A[idx])
                SB.append(B[idx])
                idx += 1

            if sorted(SA) != sorted(SB):
                print("No")
                return

            SA = []
            SB = []
            idx += 1

        print("Yes")
        return

    else:
        if min(GB) > 2:
            print("No")
        else:
            print("Yes")


if __name__ == "__main__":
    main()
