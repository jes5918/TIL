import sys

sys.stdin = open('input6.txt', 'r')


def gotohome(x, total, n):
    global result
    if total >= result:
        return
    if n == 0:
        last = (company_x, company_y)
    else:
        last = customer[x]
    if 0 not in visited:
        total += abs(last[0] - home_x) + abs(last[1] - home_y)
        if total < result:
            result = total
        return
    for i in range(len(customer)):
        if not visited[i]:
            visited[i] = 1
            now = customer[i]
            gotohome(i, total + abs(last[0] - now[0]) + abs(last[1] - now[1]), n+1)
            visited[i] = 0


for tc in range(1, int(input().rstrip()) + 1):
    N = int(input().rstrip())
    input_li = list(map(int, input().rstrip().split()))
    company_x, company_y = input_li[0], input_li[1]
    home_x, home_y = input_li[2], input_li[3]
    customer = []
    for x in range(4, 2*N+4, 2):
        customer.append((input_li[x], input_li[x + 1]))
    result = 987654321
    visited = [0] * N
    gotohome(0, 0, 0)
    print('#{} {}'.format(tc, result))
