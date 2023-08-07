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
EI = lambda m: [NLI() for _ in range(m)]


class Bucket:
    def __init__(self, _data):
        self.data = _data[:]
        self.cnts = Counter(self.data)
        # for d in self.data:
        #     self.cnts[d] += 1
        self.state = 0 # 1: 昇順, -1: 降順 にソートすみ


    def agg(self):
        # stateの解消
        if self.state == 0:
            return
        elif self.state == 1:
            now = 0
            tmp_cnts = self.cnts.copy()
            for k in range(len(self.data)):
                while tmp_cnts[now] == 0:
                    now += 1
                self.data[k] = now
                tmp_cnts[now] -= 1
        else:
            now = 0
            tmp_cnts = self.cnts.copy()
            for k in range(len(self.data)-1, -1, -1):
                while tmp_cnts[now] == 0:
                    now += 1
                self.data[k] = now
                tmp_cnts[now] -= 1

        self.state = 0


    def set(self, i, x):
        old = self.data[i]
        self.cnts[old] -= 1
        self.data[i] = x
        self.cnts[x] += 1


    def __str__(self):
        return f"{self.data}"

    def __repr__(self):
        return self.__str__()


def pick_k(C: Counter, k: int, rev=False):
    # Counterの値の小さいほうからk個とる
    res = Counter()
    if k == 0:
        return res

    keys = sorted(list(C.keys()), reverse=rev)
    for key in keys:
        x = C[key]
        if k > x:
            k -= x
            C[key] -= x
            res[key] += x
        else:
            C[key] -= k
            res[key] += k
            k = 0
            break
    return res


def main():
    N, Q = NMI()
    A = NLI()
    # sz = int(N**0.5)+1
    sz = 1000
    bn = (N+sz-1) // sz
    B = [[] for _ in range(bn)]
    for i, a in enumerate(A):
        B[i//sz].append(a)
    B = [Bucket(b) for b in B]

    for _ in range(Q):
        C, L, R = NMI()
        L -= 1 # 0-indexの半開区間[L, R)
        # print(C, L, R)

        bl = (L + sz - 1) // sz
        br = R // sz
        IL = bl * sz
        IR = br * sz

        if bl > br:
            # print(B[br])
            B[br].agg()
            # print(B[br])
            cnts = Counter()
            l, r = L%sz, L%sz + (R-L)
            for i in range(l, r):
                cnts[B[br].data[i]] += 1

            if C == 1:
                now = 0
                for k in range(l, r):
                    while cnts[now] == 0:
                        now += 1
                    B[br].set(k, now)
                    cnts[now] -= 1

            elif C == 2:
                now = 10
                for k in range(l, r):
                    while cnts[now] == 0:
                        now -= 1
                    B[br].set(k, now)
                    cnts[now] -= 1

            else:
                ans = 0
                for x in range(1, 11):
                    ans += x * cnts[x]
                print(ans)

            continue


        else:
            # 端の個数
            rem_l = IL - L
            rem_r = R - IR

            # print(L, R, bl, br, IL, IR, rem_l, rem_r)

            # cntsを取得 stateを変更
            cnts = Counter()
            for bi in range(bl, br):
                if C == 1:
                    B[bi].state = 1
                elif C == 2:
                    B[bi].state = -1
                cnts += B[bi].cnts

            # 端のbucketの遅延処理
            # 端の取得
            if rem_l > 0:
                B[bl - 1].agg()
                for k in range(1, rem_l + 1):
                    # print(bl, k, rem_l, B)
                    a = B[bl - 1].data[-k]
                    cnts[a] += 1

            if rem_r > 0:
                B[br].agg()
                for k in range(rem_r):
                    a = B[br].data[k]
                    cnts[a] += 1

        # この時点でcntsはA[L:R)のCounterのはず
        # 端の遅延処理は終わっている
        # print("cnts", cnts)

        if C == 1:
            l_cnts = pick_k(cnts, rem_l, rev=False)
            r_cnts = pick_k(cnts, rem_r, rev=True)

            # もどす
            if rem_l > 0:
                now = 0
                for k in range(-rem_l, 0):
                    while l_cnts[now] == 0:
                        now += 1
                    B[bl-1].set(k, now)
                    l_cnts[now] -= 1

            if rem_r > 0:
                now = 0
                # print(r_cnts)
                for k in range(rem_r):
                    while r_cnts[now] == 0:
                        now += 1
                    # print(k, now)
                    B[br].set(k, now)
                    r_cnts[now] -= 1

            for bi in range(bl, br):
                B[bi].cnts = pick_k(cnts, sz)

            # print(B[0])
            # B[0].agg()
            # print(B[0])

        elif C == 2:
            l_cnts = pick_k(cnts, rem_l, rev=True)
            r_cnts = pick_k(cnts, rem_r, rev=False)
            # print("cnts", cnts, l_cnts, r_cnts, bl, br)

            # もどす
            if rem_l > 0:
                now = 10
                # print(l_cnts)
                for k in range(-rem_l, 0):
                    while l_cnts[now] == 0:
                        now -= 1
                    B[bl - 1].set(k, now)
                    l_cnts[now] -= 1

            if rem_r > 0:
                now = 10
                # print(r_cnts)
                for k in range(rem_r):
                    while r_cnts[now] == 0:
                        now -= 1
                    B[br].set(k, now)
                    r_cnts[now] -= 1

            for bi in range(bl, br):
                B[bi].cnts = pick_k(cnts, sz, rev=True)

        else:
            ans = 0
            for x in range(1, 11):
                ans += x * cnts[x]
            print(ans)


if __name__ == "__main__":
    main()
