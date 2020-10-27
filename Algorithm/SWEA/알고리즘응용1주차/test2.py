num = 0x01D06079861D79F99F
binay_num = bin(num)[2:]
temp = (len(str(num))-2) * 4 - len(binay_num)
binay_num = '0' * temp + binay_num
for i in range(0, len(binay_num), 7):
    print(int(binay_num[i:i+7], 2))
