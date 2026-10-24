"""Trie・Aho–Corasick。出典: ABC362G, yuki_0430を配列と辞書で整理。
PyPy向け。Ahoは検索ごとの計数をfail木で集約し、出力リストの複製を避ける。

使い方（このファイルを解答の先頭に貼り付けてから実行）
    trie = Trie()
    trie.add('ab'); trie.add('abc'); trie.add('ab')
    trie.count('ab'), trie.count_prefix('a'), trie.count('a')  # => (2, 3, 0)
    ac = AhoCorasick(['aba', 'ba', ''])
    ac.count('ababa')  # => [2, 2, 6]
"""

from collections import deque


class Trie:
    """文字列（またはhashableな要素の列）を重複付きで登録する空のTrie。
    addで登録し、countで完全一致数、count_prefixで接頭辞一致数を得る。削除は非対応。
    引数なしで空のTrieをO(1)時間・空間で作る。word/prefixは文字列またはhashableな要素の列。Lは渡した列の長さ。
    add/count/count_prefixはO(L)期待時間。全体の空間は登録した文字総長Sに対しO(S)。
    """
    def __init__(self):
        """引数なしで空のTrieをO(1)時間・空間で作る。word/prefixは文字列またはhashableな要素の列。Lは渡した列の長さ。
        add/count/count_prefixはO(L)期待時間。全体の空間は登録した文字総長Sに対しO(S)。
        """
        self.next = [{}]
        self.counts = [0]
        self.terminals = [0]

    def add(self, word):
        """O(|word|)。重複と空文字列に対応。"""
        u = 0
        self.counts[u] += 1
        for ch in word:
            if ch not in self.next[u]:
                self.next[u][ch] = len(self.next)
                self.next.append({})
                self.counts.append(0)
                self.terminals.append(0)
            u = self.next[u][ch]
            self.counts[u] += 1
        self.terminals[u] += 1

    def _node(self, word):
        u = 0
        for ch in word:
            u = self.next[u].get(ch, -1)
            if u == -1:
                break
        return u

    def count(self, word):
        """wordに完全一致する登録数を返す。未登録なら0。O(|word|)。
        """
        u = self._node(word)
        return self.terminals[u] if u >= 0 else 0

    def count_prefix(self, prefix):
        """prefixから始まる登録文字列数を重複込みで返す。空prefixなら全登録数。O(|prefix|)。
        """
        u = self._node(prefix)
        return self.counts[u] if u >= 0 else 0


class AhoCorasick:
    """patternsの全パターンを先に登録し、複数文字列検索器を構築する。
    count(text)[i]はpatterns[i]の出現回数。重複パターンも入力順に保持する。
    空パターンはlen(text)+1回。構築後の追加は不可。検索のたびに計数を初期化する。
    入力: patternsはstrの列（重複・空文字も可）。Sは登録文字総長、Lは最長パターン長、Kは状態数（K<=S+1）。
    構築は疎な辞書でfailureを探索するため安全側でO(S+K*L)時間、空間O(S+len(patterns))。
    count(text)のtextはstr、検索はO(len(text)+K+len(patterns))期待時間。
    """
    def __init__(self, patterns):
        """入力: patternsはstrの列（重複・空文字も可）。Sは登録文字総長、Lは最長パターン長、Kは状態数（K<=S+1）。
        構築は疎な辞書でfailureを探索するため安全側でO(S+K*L)時間、空間O(S+len(patterns))。
        count(text)のtextはstr、検索はO(len(text)+K+len(patterns))期待時間。
        """
        self.next = [{}]
        self.fail = [0]
        self.ends = []
        for word in patterns:
            u = 0
            for ch in word:
                if ch not in self.next[u]:
                    self.next[u][ch] = len(self.next)
                    self.next.append({})
                    self.fail.append(0)
                u = self.next[u][ch]
            self.ends.append(u)
        queue = deque(self.next[0].values())
        self.order = []
        while queue:
            u = queue.popleft()
            self.order.append(u)
            for ch, v in self.next[u].items():
                f = self.fail[u]
                while f and ch not in self.next[f]:
                    f = self.fail[f]
                self.fail[v] = self.next[f].get(ch, 0)
                queue.append(v)

    def count(self, text):
        """パターンごとの出現数。重複一致を含む。O(|text|+ノード数)。
        textは検索する文字列。戻り値はpatternsの入力順で長さlen(patterns)。作業空間O(状態数)、出力空間O(len(patterns))。
        """
        visits = [0] * len(self.next)
        u = 0
        for ch in text:
            while u and ch not in self.next[u]:
                u = self.fail[u]
            u = self.next[u].get(ch, 0)
            visits[u] += 1
        for v in reversed(self.order):
            visits[self.fail[v]] += visits[v]
        visits[0] = len(text) + 1
        return [visits[v] for v in self.ends]
