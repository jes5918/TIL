#### 1. python에서 사용할 수 없는 식별자(예약어)를 찾아 작성하시오.
```python
import keyword
print(keyword.kwlist)
```

```python
['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
```



#### 2.실수비교

```python
num1 = 0.1 * 3
num2 = 0.3
round(num1,1) == num2
```

> 결과 : True

```python
import math
num1 = 0.1 * 3
num2 = 0.3
math.isclose(num1, num2)
```

>  결과 : True

```python
import sys
num1 = 0.1 * 3
num2 = 0.3
abs(num1-num2) <= sys.float_info.epsilon
```

> 결과 : True



#### 3.이스케이프 시퀀스

(1) 줄 바꿈 => \n

```python
print('나는\n이스케이프\n시퀀스야')
```

```python
나는
이스케이프
시퀀스야
```

(2) 탭 => \t

```python
print('나는\t이스케이프\t시퀀스야')
```

```python
나는	이스케이프	시퀀스야
```

(3) 백슬래시 => \\\

```python
print('나는\\이스케이프\\시퀀스야')
```

```python
나는\이스케이프\시퀀스야
```



#### 4. String Interpolation

(1) %-formatting

```python
name = '철수'
print('안녕, %s야' %name)
```

```python
안녕, 철수야
```

(1) str.format()

```python
name = '철수'
print('안녕, {}야'.format(name))
```

```python
안녕, 철수야
```

(1) f-strings

```python
name = '철수'
print(f'안녕, {name}야')
```

```python
안녕, 철수야
```



#### 5. 형 변환

​	다음 중, 실행 시 오류가 발생하는 코드를 고르시오.

```python
str(1) # (1)
int('30') # (2)
int(5) # (3)
bool('50') # (4)
int('3.5') # (5)
```

> 답 : (5)가 오류가 발생된다

> 이유 : 명시적 형변환에 의해 string -> intger는 형식에 맞는 숫자만 가능하고, integer -> string은 모두 가능하다. 
>
> 즉, int('3.5')는 형식에 맞지 않는 3.5라는 숫자가 들어왔으니 오류가 발생된다.

만일 int(3.5) 였으면 3.5의 형식이 float형 이기 때문에 결과가 3이 나오게 된다



#### 6. 네모 출력

![image-20200720223113010](C:\Users\Jeon\AppData\Roaming\Typora\typora-user-images\image-20200720223113010.png)

```python
n = 5
m = 9
print('*' * n) 
print('*',' ','*')
print('*',' ','*')
print('*',' ','*')
print('*',' ','*')
print('*',' ','*')
print('*',' ','*')
print('*',' ','*')
print('*' * n) 

```



#### 7. 이스케이프 시퀀스 응용

```python
“파일은 c:\Windows\Users\내문서\Python에 저장이 되었습니다.”
나는 생각했다. ‘cd를 써서 git bash로 들어가 봐야지.’
```

```python
print('\"파일은 c:\\Windows\\Users\\내문서\\Python에 저장이 되었습니다.\"\n나는 생각했다. \'cd를 써서 git bash로 들어가 봐야지.\'')
```



#### 8. 근의 공식![image-20200720222212677](C:\Users\Jeon\AppData\Roaming\Typora\typora-user-images\image-20200720222212677.png)

```python
a, b, c = map(int,input('근의 공식에 대입할 a, b, c (숫자)를 차례로 입력하세요(띄어쓰기로 구분) : ').split())

root1 = (-b + ((b ** b) - (4 * a * c) ** 0.5)) / (2 * a)
root2 = (-b - ((b ** b) - (4 * a * c) ** 0.5)) / (2 * a)

print(f'2차 방정식의 근은 {root1}, {root2}입니다')
```

