import sys
sys.stdin = open('계산기.txt', 'r')

for tc in range(1, 11):
    N = int(input())
    cal = input()
    stack = [] # 연산자들을 저장할 리스트
    res = [] # 결과값 저장 리스트(후입표기법 대로 저장됨)
    index_num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] # 숫자인지 확인하기 위한 인덱스

    # 입력받은 cal을 하나씩 까보자,,
    for i in range(N):
        # ICP => (  +-  */  ) 순서로 코드 작성
        # 여는괄호 : 가장 중요한 토큰... 계산의 시작
        if cal[i] == '(':
            stack.append(cal[i])
            continue

        # 숫자가 나오면 결과리스트에 저장
        elif cal[i] in index_num:
            res.append(cal[i])
            continue

        # 그다음 중요한 + (stack은 나중에 들어온것을 pop 하므로)
        elif cal[i] == '+':
            # 여는 괄호 나오면 stack에 저장 -> 마치 시작점이 계속해서 옮겨간다.
            if stack[-1] == '(':
                stack.append(cal[i])
                continue
            else:
                # 괄호 안을 파고드는 while
                while True:
                    if stack[-1] == '*' or stack[-1] == '+':
                        res.append(stack.pop())
                    # + 보다 뒤에 있는 ( 토큰이 나오면 반복문 나감
                    if stack[-1] == '(':
                        stack.append(cal[i])
                        break
                continue

        # 그다음 중요한 *
        elif cal[i] == '*':
            if stack[-1] == '(' or stack[-1] == '+':
                stack.append(cal[i])
                continue
            else:
                # 괄호 안을 파고드는 while
                while True:
                    if stack[-1] == '*':
                        res.append(stack.pop())
                    # *보다 뒤에 있는 (, + 토큰이 나오면 와일문 탈출
                    if stack[-1] == '(' or stack[-1] == '+':
                        stack.append(cal[i])
                        break
                continue

        # 닫히는 괄호 나오면  계산을 본격적으로 시작
        elif cal[i] == ')':
            while True:
                # 열리는 괄호 나오면 (괄호 사이에 다른 연산자 없으면)
                if stack[-1] == '(':
                    stack.pop()
                    break
                else:
                    res.append(stack.pop())

    # res에 후입표기법으로 저장되어 있는데 그것을 계산하는 식(swea 4874 계산기)
    for i in range(len(res)):
        if res[i].isdigit():
            stack.append(int(res[i]))
            continue
        else:
            n2 = stack.pop()
            n1 = stack.pop()
            if res[i] == '+':
                stack.append(n1 + n2)
            elif res[i] == '*':
                stack.append(n1 * n2)
    print("#{} {}".format(tc, stack[0]))





# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# q = ['', '+', '*', '(']
# op = ['(', '+', '*']
# T = 10
# for tc in range(1, T+1):
#     N = int(input())
#     formula = input()
#     operater = []
#     stack = []
#     for f in formula:
#         if f in numbers:
#             stack.append(f)
#         else:
#             if len(operater) == 0:
#                 operater.append(f)
#             elif len(operater) != 0:
#                 if f == ')':
#                     while operater[-1] != '(':
#                         stack.append(operater.pop())
#                     operater.pop()
#                 elif q.index(f) > op.index(operater[-1]):
#                     operater.append(f)
#                 else:
#                     while q.index(f) <= op.index(operater[-1]):
#                         stack.append(operater.pop())
#                     operater.append(f)
#
#     res = []
#     for s in stack:
#         if s in numbers:
#             res.append(int(s))
#         else:
#             b = res.pop()
#             a = res.pop()
#             if s == '*':
#                 res.append(a * b)
#             elif s == '+':
#                 res.append(a + b)
#     print('#{} {}'.format(tc, res[0]))