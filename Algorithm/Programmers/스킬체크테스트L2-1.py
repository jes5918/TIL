def solution(n):
    answer = 0
    n_count = bin(78)[2:].count('1')
    for i in range(n, n*n):
        if bin(i)[2:].count('1') == n_count:
            answer = i
    return answer