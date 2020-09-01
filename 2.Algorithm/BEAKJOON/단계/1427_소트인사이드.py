N = int(input())
a = []
while N:
    a.append(N % 10)
    N //= 10
a.sort()
b = 0
for i in range(len(a)):
    b += a[len(a)-i-1]
    b *= 10
print(b//10)
