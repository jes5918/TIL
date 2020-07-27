a, b = input().split()
if  a > b:
    if a == '3' and b == '1':
        print('B')
    else:
        print('A')
elif a < b:
    if a == '1' and b == '3':
        print('A')
    else:
        print('B')