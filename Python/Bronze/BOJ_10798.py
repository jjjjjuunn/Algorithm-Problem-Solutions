# 세로로 읽기 문제 (BOJ 10798) - 두 가지 해결 방법

# 방법 1: 조건문을 이용한 방법 (현재 사용)
str_array = [list(input()) for _ in range(5)]

word = []
for i in range(15):
    for j in range(5):
        # 해당 위치에 문자가 존재하는 경우에만 추가
        if i < len(str_array[j]):
            word.append(str_array[j][i])

print(''.join(word))

# 방법 2: 패딩을 이용한 방법 (주석처리)
"""
str_array = [list(input()) for _ in range(5)]

# 모든 문자열을 15글자로 패딩 (빈 문자열로 채움)
for i in str_array:
    while len(i) < 15:
        i.append('')

word = []
for i in range(15):
    for j in range(5):
        word.append(str_array[j][i])

print(''.join(word))
"""
