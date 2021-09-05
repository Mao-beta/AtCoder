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


def divisors(x):
    res = set()
    for i in range(1, int(x**0.5)+2):
        if x % i == 0:
            res.add(i)
            res.add(x//i)
    return res


def main():
    N = NI()
    AB = [NLI() for _ in range(N)]

    AG = divisors(AB[0][0])
    BG = divisors(AB[0][1])

    ans = 1

    for ag in AG:
        for bg in BG:
            ok = True
            for a, b in AB:
                if (a % ag or b % bg) and (a % bg or b % ag):
                    ok = False
                    break
            if ok:
                ans = max(ans, ag * bg // math.gcd(ag, bg))

    print(ans)




if __name__ == "__main__":
    main()
