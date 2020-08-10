import sys
import math
from collections import defaultdict

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def make_grid(h, w, num): return [[int(num)] * w for _ in range(h)]


def main():
    N = NI()
    A = [SI() for _ in range(N)]
    B = defaultdict(list)
    for a in A:
        if a.count(".") != 1:
            B[int(a)].append(1)
            continue
        ba, bb = a.split(".")
        ba = int(ba+bb)
        bb = 10**len(bb)
        g = math.gcd(ba, bb)
        ba //= g
        bb //= g
        B[ba].append(bb)

    facts = defaultdict(int)
    for ba, bbs in B.items():
        tmp = ba
        ba_fac_2 = 0
        while True:
            if tmp % 2: break
            ba_fac_2 += 1
            tmp //= 2
        tmp = ba
        ba_fac_5 = 0
        while True:
            if tmp % 5: break
            ba_fac_5 += 1
            tmp //= 5

        for bb in bbs:
            tmp = bb
            bb_fac_2 = 0
            while True:
                if tmp % 2: break
                bb_fac_2 += 1
                tmp //= 2
            tmp = bb
            bb_fac_5 = 0
            while True:
                if tmp % 5: break
                bb_fac_5 += 1
                tmp //= 5
            facts[(ba_fac_2 - bb_fac_2, ba_fac_5 - bb_fac_5)] += 1

    ans = 0
    for fact, k in list(facts.items()):

        fac2, fac5 = fact
        for i in range(-fac2, 50):
            for j in range(-fac5, 20):
                if fac2 == i and fac5 == j:
                    ans += k * (k-1)
                else:
                    ans += k * facts[(i, j)]


    print(ans//2)


if __name__ == "__main__":
    main()