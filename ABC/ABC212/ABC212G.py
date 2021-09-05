import sys
import math
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 998244353
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


# Nの素因数分解を辞書で返す(単体)
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


def divisors(n):
    res = set()
    for i in range(1, int(n**0.5)+2):
        if n % i == 0:
            res.add(i)
            res.add(n//i)
    return res


def euler(n):
    res = n
    fac = prime_fact(n)
    for p, k in fac.items():
        res = res * (p-1) // p
    return res


def main():
    N = NI()
    divs = divisors(N-1)
    ans = 1
    for div in divs:
        ans += div * euler(div)
        ans %= MOD
    print(ans)


if __name__ == "__main__":
    main()
