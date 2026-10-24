"""部分列の復元・計数・辞書順最小、上限付き編集距離。
部分列は連続でなくてよい。文字列または要素列を入力し、入力自体は変更しない。
通常Pythonで使用可能。Codonコンパイル未確認。

使い方（このファイル全体を貼り付けてから実行）
    subsequence_positions('atcoder', 'ace')  # => [0, 2, 5]
    smallest_subsequence('cbacd', 3)  # => 'acd'
    count_subsequence('ababa', 'aba')  # => 4
    count_distinct_subsequences('aba')  # => 6
    lcs_restore('abc', 'axc')  # => 'ac'
    edit_distance_bounded('kitten', 'sitting', 2)  # => 3
    edit_distance_bounded('kitten', 'sitting', 3)  # => 3
"""


def subsequence_positions(sequence, pattern):
    """patternが部分列なら最も左を選ぶ添字list、そうでなければNone。空patternは[]。
    O(N+M)時間。結果からsequence[i]を取り出すとpatternになる。
    sequence/patternは文字列または等号比較できる同種の要素の列。N=len(sequence)、M=len(pattern)。
    追加・出力空間O(M)。
    """
    result, j = [], 0
    for i, value in enumerate(sequence):
        if j < len(pattern) and value == pattern[j]:
            result.append(i)
            j += 1
    return result if j == len(pattern) else None


def smallest_subsequence(sequence, k):
    """長さkの辞書順最小部分列。str入力ならstr、それ以外はlist。0<=k<=N。
    単調スタック、O(N)時間・O(N)空間。要素は大小比較できる必要がある。
    sequenceは文字列または要素列、N=len(sequence)。
    """
    assert 0 <= k <= len(sequence)
    remove, stack = len(sequence) - k, []
    for value in sequence:
        while remove and stack and stack[-1] > value:
            stack.pop()
            remove -= 1
        stack.append(value)
    result = stack[:k]
    return "".join(result) if isinstance(sequence, str) else result


def count_subsequence(sequence, pattern, mod=1000000007):
    """添字の選び方としてpatternになる部分列の数。同じ文字でも位置が違えば別。
    空patternは1。O(NM)時間・O(M)空間。mod=0で厳密整数。
    sequence/patternは文字列または等号比較できる同種の要素の列。N=len(sequence)、M=len(pattern)。
    modは非負整数の法。0なら任意精度整数で正確に数え、正なら剰余を返す。
    """
    assert mod >= 0
    dp = [1] + [0] * len(pattern)
    for value in sequence:
        for j in range(len(pattern) - 1, -1, -1):
            if value == pattern[j]:
                dp[j + 1] += dp[j]
                if mod:
                    dp[j + 1] %= mod
    return dp[-1] % mod if mod else dp[-1]


def count_distinct_subsequences(sequence, mod=1000000007, include_empty=False):
    """文字列・要素列として異なる部分列の数。通常は空列を除く。要素はhash可能。
    O(N)期待時間・O(異なる要素数)空間。mod=0で厳密整数。
    sequenceは文字列または要素列、N=len(sequence)。
    modは非負整数の法。0なら任意精度整数で正確に数え、正なら剰余を返す。
    include_emptyは空部分列を含めるかのbool。
    """
    assert mod >= 0
    last, total = {}, 1
    for value in sequence:
        nxt = 2 * total - last.get(value, 0)
        last[value] = total
        total = nxt % mod if mod else nxt
    answer = total - (not include_empty)
    return answer % mod if mod else answer


def lcs_restore(a, b):
    """最長共通部分列を1つ復元。両方strならstr、それ以外はlist。O(NM)時間・空間。
    長い列の長さだけが必要ならmatching.pyのlcs_lengthを使う。
    a/bは文字列、または等号比較できる同種の要素列。N=len(a)、M=len(b)。
    """
    n, m = len(a), len(b)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n):
        row, previous = dp[i + 1], dp[i]
        for j in range(m):
            row[j + 1] = (
                previous[j] + 1 if a[i] == b[j] else max(previous[j + 1], row[j])
            )
    result, i, j = [], n, m
    while i and j:
        if a[i - 1] == b[j - 1]:
            result.append(a[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    result.reverse()
    return "".join(result) if isinstance(a, str) and isinstance(b, str) else result


def edit_distance_bounded(a, b, k):
    """挿入・削除・置換が各1の編集距離。距離<=kなら正確な値、超えるとk+1。
    k>=0。帯状DPでO((k+1)*min(N,M))時間・O(k+1)空間。文字列以外の列も可。
    a/bは文字列、または等号比較できる同種の要素列。N=len(a)、M=len(b)。
    """
    assert k >= 0
    if len(a) > len(b):
        a, b = b, a
    n, m = len(a), len(b)
    if m - n > k:
        return k + 1
    previous, previous_left = list(range(min(m, k) + 1)), 0
    inf = k + 1
    for i in range(1, n + 1):
        left, right = max(0, i - k), min(m, i + k)
        row = [inf] * (right - left + 1)
        for j in range(left, right + 1):
            if j == 0:
                row[0] = i
                continue
            best = row[j - left - 1] + 1 if j > left else inf
            p = j - previous_left
            if 0 <= p < len(previous):
                best = min(best, previous[p] + 1)
            if 0 <= p - 1 < len(previous):
                best = min(best, previous[p - 1] + (a[i - 1] != b[j - 1]))
            row[j - left] = best
        if min(row) > k:
            return inf
        previous, previous_left = row, left
    return min(inf, previous[m - previous_left])
