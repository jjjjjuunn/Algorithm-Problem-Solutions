# 킹, 퀸, 룩, 비숍, 나이트, 폰

K,Q,L,B,N,P = map(int,input().split())

print(1-K,1-Q,2-L,2-B,2-N,8-P)

# 방법 2 : join()과 zip()을 이용한 간결한 버전 및 유지보수성 개선
'''
pieces = [1, 1, 2, 2, 2, 8]
current = list(map(int,input().split()))

print(' '.join(str(p-c) for p, c in zip(pieces, current)))
'''

