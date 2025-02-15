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

input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()
SMI = lambda: input().split()
SLI = lambda: list(SMI())
EI = lambda m: [NLI() for _ in range(m)]


def extgcd(a, b):
    if b:
        d, y, x = extgcd(b, a % b)
        y -= (a // b)*x
        return d, x, y
    return a, 1, 0

def main():
    Q = NI()
    for qi in range(Q):
        W, H, D, Mx, My, Hx, Hy, Vx, Vy = NMI()
        if Vx < 0:
            Vx *= -1
            Hx = W - Hx
            Mx = W - Mx
        if Vy < 0:
            Vy *= -1
            Hy = H - Hy
            My = H - My

        if Vx == 0:
            if Hx != Mx:
                print("Miss")
            else:
                if My < Hy:
                    My = 2*H - My
                if Vy * D < My - Hy:
                    print("Miss")
                else:
                    print("Hit")
            continue
        if Vy == 0:
            if Hy != My:
                print("Miss")
            else:
                if Mx < Hx:
                    Mx = 2*W - Mx
                if Vx * D < Mx - Hx:
                    print("Miss")
                else:
                    print("Hit")
            continue

        vg = math.gcd(Vx, Vy)
        Vx //= vg
        Vy //= vg
        D *= vg

        # Vx > 0, Vy > 0, 互いに素
        # (Mx + 2W*i, My + 2H*j)
        # (2W-Mx + 2W*i, My + 2H*j)
        # (Mx + 2W*i, 2H-My + 2H*j)
        # (2W-Mx + 2W*i, 2H-My + 2H*j)
        # が Vy(x-Hx) - Vx(y-Hy) = 0上にあるか

        # Vy(Mx-Hx + 2W*i) - Vx(My-Hy + 2H*j) = 0
        # 2Vy*W*i - 2Vx*H*j = -Vy(Mx-Hx) + Vx(My-Hy)
        # を満たす整数i, jが存在するか？
        # g=gcd(2Vy*W, -2Vx*H)でわっておく、右辺が割れないなら無理
        # ai+bj = Rとすると、extgcdでi,jがひとつ求まる(p, qとする)
        # a(i-p) + b(j-q) = 0
        # iはpからbずつ動かせるので、HxからVx方向に一番近いものを求めたい
        # iをb動かすとxは2W*b動く, jはa動くのでyは-2H*a動く
        # mx + (2W*b) * k > Hx をみたす最小のk

        MXS = [Mx, Mx, 2*W-Mx, 2*W-Mx]
        MYS = [My, 2*H-My, My, 2*H-My]
        ok = False

        for MX, MY in zip(MXS, MYS):
            R = -Vy*(MX-Hx) + Vx*(MY-Hy)
            g = math.gcd(2*Vy*W, -2*Vx*H)
            if R % g:
                continue
            a = 2*Vy*W // g
            b = -2*Vx*H // g
            d, p, q = extgcd(a, b)
            p *= R // g // d
            q *= R // g // d
            # print(a, p, b, q, R//g)
            assert a * p + b * q == R//g, (a * p + b * q, R//g, d)
            mx = MX + 2*W * p
            my = MY + 2*H * q
            kx = (Hx-mx) // (2*W*b)
            mx += kx * 2*W*b
            my += -kx * 2*H*a

            if mx - Hx <= Vx * D:
                # print(f"H: {(Hx, Hy)}, M: {(mx, my)}, V: {(Vx, Vy)}, a*p+b*q=R//g: ({a})*({p})+({b})*({q})={R//g}")
                ok = True


        if ok:
            print("Hit")
        else:
            print("Miss")


if __name__ == "__main__":
    main()
