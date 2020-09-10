arr = [[1,2,3], [4,5,6], [7,8,9]]
t = []
for i in range(3):
    sample = arr[i] # 가로
    t.append([a[i] for a in arr])

print(t)


