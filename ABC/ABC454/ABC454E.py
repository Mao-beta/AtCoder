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
        N, A, B = NMI()
        if N % 2:
            print("No")
            continue
        if (A+B) % 2 == 0:
            print("No")
            continue

        if N == 2:
            if A == 1 and B == 2:
                print("Yes")
                print("DR")
            else:
                print("Yes")
                print("RD")
            continue

        rev = False
        if B % 2:
            A, B = B, A
            rev = True
        x, y = 1, 1
        ans = []
        if A > 1:
            k = (A-1) // 2
            for _ in range(k):
                ans.append("R"*(N-1))
                ans.append("D")
                ans.append("L"*(N-1))
                ans.append("D")
            x += 2*k
        if B == N:
            k = (N-1) // 2
            ans.append("DRUR"*k)
            ans.append("DR")
            x = A+1
            y = N
        else:
            k = (B-1) // 2
            ans.append("DRUR"*k)
            ans.append("DRRURD")
            y = B+2
            k = (N-y) // 2
            ans.append("RURD"*k)
            x = A+1
            y = N
        k = (N-x) // 2
        for _ in range(k):
            ans.append("D")
            ans.append("L"*(N-1))
            ans.append("D")
            ans.append("R"*(N-1))
        if rev:
            table = str.maketrans("LURD", "ULDR")
            ans = "".join(ans).translate(table)
        else:
            ans = "".join(ans)
        print("Yes")
        print(ans)


if __name__ == "__main__":
    main()
