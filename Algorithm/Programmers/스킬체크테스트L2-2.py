def solution(prices):
    answer = []

    q = prices[:]

    while q:
        price = q.pop(0)
        res = 0
        for n in q:
            res += 1
            if price > n:
                break
        answer.append(res)

    return answer

print(solution([1,2,3,2,3]))