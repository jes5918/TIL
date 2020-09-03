N = int(input())
flag = True
for i in range(int(N/2), N):
    if sum(map(int, str(i))) + i == N:
        print(i)
        flag = False
        break
if flag:
    print('0')