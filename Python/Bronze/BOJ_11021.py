import sys

input = sys.stdin.readline
Test_case = int(input())

for i in range(Test_case):
    a,b = map(int,input().split())
    print(f'Case #{i+1}: {a+b}')