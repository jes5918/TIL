Q = [0] * 3
front, rear = -1, -1

def enQueue(item):
    global rear
    if rear == len(Q) - 1:
        print('Queue Full')
    else:
        rear = rear + 1
        Q[rear] = item

def deQueue():
    global front
    if front == rear:
        print('Queue Empty')
    else:
        front += 1
        return Q[front]

def Qpeek():
    if front == rear:
        print('Queue Empty')
    else:
        return Q[front+1]

enQueue(1)
enQueue(2)
enQueue(3)
print(Qpeek())
print(deQueue())
print(deQueue())
print(deQueue())
print(Q)
