for _ in range(int(input())):
    arr = input()
    cnt = 0
    count = 0
    for i in range(len(arr)):
        if arr[i] == 'O':
            cnt += 1
            count += cnt
        elif arr[i] == 'X':
            cnt = 0
    print(count)
