question_num = 50
ans = [0] * 5
print('あてはまれば1、違えば2で入力')
input_to_digit = {'1': 1, '2': 0}
for i in range(question_num):
    i += 1
    while True:
        res = input('Q' + str(i) + ': ')
        if res == '1' or res == '2':
            break
        else:
            print('あてはまれば1、違えば2で入力してください')
    ans[i%5 - 1] += int(input_to_digit[res])

for i, a in enumerate(ans):
    print(chr(65+i) + ': ' + str(a))
