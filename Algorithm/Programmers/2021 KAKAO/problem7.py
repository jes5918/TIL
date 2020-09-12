def solution(sales, links):
    N = len(sales)
    L = [0] * (N + 1)
    R = [0] * (N + 1)
    P = [0] + sales
    for l in links:
        if not L[l[0]]:
            L[l[0]] = l[1]
        else:
            R[l[0]] = l[1]

    def PLR(x):
        temp = []
        if x in res:
            temp.append(P[x])
            # print(P[x])
            if L[x]:
                PLR(L[x])
                temp.append(P[L[x]])
            if R[x]:
                PLR(R[x])
                temp.append(P[R[x]])
            # print(temp)
            result.append(min(temp))

        if sum(result) > P[x]:
            return [P[R[x]]]
        return result

    res = [1]
    for i in range(2, N + 1):
        if L[i] and R[i]:
            res.append(i)
    result = []
    ans = PLR(1)
    answer = sum(ans)
    return answer


print(solution([14, 17, 15, 18, 19, 14, 13, 16, 28, 17], [[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]]))
print(solution([5, 6, 5, 3, 4], [[2, 3], [1, 4], [2, 5], [1, 2]]))
print(solution([5, 6, 5, 1, 4], [[2, 3], [1, 4], [2, 5], [1, 2]]))
print(solution([10, 10, 1, 1], [[3, 2], [4, 3], [1, 4]]))
