import sys
sys.stdin = open("input1.txt", "r")

for tc in range(1, int(input())+1):
    temp = list(input().split())
    stack = []
    res = 0
    for i in range(len(temp)-1):
        if temp[i].isdigit():
            stack.append(temp[i])
        else:
            try:
                n2 = int(stack.pop())
                n1 = int(stack.pop())
                if temp[i] == "+":
                    result = n1 + n2
                elif temp[i] == "-":
                    result = n1 - n2
                elif temp[i] == "*":
                    result = n1 * n2
                elif temp[i] == "/":
                    result = n1 // n2
                stack.append(result)
            except:
                res = 'error'
    if res == 0 and len(stack) == 1:
        print('#{} {}'.format(tc, stack.pop()))
    elif res == 'error' or len(stack) > 1:
        print('#{} error'.format(tc))