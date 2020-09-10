burgers = []
beverages = []
for i in range(3):
    burgers.append(int(input()))
for i in range(2):
    beverages.append(int(input()))
print(min(burgers) + min(beverages) - 50)    