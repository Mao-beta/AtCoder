S = input()
T = input()
for i in range(len(S)):
    if S[i] != T[i]:
        print('No')
        exit()
print('No' if len(S) != len(T) - 1 else 'Yes')