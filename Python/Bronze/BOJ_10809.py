# 알파벳 찾기 (BOJ 10809)
# 입력받은 단어에서 a~z 각 알파벳이 처음 등장하는 위치를 출력
# 없으면 -1 출력

'''
# 원래 작성했던 방식 (비효율적, 중복 탐색)
alphabet = list('abcdefghijklmnopqrstuvwxyz')
word = input()
for idx in alphabet:
    if idx in word:
        print(word.index(idx), end=' ')
    else:
        print('-1', end=' ')
print()
'''

# 파이썬다운 방식: 아스키코드와 str.find() 활용 (효율적)
word = input()
for i in range(26):
    ch = chr(i + 97)  # 97~122: a~z
    print(word.find(ch), end=' ')
print()

'''
# 리스트 컴프리헨션으로 더 간결하게
word = input()
print(' '.join(str(word.find(chr(i + 97))) for i in range(26)))
'''