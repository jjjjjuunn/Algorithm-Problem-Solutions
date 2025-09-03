# Silver 5
# 분수찾기

Number_of_repetitions = 0 
sum_for_diagonal = 0

N = int(input())

while N > sum_for_diagonal:
    Number_of_repetitions += 1
    sum_for_diagonal += Number_of_repetitions

molecule = 1
denominator = Number_of_repetitions

for i in range(sum_for_diagonal - N):
    denominator -= 1
    molecule += 1

if Number_of_repetitions % 2 == 0:
    print(str(denominator) + "/" + str(molecule))
else:
    print(str(molecule) + "/" + str(denominator))