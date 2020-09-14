index_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
string = input()
cnt = 0
i = 0
while i < len(string):
    if string[i:i+3] in index_list:
        cnt += 1
        i += 3
    elif string[i:i+2] in index_list:
        cnt += 1
        i += 2
    else:
        cnt += 1
        i += 1
print(cnt)
