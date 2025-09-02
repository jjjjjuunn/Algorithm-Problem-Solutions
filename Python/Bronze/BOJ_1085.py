# Bronze 3
# 직사각형에서 탈출
# 직사각형의 경계선까지 가는 거리의 최솟값을 구해라

x, y, w, h = map(int,input().split())

distance_list = []
distance_list.append(x)
distance_list.append(y)
distance_list.append(w - x)
distance_list.append(h - y)

print(min(distance_list))

# 한 줄로 풀이
x, y, w, h = map(int, input().split())
print(min(x, y, w-x, h-y))