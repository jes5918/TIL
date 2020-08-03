list=[0, 1, 3, 5, 7, 9, 10] # 3 => 3
k = 3
base = 0
for li in list:
    if li - base == k:
        count += 1
        base = li
    elif li - base > k:
        base = 


# 0 4 7 9 14 17 20    # 5 => 4
# 7 5 7 8 6

# 0 1 2 3 4 5 6 7 10  # 4
# 2 2 2 2 2 2 4