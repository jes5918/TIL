T = int(input())
list_num = list(map(int, input().split()))
sorted_num = sorted(list_num)
print(sorted_num)
print(sorted_num[round(T/2)-1])