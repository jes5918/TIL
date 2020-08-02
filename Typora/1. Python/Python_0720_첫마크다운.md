# Python 1일차 (20.07.20)

## 1. Python 기초

### 기초문법	

	>주석(comment)

- 한 줄 주석은  `#`으로 표현한다.
- `'''` 으로 여러줄의 주석을 표현할 수 있습니다.

```python
"""
  이건 여러
  줄의 걸쳐
  쓸수있는 주석입니다.
"""
```

> 코드 라인

- 파이썬 코드는 1줄에 1문장이 원칙
- 기본적으로 파이썬에서는 `;`을 작성하지 않는다.
- 한 줄로 표기할때는 `;`을 작성하여 표기할 수 있다.



## 2. 헤더

```python
print('hello','p'+'22''2') 
print('world')
print('hello','p'+'22''2'); print('world')
print(
    '''
    안녕
    나는
    python이야
    '''
)
print('안녕\
나는\
python이야\
')

menu =[
       '김밥',
       '돈까스',
       '햄버거'
]
print(menu)
```



## 3. 변수(Variable)

### 변수

> 할당연산자

- 변수는`=`를 통해 할당된다

```python
x = 'ssafy'
```

- 해당 데이터 타입을 확인하기 위해서는 `tpye()`을 활용한다.

```python
type(x)
```

- 해당 값의 메모리 주소를 확인하기 위해서는 `id()`를 활용한다.

```python
id(x)
```

- 같은 값을 동시에 할당 가능하다.

```python
x = y = 'ssafy'
print(x,y)
```

- 다른 값을 동시에 할당 가능하다.

```python
a, b = 2020, 4
print(a,b)
```



>식별자

- 파이썬에서 식별자는 변수, 함수, 모듈, 클래스 등을 식별하는데 사용되는 이름
  - 대소문자를 구별한다
  - 첫글자에 숫자가 올 수 없다
  - 식별자의 이름은 영문알파벳, 밑줄, 숫자로 구성된다.
  - 길이제한이 없다

```	python
import keyword
print(keyword.kwlist)
```



## 4. 데이터타입(Data Type)

### 숫자타입

> 1. int(정수)

- 모든 정수는 `int`로 표현됩니다.

- 파이썬 3.x 버전에서는 `long` 타입은 없고 모두 `int`타입으로 표기 된다.

- 8진수 : `0o` / 2진수 : `0b` / 16진수: `0x` 로도 표현 가능합니다.

  ```python
  binary_number = 0b10
  octal_number = 0o10
  hexadecimal_number = 0x10
  print(binary_number)
  print(octal_number)
  print(hexadecimal_number)
  ```

>2. float(실수)

- 실수는 `float`로 표현됩니다. 

- 다만, 실수를 컴퓨터가 표현하는 과정에서 부동소수점을 사용하며, 항상 같은 값으로 일치되지 않습니다. (floating point rounding error) 이는 컴퓨터가 2진수(비트)를 통해 숫자를 표현하는 과정에서 생기는 오류이며, 대부분의 경우는 중요하지 않으나 값을 같은지 비교하는 과정에서 문제가 발생할 수 있습니다.

  ```pyrhon
  3.5 - 3.2 == 0.3
  ```

  ```python
  False
  ```
  ```pyrhon
  round(3.5 - 3.2,1) == 0.3
  ```

  ```python
  True
  ```

  (round 의 1은 유효숫자 1자리까지 반올림 한다는 말이다.)
  
- 컴퓨터식 지수 표현 방식

  - E를 사용할 수 있다.

   ```python
  b = 314E-2
  print(b)
   ```


> 3. complex(복소수)

- 복소수는 허수부를 `j`로 표현합니다.

	```python
	b = complex('3+4j')
	type(b)
	```

- 문자열을 변환할 때, 문자열은 중앙의 + 또는 - 연산자 주위에 공백을 포함해서는 안 됩니다. (아래는 오류가 뜬다)

  ```python
  c = complex('3 + 4j')
  ```

  

### 문자타입

> 기본 활용법

- 문자열은 Single quotes(`'`)나 Double quotes(`"`)을 활용하여 표현 가능하다.
  - 작은따옴표: `'"큰" 따옴표를 담을 수 있습니다'`
  - 큰따옴표: `"'작은' 따옴표를 담을 수 있습니다"`
  - 삼중 따옴표: `'''세 개의 작은따옴표'''`, `"""세 개의 큰따옴표"""`

> 따옴표 사용

- 문자열 안에 문장부호(`'`, `"`)가 사용될 경우 이스케이프 문자(`\`)를 활용 가능 합니다.

```python
"그의 이름은 "ssafy"였다"
```

  위는 오류가 발생한다

```python
"그의 이름은 \"ssafy\"였다"
```



>이스케이프 시퀀스

- 문자열을 활용하는 경우 특수문자 혹은 조작을 하기 위하여 사용되는 것으로 `\`를 활용하여 이를 구분합니다.

| 예약문자 | 내용(의미)        |
| -------- | ----------------- |
| \n       | 줄 바꿈           |
| \t       | 탭                |
| \r       | 캐리지리턴        |
| \0       | 널(Null)          |
| \\       | `\`               |
| \'       | 단일인용부호(`'`) |
| \"       | 이중인용부호(`"`) |

> String interpolation

- `%-formatting`

```python
print('내 이름은 %s 입니다.' %name)
'내 이름은 %s 입니다.' %name
```

- [`str.format()`](https://pyformat.info/)

```python
print('내 이름은 {}입니다.'.format(name))
```

- [`f-strings`](https://www.python.org/dev/peps/pep-0498/) : 파이썬 3.6 이후 버전에서 지원

```python
print(f'내 이름은 {name}입니다.')
```

- f-strings에서는 형식을 지정할 수 있다.

```python import datetime
import datetime
now = datetime.datetime.now()
print(now)

now.today()
print(f'올해는 {now:%Y}년 이번달은 {now:%m}월 오늘은 {now:%d}일')
```

```python
pi = 3.141592
r = 10
print(f'{pi:.3} 넓이는 : {pi*r*r:.3}')
```



### 참/거짓 타입

> 파이썬에는 `True`와 `False`로 이뤄진 `bool` 타입이 있습니다.비교/논리 연산을 수행 등에서 활용됩니다. 다음은 `False`로 변환됩니다.

```python
0, 0.0, (), [], {}, '', None
```

```python
bool('')
```

결과는 False

> 1. None 타입

- 파이썬에서는 값이 없음을 표현하기 위해 `None` 타입이 존재합니다.

```python
type(None)
```

결과는 NoneType



### 형변환

> 	1. 암시적 형변환

- boolean 과 integer는 더할 수 있을까요?

```python
True + 3
```

결과는 4

```python
False + 3
```

결과는 3

```python
True + 3
int(True)
```

결과는 1

```python
result = None
result + 3
```

오류발생

```python
int_number = 2020
float_number = 3.14
complex_number = 2 + 3j
print(int_number + float_number)
print(int_number + complex_number)
```

결과는 2023.14

​			(2022+3j)

complex >> float >> int 이다

> 2. 명시적 형변환

- 위의 상황을 제외하고는 모두 명시적으로 형 변환을 해주어야합니다.

  - string -> intger : 형식에 맞는 숫자만 가능
  - integer -> string : 모두 가능
- 위의 상황을 제외하고는 모두 명시적으로 형 변환을 해주어야합니다.

  - `int()` : string, float를 int로 변환
  - `float()` : string, int를 float로 변환
  - `str()` : int, float, list, tuple, dictionary를 문자열로 변환



## 5. 연산자(Operater)



