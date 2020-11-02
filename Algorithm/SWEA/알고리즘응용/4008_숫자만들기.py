import sys
from itertools import permutations

sys.stdin = open('input.txt', 'r')

# index_op = ['+', '-', '*', '/']
#
#
# def calculate(temp, arr):
#     num = temp[:]
#     a = num.pop(0)
#     while num or arr:
#         b, oper = num.pop(0), arr.pop(0)
#         if oper == '+':
#             a = a + b
#         elif oper == '-':
#             a = a - b
#         elif oper == '*':
#             a = a * b
#         elif oper == '/':
#             a = int(a / b)
#     return a
#
#
# for tc in range(1, int(input().rstrip()) + 1):
#     N = int(input().rstrip())
#     operator_input = list(map(int, input().rstrip().split()))
#     operator = []
#     for idx, value in enumerate(operator_input):
#         for _ in range(operator_input[idx]):
#             operator.append(index_op[idx])
#     nums = list(map(int, input().rstrip().split()))
#     calculate_list = []
#     res = []
#     for i in permutations(operator):
#         calculate_list.append(list(i))
#     for c in calculate_list:
#         res.append(calculate(nums, c))
#     result = max(res) - min(res)
#     print('#{} {}'.format(tc, result))

def make_number(x, total):
    if x == N-1:
        # print(total)
        if total < result[0]:
            result[0] = total
        if total > result[1]:
            result[1] = total
        return
    for i in range(4):
        if c[i]:
            c[i] -= 1
            if i == 0:
                make_number(x+1, total + number[x+1])
            elif i == 1:
                make_number(x+1, total - number[x+1])
            elif i == 2:
                make_number(x+1, total * number[x+1])
            elif i == 3:
                make_number(x+1, int(total / number[x+1]))
            c[i] += 1



for test_case in range(1, int(input()) + 1):
    N = int(input())
    sign = '+-*/'
    o_s = ''
    c = list(map(int,input().split()))
    for k in range(4):
        o_s += sign[k]*c[k]
    # 0번 인덱스는 min값, 1번 인덱스는 max값
    result = [10**12,-(10**12)]
    number = list(map(int,input().split()))
    # visited = [0]*(len(o_s))
    make_number(0, number[0])
    print('#{} {}'.format(test_case, result[1]-result[0]))
