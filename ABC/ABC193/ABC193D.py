import sys
import math
from collections import Counter

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def make_grid(h, w, num): return [[int(num)] * w for _ in range(h)]


def main():
    K = NI()
    S = SI()
    T = SI()
    S_card = Counter(S[:-1])
    T_card = Counter(T[:-1])
    total_card = Counter(S[:-1]) + Counter(T[:-1])
    total_case = 0
    taka_case = 0
    for p in range(1, 10):
        for q in range(1, 10):
            if p == q and total_card[str(p)] >= K-1:
                continue
            elif total_card[str(p)] >= K or total_card[str(q)] >= K:
                continue

            now_S_card = S_card.copy()
            now_S_card[str(p)] = now_S_card.get(str(p), 0) + 1
            now_T_card = T_card.copy()
            now_T_card[str(q)] = now_T_card.get(str(q), 0) + 1

            base = total_case
            if p != q:
                total_case += (K - total_card[str(p)]) * (K - total_card[str(q)])
            else:
                total_case += (K - total_card[str(p)]) * (K - total_card[str(p)] - 1)
            #print(total_case - base)

            #print(now_S_card)
            #print(now_T_card)
            sp = 0
            for card, n in now_S_card.items():
                card = int(card)
                sp += (10**n-1) * card

            tp = 0
            for card, n in now_T_card.items():
                card = int(card)
                tp += (10**n-1) * card

            #print(p, q, sp, tp)
            if sp > tp:

                if p != q:
                    taka_case += (K - total_card[str(p)]) * (K - total_card[str(q)])
                else:
                    taka_case += (K - total_card[str(p)]) * (K - total_card[str(p)] - 1)

    #print(taka_case, total_case)
    print(taka_case / total_case)



if __name__ == "__main__":
    main()
