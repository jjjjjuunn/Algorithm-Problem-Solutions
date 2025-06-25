# 바구니 뒤집기
# 슬라이싱한 리스트에 reverse를 써도 원본 리스트는 바뀌지 않는다.
# 원본을 바꾸려면 슬라이스에 할당해야 한다.
# [::-1]은 파이썬에서 리스트, 문자열을 뒤집을 때 가장 많이 쓰이는 간단하고 강력한 문법.
# 코딩 테스트와 실전 코드 모두에서 자주 사용된다.

M, N = map(int, input().split())
arr = [num + 1 for num in range(M)]

# 방법 1: [::-1]을 사용한 구간 뒤집기 (추천)
for _ in range(N):
    i, j = map(int, input().split())
    arr[i-1:j] = arr[i-1:j][::-1]

print(*arr)

'''
# 방법 2: [::-1]을 사용하지 않고 직접 swap으로 구현 (동일한 결과, 실전에서도 사용 가능)
M, N = map(int, input().split())
arr = [num + 1 for num in range(M)]
for _ in range(N):
    i, j = map(int, input().split())
    left, right = i-1, j-1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
print(*arr)
'''