import sys
import math
from collections import defaultdict
from collections import deque
from collections import Counter

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    N = NI()
    S = [SI() for _ in range(N)]
    C = Counter(S).most_common()
    C.sort(key=lambda x: (-x[1], (x[0])))
    max_n = C[0][1]
    for c, num in C:
        if num != max_n:
            break
        print(c)


if __name__ == "__main__":
    main()
