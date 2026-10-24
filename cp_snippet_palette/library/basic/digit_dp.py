"""10進数の桁DP。bound以下の非負整数について数える（含める0は各関数を参照）。
boundは整数または巨大な10進文字列。負の上限は0件。mod=0なら厳密整数。
文字列をintに変換せず処理する。計数が巨大な場合の整数演算コストは別途。

使い方（このファイル全体を貼り付けてから実行）
    count_nonzero_digits('100', 1)  # => 19
    count_digit_sum_mod('20', 3)  # => 6
    count_avoiding_digits('20', {4, 9})  # => 17
    count_digit_occurrences('13', 1)  # => 6
    count_digit_occurrences('10', 0)  # => 2
"""


def _decimal_digits(bound):
    text = str(bound)
    if text.startswith("-"):
        return None
    if not text or any(c < "0" or c > "9" for c in text):
        raise ValueError("bound must be a decimal integer")
    return [ord(c) - 48 for c in text.lstrip("0") or "0"]


def count_nonzero_digits(bound, k, mod=0):
    """0<=x<=boundで非零桁がちょうどk個の整数の数。0はk=0に含む。
    先頭の0は数えない。O(L*k*10)時間・O(k)空間。
    入力: boundは10進数字のstrまたは整数の上限（含む）。Lはその桁数。modは非負整数で、0なら剰余なし、正なら答えをmodで割った余り。負のboundに対する答えは0。
    kは数えたい非零桁数の整数。k<0またはk>Lなら0。
    """
    assert mod >= 0
    digits = _decimal_digits(bound)
    if digits is None or k < 0 or k > len(digits):
        return 0
    loose = [0] * (k + 1)
    tight_count = 0
    for digit in digits:
        nxt = loose[:]
        for j in range(1, k + 1):
            nxt[j] += 9 * loose[j - 1]
        if tight_count <= k:
            if digit:
                nxt[tight_count] += 1
            if digit > 1 and tight_count < k:
                nxt[tight_count + 1] += digit - 1
        tight_count += digit != 0
        loose = [x % mod for x in nxt] if mod else nxt
    result = loose[k] + (tight_count == k)
    return result % mod if mod else result


def count_digit_sum_mod(bound, divisor, mod=1000000007, include_zero=False):
    """各桁の和がdivisorの倍数である0..boundの整数の数。既定では0を除く。
    divisor>0。O(L*divisor*10)時間・O(divisor)空間。
    入力: boundは10進数字のstrまたは整数の上限（含む）。Lはその桁数。modは非負整数で、0なら剰余なし、正なら答えをmodで割った余り。負のboundに対する答えは0。
    include_zeroは整数0を答えに含めるかを表すbool。
    """
    assert divisor > 0 and mod >= 0
    digits = _decimal_digits(bound)
    if digits is None:
        return 0
    loose, tight_sum = [0] * divisor, 0
    for digit in digits:
        nxt = [0] * divisor
        for r, count in enumerate(loose):
            if count:
                for d in range(10):
                    nxt[(r + d) % divisor] += count
        for d in range(digit):
            nxt[(tight_sum + d) % divisor] += 1
        tight_sum = (tight_sum + digit) % divisor
        loose = [x % mod for x in nxt] if mod else nxt
    result = loose[0] + (tight_sum == 0) - (not include_zero)
    return result % mod if mod else result


def count_avoiding_digits(bound, forbidden, mod=0):
    """通常の10進表記に禁止桁を含まない0..boundの整数の数。0の表記は'0'。
    先頭の補助的な0は無視。forbiddenは0..9の集合など。O(L*10)時間・O(1)状態。
    入力: boundは10進数字のstrまたは整数の上限（含む）。Lはその桁数。modは非負整数で、0なら剰余なし、正なら答えをmodで割った余り。負のboundに対する答えは0。
    """
    assert mod >= 0
    digits = _decimal_digits(bound)
    if digits is None:
        return 0
    forbidden = set(forbidden)
    assert all(0 <= d <= 9 for d in forbidden)
    dp = {(True, False): 1}
    for digit in digits:
        nxt = {}
        for (tight, started), count in dp.items():
            for d in range((digit if tight else 9) + 1):
                begun = started or d != 0
                if begun and d in forbidden:
                    continue
                key = (tight and d == digit, begun)
                nxt[key] = nxt.get(key, 0) + count
        dp = {k: v % mod for k, v in nxt.items()} if mod else nxt
    result = sum(
        count for (_, started), count in dp.items() if started or 0 not in forbidden
    )
    return result % mod if mod else result


def count_digit_occurrences(bound, digit, mod=0):
    """0..boundを全て書いたときのdigitの出現回数。0は一桁の'0'として数える。
    例: 0..10の0は0と10の2回。先頭の0を除外。O(L*10)時間・O(1)状態。
    入力: boundは10進数字のstrまたは整数の上限（含む）。Lはその桁数。modは非負整数で、0なら剰余なし、正なら答えをmodで割った余り。負のboundに対する答えは0。
    digitは数えたい数字を表す整数0..9。
    """
    assert 0 <= digit <= 9 and mod >= 0
    digits = _decimal_digits(bound)
    if digits is None:
        return 0
    dp = {(True, False): (1, 0)}
    for upper in digits:
        nxt = {}
        for (tight, started), (count, total) in dp.items():
            for d in range((upper if tight else 9) + 1):
                begun = started or d != 0
                key = (tight and d == upper, begun)
                c, s = nxt.get(key, (0, 0))
                nxt[key] = (c + count, s + total + count * (begun and d == digit))
        dp = {k: (c % mod, s % mod) for k, (c, s) in nxt.items()} if mod else nxt
    result = sum(total for count, total in dp.values()) + (digit == 0)
    return result % mod if mod else result
