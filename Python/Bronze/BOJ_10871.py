# X보다 작은 수
#정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.

# ' '.join(리스트)은 리스트의 각 요소를 공백으로 이어붙여 하나의 문자열로 만든다.
# 리스트 안에 문자열이 여러 개 있을 때, 각 요소 사이에 지정한 구분자를 넣어서 합친다.
# join은 문자열(str)끼리만 사용할 수 있다.
N,X = map(int,input().split())
arr = list(map(int,input().split()))

print(' '.join(str(num) for num in arr if num<X))