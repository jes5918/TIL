### Generator?

>D2_1926 369게임 만들기 문제를 풀고 Pass 한뒤 제타위키를 찾아보았는데 매우 쉬운 방법으로 문제를 해결했다. 요지를 보니 제너레이터를 사용했다. 과연 무엇일까?

- 내가 코딩한 것

```python
def game369(a):
    count = 0
    for x in range(len(a)):
        if "3" in a[x] or "6" in a[x] or "9" in a[x]:
            count += 1   

    if count == 1:  
        return '-'
    elif count == 2:
        return '--'
    elif count == 3:
        return '---'
    else:
        return i

N = int(input())
for i in range(1, N+1):
    a = list(str(i))
    print(game369(a), end=' ')
```



- 제타위키 답안

```python
T = int(input())
for i in range(1, T+1):
    s = sum(1 for x in str(i) if x in ['3','6','9'])
    if s==0:
        print( i, end=' ' )
    else:
        print( '-'*s, end=' ' )
```



- 제너레이터가 뭘까?

```python
i = int(input())

s = (1 for x in str(i) if x in ['3','6','9'])

print(s)

print(type(s))

print(sum(s))
```

class<generator>가 뭘까? 꼭 찾아봐라

출처 : https://wikidocs.net/16069

## 1. Generator란?

- generator : iterator를 생성해주는 함수, 함수안에 yield 키워드를 사용함
- genrator 특징
  - iterable한 순서가 지정됨(모든 generator는 iterator)
  - 느슨하게 평가된다.(순서의 다음 값은 필요에 따라 계산됨)
  - 함수의 내부 로컬 변수를 통해 내부상태가 유지된다.
  - 무한한 순서가 있는 객체를 모델링할 수 있다.(명확한 끝이 없는 데이터 스트림)
  - 자연스러운 스트림 처리를 위 파이프라인으로 구성할수 있다.(Java에서 파일스트림 처리시에 특정 바이트단위로 반복하는 것을 말하는듯..)



## 2. Generator 간단하게 사용해보기

- REPL을 실행합니다.
- `yield` 키워드를 사용해 generator를 만들어 봅니다.
- `yield` 가 호출되면 암시적으로 return이 호출되며, 한번 더 실행되면 실행되었던 `yield' 다음 코드가 실행됩니다.

```
>>> def test_generator():
...     yield 1
...     yield 2
...     yield 3
... 
>>> gen = test_generator()
>>> type(gen)
<class 'generator'>
>>> next(gen)
1
>>> next(gen)
2
>>> next(gen)
3
>>> next(gen)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```

- 이렇게 생성한 genertaor는 iterable한 객체가 되며 for문에서 사용할 수 있습니다.

```
>>> import collections
>>> isinstance(gen, collections.Iterable)
True
>>> for i in test_generator():
...     print(i)
... 
1
2
3
```

- generator를 동시에 두개 생성하면, 서로가 다른 객체이며, 각기 따로 동작합니다.

```
>>> h = test_generator()
>>> i = test_generator()
>>> h == i
False
>>> h is i
False
>>> next(h)
1
>>> next(i)
1
>>> next(h)
2
>>> next(i)
2
>>> next(i)
3
>>> next(h)
3
```

- yield 사이에 추가로 코드를 입력해 동작을 확인해보겠습니다.
- yield 로 반환하는 사이사이의 코드들이 실행되었습니다.

```
>>> def test_generator():
...     print('yield 1 전')
...     yield 1
...     print('yield 1과 2사이')
...     yield 2
...     print('yield 2와 3사이')
...     yield 3
...     print('yield 3 후')
... 
>>> g = test_generator()
>>> next(g)
yield 1 전
1
>>> next(g)
yield 1과 2사이
2
>>> next(g)
yield 2와 3사이
3
>>> next(g)
yield 3 후
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```

- 그 때 그 때 생성되는 무한한 순서있는 객체를 모델링할 수 있습니다.
- 그리고 이렇게 무한하게 숫자를 리턴할 수있는 이유는 generator를 실행할때마다 느슨하게 평가되며 내부의 변수가 유지되고 있기 때문입니다.

```
>>> def infinite_generator():
...     count = 0
...     while True:
...             count+=1
...             yield count
... 
>>> gen = infinite_generator()
>>> next(gen)
1
>>> next(gen)
2
>>> next(gen)
3
>>> next(gen)
4
>>> next(gen)
5
>>> next(gen)
6
>>> next(gen)
7
>>> next(gen)
8
>>> next(gen)
9
>>> next(gen)
10
>>> next(gen)
11
>>> next(gen)
12
... 계속
```

- 우리가 알고 있는 리스트, Set, Dictionary의 표현식의 내부도 사실 generator입니다.

```
>>> type(x*x for x in [2, 4, 6])
<class 'generator'>
```



## 3. yield from

- 파이썬 3.3 이상 부터 사용가능
- yield문은 한번씩 값을 바깥으로 전달했습니다. 여러번 바깥으로 전달할려면 for문을 아래와 같이 사용해야합니다.

```
>>> def three_generator():
...     a = [1, 2, 3]
...     for i in a:
...             yield i
... 
>>> gen = three_generator()
>>> list(gen)
[1, 2, 3]
```

- 이러한 상황에서 for문 대신에 iterable한객체를 yield할 때는 `yield from iterable` 로 값을 전달할 수 있습니다.
- 위의 코드를 변경해보겠습니다.

```
>>> def three_generator():
...     a = [1, 2, 3]
...     yield from a
... 
>>> gen = three_generator()
>>> list(gen)
[1, 2, 3]
```