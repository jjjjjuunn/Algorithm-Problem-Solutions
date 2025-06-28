# 단어 공부
# 다른 방법으로도 구현해보기
# 복습하기

word = input().upper()

word_dict = {}

for ch in word:
    if ch not in word_dict.keys() :
        word_dict.setdefault(ch,1)
    else :
        word_dict[ch] += 1

max_value = max(word_dict.values())

count = 0 
max_key = ''
for key in word_dict.keys() :
    if word_dict[key] == max_value:
        count+=1
        max_key = key

if count == 1:
    print(max_key)
else :
    print('?')