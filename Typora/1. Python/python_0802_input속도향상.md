# input()의 속도는 느리다?

>coding을 하면서 처리 속도를 높이는데 핵심은 입출력의 속도를 향상시키는 것이다.
>
>input() 보다 더 빠르게 처리할 수 있는 sys.stdin.readline() 이라는 것을 알아보자



#### 백준 15552번 문제 참고

본격적으로 for문 문제를 풀기 전에 주의해야 할 점이 있다. 입출력 방식이 느리면 여러 줄을 입력받거나 출력할 때 시간초과가 날 수 있다는 점이다.

C++을 사용하고 있고 `cin`/`cout`을 사용하고자 한다면, `cin.tie(NULL)`과 `sync_with_stdio(false)`를 둘 다 적용해 주고, `endl` 대신 개행문자(`\n`)를 쓰자. 단, 이렇게 하면 더 이상 `scanf`/`printf`/`puts`/`getchar`/`putchar` 등 C의 입출력 방식을 사용하면 안 된다.

Java를 사용하고 있다면, `Scanner`와 `System.out.println` 대신 `BufferedReader`와 `BufferedWriter`를 사용할 수 있다. `BufferedWriter.flush`는 맨 마지막에 한 번만 하면 된다.

Python을 사용하고 있다면, `input` 대신 `sys.stdin.readline`을 사용할 수 있다. 단, 이때는 맨 끝의 개행문자까지 같이 입력받기 때문에 문자열을 저장하고 싶을 경우 `.rstrip()`을 추가로 해 주는 것이 좋다.

또한 입력과 출력 스트림은 별개이므로, 테스트케이스를 전부 입력받아서 저장한 뒤 전부 출력할 필요는 없다. 테스트케이스를 하나 받은 뒤 하나 출력해도 된다.

자세한 설명 및 다른 언어의 경우는 [이 글](http://www.acmicpc.net/board/view/22716)에 설명되어 있다.

[이 블로그 글](http://www.acmicpc.net/blog/view/55)에서 BOJ의 기타 여러 가지 팁을 볼 수 있다.



#### 그렇다면 내가 한번 예시를 코딩해 보자

```python
import sys
a = sys.stdin.readline() # 한개의 문자를 받는다.
b = int(sys.stdin.readline()) # 한개의 문자를 받아 숫자로 변환시켜줌
c = sys.stdin.readline().split() # 띄어쓰기를 이용하여 여러개의 문자를 받아 리스트로 만들어준다
d = map(int, sys.stdin.readline().split()) # 여러개의 문자를 입력받아 숫자로 반환

print(type(a))
print(a)
print(type(b))
print(b)
print(type(c))
print(c)
print(type(d))
print(d)
```

- 입력부분

```python
asdaasd
23
23 32
43 43 23
```

- 출력부분

```python
<class 'str'>
asdaasd

<class 'int'>
23
<class 'list'>
['23', '32']
<class 'map'>
<map object at 0x00000133644D9AC8>
```

> 예상대로 str, int , list, map 이 출력되었다. 여기서 궁금한 것은 과연  3번째 줄에 공백이 왜 생겼을까?

Python을 사용하고 있다면, `input` 대신 `sys.stdin.readline`을 사용할 수 있다. 단, 이때는 맨 끝의 개행문자까지 같이 입력받기 때문에 문자열을 저장하고 싶을 경우 `.rstrip()`을 추가로 해 주는 것이 좋다.

> 이와같이 개행문자까지 같이 입력받기 때문에 문자열을 저장하고 싶은 경우는 `.rstrip()`을 추가하여 공백을 없앨 수 있다.

```python
import sys
a = sys.stdin.readline().rstrip()
print(type(a))
print(a)
print('여기가 끝이다.')
```

- 출력결과

```python
asdasd
<class 'str'>
asdasd
여기가 끝이다.
```

> 이와같이 이번에는 공백이 생기지 않게 되었다.