T = int(input())
for tc in range(1, T + 1):
    N = int(input()) # 몇번 입력 넣을거니?!?
    now_velocity = 0 # 현재속도 초기화
    distance = 0 # 현재거리 초기화
    for n in range(N):  
        arr = list(map(int, input().split())) # 리스트로 입력받자
        
        if arr[0] == 0:    # arr[0]은 어떻게 조종할지 커맨드 0유지 , 1 가속,  2 감속 셋중하나 
            distance += now_velocity    # 현재 위치에 지금 속도 입력(1초 동안만 움직였다)
        
        elif arr[0] == 1: # 가속 커맨드 두두등장
            now_velocity += arr[1] # 현재속도에 얼마나 가속을 할지 더하자
            distance += now_velocity # 현재위치에 현재속도 더하기(1초 동안만 움직였다)
            
        elif arr[0] == 2: # 감속 커맨드 등장
            now_velocity -= arr[1] # 감속이니 빼준다
            if now_velocity < 0: # 만약 현재속도가 감속에 의해 0보다 작아지면
                now_velocity = 0 # 0값을 가져라
            distance += now_velocity # 현재위치에 현재속도 더하기(1초 동안만 움직였다)
        
    
    print(f'#{tc} {distance}')