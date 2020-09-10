import sys
sys.stdin = open("input.txt", "r")

for tc in range(1, int(input())+1):
    str1 = input()
    stack = []
    for i in str1:
        if len(stack) == 0:
            stack.append(i)
        else:
            if i == stack[-1]:
                stack.pop()
            else:
                stack.append(i)
    print('#{} {}'.format(tc, len(stack)))
