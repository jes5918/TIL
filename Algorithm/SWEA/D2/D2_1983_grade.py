T = int(input())
for tc in range(1, T+1):
    N, target = map(int, input().split())
    grade = [0] * 3
    res_grade = [0] * N
    for i in range(N):
        grade[0], grade[1], grade[2] = map(int, input().split())
        res_grade[i] = round((grade[0]*0.35) + (grade[1]*0.45) + (grade[2]*0.20), 2)
    
    sorted_grade = sorted(res_grade)
    for i in range(n/10):
        a[i] = sorted_grade[i*10:(i+1)*10]
    
    
    if sorted_grade[i:N/10] < N:

    res_grade[target-1]


    print(f'#{tc} {result}')