# Bronze 2
# 알고리즘 수업 - 알고리즘의 수행 시간 6

"""
【문제 분석】
의사코드:
    for i = 1 to n-2
        for j = i+1 to n-1  
            for k = j+1 to n
                sum = sum + A[i] × A[j] × A[k]

핵심: 1 ≤ i < j < k ≤ n 인 모든 (i,j,k) 조합의 개수
    = C(n,3) = n(n-1)(n-2)/6

【해법 아이디어】
3중 루프를 수학적 패턴으로 최적화
- 삼각수(1, 3, 6, 10, 15, ...)의 합을 이용
- 삼각수의 합 = 사면체수 = C(n,3)와 동일한 결과
"""

# ==================== 실패한 첫 번째 시도 ====================
''' 
n = int(input())

sum = 0
i = 1
for j in range(n - 2, 0, -1):
    sum += j * i
    i += 1

print(sum)
print(3)
'''

# ==================== 성공한 최종 해법 ====================
n = int(input())

sum = 0
plus_factor = 1  # 삼각수 시작: T(1) = 1

for i in range(2, n):           # i = 2, 3, ..., n-1
    sum += plus_factor          # T(1) + T(2) + ... + T(n-2) 누적
    plus_factor += i            # 다음 삼각수 생성: T(k+1) = T(k) + (k+1)

print(sum)  # 3중 루프 실행 횟수 = C(n,3)
print(3)    # 시간복잡도 O(n³)의 최고차항 차수

# 수학적 공식 활용

n = int(input())

sum = n * (n-1) * (n-2) // 6 

print(sum)
print(3)