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


def prime_fact(n):
    root = int(n**0.5) + 1
    prime_dict = {}
    for i in range(2, root):
        cnt = 0
        while n % i == 0:
            cnt += 1
            n = n // i
        if cnt:
            prime_dict[i] = cnt
    if n != 1:
        prime_dict[n] = 1
    return prime_dict


def main():
    N, M = NMI()
    A = NLI()
    P = set()
    for a in A:
        dic = prime_fact(a)
        for p in dic.keys():
            P.add(p)

    is_P = [1] * (M+1)
    is_P[0] = 0
    for p in P:
        for x in range(p, M+1, p):
            is_P[x] = 0

    print(sum(is_P))
    for i, x in enumerate(is_P):
        if x:
            print(i)


if __name__ == "__main__":
    main()
