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


E = 12
N = 11
arr = [1, 2, 1, 3, 2, 4, 3, 5, 3, 6, 4, 7, 5, 8, 5, 9, 6, 10, 6, 11, 7, 12, 11, 13]
L = [0] * 20
R = [0] * 20
P = [0] * 20
for i in range(0, len(arr), 2):
    p = arr[i]
    c = arr[i + 1]
    if L[p] == 0:
        L[p] = c
    else:
        R[p] = c
    P[c] = p

print('전위순회')
PLR(1)
print()
print('중위순회')
LPR(1)
print()
print('후위순회')
LRP(1)
