# 체스판 다시 칠하기
# Silver 3

N, M = map(int, input().split())

board = []
for _ in range(N):
    color = list(input())
    board.append(color)

min_count = 32

for start_row in range(N - 7):
    for start_column in range(M - 7):

        count1 = 0
        for x in range(8):
            for y in range(8):
                ori_color = board[start_row + x][start_column + y]
                
                if (x + y) % 2 == 0:
                    if ori_color != 'W':
                        count1 += 1
                else:
                    if ori_color != 'B':
                        count1 += 1

        count2 = 0
        for x in range(8):
            for y in range(8):
                ori_color = board[start_row + x][start_column + y]
                
                if (x + y) % 2 == 0:
                    if ori_color != 'B':
                        count2 += 1
                else:
                    if ori_color != 'W':
                        count2 += 1

        min_count = min(min_count, count1, count2)

print(min_count)
