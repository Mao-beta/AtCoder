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

import time
def main(N, A, B):
    if sum(A) != sum(B):
        print("No")
        return
    if A == B:
        print("Yes")
        print(0)
        return
    if N == 2:
        if A[1]-1 == B[0] or A[0]+1 == B[1]:
            print("Yes")
            print(1)
            print(1, 2)
        else:
            print("No")
        return


    def swap(i, j):
        A[i], A[j] = A[j]-1, A[i]+1
        ans.append([i+1, j+1])

    def exchange(i, j):
        swap(i, 2)
        swap(j, 2)
        swap(i, 2)


    ans = []
    for i in range(N-1, 1, -1):
        b = B[i]
        if A[i] == b:
            continue
        if A[i] > b:
            now = i
            while A[now] >= b:
                if now >= 1:
                    swap(now-1, now)
                    now -= 1
                else:
                    swap(now, i)
                    now = i
            swap(now, i)
        else:
            now = i
            while A[now] < b-1:
                if now < i:
                    swap(now, now+1)
                    now += 1
                else:
                    swap(0, now)
                    now = 0

            if now != i:
                swap(now, i)
            else:
                swap(now-2, now)
                now -= 2
                swap(now, now+1)
                now += 1
                swap(now, now+1)
                now += 1

    if abs(A[1]-A[0]) > abs(B[1]-B[0]):
        while A[1] != B[1]:
            # print(A, B)
            if A[0] > A[1]:
                exchange(0, 1)
            if A[1] == B[1]:
                break
            if A[0] == B[1]:
                exchange(0, 1)
                break
            swap(0, 1)
            if A[1] == B[1]:
                break
            if A[0] == B[1]:
                exchange(0, 1)
                break
    else:
        while A[1] != B[1]:
            # print(A, B)
            if A[0] < A[1]:
                exchange(0, 1)
            if A[1] == B[1]:
                break
            if A[0] == B[1]:
                exchange(0, 1)
                break
            swap(0, 1)
            if A[1] == B[1]:
                break
            if A[0] == B[1]:
                exchange(0, 1)
                break

    print("Yes")
    print(len(ans))
    for a in ans:
        print(*a)



if __name__ == "__main__":
    N = NI()
    A = NLI()
    B = NLI()
    main(N, A, B)

