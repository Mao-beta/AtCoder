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
    N, K = NMI()
    seen_s = {N}
    seen = [N]
    start, end = None, None
    for i in range(1, 100002):
        x = seen[-1]
        s = sum([int(xx) for xx in str(x)])
        x = (x + s) % 100000
        seen.append(x)
        if start is None and x in seen_s:
            start = seen.index(x)
            end = i
        seen_s.add(x)

    cycle = end - start
    if K <= 100000:
        print(seen[K])
        exit()

    rem = (K - start) % cycle
    print(seen[start + rem])



if __name__ == "__main__":
    main()
