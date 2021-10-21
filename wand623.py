import sys
import math
from collections import defaultdict
from collections import deque
from itertools import permutations

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


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

prime_table = make_prime_table(100010)
P = [p for i, p in enumerate(prime_table) if i == p and len(str(p)) == len(set(str(p)))]

def check(N):
    N = str(N)
    if len(set(N)) != 9:
        return False
    if "4" in N:
        return False
    if N.count("8") != 2:
        return False

    return True


def factorize(n):
    full = set("0123456789")
    used = set()
    used_ = []
    now = n
    for p in P:
        if now == 1:
            break

        if now % p:
            continue
        if used & set(str(p)):
            return False, used_
        used |= set(str(p))
        used_.append(p)
        now //= p

        if now % p == 0:
            return False, used_

    if now <= 10**5:
        return False, used_

    elif now != 1:
        used_.append(now)
        now = set(str(now))
        if len(str(now)) != len(set(str(now))):
            return False, used_
        elif used & now:
            return False, used_
        elif (used | now) & full == full:
            return n, used_
        else:
            return False, used_

    else:
        if used == full:
            return n, used_
        else:
            return False, used_


def main():
    print(len(P))
    print(P)
    perm = permutations("0123567889", 10)
    for n in perm:
        n = int("".join(n))
        res, used = factorize(n)
        if res:
            print(res, used)


if __name__ == "__main__":
    main()
