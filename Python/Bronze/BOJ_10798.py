# Bronze 1
# 세로 읽기

str_array = [list(input()) for _ in range(5)]

word = []
for i in range(15):
    for j in range(5):
        if i < len(str_array[j]):
            word.append(str_array[j][i])

print(''.join(word))
