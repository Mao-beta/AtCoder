import sys
import math
import bisect
from heapq import heapify, heappop, heappush
from collections import deque, defaultdict, Counter
from functools import lru_cache
from itertools import accumulate, combinations, permutations

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
MOD99 = 998244353

input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()
SMI = lambda: input().split()
SLI = lambda: list(SMI())


# ACL for Python
class string:
    def z_algorithm(s):
        """
        文字列が与えられた時、各 i について
        「S と S[i:] の最長共通接頭辞の長さ」
        を記録した配列 A を O(|S|) で構築する
        """
        n=len(s)
        if n==0:
            return []
        z=[0]*n
        i=1;j=0
        while(i<n):
            z[i]=0 if (j+z[j]<=i) else min(j+z[j]-i,z[i-j])
            while((i+z[i]<n) and (s[z[i]]==s[i+z[i]])):
                z[i]+=1
            if (j+z[j]<i+z[i]):
                j=i
            i+=1
        z[0]=n
        return z


def main():
    S = SI()
    T = SI()
    # TとS[i:]の最長共通prefixの長さの配列
    Z = string.z_algorithm(S+"$"+T)

    print(Z)
    INF = 10**6
    # i文字目まで連結したときの最小のk
    dp = [INF] * (len(T)+1)
    dp[0] = 0




if __name__ == "__main__":
    main()
