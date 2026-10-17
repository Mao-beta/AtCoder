"""線形漸化式。出典: LibraryChecker/LC_Mutipoint_Evaluation.py。
係数c[j]はa[n-j-1]に掛かる。modは素数。PyPy向け。
Codonでは積を取る前にmodで正規化し、mod²を64bit以内にする。
"""


def berlekamp_massey(values, mod=998244353):
    """O(N²)。与えられた列に適合する最短の線形漸化式係数を返す。"""
    if mod < 2:
        raise ValueError("prime mod required")
    a = [x % mod for x in values]
    c, b = [1], [1]
    length, shift, last = 0, 1, 1
    for n in range(len(a)):
        discrepancy = a[n]
        for i in range(1, length + 1):
            discrepancy = (discrepancy + c[i] * a[n - i]) % mod
        if discrepancy == 0:
            shift += 1
            continue
        old = c[:]
        factor = discrepancy * pow(last, mod - 2, mod) % mod
        if len(c) < len(b) + shift:
            c += [0] * (len(b) + shift - len(c))
        for i, x in enumerate(b):
            c[i + shift] = (c[i + shift] - factor * x) % mod
        if 2 * length <= n:
            length = n + 1 - length
            b, last, shift = old, discrepancy, 1
        else:
            shift += 1
    return [(-x) % mod for x in c[1 : length + 1]]


def linear_recurrence(initial, coefficients, n, mod=998244353):
    """O(k² log n)。initialは先頭k項。nは0-indexed。空の漸化式は零列。"""
    k = len(coefficients)
    if n < 0 or mod < 2 or len(initial) != k:
        raise ValueError("invalid recurrence parameters")
    if k == 0:
        return 0
    c = [x % mod for x in coefficients]

    def multiply(a, b):
        result = [0] * (2 * k - 1)
        for i in range(k):
            for j in range(k):
                result[i + j] = (result[i + j] + a[i] * b[j]) % mod
        for i in range(2 * k - 2, k - 1, -1):
            for j in range(k):
                result[i - j - 1] = (result[i - j - 1] + result[i] * c[j]) % mod
        return result[:k]

    result = [1] + [0] * (k - 1)
    base = [c[0]] if k == 1 else [0, 1] + [0] * (k - 2)
    while n:
        if n & 1:
            result = multiply(result, base)
        n >>= 1
        if n:
            base = multiply(base, base)
    answer = 0
    for x, y in zip(result, initial):
        answer = (answer + x * (y % mod)) % mod
    return answer
