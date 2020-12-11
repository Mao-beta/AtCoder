import sys
import math
from collections import defaultdict
from collections import deque

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    X, Y = NMI()

    if Y == 0:
        print("ERROR")
        exit()
    if X == 0:
        print("0.00")
        exit()

    ans = str(math.floor(100*X/Y))
    ans = ans[:-2] + "." + ans[-2:]
    if ans[0] == ".":
        print("0"+ans)
    else:
        print(ans)

    



if __name__ == "__main__":
    main()
