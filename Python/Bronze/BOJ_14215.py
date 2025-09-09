# Bronze 3
# 세 막대
# a, b, c가 주어졌을 때, 만들 수 있는 삼각형의 가장 큰 둘레를 구해라(막대의 길이는 줄일 수 있다.)

a, b, c = map(int, input().split())

sides = [a, b, c]
sides.sort()

if max(sides) >= sum(sides)-max(sides):
    other_two_sum = sum(sides) - max(sides)
    sides[2] = other_two_sum - 1

side_total = sum(sides)

print(side_total)
