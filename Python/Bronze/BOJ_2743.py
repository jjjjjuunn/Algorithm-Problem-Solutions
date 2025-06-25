# 단어의 길이 구하기

# 방법 1: 내장 함수 len() 사용 (가장 간단하고 권장)
word = input()
print(len(word))

# 방법 2: len()을 사용하지 않고 for문으로 직접 세기
word = input()
count = 0
for _ in word:
    count += 1
print(count)

# 방법 3: len()을 사용하지 않고 while문 + 예외처리로 세기
word = input()
i = 0
while True:
    try:
        word[i]
        i += 1
    except IndexError:
        break
print(i)

# 각 방법 모두 정상 동작하며, for문/while문 방식은 직접 길이를 세는 원리를 이해하는 데 도움이 됩니다.
# 실전에서는 len()을 사용하는 것이 가장 간단하고 효율적입니다.