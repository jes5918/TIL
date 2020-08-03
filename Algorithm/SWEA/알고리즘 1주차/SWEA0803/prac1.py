from random import*

def build_data():
    for i in range(0, 100):
        data[i]=randint(0, 100)


data=[0]*100
for i in range(0, 100):
    build_data()

MAX = 0
for i in range(100):
    cnt = 0
    for j in range(i+1, 100):
        if data[i] > data[j]:
            cnt += 1
    if MAX < cnt:
        MAX = cnt
print(MAX)