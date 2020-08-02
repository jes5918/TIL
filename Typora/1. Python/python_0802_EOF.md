# EOF(End Of Files) 이란 무엇일까?

>백준 10952 문제를 참고해보면 while문을 이용하여 2자리 수를 입력받고 그 합을 출력한다. 그 후 아무것도 입력이 들어오지 않으면 while문을 빠져나가는 알고리즘을 구현해야 한다.



## 10952 문제

두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

## 입력

입력은 여러 개의 테스트 케이스로 이루어져 있다.

각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)

## 출력

각 테스트 케이스마다 A+B를 출력한다.

```
1 1
2 3
3 4
9 8
5 2
```

```
2
5
7
17
7
```



#### 내가 푼 풀이

```python
import sys
while True:
    line = sys.stdin.readline().split()
    if not line:
        break
    numbers = list(map(int, line))
    print(sum(numbers))
```

```python
3 5
8
2 4
6
5 3
8

```

> 각각의 숫자를 space를 사용하여 입력하고 그 합을 출력해 낸다. 그후 아무것도 입력하지 않으면
>
> break를 이용해서 while을 빠져 나오는 알고리즘을 구현하였다.