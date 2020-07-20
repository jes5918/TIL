#### 1. 세로로 출력하기
```python
number = int(input('자연수 number를 입력하세요 : '))
for i in range(1,number+1):
    print(i)
```

```python
자연수 number를 입력하세요 : 10
1
2
3
4
5
6
7
8
9
10
```



#### 2. 세로로 출력하기

```python
number = int(input('자연수 number를 입력하세요 : '))
for i in range(1,number+1):
    print(i, end = ' ')
```

```python
자연수 number를 입력하세요 : 10
1 2 3 4 5 6 7 8 9 10 
```



#### 3. 거꾸로 세로로 출력하기

```python
number = int(input('자연수 number를 입력하세요 : '))
while number != 0:
    print(number)
    number = number - 1
```

```python
자연수 number를 입력하세요 : 5
5
4
3
2
1
```



#### 4. 거꾸로 출력해 보아요

```python
number = int(input('자연수 number를 입력하세요 : '))
while number != 0:
    print(number, end = ' ')
    number = number - 1
```

```python
자연수 number를 입력하세요 : 5
5 4 3 2 1 
```



#### 5. N줄 덧셈

```python
number = int(input('자연수 number를 입력하세요 : '))
a = 1
sum = 0
if number <= 10000:
  while a != number+1:
    sum = sum + a
    a = a + 1
  print(sum)
else:
  print('10000이하의 숫자를 입력하세요')
```

```python
자연수 number를 입력하세요 : 10
55
```

