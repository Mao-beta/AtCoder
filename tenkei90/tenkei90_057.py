import sys
import math
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    N, M = NMI()
    A = []
    for _ in range(N):
        T = NI()
        tmp = NLI()
        a = 0
        for x in tmp:
            a |= 1 << (M-x)
        A.append(a)
    S = NLI()
    Sb = 0
    for i, s in enumerate(S):
        if s:
            Sb |= 1 << (M-1-i)

    for i in range(N):
        A.sort(reverse=True)
        base = A[i]
        for j in range(i+1, N):
            other = A[j]
            if M-1-i < 0: continue
            if (base >> (M-1-i)) & (other >> (M-1-i)):
                other ^= base
                A[j] = other
    A.sort(reverse=True)

    flag = 0
    for a in A:
        flag |= a

    for a in A:
        k = len(bin(a))-3
        if (Sb & a) >> k:
            Sb ^= a
        if Sb == 0:
            num = sum([1 if a == 0 else 0 for a in A])
            print(pow(2, num, 998244353))
            exit()

    if Sb:
        print(0)



if __name__ == "__main__":
    main()
