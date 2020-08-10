a = 1
def f1():
    a = 5
    def f2():
        print(a, end='')
    f2()
f1()
print(a)