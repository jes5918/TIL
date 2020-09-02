SIZE = 4
Q = [0] * SIZE
front, rear = 0, 0

def enQueue(item):
    global rear
    if (rear+1) % SIZE == front:
        print('Queue Full')
    else:
        rear = (rear+1) % SIZE
        Q[rear] = item

def deQueue():
    global front
    if front == rear:
        print('Queue Empty')
    else:
        front = (front + 1) % SIZE
        return Q[front]

def Qpeek():
    if front == rear:
        print('Queue Empty')
    else:
        return Q[(front + 1) % SIZE]

enQueue(1)
enQueue(2)
enQueue(3)

print(deQueue())
print(deQueue())
print(deQueue())
print(Q)
