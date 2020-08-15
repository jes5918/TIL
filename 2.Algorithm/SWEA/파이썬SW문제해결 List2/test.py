def selectionsort(li, x):
    for i in range(0, x):
        min_li = i
        for j in range(i, N):
             if li[min_li] > li[j]:
                 min_li = j
        li[i], li[min_li] = li[min_li], li[i]
    return li

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lists = list(map(int, input().split()))
    print(f'#{tc}', end=' ')
    cnt = 0
    sorted_lists = selectionsort(lists, 1)
    for a in range(N, N//2,-1):
        print(sorted_lists[N-1], end=' ')
        print(sorted_lists[N-a]), end=' ')
        cnt += 1
        if cnt >= 5:
            break
    print()