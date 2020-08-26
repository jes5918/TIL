'''
3 3
1 2 3
4 5 6
7 8 9
'''

N, M = map(int, input().split())
mylist = [list(map(int, input().split())) for _ in range(N)]
print(mylist)