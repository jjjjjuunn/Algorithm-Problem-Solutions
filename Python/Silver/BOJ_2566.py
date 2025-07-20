# 행렬에서 최댓값 찾기 문제
matrix = []

for _ in range(9):
    matrix.append(list(map(int,input().split())))

max_num = 0
max_pos = []
for i in range(9):
    for j in range(9):
        if max_num < matrix[i][j]:
            max_num = matrix[i][j]
            max_pos = [i+1,j+1]

        elif max_num == matrix[i][j]:
            max_pos = [i+1,j+1]

print(max_num)
print(*max_pos)
