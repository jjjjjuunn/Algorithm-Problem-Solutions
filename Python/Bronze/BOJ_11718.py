# 그대로 출력하기 (BOJ 11718) / 복습 필요
# 입력받은 모든 줄을 한 번에 출력하는 대표적인 방법들

'''
# 방법 1: 리스트에 저장 후 join으로 한 번에 출력 (가장 파이썬다운 방식)
lines = []
while True:
    try:
        line = input()
        if line == '':  # 빈 줄 입력 시 종료 (필요에 따라 생략 가능)
            break
        lines.append(line)
    except EOFError:
        break
print('\n'.join(lines))  # 마지막 줄에 불필요한 줄바꿈이 추가되지 않음
'''

# 방법 2: sys.stdin을 활용해 입력을 한 번에 출력 (대량 입력, 빠른 처리에 적합)
import sys
for line in sys.stdin:
    print(line, end='')  # 입력 그대로 출력 (줄바꿈 포함)

# 정리:
# - join 방식은 입력을 모두 저장한 뒤 원하는 형식으로 한 번에 출력할 때 유용
# - sys.stdin 방식은 입력이 많을 때 빠르고, 입력 그대로 출력할 때 적합
# - 상황에 따라 두 방법 모두 실전에서 널리 사용됨