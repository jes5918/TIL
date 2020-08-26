def atoi(str1):
    num = 0
    for i in str1:
        num *= 10
        num += ord(i)-48
    return num

def itoa(num):
    line = ''
    tmp = num
    while tmp > 0:
        number = tmp % 10
        line = line + chr(number+ord('0'))
        tmp //= 10
    return line

line = 1234
str11 = '1234'
print(atoi(str11))
print(itoa(line))

