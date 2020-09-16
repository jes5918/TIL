import sys
sys.stdin = open('input.txt', 'r')

# 위에거는 다른사람 코드,, 역시 딕셔너리가 빨라빨라 왜 그런지 찾아본다
from sys import stdin
read = stdin.readline

dic = {}
for i in range(1, int(read())+1):
    dic[i] = set()
for j in range(int(read())):
    a, b = map(int, read().split())
    dic[a].add(b)
    dic[b].add(a)

def dfs(start, dic):
    for i in dic[start]:
        print(i)
        if i not in visited:
            visited.append(i)
            dfs(i, dic)
visited = []
dfs(1, dic)
print(len(visited)-1)

# 내껀 파이참에선 돌아가는데 실행속도 때문에 백준에서는 안돌아간다,,
# def dfs(start_node):
#     global res
#     visited[start_node] = True
#     for i in range(1, K+1):
#         if not arr[start_node][i]:
#             continue
#         if visited[i]:
#             continue
#         dfs(i)
#         res += 1
#     return
#
# N = int(input())
# K = int(input())
# arr = [[False]*(N+1) for _ in range(N+1)]
# visited = [False]*(N+1)
# for i in range(K):
#     a, b = map(int, input().split())
#     arr[a][b] = True
# res = 0
# dfs(1)
# print(res)