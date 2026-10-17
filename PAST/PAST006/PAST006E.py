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
    N = NI()
    S = SI()
    A = deque()

    dic = {"A": [1, 0], "B": [2, 0], "C": [3, 0],
           "D": [1, 1], "E": [2, 1], "F": [3, 1]}

    for i, s in enumerate(S, start=1):

        if s == "L":
            A.appendleft(i)
        elif s == "R":
            A.append(i)
        else:
            k, is_r = dic[s]
            if len(A) < k:
                print("ERROR")
                continue
            tmp = deque()
            for _ in range(k):
                if is_r:
                    tmp.append(A.pop())
                else:
                    tmp.append(A.popleft())
            print(tmp.pop())
            for _ in range(k-1):
                if is_r:
                    A.append(tmp.pop())
                else:
                    A.appendleft(tmp.pop())



if __name__ == "__main__":
    main()
