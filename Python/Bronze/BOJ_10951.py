#Python에서 EOF 조건 처리하는 법
# 입력이 더 이상 없을 때 예외가 발생하는 것을 이용
# try-except로 EOFError 또는 ValueError를 잡아준다.
import sys

input = sys.stdin.readline

while True:
    try:
        a,b = map(int, input().split())
        print(a+b)

    except:
        break
