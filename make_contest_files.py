import shutil
import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
MOD99 = 998244353

NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()
SMI = lambda: input().split()
SLI = lambda: list(SMI())
EI = lambda m: [NLI() for _ in range(m)]


def main():
    contest_name = input("input contest name: ")
    num = int(input("input number of problems: "))
    S = [chr(ord("A") + i) for i in range(num)]
    check = input(f"Do you make {contest_name}{S[0]} ~ {contest_name}{S[-1]}? (Y/else): ")
    check = check.lower()
    if check == "y":
        for s in S:
            shutil.copy("./atcoder_template.py", f"./{contest_name}{s}.py")
    else:
        print("canceled.")


if __name__ == "__main__":
    main()
