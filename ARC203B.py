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
        if solve(N, A, B):
            print("Yes")
        else:
            print("No")


def solve(N, A, B):
    if sum(A) != sum(B):
        return False
    elif A == B:
        return True
    elif sum(A) == 1:
        if A[0] == 0 and A[-1] == 0 and B[0] == 0 and B[-1] == 0:
            return True
        else:
            return False
    else:
        return True


def guchoku(N, A, B):
    seen = set()
    seen.add("".join(map(str, A)))
    que = deque()
    que.append(A[:])
    while que:
        A = que.popleft()
        for P in combinations(range(1, N+3), 4):
            P = [P[0]-1, P[1]-1, P[2]-2, P[3]-2]
            if sum(A[P[0]:P[1]]) != sum(A[P[2]:P[3]]):
                continue
            X = A[:P[0]] + A[P[2]:P[3]] + A[P[1]:P[2]] + A[P[0]:P[1]] + A[P[3]:]
            if "".join(map(str, X)) not in seen:
                seen.add("".join(map(str, X)))
                que.append(X)
    # print(sorted(list(seen)))
    return "".join(map(str, B)) in seen


if __name__ == "__main__":

    main()
    exit()

    N = 5
    for A in product([0, 1], repeat=N):
        for B in product([0, 1], repeat=N):
            if sum(A) != sum(B):
                continue

            gu = guchoku(N, A, B)
            ans = solve(N, A, B)
            if gu != ans:
                print(A, B)
                print(gu, ans)

