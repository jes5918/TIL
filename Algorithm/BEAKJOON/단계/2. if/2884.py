a, b = map(int, input().split())
if 1 <= a < 24:
    if 45 <= b < 60:
        print(a, b-45)
    else:
        print(a-1, b+15)
else:
    if 45 <= b < 60:
        print(a, b-45)
    else:
        print(a+23, b+15)
