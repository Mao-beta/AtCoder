"""SA-IS・LCP・Z。shakayami/ACL-for-pythonのString(s)形式。
Unicode・空入力対応。前処理O(N log N)、SA-IS/LCP/ZはO(N)。PyPy向け、Codon未確認。

使い方（このファイルを解答の先頭に貼り付けてから実行）
    text = String('banana')
    sa = text.suffix_array()
    sa, text.lcp_array(sa)  # => ([5, 3, 1, 0, 4, 2], [1, 3, 0, 0, 2])
    String('ababa').z_algorithm()  # => [5, 0, 3, 0, 1]
    String([2, 0, 2, 0]).suffix_array()  # => [3, 1, 2, 0]
    longest_common_substring('xabcy', 'zabcw')  # => (1, 4, 1, 4)
longest_common_substring(s,t)は独自拡張。共通区間(a,b,c,d)を返す。
"""


class _SuffixArray:
    def sa_is(s, upper):
        n = len(s)
        if n == 0:
            return []
        if n == 1:
            return [0]
        if n == 2:
            if s[0] < s[1]:
                return [0, 1]
            else:
                return [1, 0]
        sa = [0] * n
        ls = [0] * n
        for i in range(n - 2, -1, -1):
            ls[i] = ls[i + 1] if (s[i] == s[i + 1]) else (s[i] < s[i + 1])
        sum_l = [0] * (upper + 1)
        sum_s = [0] * (upper + 1)
        for i in range(n):
            if not (ls[i]):
                sum_s[s[i]] += 1
            else:
                sum_l[s[i] + 1] += 1
        for i in range(upper + 1):
            sum_s[i] += sum_l[i]
            if i < upper:
                sum_l[i + 1] += sum_s[i]

        def induce(lms):
            for i in range(n):
                sa[i] = -1
            buf = sum_s[:]
            for d in lms:
                if d == n:
                    continue
                sa[buf[s[d]]] = d
                buf[s[d]] += 1
            buf = sum_l[:]
            sa[buf[s[n - 1]]] = n - 1
            buf[s[n - 1]] += 1
            for i in range(n):
                v = sa[i]
                if v >= 1 and not (ls[v - 1]):
                    sa[buf[s[v - 1]]] = v - 1
                    buf[s[v - 1]] += 1
            buf = sum_l[:]
            for i in range(n - 1, -1, -1):
                v = sa[i]
                if v >= 1 and ls[v - 1]:
                    buf[s[v - 1] + 1] -= 1
                    sa[buf[s[v - 1] + 1]] = v - 1

        lms_map = [-1] * (n + 1)
        m = 0
        for i in range(1, n):
            if not (ls[i - 1]) and ls[i]:
                lms_map[i] = m
                m += 1
        lms = []
        for i in range(1, n):
            if not (ls[i - 1]) and ls[i]:
                lms.append(i)
        induce(lms)
        if m:
            sorted_lms = []
            for v in sa:
                if lms_map[v] != -1:
                    sorted_lms.append(v)
            rec_s = [0] * m
            rec_upper = 0
            rec_s[lms_map[sorted_lms[0]]] = 0
            for i in range(1, m):
                l = sorted_lms[i - 1]
                r = sorted_lms[i]
                end_l = lms[lms_map[l] + 1] if (lms_map[l] + 1 < m) else n
                end_r = lms[lms_map[r] + 1] if (lms_map[r] + 1 < m) else n
                same = True
                if end_l - l != end_r - r:
                    same = False
                else:
                    while l < end_l:
                        if s[l] != s[r]:
                            break
                        l += 1
                        r += 1
                    if (l == n) or (s[l] != s[r]):
                        same = False
                if not (same):
                    rec_upper += 1
                rec_s[lms_map[sorted_lms[i]]] = rec_upper
            rec_sa = _SuffixArray.sa_is(rec_s, rec_upper)
            for i in range(m):
                sorted_lms[i] = lms[rec_sa[i]]
            induce(sorted_lms)
        return sa

    def suffix_array_upper(s, upper):
        assert 0 <= upper
        for d in s:
            assert 0 <= d and d <= upper
        return _SuffixArray.sa_is(s, upper)

    def _suffix_array(s):
        # 文字列 S に対し、i 文字目から j 文字目までの文字からなる連続部分文字列を S[i:j] とおきます。
        # S の suffix array とは、(1,2,…,N) の順列 P であって、
        # 1≤i≤N−1 に対し S[Pi:N] < S[Pi+1:N]を満たす唯一のものを指します。
        n = len(s)
        if type(s) == str:
            s2 = [ord(i) for i in s]
            return _SuffixArray.sa_is(s2, 255)
        else:
            idx = list(range(n))
            idx.sort(key=lambda x: s[x])
            s2 = [0] * n
            now = 0
            for i in range(n):
                if i and s[idx[i - 1]] != s[idx[i]]:
                    now += 1
                s2[idx[i]] = now
            return _SuffixArray.sa_is(s2, now)

    def _lcp_array(s, sa):
        """
        lcp-array(Longest Common Prefix)を求めます。
        呼び出す際には事前にsuffix_arrayのリストを持つことが要求されます。
        """
        n = len(s)
        if n == 0:
            return []
        rnk = [0] * n
        for i in range(n):
            rnk[sa[i]] = i
        lcp = [0] * (n - 1)
        h = 0
        for i in range(n):
            if h > 0:
                h -= 1
            if rnk[i] == 0:
                continue
            j = sa[rnk[i] - 1]
            while j + h < n and i + h < n:
                if s[j + h] != s[i + h]:
                    break
                h += 1
            lcp[rnk[i] - 1] = h
        return lcp

    def _z_algorithm(s):
        """
        文字列が与えられた時、各 i について
        「S と S[i:] の最長共通接頭辞の長さ」
        を記録した配列 A を O(|S|) で構築する
        """
        n = len(s)
        if n == 0:
            return []
        z = [0] * n
        i = 1
        j = 0
        while i < n:
            z[i] = 0 if (j + z[j] <= i) else min(j + z[j] - i, z[i - j])
            while (i + z[i] < n) and (s[z[i]] == s[i + z[i]]):
                z[i] += 1
            if j + z[j] < i + z[i]:
                j = i
            i += 1
        z[0] = n
        return z


