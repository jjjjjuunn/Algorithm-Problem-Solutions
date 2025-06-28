# 다이얼 (BOJ 5622)
# 입력받은 단어의 각 알파벳을 다이얼로 걸 때 걸리는 시간의 합을 구하는 문제
# 방법 3 나중에 다시 보기

# 방법 1: if-elif로 그룹별로 처리 (직관적이지만 코드가 길어짐)
'''
word = list(input())
time = 0
for ch in word:
    if ch in 'ABC':
        time += 3
    elif ch in 'DEF':
        time += 4
    elif ch in 'GHI':
        time += 5
    elif ch in 'JKL':
        time += 6
    elif ch in 'MNO':
        time += 7
    elif ch in 'PQRS':
        time += 8
    elif ch in 'TUV':
        time += 9
    else:
        time += 10
print(time)
'''

# 방법 2: 리스트와 이중 for문 (확장성, 유지보수성 좋음)
word = input()
dial = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
time = 0
for ch in word:
    for i in range(len(dial)):
        if ch in dial[i]:
            time += i + 3
            break
print(time)

# enumerate() : 리스트(또는 반복 가능한 객체)를 반복할 때 인덱스와 값을 동시에 얻을 수 있게 해준다.

# 방법 3: 딕셔너리로 알파벳-시간 매핑 (가장 효율적, 파이썬다운 방식)
dial = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
dial_dict = {}
for i, group in enumerate(dial):  # i: 인덱스(0~7), group: 'ABC' 등
    for ch in group:
        dial_dict[ch] = i + 3  # 각 알파벳에 해당하는 시간 저장
word = input()
time = sum(dial_dict[ch] for ch in word)  # 각 알파벳에 해당하는 시간의 합
print(time)

# 정리:
# - 방법 1: 직관적이지만 코드가 길어짐
# - 방법 2: 리스트로 그룹 관리, 유지보수성 좋음
# - 방법 3: 딕셔너리 매핑으로 가장 효율적이고 파이썬다운 방식