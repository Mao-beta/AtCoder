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


def solve(N, _A):
    A = [x - 1 for x in _A]
    Ls = [-1] * N
    ans = 0
    for i, a in enumerate(A):
        if Ls[a] == -1:
            Ls[a] = i
        elif Ls[a] == i - 1:
            continue
        else:
            x = A[i - 1]
            lx = Ls[x]
            if lx != -1 and lx != i-1 and abs(i - 1 - lx) != 1 and abs(lx - Ls[a]) == 1:
                # print(
                #     f"i={i}, a={a}, x={x}, lx={lx}, Ls[x]={Ls[x]}, Ls[a]={Ls[a]}")
                ans += 1
            if i < 2 * N - 1:
                x = A[i + 1]
                lx = Ls[x]
                if lx != -1 and lx != i+1 and abs(i + 1 - lx) != 1 and abs(lx - Ls[a]) == 1:
                    # print(
                    #     f"i={i}, a={a}, x={x}, lx={lx}, Ls[x]={Ls[x]}, Ls[a]={Ls[a]}")
                    ans += 1
    return ans // 2

def main():
    T = NI()
    for _ in range(T):
        N = NI()
        A = NLI()
        ans = solve(N, A)
        print(ans)


def guchoku(N, _A):
    A = [x-1 for x in _A]
    ans = 0
    for a in range(N):
        for b in range(a+1, N):
            al, ar, bl, br = -1, -1, -1, -1
            for i, x in enumerate(A):
                if x == a:
                    if al == -1:
                        al = i
                    else:
                        ar = i
                if x == b:
                    if bl == -1:
                        bl = i
                    else:
                        br = i
            if abs(al-ar) == 1 or abs(bl-br) == 1:
                continue
            if abs(al-bl) == 1 and abs(ar-br) == 1:
                ans += 1
    return ans


def debug():
    from random import shuffle
    for _ in range(100):
        print("##")
        N = 4
        A = list(range(1, N+1)) * 2
        shuffle(A)
        ans = solve(N, A)
        gu = guchoku(N, A)
        assert ans == gu, (ans, gu, [a-1 for a in A])


if __name__ == "__main__":
    main()
