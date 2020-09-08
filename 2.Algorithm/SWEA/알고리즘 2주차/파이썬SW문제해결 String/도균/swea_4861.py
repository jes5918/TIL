import sys

sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    words = [input() for _ in range(N)]
    res = []
    # 가로 회문 검사.
    for w in words:
        for i in range(N-M+1):
            if w[i:i+M] == w[i:i+M][::-1]:
                res = w[i:i + M]
    if res is True:
        print('#{} {}'.format(test_case, res))
    else:
        vertical = []
        for x in range(N):
            v = ''
            for y in range(N):
                v += words[y][x]
            vertical.append(v)
        
        for v_data in vertical:
            for j in range(N-M+1):
                if v_data[j:j+M] == v_data[j:j+M][::-1]:
                    res = (v_data[j:j + M])
        
        print('#{} {}'.format(test_case, res))
        # 세로 회문 검사.

                         