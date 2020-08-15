T = int(input())
for tc in range(1, T+1):
    N = int(input()) # str로 바로 받을까 생각했는데 숫자의 연산이 이루어져야 하기 때문에 우선 숫자로 받는다.
    
    index = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'} # 비교를 하기 위해 인덱스를 설정!
    temp = [] # 빈 리스트 초기화
    step = 0 # 단계 초기화
    
    while True: 
        step += 1 # 몇단계 까지 갈까
        num = N * step # num = 입력값 * 단계, 여기서 숫자의 연산이 이루어져야 하기 때문에 처음에 N을 인트로 받은것
        
        num_str = str(num) # set이랑 비교하기 위해서는 int를  str로 바꿔줘야한다
        temp.extend(num_str) # temp에 계속 추가하자 
       
        res = set(temp) # 중복제거하기위해 set을 사용  
        if res == index: # 중복제거한 결과와 인덱스 비교해서 같으면 와일문 탈출
            break 
    print(f'#{tc} {num}')