T = int(input())
for tc in range(1, T+1):
    N = int(input()) 
    stone_throw = list(map(int, input().split())) # 입력데이터를 받자 받자
    min_stone = abs(stone_throw[0]) # 첫번째 입력데이터의 절댓값을 변수에 저장
    cnt = 0 # 최소데이터가 몇번 나오는지 카운트 하기 위해 존재
    for stone in stone_throw: # 리스트를 하나씩 까보자
        if min_stone > abs(stone): # 꺼낸 데이터의 절댓값이 최솟값보다 작으면
            cnt = 1 # 카운트 1로 초기화
            min_stone = abs(stone) # 최솟값에 꺼낸 데이터의 절댓값 저장
        elif min_stone == abs(stone): # 최솟값 데이터와 꺼낸 데이터의 값이 같다면
            cnt += 1 # 카운트 +1 
    print(f'#{tc} {min_stone} {cnt}')