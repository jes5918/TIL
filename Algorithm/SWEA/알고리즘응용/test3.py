import sys
sys.stdin = open('input6.txt')

for tc in range(1, int(input())+1):
    binary = input()
    ternary = input()
    bin_list = []
    ans = 0
    for i in range(len(binary)):
        if binary[i] == '1':
            temp = '0'
        else:
            temp = '1'
        bin_list.append(int(binary[:i] + temp + binary[i+1:], 2))
    for j in range(len(ternary)):
        for k in range(3):
            if ternary[j] == str(k):
                pass
            ter_num = int(ternary[:j] + str(k) + ternary[j+1:], 3)
            if ter_num in bin_list:
                ans = ter_num
    print('#{} {}'.format(tc, ans))