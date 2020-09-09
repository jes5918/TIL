import sys
sys.stdin = open('5177.txt', 'r')

def heappush(x):
    global heapcount
    heapcount += 1
    heap[heapcount] = x

    cur = heapcount
    parent = cur // 2

    while parent and heap[parent] > heap[cur]:
        heap[parent], heap[cur] = heap[cur], heap[parent]
        cur = parent
        parent = cur // 2

for tc in range(1, int(input())+1):
    N = int(input())
    temp = list(map(int, input().split()))
    heapcount = 0
    heap = [0] * (N + 1)
    for i in range(N):
        heappush(temp[i])
    res = 0
    while N:
        N //= 2
        res += heap[N]
    print('#{} {}'.format(tc, res))