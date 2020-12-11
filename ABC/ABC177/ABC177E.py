import sys
import math
import fractions
from collections import deque
from collections import defaultdict

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def make_grid(h, w, num): return [[int(num)] * w for _ in range(h)]


# Nの素因数分解を辞書で返す
def prime_fact(n, ela):
    if n == 1:
        return {1: 1}


    prime_dict = {}
    for i in ela:
        cnt = 0
        while n % i == 0:
            cnt += 1
            n = n // i
        if cnt:
            prime_dict[i] = cnt
        if n == 1:
            break
    if n != 1:
        prime_dict[n] = 1
    return prime_dict


def sieve_of_erastosthenes(num):
    input_list = [False if i % 2 == 0 or i % 3 == 0 or i % 5 == 0 else True for i in range(num)]
    input_list[0] = input_list[1] = False
    input_list[2] = input_list[3] = input_list[5] = True
    sqrt = math.sqrt(num)

    for serial in range(3, num, 2):
        if not input_list[serial]:
            continue

        if serial >= sqrt:
            return input_list

        for s in range(serial ** 2, num, serial):
            input_list[s] = False


def main():
    N = NI()
    A = NLI()
    ela = sieve_of_erastosthenes(1001)
    ela2 = [i for i, b in enumerate(ela) if b]

    if max(A) == 1:
        print("pairwise coprime")
        exit()

    g = A[0]
    for a in A:
        g = math.gcd(g, a)
    if g > 1:
        print("not coprime")
        exit()

    SA = set(A)
    SA.discard(1)
    if len(SA) >= 90000:
        print("setwise coprime")
        exit()

    p_cnt = defaultdict(int)
    PD_list = defaultdict(dict)
    cnt = 0
    for a in A:
        if a == 1:
            continue

        if PD_list[a]:
            AP = PD_list[a]
        else:
            AP = prime_fact(a, ela2)
            PD_list[a] = AP
        for apk in AP.keys():
            p_cnt[apk] += 1

    max_p = max(p_cnt.values())
    if max_p == 1:
        print("pairwise coprime")
    elif max_p == N:
        print("not coprime")
    else:
        print("setwise coprime")



if __name__ == "__main__":
    main()