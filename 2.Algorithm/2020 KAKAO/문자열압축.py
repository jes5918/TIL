import sys
sys.stdin = open('test.txt', 'r')

def solution(s):
    answer = 123456789
    for i in range(1, (len(s)//2)+2):
        temp = ''
        step = 0
        cnt = 1
        while step < len(s):
            if s[step:step+i] == s[step+i:step+(i*2)]:
                cnt += 1
            elif cnt <= 1:
                temp += s[step:step+i]
                cnt = 1
            else:
                temp += str(cnt) + s[step:step+i]
                cnt = 1
            step += i
        if answer > len(temp):
            answer = len(temp)
    return answer

for _ in range(5):
    ss = input()
    print(solution(ss))
