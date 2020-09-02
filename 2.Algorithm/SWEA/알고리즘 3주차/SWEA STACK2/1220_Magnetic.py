import sys
sys.stdin = open('mg.txt', 'r')


# 조건설명
# 배열 col로 탐색 위 -> 아래
# 1은 아래로 가야함, 2는 위로 가야함, 둘이 부딫히면 cnt += 1

# stack을 활용? 그냥 flag로 신호줘서 메모리 줄이는거도 가능한가?
# 열을 쭉 탐색하다가 1을 만나고, 이전에 1을 담아둔 stack이 없다면 stack에 1을 추가(반복적으로 1이 나오는 경우 무시할라구,,,)
# stack에 1이 들어있는 상태이고, 2를 만나게 된다면 stack을 초기화 하고 cnt 하나 세기
# 결과적으로 1과 2 직접적으로 만나는 세트만 카운트 하면댐!!

for tc in range(1, 11):
    N = int(input())
    mag = [[int(x) for x in input().split()] for _ in range(N)]
    cnt = 0
    for j in range(N):
        flag = False # stack = []로 바꿔도댐
        for i in range(N):
            if mag[i][j] == 1 and not flag:
                flag = True # stack.append(1)으로 바꿔도댐
            elif mag[i][j] == 2 and flag:
                flag = False # stack.pop()으로 바꿔도댐
                cnt += 1
    print('#{} {}'.format(tc, cnt))

# 구조교 코드
# for t in range(10):
#     b=[''.join(i)for i in zip(*[input().split()for _ in range(int(input()))])]
#     a=0
#     for i in b:
#         a+=i.replace('0','').count('12')
#     print('#{}'.format(t+1),a)

# 멍군이의 스트링코드,,,실행시간 훨 빠르당
# for tc in range(1, 11):
#     N = int(input())
#     mag = [list(input().split()) for i in range(N)]
#     mag = list(zip(*mag))
#     cnt = 0
#     for m in mag:
#         l = ''
#         for a in m:
#             if a == '1':
#                 l += a
#             elif a == '2':
#                 l += a
#         cnt += l.count('12')
#     print('#{} {}'.format(tc, cnt))

