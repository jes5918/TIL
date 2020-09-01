def partition(a, begin, end):
    pivot = (begin + end) // 2
    L = begin
    R = end
    while L < R:
        while a[L]  < a[pivot] and L < R:
            L += 1
        while a[R] >= a[pivot] and L < R:
            R -= 1
        if L < R:
            if L == pivot:
                pivot = R
            a[L], a[R] = a[R], a[L]
        a[pivot], a[R] = a[R], a[pivot]
        return R

arr = list(map(int, input().split()))
print(arr)
s = arr[1]
e = arr[-1]
print(partition(arr, s, e))


def sol(x):
    for y in range(98,0,-1):
        if x and arr[y][x-1]:
            while x and arr[y][x-1]:
                x-=1
        elif x<99 and arr[y][x+1]:
            while x<99 and arr[y][x+1]:
                x+=1
    return x
for t in range(10):
    input()
    arr=[list(map(int,input().split()))for _ in range(100)]
    print('#{} {}'.format(t+1,sol(arr[99].index(2))))
