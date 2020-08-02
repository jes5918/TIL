# import sys
# a = sys.stdin.readline() # 한개의 문자를 받는다.
# b = int(sys.stdin.readline()) # 한개의 문자를 받아 숫자로 변환시켜줌
# c = sys.stdin.readline().split() # 띄어쓰기를 이용하여 여러개의 문자를 받아 리스트로 만들어준다
# d = map(int, sys.stdin.readline().split()) # 여러개의 문자를 입력받아 숫자로 반환

# print(type(a))
# print(a)
# print(type(b))
# print(b)
# print(type(c))
# print(c)
# print(type(d))
# print(d)

import sys
a = sys.stdin.readline()
print(type(a))
print(a)
print('여기가 끝이다.')


# import sys
# T = int(sys.stdin.readline())
# for i in range(T):
#     a = map(int, sys.stdin.readline().split())
#     print(sum(a))