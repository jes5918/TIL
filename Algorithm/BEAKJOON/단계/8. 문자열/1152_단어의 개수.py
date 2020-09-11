string = input()
a = string.split(' ')
cnt = 0
for aa in a:
    if aa == '':
        cnt += 1
print(len(string.split(' ')) - cnt)