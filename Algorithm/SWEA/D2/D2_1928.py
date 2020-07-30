# from base64 import b64decode

# T = int(input())
# for tc in range(1, T+1):
#     print(f'#{tc} {b64decode(input()).decode("UTF-8")}')

def make_bin(z):
    result = bin(z)[2:]
    result = '0'*(6-len(result)) + result
    return result

T = int(input())
index ='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
for test_case in range(1, T + 1):
    code = input()
    result = ''
    for x in range(0, len(code), 4):
        binarystring = ''
        word = code[x:x+4]
        for y in range(4):
            binarystring += make_bin(index.find(word[y]))
        
        result += chr(int(binarystring[:8], 2))
        result += chr(int(binarystring[8:16], 2))
        result += chr(int(binarystring[16:], 2))
    print(f'#{test_case} {result}')
