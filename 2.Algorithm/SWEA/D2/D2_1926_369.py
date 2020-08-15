"""
1. N로 어디까지 369할건지 입력받는다. (10 <= N <=1000)
2. for문을 이용해서 차례대로 프린트한다.
3. if 1의자리 10의자리 100의자리
1의자리 i % 3 == 0
2의자리 i % 3 == 0 and (i//10) % 3 ==0 2번

"""
# 아래 코딩은 너무 하드하다
# N = int(input())
# for i in range(1, N+1)
#     if 0 < i <= 10:
#         if i % 3 != 0:
#             print(i, end=' ')
#         else:
#             print('-', end=' ')
#     elif 10 < i <= 100:
#         if (i//10) % 3 != 0 and i % 3 != 0:
#             print(i, end=' ')
#         elif (i//10) % 3 != 0 and i % 3 == 0:
#             print('-', end=' ')
#         elif (i//10) % 3 == 0 and i % 3 != 0:
#             print('-', end=' ')
#         elif (i//10) % 3 == 0 and i % 3 == 0:
#             print('--', end=' ')
#     else:
#         if (i//10) % 3 != 0 and i % 3 != 0:
#             print(i, end=' ')
#         elif (i//10) % 3 != 0 and i % 3 == 0:
#             print('-', end=' ')
#         elif (i//10) % 3 == 0 and i % 3 != 0:
#             print('-', end=' ')
#         elif (i//10) % 3 == 0 and i % 3 == 0:
#             print('--', end=' ')
def game369(a):
    count = 0
    for x in range(len(a)):
        if "3" in a[x] or "6" in a[x] or "9" in a[x]:
            count += 1   

    if count == 1:  
        return '-'
    elif count == 2:
        return '--'
    elif count == 3:
        return '---'
    else:
        return i

N = int(input())
for i in range(1, N+1):
    a = list(str(i))
    print(game369(a), end=' ')

""" 아래는 제타위키에 올라온 답안... 미쳤다.

T = int(input())
for i in range(1, T+1):
    s = sum(1 for x in str(i) if x in ['3','6','9'])
    if s==0:
        print( i, end=' ' )
    else:
        print( '-'*s, end=' ' )

#
# 
# i = int(input())
s = (1 for x in str(i) if x in ['3','6','9'])
print(s)
print(type(s))
print(sum(s))

class<generator>가 뭘까? 꼭 찾아봐라
https://wikidocs.net/16069

"""