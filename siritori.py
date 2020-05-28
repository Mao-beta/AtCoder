words = list(input().split())
moji = []
for i in range(85):
    moji.append(chr(12354+i))
print(moji)


num_hira = 85   #ひらがなの数
ord_hira_a = 12354  #ord("あ")

#単語自身と最初と最後の文字を保持
words_WFL = []
for word in words:
    ord_F = ord(word[0]) - ord_hira_a
    ord_L = ord(word[-1]) - ord_hira_a
    if ord_F < 0 or ord_F > 84 or ord_L < 0 or ord_L > 84:
        print("ひらがなでない単語があるため除外します")
        continue
    words_WFL.append([word, ord_F, ord_L])
print(words_WFL)

#ある単語から行き先を調べるときに使うテーブル
hiragana_table = [[] for _ in range(num_hira)]
for idx, word_WFL in enumerate(words_WFL):
    hiragana_table[word_WFL[1]].append(idx)
print(hiragana_table)

