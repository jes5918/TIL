print((lambda x, y: x+y)(3, 5))
add = lambda x, y: x+y

print(add(3, 5))


ans = [[2, 4], [2, 34], [1, 43]]
num = sorted(ans, key=lambda x: x[0])
print(num)