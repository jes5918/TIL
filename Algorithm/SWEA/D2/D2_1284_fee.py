'''
P : A사의 1L당 요금
Q : B사의 기준점 이하 요금(기준요금)
R : B사의 기준점
S : B사의 기준점 이상 요금(L당요금)
W : 삼성전자 사원 종민이의 수도 사용량(L)
'''

T = int(input())
for tc in range(1, T + 1):
    P, Q, R, S, W = map(int, input().split())
    
    # A사의 수도요금 계산 
    fee_a = P * W
    
    # B사의 수도요금 계산
    if W >= R: # 기준점 이상일때 요금
        fee_b = Q + ((W - R) * S)
    
    else:  # 기준점 이하일때 요금
        fee_b = Q 
    
    # python 시험준비하면서 배운 한줄작성을 써보자
    print(f'#{tc} {fee_b}') if fee_a >= fee_b else print(f'#{tc} {fee_a}') 