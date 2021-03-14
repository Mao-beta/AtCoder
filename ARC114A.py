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


def make_grid(h, w, num): return [[int(num)] * w for _ in range(h)]


# 高速エラストテネス　sieve[n]はnの最小の素因数
def make_prime_table(n):
    sieve = list(range(n + 1))
    sieve[0] = -1
    sieve[1] = -1
    for i in range(4, n + 1, 2):
        sieve[i] = 2
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i] != i:
            continue
        for j in range(i * i, n + 1, i * 2):
            if sieve[j] == j:
                sieve[j] = i
    return sieve

prime_table = make_prime_table(50)

# 素因数分解　上のprime_tableと組み合わせて使う
def prime_factorize(n):
    result = []
    while n != 1:
        p = prime_table[n]
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        result.append((p, e))
    return result


def main():
    N = NI()
    X = NLI()

    P = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    bits = []
    for x in X:
        b = 0
        for i, p in enumerate(P):
            if x % p == 0:
                b += 1 << i
        bits.append(b)

    pn = len(P)
    ans = 10**20
    for case in range(1<<pn):
        flag = True
        for b in bits:
            if b & case == 0:
                flag = False

        if flag:
            tmp = 1
            for i, p in enumerate(P):
                if (case>>i) & 1:
                    tmp *= p
                if tmp > ans:
                    flag = False
                    break
        if flag:
            ans = min(ans, tmp)

    print(ans)


if __name__ == "__main__":
    main()
