# 문자열 반복 (BOJ 2675)
# 각 테스트케이스마다 문자열 S의 각 문자를 R번 반복해 출력

'''
# 방법 1: 리스트에 입력을 저장하고, 인덱스 계산으로 처리 (비효율적, 비추천)
T = int(input())
arr = []
for _ in range(T):
    R, S = map(str, input().split())
    R = int(R)
    arr.append(R)
    arr.append(S)
for i in range(1, len(arr), 2):
    j = 0
    for _ in arr[i]:
        print(arr[i][j] * arr[i-1], end='')
        j += 1
    print()
'''

# 방법 2: 입력을 바로 처리 (파이썬다운, 효율적, 추천)
T = int(input())
for _ in range(T):
    R, S = input().split()
    R = int(R)
    result = ''
    for word in S:
        result += word * R
    print(result)

# 방법 2-1: 리스트 컴프리헨션과 join을 활용한 더 간결한 버전
# T = int(input())
# for _ in range(T):
#     R, S = input().split()
#     print(''.join(char * int(R) for char in S))

# 정리:
# - 방법 2, 2-1이 파이썬스럽고 효율적이며, 실전에서도 추천되는 방식입니다.
# - 방법 1은 인덱스 관리가 복잡하고 비효율적이므로 피하는 것이 좋습니다.