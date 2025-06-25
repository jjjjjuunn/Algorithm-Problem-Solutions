test_case = int(input())

case = [input() for _ in range(test_case)]

for i in range(test_case):
    print(f'{case[i][0]}{case[i][-1]}')