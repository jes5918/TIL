print(int(3.5))
print(int(4.5))
print(round(3.5))
print(round(4.5))
print(3.5 / 1)
print(-3.5 // 1)
print(int(-3/2))
# import sys
#
# sys.stdin = open('input.txt', 'r')
#
def calculate(idx, now, res):
    if idx == 0:
        nres = res + nums[now + 1]
    elif idx == 1:
        nres = res - nums[now + 1]
    elif idx == 2:
        nres = res * nums[now + 1]
    elif idx == 3:
        nres = int(res / nums[now + 1])
    return nres


def makingnum(x, res):
    if x == N-1:
        result.append(res)
        return
    for i in range(4):
        if operator[i]:
            operator[i] -= 1
            makingnum(x + 1, calculate(i, x, res))
            operator[i] += 1


for tc in range(1, int(input().rstrip()) + 1):
    N = int(input().rstrip())
    operator = list(map(int, input().rstrip().split()))
    nums = list(map(int, input().rstrip().split()))
    result = []
    makingnum(0, nums[0])
    print('#{} {}'.format(tc, max(result) - min(result)))
