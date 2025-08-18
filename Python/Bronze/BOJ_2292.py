# Bronze 2
# 벌집 문제 - 3가지 해결 방법 비교

# 벌집 패턴: 1층(1개) -> 2층(2~7, 6개) -> 3층(8~19, 12개) -> 4층(20~37, 18개) ...
# 각 층마다 6k개씩 증가 (k는 층수)

N = int(input())

# 방법 2: 수학적 공식 활용 (현재 사용) - O(√N)
# k층의 마지막 번호 = 1 + 3k(k-1)
boundary_num = 1
while N > 1 + 3*boundary_num*(boundary_num-1):
    boundary_num += 1
print(boundary_num)

"""
방법 1: 처음 작성한 코드 (시간초과 발생)
문제점: N까지 하나씩 세면서 확인 -> O(N) 시간복잡도
N이 최대 100만이므로 시간초과 발생

boundary_num = 1
hexagon_num = 0
boundary_producing_num = 2

while hexagon_num != N:
    hexagon_num += 1  # 1부터 N까지 하나씩 증가 (비효율적!)
    if hexagon_num == boundary_producing_num:
        boundary_num += 1
        boundary_producing_num += 6 * (boundary_num-1)
print(boundary_num)
"""

"""
방법 3: 직관적 접근 (누적 합산) - O(√N)
각 층마다 추가되는 방의 개수를 순차적으로 더해가는 방식
이해하기 쉽고 벌집의 성장 과정을 자연스럽게 시뮬레이션

n = int(input())
end = 1      # 현재 층까지의 마지막 방 번호
count = 1    # 현재 층수
while n > end:
    end += 6 * count  # 다음 층에 추가되는 방의 개수 (6, 12, 18, 24...)
    count += 1
print(count)
"""