# Bronze 3
# 대지
# 좌표가 주어지고, 형성될 수 있는 직사각형 넓이의 최댓값을 구해라

N = int(input())
points = [list(map(int, input().split())) for _ in range(N)]

if N == 1:
    print(0)

else:
    x_coords = [p[0] for p in points]
    y_coords = [p[1] for p in points]

    width = max(x_coords)-min(x_coords)
    height = max(y_coords) - min(y_coords)

    print(width * height)