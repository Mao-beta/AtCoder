import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.set_int_max_str_digits(10 ** 6)
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
    T, A, B = NMI()

    if T < max(A, B):
        print("NO")
        return

    if A == B == 0:
        if T == 1:
            print("NO")
            return
        print("YES")
        if T % 2:
            print(">")
            print("^<")
            print("v")
            for _ in range(T//2 - 1):
                print(">")
                print("<")
        else:
            for _ in range(T//2):
                print(">")
                print("<")
        return


    if A >= B:
        ans = []
        for i in range(A-B):
            ans.append("^")
        for i in range(B):
            ans.append("^>")
        if (T - A) % 2:
            x = ans.pop()
            if x == "^":
                ans.append(">")
                ans.append("<^")
            else:
                ans.append(">")
                ans.append("^")
        for i in range((T-A)//2):
            ans.append(">")
            ans.append("<")

    else:
        ans = []
        for i in range(B-A):
            ans.append(">")
        for i in range(A):
            ans.append("^>")
        if (T - B) % 2:
            x = ans.pop()
            if x == ">":
                ans.append("v")
                ans.append(">^")
            else:
                ans.append(">")
                ans.append("^")
        for i in range((T - B) // 2):
            ans.append(">")
            ans.append("<")

    print("YES")
    for s in ans:
        print(s)


if __name__ == "__main__":
    main()
