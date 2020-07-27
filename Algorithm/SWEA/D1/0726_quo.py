T = int(input())
for tc in range(1, T + 1):
    a, b = input().split()
    a = int(a)
    b = int(b)
	quo = a // b
    rem = a % b
    print(f'#{tc} {quo} {rem}')