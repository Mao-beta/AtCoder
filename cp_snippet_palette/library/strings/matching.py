"""KMP・Manacher・編集距離・LCS。出典: _Strings.py。
0-indexed。空パターンは文字間を含む全位置に一致する。入力は変更しない。
PyPy向け。Codonでは両入力の要素型を揃える。

使い方（このファイルを解答の先頭に貼り付けてから実行）
    prefix_function('ababa'), kmp_search('abababa', 'aba')  # => ([0, 0, 1, 2, 3], [0, 2, 4])
    odd, even = manacher('abba')
    odd, even  # 中心1/2間の半径2 -> 長さ4
    # => ([1, 1, 1, 1], [0, 0, 2, 0])
    edit_distance('kitten', 'sitting'), lcs_length('abcde', 'ace')  # => (3, 3)
"""


def prefix_function(pattern):
    """KMPの失敗関数。O(m)。pi[i]=真の接頭辞かつ接尾辞の最長長。
    入力は文字列、または等号比較できる要素の列。n/mは入力の長さ。追加空間O(入力長)。
    patternが照合したいパターン列。m=len(pattern)。
    """
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
    """text内のpatternの全一致開始位置を昇順listで返す。重なりも含む。
    文字列または同じ要素型の列。空patternは0..len(text)の全位置に一致。O(n+m)。
    n=len(text)、m=len(pattern)。追加空間O(m+一致箇所数)。
    """
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
    """(odd,even)の2配列を返す。odd[i]は中心iを含む半径、even[i]はi-1/i間の半径。
    奇数長回文はtext[i-odd[i]+1:i+odd[i]]、長さ2*odd[i]-1。
    偶数長回文はtext[i-even[i]:i+even[i]]、長さ2*even[i]。O(n)。
    入力は文字列、または等号比較できる要素の列。n/mは入力の長さ。追加空間O(入力長)。
    """
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
    """挿入・削除・置換のコスト1。O(nm)時間、O(min(n,m))空間。
    a/bは文字列、または等号比較できる同種の要素の列。n=len(a)、m=len(b)。
    """
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
    """最長共通部分列の長さ。O(nm)時間、O(min(n,m))空間。
    a/bは文字列、または等号比較できる同種の要素の列。n=len(a)、m=len(b)。
    """
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
