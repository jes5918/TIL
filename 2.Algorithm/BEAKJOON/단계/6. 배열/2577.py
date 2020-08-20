a = int(input())
b = int(input())
c = int(input())

num = a * b * c
num = str(num)

a = [0] * 10
for n in num:
    a[int(n)] += 1
for i in range(10):
    print(a[i])


# number = {}
# for n in num:
#     number[n] = number.get(n, 0) + 1
# res = sorted(number.items(), key=lambda x: x[0])

# for i in range(10):