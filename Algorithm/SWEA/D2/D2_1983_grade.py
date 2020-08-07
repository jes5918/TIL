T = int(input())
for tc in range(1, T+1):
    N, target = map(int, input().split())
    gradeindex = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    grade = [0] * 3
    res_grade = [0] * N
    for i in range(N):
        grade[0], grade[1], grade[2] = map(int, input().split())
        res_grade[i] = round((grade[0]*0.35) + (grade[1]*0.45) + (grade[2]*0.20), 2)
    
    target_score = res_grade[target-1]
    res_grade.sort(reverse=True)
    result = gradeindex[res_grade.index(target_scoree) // (N // 10)]
    
    print(f'#{tc} {result}')