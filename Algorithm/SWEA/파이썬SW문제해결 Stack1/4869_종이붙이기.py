for tc in range(1, int(input()) + 1):
    N = int(input())
    paper = [1, 3]
    for i in range(2, N//10):
        num = paper[i - 1] + paper[i - 2] * 2
        paper.append(num)
    print('#{} {}'.format(tc, paper[-1]))