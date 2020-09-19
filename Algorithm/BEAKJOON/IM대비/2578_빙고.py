from collections import deque

def check():
    count = 0
    cross1 = 0
    cross2 = 0
    for x in range(5):
        if sum(bingo[x]) == 0:
            count += 1
            if count == 3:
                return count
        if sum(list(zip(*bingo))[x]) == 0:
            count += 1
            if count == 3:
                return count
        if bingo[x][x] == 0:
            cross1 += 1
        if bingo[x][4-x] == 0:
            cross2 += 1
    if cross1 == 5:
        count += 1
        if count == 3:
            return count
    if cross2 == 5:
        count += 1
        if count == 3:
            return count

bingo = [[int(x) for x in input().split()] for _ in range(5)]
numbers = deque()
for i in range(5):
    numbers.extend([int(x) for x in input().split()])

cnt = 0
while numbers:
    n = numbers.popleft()
    cnt += 1
    flag = False
    for i in range(5):
        for j in range(5):
            if bingo[i][j] == n:
                bingo[i][j] = 0
                flag = True
                break
        if flag:
            break

    if cnt >= 12:
        if check() == 3:
            break
print(cnt)

