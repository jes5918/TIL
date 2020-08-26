# for tc in range(1, int(input()) + 1):
#     string1 = input()
#     string2 = input()
#     res = 0
#     for i in range(len(string2)-len(string1)+1):
#         if string1 == string2[i:i+len(string1)]:
#             res = 1
#     print(f'#{tc} {res}')
    
# 보이어-무어 알고리즘 사용
# 1. 두 문자열을 정렬한 후 짧은 문자열의 뒤에서부터 비교
# 2. 짧은 문자열과 모두 일치하면 1을 출력
# 3. 다른 문자가 있다면 해당 문자가 짧은 문자열에 존재하는지 조사
# 4.   존재한다면 같은 문자를 기준으로 두 문자열을 정렬 -> 1
# 5.   없다면 짧은 문자열의 길이만큼 오른쪽으로 이동하여 두 문자열 정렬 -> 1   
 
t = int(input())
for i in range(t):
    short = input()
    long = input()
    ln_s, ln_l = len(short), len(long)
    cnt = 0

    while cnt < ln_l - ln_s + 1:
        for j in range(ln_s):
            xxx = ln_s-1 - j
            if long[cnt+xxx] != short[xxx]:
                break
        else:
            result = 1
            break

        for k in range(len(short[:xxx])):
            if short[xxx-1-k] == long[cnt+xxx]:
                cnt += k+1
                break
        else:
            cnt += xxx+1

        result = 0

    print("#{} {}".format(i+1, result))