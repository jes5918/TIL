def solution(orders, course):
    menus = []
    for order in orders:
        menus.extend(order)
    menus = sorted(list(set(menus)))

    def combi(k, menu):
        n = len(menu)
        temp = []
        for i in range(1 << n):
            sel = []
            for j in range(n):
                if i & (1 << j):
                    sel.append(menu[j])
            if len(sel) == k:
                temp.append(sel)
        return temp


    def kakao(order, comb):
        count = len(comb)
        count2 = 0
        for orde in order:
            cnt = 0
            for com in comb:
                for ord in orde:
                    if ord == com:
                        cnt += 1
            if cnt == count:
                count2 += 1
                resultist.append((comb, count2))

    result = []
    for c in course:
        resultist = []
        aa = combi(c, menus)
        for a in aa:
            kakao(orders, a)

        if resultist:
            resultist.sort(key=lambda x: -x[1])
            maxx = resultist[0][1]
            for r in resultist:
                if maxx == r[1]:
                    if r[1] < 2:
                        continue
                    result.append(''.join(r[0]))
                else:
                    break
    result.sort()
    return result




print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]))
print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))