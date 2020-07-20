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

> 3. complex(복소수)

### 문자타입

> 1. 따옴표 사용

>2. 이스케이프 시퀀스

> 3. String interpolation

### 참/거짓 타입

> 1. None 타입

### 형변환

> ​	1. 암시적 형변환

> ​	2. 명시적 형변환



## 5. 연산자(Operater)



