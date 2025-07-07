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
    T = NI()
    for _ in range(T):
        N = NI()
        A = NLI()
        B = NLI()
        if N == 1:
            print("No")
        else:
            ok = []
            for i in range(N):
                c = A[i] * B[(i+1)%N] - A[(i+1)%N] * B[i]
                if c != 0:
                    ok.append([i, (i+1)%N])
                    break
            if not ok:
                print("No")
            else:
                dot = sum([a*b for a, b in zip(A, B)])
                if dot < 0:
                    print("Yes")
                    print(*A)
                    continue
                i, j = ok[0]
                X = [0] * N
                X[i] = -A[j] - B[j]
                X[j] = A[i] + B[i]
                if X[i] * A[i] + X[j] * A[j] > 0 and X[i] * B[i] + X[j] * B[j] < 0:
                    print("Yes")
                    print(*X)
                    continue
                X[i] = A[j] + B[j]
                X[j] = -A[i] - B[i]
                if X[i] * A[i] + X[j] * A[j] > 0 and X[i] * B[i] + X[j] * B[j] < 0:
                    print("Yes")
                    print(*X)
                    continue
                print("No")



if __name__ == "__main__":
    main()
