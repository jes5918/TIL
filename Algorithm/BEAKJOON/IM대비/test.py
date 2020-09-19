def check():

    # 가로 체크
    cnt = 0
    cnt_check2 = 0
    cnt_check3 = 0
    for i in range(5):
        if arr[i].count(0) == 5:
            cnt += 1
            if cnt == 3:
                return cnt

    #세로 체크
        cnt_check = 0
        for j in range(5):
            if arr[j][i] == 0:
                cnt_check += 1
                if cnt_check == 5:
                    cnt +=1
                    if cnt == 3:
                        return cnt

    # 대각선 좌선체크
        for j in range(5):
            if i == j and arr[i][j] == 0:
                cnt_check2 += 1
                if cnt_check2 == 5:
                    cnt +=1
                    if cnt == 3:
                        return cnt
    # 대각선 우선체크
        for j in range(4,-1,-1):
            if arr[i][j] == 0:
                cnt_check3 +=1
                if cnt_check3 == 5:
                    cnt += 1
                    if cnt == 3:
                        return cnt



# 입력을 받자.
arr = [list(map(int,input().split())) for _ in range(5)]
soci = [list(map(int,input().split())) for _ in range(5)]
# 입력완료
#이제 체크를 하러가자
result = 0
res = 0
for i in range(5):
    for j in range(5):
        for a in range(5):
            for b in range(5):
                if soci[i][j] == arr[a][b]:
                    arr[a][b] = 0
                    res += 1

                    if check() == 3:
                        print(arr, res)
                        break