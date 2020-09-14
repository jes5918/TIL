words = input()
cnt = 0
for i in range(len(words)):
    if words[i] == ' ':
        if i == 0:
            continue
        elif i == len(words)-1:
            continue
        cnt += 1
print(cnt + 1)