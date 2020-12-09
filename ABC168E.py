import sys
import math
from collections import defaultdict

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline().strip()
NI = lambda: int(input())
NMI = lambda: map(int, input().split())
NLI = lambda: list(NMI())
SI = lambda: input()


class Iwashi():
    def __init__(self, a, b):
        self.a = a
        self.b = b

        if a == b == 0:
            pass
        else:
            if b < 0:
                self.a, self.b = -self.a, -self.b
            g = math.gcd(self.a, self.b)
            self.a, self.b = self.a // g, self.b // g

    def __eq__(self, other):
        return (self.a == other.a) and (self.b == other.b)

    def __repr__(self):
        return str((self.a, self.b))

    def get_ab(self):
        return self.a, self.b

    def get_bad_iwashi(self):
        if self.a <= 0:
            return self.b, -self.a
        else:
            return -self.b, self.a


def main():
    N = NI()
    iwashis = [Iwashi(*NMI()) for _ in range(N)]

    iwashi_dic = defaultdict(int)
    for iw in iwashis:
        iwashi_dic[iw.get_ab()] += 1

    ans = 1
    checked_iwashi = set()
    for iw, num in list(iwashi_dic.items()):
        if iw in checked_iwashi:
            continue

        # (0, 0)は最後に足す
        if iw == (0, 0):
            continue

        bad_iw = Iwashi(*iw).get_bad_iwashi()
        bad_num = iwashi_dic[bad_iw]
        ans *= pow(2, num, MOD) + pow(2, bad_num, MOD) - 1
        ans %= MOD

        checked_iwashi.add(iw)
        checked_iwashi.add(bad_iw)

    ans = ans + iwashi_dic[(0, 0)] - 1
    print(ans%MOD)



if __name__ == "__main__":
    main()
