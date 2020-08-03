def maxmin(numbers):
    max_num = numbers[0]
    min_num = numbers[0]
    for number in numbers:
        if max_num < number:
            max_num = number
        if min_num > number:
            min_num = number
    return max_num - min_num

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    print(f'#{tc} {maxmin(numbers)}')