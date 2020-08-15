lists = input()
result = ''
for i in lists:
    if 97 <= ord(i) <= 122:
        result += chr(ord(i) - 32)
    else:
        result += i
print(result)