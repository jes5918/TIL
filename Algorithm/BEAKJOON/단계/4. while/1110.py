import sys

def pluscycle(a, b, count):
    count += 1
    c = b
    d = (a + b) % 10 
    if digit_10 == c and digit_1 == d:
        return count
    else:
        return pluscycle(c, d, count)

number = int(sys.stdin.readline())
count = 0
digit_10 = number // 10
digit_1 = number % 10
if 0 <= number < 100:
    print(pluscycle(digit_10, digit_1, count))
else:
    print('0보다 크거나 같고, 99보다 작거나 같은 정수를 입력하세요')