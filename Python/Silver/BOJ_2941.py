# 크로아티아 알파벳

k_alpha_arr = ['c=','c-','dz=','d-','lj','nj','s=','z=']

word = list(input())

for i in range(2,len(word)):
    if word[i-2] + word[i-1] + word[i] in k_alpha_arr :
        word.pop(i)
        word.insert(i,'0')
        word.pop(i-1)
        word.insert(i-1,'0')

for i in range(1,len(word)) :
    if word[i-1] + word[i] in k_alpha_arr :
        word.pop(i)
        word.insert(i,'0')

count = 0

for ch in word :
    if ch != '0' :
        count +=1
    else :
        continue

print(count)