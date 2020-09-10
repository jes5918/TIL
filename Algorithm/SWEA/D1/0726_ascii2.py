lists = input()
res = ''
for i in lists:
    if 97 <= ord(i) <= 122:
        res += chr(ord(i) - 32)
    else:
        res += i
print(res)