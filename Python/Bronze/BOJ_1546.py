# 평균
n = int(input())
scores = list(map(int, input().split()))
max_score = max(scores)

# 방법 1: for문으로 각 점수 변환
# for i in range(n):
#     scores[i] = (scores[i] / max_score) * 100

# 방법 2: 리스트 컴프리헨션으로 각 점수 변환 (더 파이썬다운 방식)
new_scores = [(score / max_score) * 100 for score in scores]

avg_score = sum(new_scores) / n
print(avg_score)