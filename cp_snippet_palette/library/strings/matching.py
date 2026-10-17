"""KMP・Manacher・編集距離・LCS。出典: _Strings.py。
0-indexed。空パターンは文字間を含む全位置に一致する。入力は変更しない。
PyPy向け。Codonでは両入力の要素型を揃える。
"""


def prefix_function(pattern):
    """KMPの失敗関数。O(m)。pi[i]=真の接頭辞かつ接尾辞の最長長。"""
    pi = [0] * len(pattern)
    for i in range(1, len(pattern)):
        j = pi[i - 1]
        while j and pattern[i] != pattern[j]:
            j = pi[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
        pi[i] = j
    return pi


def kmp_search(text, pattern):
    """O(n+m)。重なりを含む全一致の開始位置。"""
    if not pattern:
        return list(range(len(text) + 1))
    pi = prefix_function(pattern)
    answer, j = [], 0
    for i, x in enumerate(text):
        while j and x != pattern[j]:
            j = pi[j - 1]
        if x == pattern[j]:
            j += 1
        if j == len(pattern):
            answer.append(i - j + 1)
            j = pi[j - 1]
    return answer


def manacher(text):
    """O(n)。odd[i]:中心iを含む半径、even[i]:中心i-1/i間の半径。"""
    n = len(text)
    odd, even = [0] * n, [0] * n
    left, right = 0, -1
    for i in range(n):
        k = 1 if i > right else min(odd[left + right - i], right - i + 1)
        while 0 <= i - k and i + k < n and text[i - k] == text[i + k]:
            k += 1
        odd[i] = k
        if i + k - 1 > right:
            left, right = i - k + 1, i + k - 1
    left, right = 0, -1
    for i in range(n):
        k = 0 if i > right else min(even[left + right - i + 1], right - i + 1)
        while 0 <= i - k - 1 and i + k < n and text[i - k - 1] == text[i + k]:
            k += 1
        even[i] = k
        if i + k - 1 > right:
            left, right = i - k, i + k - 1
    return odd, even


def edit_distance(a, b):
    """挿入・削除・置換のコスト1。O(nm)時間、O(min(n,m))空間。"""
    if len(a) < len(b):
        a, b = b, a
    dp = list(range(len(b) + 1))
    for i, x in enumerate(a, 1):
        row = [i]
        for j, y in enumerate(b):
            row.append(min(row[-1] + 1, dp[j + 1] + 1, dp[j] + (x != y)))
        dp = row
    return dp[-1]


def lcs_length(a, b):
    """最長共通部分列の長さ。O(nm)時間、O(min(n,m))空間。"""
    if len(a) < len(b):
        a, b = b, a
    dp = [0] * (len(b) + 1)
    for x in a:
        diagonal = 0
        for j, y in enumerate(b):
            old = dp[j + 1]
            dp[j + 1] = diagonal + 1 if x == y else max(dp[j], old)
            diagonal = old
    return dp[-1]
