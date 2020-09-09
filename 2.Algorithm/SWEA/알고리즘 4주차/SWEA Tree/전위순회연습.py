import sys
sys.stdin = open('test.txt', 'r')

# 전위
def PLR(x):
    print(x, end=' ')
    if L[x]:
        PLR(L[x])
    if R[x]:
        PLR(R[x])

# 중위
def LPR(x):
    if L[x]:
        LPR(L[x])
    print(x, end=' ')
    if R[x]:
        LPR(R[x])

# 후위
def LRP(x):
    if L[x]:
        LRP(L[x])
    if R[x]:
        LRP(R[x])
    print(x, end=' ')

N = int(input())
arr = list(map(int, input().split()))
L = [0] * (N + 1)
R = [0] * (N + 1)
P = [0] * (N + 1)
for i in range(0, len(arr), 2):
    p = arr[i]
    c = arr[i + 1]
    if L[p] == 0:
        L[p] = c
    else:
        R[p] = c
    P[c] = p

# print(L)
# print(R)
# print(P)

print('전위 순회')
PLR(1)
print()

print('중위 순회')
LPR(1)
print()

print('후위 순회')
LRP(1)
print()
