# Bronze 3
# 네 번째 점
# 세 점이 주어졌을 때, 축에 평행한 직사각형을 만들기 위해서 필요한 네 번째 점을 찾아라

# 초기 버전
# 로직은 정확하지만 억지스러움
'''
dot_position = []
dot_x_position = []
dot_y_position = []

for i in range(3):
    dot_position.append(list(map(int, input().split())))

for i in range(3):
    dot_x_position.append(dot_position[i][0])
    dot_y_position.append(dot_position[i][1])

for i in range(3):
    if dot_x_position.count(dot_x_position[i]) == 1:
        dot_x_position.append(dot_x_position[i])

    if dot_y_position.count(dot_y_position[i]) == 1:
        dot_y_position.append(dot_y_position[i])

print(dot_x_position[3],dot_y_position[3])
'''

# XOR 활용

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

fourth_x = x1 ^ x2 ^ x3
fourth_y = y1 ^ y2 ^ y3

print(fourth_x, fourth_y)


# XOR(배타적 논리합)을 사용하지 않은 가장 간결한 버전
points = [list(map(int, input().split())) for _ in range(3)]

x_coords = [p[0] for p in points]
y_coords = [p[1] for p in points]

fourth_x = [x for x in x_coords if x_coords.count(x) == 1][0]
fourth_y = [y for y in y_coords if y_coords.count(y)== 1][0]

print(fourth_x, fourth_y)