number = [[], [], ['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I'], ['J', 'K', 'L'], ['M', 'N', 'O'],
          ['P', 'Q', 'R', 'S'], ['T', 'U', 'V'], ['W', 'X', 'Y', 'Z']]
A = input()
cnt = 0
for a in A:
    for i in range(10):
        if a in number[i]:
            cnt += i
cnt += len(A)
print(cnt)
