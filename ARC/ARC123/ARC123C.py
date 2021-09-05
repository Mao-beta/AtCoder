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
    T = NI()
    for i in range(T):
        X = SI()[::-1]

        ans = 1
        for x in X:
            x = int(x)
            if x not in [1, 2, 3]:
                ans += 1
                break

        if ans == 1:
            print(ans)
            continue

        for x in X:
            x = int(x)
            if x == 0 or x >= 7:
                ans += 1
                break

        if ans == 2:
            print(ans)
            continue

        use = 3
        for x in X:
            x = int(x)
            if use == 3:
                if x == 2:
                    use = 2
                elif x == 1:
                    use = 1
                elif x == 0:
                    ans += 1
                    break
            elif use == 2:
                if x >= 7 or x == 0:
                    ans += 1
                    break
                elif x == 1:
                    use = 1
            else:
                if x == 0 or x >= 4:
                    ans += 1
                    break

        if ans == 3:
            print(ans)
            continue

        print(4)

    SS = [1, 2, 3, 11, 12, 13, 21, 22, 23, 31, 32, 33, 111,112,113,121,122,123,131,132,133,211,212,213,221,222,223,231,232,233,311,312,313,321,322,323,331,332,333]
    ans = set()
    for x in SS:
        ans.add(x)
        for y in SS:
            ans.add(x+y)
            for z in SS:
                ans.add(x+y+z)
                for t in SS:
                    ans.add(x+y+z+t)
    print(sorted(list(ans)))
    for i in range(1, 1111):
        if i not in ans:
            print(i)


if __name__ == "__main__":
    main()
