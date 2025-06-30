# 그룹 단어 체커
# 잘 모르겠음

n = int(input())

str_arr = [input() for _ in range(n)]

num_count = 0
for word in str_arr :
    count = 0
    for ch in word :
        ch_num = word.count(ch)
        if ch_num == word[word.index(ch):word.index(ch)+ch_num].count(ch) :
            count += 1
        if count == len(word):
            num_count +=1

print(num_count)

