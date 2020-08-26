import sys

#sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = input()
    M = input()
    word = {}
    for n in N:
        if n in word.keys():
            pass
        else:
            word[n] = M.count(n)
    vlaues = list(word.values())
    result = max(vlaues)
    print(f'#{test_case} {result}')