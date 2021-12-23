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


# アルファベットと数字の対応
alp_to_num = {chr(i+97): i for i in range(26)}
ALP_to_num = {chr(i+97).upper(): i for i in range(26)}
num_to_alp = {i: chr(i+97) for i in range(26)}
num_to_ALP = {i: chr(i+97).upper() for i in range(26)}

alp = set(alp_to_num.keys())
ALP = set(ALP_to_num.keys())
num = set("0123456789")

def main():
    S = SI()

    state = None
    NW = []

    if len(set(S)) == 1 and S[0] == "_":
        print(S)
        exit()

    f = 0
    b = 0
    for s in S:
        if s == "_":
            f += 1
        else:
            break
    for s in S[::-1]:
        if s == "_":
            b += 1
        else:
            break

    if b == 0:
        SS = S[f:]
    else:
        SS = S[f:-b]
    if "__" in SS:
        print(S)
        exit()

    if SS.count("_") == 0:
        if SS[0] in num or SS[0] in ALP:
            print(S)
            exit()

        now = ""
        for s in SS:
            if s.isupper():
                NW.append(now.lower())
                now = s
            else:
                now += s
        if now:
            NW.append(now.lower())

        print("_" * f + "_".join(NW) + "_" * b)
        exit()


    W = SS.split("_")

    for w in W:
        if not w:
            continue

        if w[0] in num:
            print(S)
            exit()

        if w.lower() == w:
            if state == "C":
                print(S)
                exit()
            else:
                state = "L"
                NW.append(w.capitalize())

        elif w.capitalize() == w:
            if state == "L":
                print(S)
                exit()
            else:
                state = "C"
                NW.append(w.lower())

        else:
            print(S)
            exit()


    if state == "C":
        ans = "_".join(NW)
        ans = "_" * f + ans + "_" * b
        print(ans)

    elif state == "L":
        NW[0] = NW[0].lower()
        ans = "".join(NW)
        ans = "_" * f + ans + "_" * b
        print(ans)




if __name__ == "__main__":
    main()
