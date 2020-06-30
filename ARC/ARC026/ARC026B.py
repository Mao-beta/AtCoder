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


#素因数分解
def prime_fact(n):
    root = int(math.sqrt(n))
    prime_dict = {}
    for i in range(2, root+1):
        cnt = 0
        while n % i == 0:
            cnt += 1
            n = n // i
        if cnt:
            prime_dict[i] = cnt
    if n != 1:
        prime_dict[n] = 1
    return prime_dict


def main():
    N = NI()
    ans = 1
    for p, x in list(prime_fact(N).items()):
        ans *= (p**(x+1)-1) // (p-1)
    ans -= N*2
    if ans > 0:
        print("Abundant")
    elif ans < 0:
        print("Deficient")
    else:
        print("Perfect")


if __name__ == "__main__":
    main()