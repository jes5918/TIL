import sys
sys.stdin = open('5120.txt', 'r')

for tc in range(1, int(input())+1):
    N, M, K = map(int, input().split())
    numbers = list(map(int, input().split()))
    x = M
    while True:
        while K != 0:
            if N < x:
                temp = x - N
                break
            if N == x:
                numbers.append(numbers[-1] + numbers[0])
                temp = M - 1
                N += 1
                K -= 1
                break
            numbers[x:0] = [numbers[x-1] + numbers[x]]
            N += 1
            x += M
            K -= 1
        if K == 0:
            break
        x = temp
    # print('#{} {}'.format(tc, ' '.join(str(x) for x in numbers[-1:-11:-1])))
    print('#{} '.format(tc), end='')
    print(*numbers[-1:-11:-1])


# 다음과 같이 풀수도 있다.
#     idx = 0
#     for _ in range(1, K+1):
#         idx += M
#         # 문자열 길이보다 작을경우
#         if idx < N:
#             numbers.insert(idx, arr[idx-1] + numbers[idx])
#         # 문자열 길이보다 클 경우
#         else:
#             if idx % N:
#                 idx = idx % N
#                 numbers.insert(idx, numbers[idx - 1] + numbers[idx])
#             # idx를 N으로 나눴을 때 0이 아니라면
#             else:
#                 numbers.insert(idx, numbers[- 1] + numbers[0])
#         N += 1
