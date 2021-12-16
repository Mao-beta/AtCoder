import sys
import math
from collections import deque

sys.setrecursionlimit(100000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def divisors(x):
    res = set()
    for i in range(1, int(x**0.5) + 2):
        if x % i == 0:
            res.add(i)
            res.add(x//i)
    return res


def main():
    K = NI()
    D = divisors(K)
    SD = sorted(list(D))
    l = len(SD)
    ans = 0
    for i in range(l):
        for j in range(i, l):
            a = SD[i]
            b = SD[j]
            if K % (a*b): continue

            c = K // a // b
            if c >= b:
                ans += 1
    print(ans)



if __name__ == "__main__":
    main()
