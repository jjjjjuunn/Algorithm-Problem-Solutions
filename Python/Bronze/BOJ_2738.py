# 행렬 덧셈
# 복습하기
# 백준에서 EOF Error 발생

M,N = map(int,input().split())

matrix_a = []
matrix_b = []

for _ in range(N) :
    matrix_a.append(list(map(int,input().split())))
for _ in range(N) :
    matrix_b.append(list(map(int,input().split())))

matrix_add = []
for i in range(N):
    added_arr = []
    for j in range(M):
        added_arr.append(matrix_a[i][j]+matrix_b[i][j])
    matrix_add.append(added_arr)

for row in matrix_add :
    print(*row)