def _suffix_array(s, upper=None):
    """sの各接尾辞を辞書順に並べた開始位置のlist。空の接尾辞は含めない。
    sは文字列または整数列。upper指定時は0<=s[i]<=upperを保証する。
    upperなしの整数列は内部で座標圧縮する。入力非破壊。
    """
    values = list(s)
    if upper is not None:
        return _SuffixArray.suffix_array_upper(values, upper)
    return _SuffixArray._suffix_array(values)


def _lcp_array(values, sa):
    """valuesとsuffix_array(values)の結果saから、隣り合う接尾辞の共通接頭辞長を返す。
    結果[i]=LCP(values[sa[i]:],values[sa[i+1]:])。長さmax(0,n-1)、O(n)。
    """
    return _SuffixArray._lcp_array(values, sa)


def longest_common_substring(s, t):
    """文字列s,tの最長共通部分文字列を区間(a,b,c,d)で返す。
    s[a:b]==t[c:d]。共通文字なしなら(0,0,0,0)。複数解の選び方は未指定。
    Unicodeにも対応。座標圧縮O(N log N)、SA-ISとLCP部分O(N)、空間O(N)。
    例: longest_common_substring('xabcy','zabcw')は(1,4,1,4)。
    計算量のN=len(s)+len(t)+1。s/tはstr。
    """
    if not s or not t:
        return 0, 0, 0, 0
    alphabet = {c: i + 1 for i, c in enumerate(sorted(set(s) | set(t)))}
    values = [alphabet[c] for c in s] + [0] + [alphabet[c] for c in t]
    sa = _suffix_array(values, len(alphabet))
    lcp = _lcp_array(values, sa)
    n, best, result = len(s), 0, (0, 0, 0, 0)
    for i, length in enumerate(lcp):
        u, v = sa[i], sa[i + 1]
        if (u < n and v > n) or (v < n and u > n):
            if length > best:
                if u > v:
                    u, v = v, u
                best = length
                result = u, u + length, v - n - 1, v - n - 1 + length
    return result


def _z_algorithm(values):
    """各位置iでvalues全体とvalues[i:]の共通接頭辞長を返す。文字列・列に対応。
    長さnのlistでz[0]=n。空なら[]、O(n)。
    """
    return _SuffixArray._z_algorithm(values)


class String:
    """String(s)。文字列・整数列のSA/LCP/Zを求める。入力は変更しない。
    APIはshakayami/ACL-for-pythonに準拠。Unicode・空入力にも対応する。
    入力: sはstrまたは比較可能な整数列。N=len(s)。構築は参照を保存するだけなのでO(1)時間・空間、構築後に元の列を変更しない。
    SAの前処理O(N log(N+1))、LCPはSA指定時O(N)、ZはO(N)。各結果の空間O(N)。
    """

    def __init__(self, s):
        """入力: sはstrまたは比較可能な整数列。N=len(s)。構築は参照を保存するだけなのでO(1)時間・空間、構築後に元の列を変更しない。
        SAの前処理O(N log(N+1))、LCPはSA指定時O(N)、ZはO(N)。各結果の空間O(N)。
        """
        self._s = s

    def suffix_array(self):
        """接尾辞を辞書順に並べた開始添字。空接尾辞は含めない。前処理込みO(N log N)。"""
        return _suffix_array(self._s)

    def lcp_array(self, sa=None):
        """隣り合う接尾辞の共通接頭辞長。sa省略時はSAを計算する。SA指定時O(N)。
        saはsuffix_array()の結果の整数list、またはNone。省略時の時間はSA構築も含みO(N log(N+1))。
        """
        if sa is None:
            sa = self.suffix_array()
        return _lcp_array(self._s, sa)

    def z_algorithm(self):
        """各iについてsとs[i:]の共通接頭辞長。z[0]=N、空なら[]。O(N)。"""
        return _z_algorithm(self._s)

    def __len__(self):
        return len(self._s)

    def __getitem__(self, idx):
        return self._s[idx]

    def __str__(self):
        return str(self._s)

    def __repr__(self):
        return f"String({self._s!r})"
