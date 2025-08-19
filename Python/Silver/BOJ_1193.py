# Silver 5
# 분수 찾기 - 지그재그 패턴으로 배열된 분수에서 N번째 분수 찾기

# 분수 배열 패턴:
# 1/1 -> 1/2,2/1 -> 3/1,2/2,1/3 -> 1/4,2/3,3/2,4/1 -> ...
# 대각선별로 개수: 1개, 2개, 3개, 4개, ...
# 방향: 홀수 대각선(아래→위), 짝수 대각선(위→아래)

N = int(input())

# 방법 1: 점진적 조정 방식 (현재 사용)
# 대각선을 찾은 후, for문으로 위치를 조정하여 분자/분모 계산

diagonal = 0 
total_count = 0

# N번째 분수가 속한 대각선 찾기
while N > total_count:
    diagonal += 1
    total_count += diagonal

# 초기값: 대각선 끝점에서 시작 (예: 3번째 대각선이면 3/1에서 시작)
numerator = 1
denominator = diagonal

# 대각선 끝에서 N번째 위치까지 조정
for _ in range(total_count - N):
    denominator -= 1  # 분모 감소
    numerator += 1    # 분자 증가

# 홀짝 대각선에 따른 출력 (홀수=분자/분모, 짝수=분모/분자)
if diagonal % 2 == 0:
    print(f"{denominator}/{numerator}")
else:
    print(f"{numerator}/{denominator}")

"""
방법 2: 직접 계산 방식
대각선과 위치를 찾은 후, 수학적 공식으로 분자/분모를 직접 계산

N = int(input())

diagonal = 0 
total_count = 0

# N번째 분수가 속한 대각선 찾기
while N > total_count:
    diagonal += 1
    total_count += diagonal

# 대각선 내에서의 위치 계산 (1부터 시작)
position_in_diagonal = N - (total_count - diagonal)

# 홀짝 대각선에 따른 분자/분모 직접 계산
if diagonal % 2 == 0:  # 짝수 대각선: 위→아래 (분자↑, 분모↓)
    numerator = position_in_diagonal
    denominator = diagonal - position_in_diagonal + 1
else:  # 홀수 대각선: 아래→위 (분자↓, 분모↑)
    numerator = diagonal - position_in_diagonal + 1
    denominator = position_in_diagonal

print(f"{numerator}/{denominator}")
"""
