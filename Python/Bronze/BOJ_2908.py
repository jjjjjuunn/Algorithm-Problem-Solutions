# 상수 (BOJ 2908)
# 두 수를 입력받아 각 숫자를 뒤집은 뒤, 더 큰 값을 출력

'''
# 내가 처음 작성했던 버전 (리스트와 pop을 이용)
A, B = map(list, input().split())
A_rev = ''
B_rev = ''
for _ in range(3):
    A_rev += A[-1]
    B_rev += B[-1]
    A.pop()
    B.pop()
if int(A_rev) > int(B_rev):
    print(A_rev)
else:
    print(B_rev)
'''

# 문자열 슬라이싱을 활용한 파이썬다운 풀이
A, B = input().split()
A_rev = int(A[::-1])  # [::-1]로 문자열을 뒤집고 int로 변환
B_rev = int(B[::-1])

# 조건문을 이용한 비교 출력
if A_rev > B_rev:
    print(A_rev)
else:
    print(B_rev)

# max()와 key=int를 활용한 더 간단한 버전
# key=int는 비교할 때 각 값을 int(정수)로 변환해서 비교하라는 의미
print(max(A_rev, B_rev, key=int))

'''
# 참고: key=int는 아래와 같이 문자열끼리 비교할 때도 유용하게 사용됨
# 예시: max('123', '321', key=int)  # '321' (정수 321이 더 크므로)
'''

