for t in range(1,11):
    planarization= int(input())
    T = list(map(int,input().split()))
    index1 = 0
    index2 = 0
    for j in range(0,planarization):
        if (max(T) - min(T)) <= 1:
            break
        index1 = T.index(max(T))
        index2 = T.index(min(T))
        T[index2] += 1
        T[index1] -= 1
    result = max(T) - min(T)
    print(f'#{t} {result}')