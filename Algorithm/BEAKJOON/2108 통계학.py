import sys
from collections import Counter

numbers = []
for i in range(int(sys.stdin.readline())):
    numbers.append(int(sys.stdin.readline()))

res = round(sum(numbers) / len(numbers))
print(res)

nums2 = numbers[:]
nums2.sort()
res = nums2[len(nums2) // 2]
print(res)

nums = numbers[:]
nums.sort()
nums_s = Counter(nums).most_common()
if len(nums_s) > 1:
    if nums_s[0][1] == nums_s[1][1]:
        print(nums_s[1][0])
    else:
        print(nums_s[0][0])
else:
    print(nums_s[0][0])

res = max(numbers) - min(numbers)
print(res)