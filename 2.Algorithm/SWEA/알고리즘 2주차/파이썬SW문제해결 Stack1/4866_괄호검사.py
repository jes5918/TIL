import sys
sys.stdin = open("input.txt", "r")

def discrim(lists):
    for i in range(len(lists)):
        if lists[i] == '(' or lists[i] == '{':
            stack.append(lists[i])
        elif lists[i] == ')' or lists[i] == '}':
            if len(stack) == 0:
                return 0
            elif (lists[i] == "}" and stack[-1] != "{") or (lists[i] == ")" and stack[-1] != "("):
                return 0
            else:
                stack.pop()
    if stack: return 0
    else: return 1

for tc in range(1, int(input())+1):
    string_list = list(input())
    stack = []
    result = discrim(string_list)
    print('#{} {}'.format(tc, result))