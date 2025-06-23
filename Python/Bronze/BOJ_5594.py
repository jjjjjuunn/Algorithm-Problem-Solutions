# 과제 안 내신 분..?

# 방법 1: 기본 리스트 사용
'''
stu_arr = []
for _ in range(28):
    stu_arr.append(int(input()))
'''

# 방법 2: 리스트 컴프리헨션 사용
'''
stu_arr = [int(input()) for _ in range(28)]
'''

# 방법 3: set(집합) 사용 - in 연산이 리스트보다 빠름
stu_set = {int(input()) for _ in range(28)}
for i in range(1, 31):
    if i not in stu_set:
        print(i)