str1 = 'algorithm'

for i in range(len(str1)-1, -1, -1):
    print(str1[i], end='')

print()

str2 = str1[::-1]
print(str2)

str3 = reversed(str1)
print(''.join(str3))

n = len(str1)//2

str4 = list(str1)
for i in range(n):
    str4[i], str4[-1-i] = str4[-1-i], str4[i]
print(''.join(str4))