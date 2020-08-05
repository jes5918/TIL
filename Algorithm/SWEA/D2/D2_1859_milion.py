# def mil(lists):
#     zero = sorted(lists, reverse = 1) # 수익이 0 일때의 판별식
#     if zero == lists:
#         return 0
    
#     result = 0
#     while True:
#         max_idx = lists.index(max(lists))  # 리스트의 가장 최댓값의 위치를 불러온다
#         lefts = lists[0:max_idx]       # 리스트의 최댓값 위치의 왼쪽부분을 잘라서
#         for left in lefts:              # max - 각각의 값 수익을 더한다
#             result += (lists[max_idx] - left)   
#         lists = lists[max_idx+1:]      # 수익을 더하는 것이 완료되면 오른쪽 부분을 짤라 다시 리스트에 넣는다.
#         if not lists:
#             break
#     return result

# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     li = list(map(int, input().split()))
#     print(f'#{tc} {mil(li)}')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    li = list(map(int, input().split()))
    profit = 0
    MAX = li[-1]
    for x in range(N-2, -1, -1):
        if MAX > li[x]:
            profit += (MAX - li[x])
        else:
            MAX = li[x]
    
    print(f'#{tc} {res}')

