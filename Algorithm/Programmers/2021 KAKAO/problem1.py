def solution(new_id):
    def fisrt(id):
        id = id.lower()
        return id


    def second(id):
        index_second = list('~!@#$%^&*()=+[{]}:?,<>')
        temp = ''
        for i in id:
            if i not in index_second:
                temp += i
        return temp


    def thrid(id):
        res = ''
        flag = False
        for i in id:
            if i == '.' and not flag:
                res += i
                flag = True
                continue
            elif i == '.' and flag:
                continue
            else:
                flag = False
                res += i
        return res


    def fourth(id):
        temp = id
        if id[0] == '.':
            temp = temp[1:]
        if id[-1] == '.':
            temp = temp[:len(temp)-1]
        return temp


    def fifth(id):
        if not id:
            id += 'a'
        return id


    def sixth(id):
        if len(id) >= 16:
            id = id[:15]
            if id[-1] == '.':
                id = id[:14]
        return id


    def seventh(id):
        if len(id) <= 2:
            temp = id[-1]
            while len(id) < 3:
                id += temp
        return id


    answer = fisrt(new_id)
    answer = second(answer)
    answer = thrid(answer)
    answer = fourth(answer)
    answer = fifth(answer)
    answer = sixth(answer)
    answer = seventh(answer)
    return answer

print(solution('...!@BaT#*..y.abcdefghijklm'))
print(solution("z-+.^."))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))