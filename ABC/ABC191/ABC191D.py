import sys
import math
from collections import defaultdict
from collections import deque
import time

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


def main():
    X, Y, R = SI().split()

    def convert_to_int(n):
        if "." in n:
            idx = n.index(".")
            keta = len(n) - 1 - idx
            n2 = n[:idx] + n[idx+1:]
            n2 = int(n2) * 10**(4-keta)
        else:
            n2 = int(n) * 10**4
        return n2

    X2 = convert_to_int(X)
    Y2 = convert_to_int(Y)
    R2 = convert_to_int(R)

    def my_sqrt(n):
        base = time.time()
        ok = int(math.sqrt(n)*0.5)
        ng = int(math.sqrt(n)*1.5)
        cnt = 0
        while abs(ok-ng) > 1:
            mid = (ok+ng) // 2
            if mid**2 <= n:
                ok = mid
            else:
                ng = mid
            cnt += 1
        t = time.time() - base
        return ok, t

    #print(my_sqrt(10**9))

    l = (X2 - R2 - 1) // 10000 + 1
    r = (X2 + R2) // 10000
    ans = 0
    total = 0
    root = R2**2 - (10000*l - X2)**2
    for x in range(l, r+1):

        gap, t = my_sqrt(root)
        #gap, t = math.sqrt(root), 0
        total += t
        M = Y2 + gap
        m = Y2 - gap
        M = M // 10000
        if m % 10000:
            m = m // 10000 + 1
        else:
            m = m // 10000
        ans += (M - m + 1)
        root += 20000 * X2 - 2*10**8 * x - 10**8

    print(int(ans))
    #print(total)


if __name__ == "__main__":
    main()
