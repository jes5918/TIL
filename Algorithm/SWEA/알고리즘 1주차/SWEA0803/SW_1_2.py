"""
1. 답을 리스트화 한다
2. cnt = int(input()), cnt -= 1, if cnt == 0 그만
3. enumerate 사용 max(li)의 idx, key 찾고 그 값에 -1
4. enumerate 사용 min(li)의 idx, key 찾고 그 값에 +1
5. max(li)-min(li) 출력

"""
for t in range(1, 11):
    N = int(input())
    li = list(map(int, input().split()))
    
    while max(li) - min(li) > 1 and N > 0:   
        li[li.index(max(li))] -= 1
        li[li.index(min(li))] += 1  
        N -= 1   
    print(f'#{t} {max(li)-min(li)}')