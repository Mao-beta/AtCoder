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


def main():
    S = SI()
    l = len(S)
    S = S[::-1] + "ppppppp"
    W = ["maerd", "remaerd", "esare", "resare"]
    idx = 0
    while idx < l:
        no_flag = True
        for w in W:
            if S[idx: idx+len(w)] == w:
                idx += len(w)
                no_flag = False

        if no_flag:
            print("NO")
            exit()

    if idx == l:
        print("YES")
    else:
        print("NO")



if __name__ == "__main__":
    main()