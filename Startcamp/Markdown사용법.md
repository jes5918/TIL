# 온라인1일차 20200717

## GIT

``````
GIT 조아요
``````

![image-20200717104319640](C:\Users\Jeon\AppData\Roaming\Typora\typora-user-images\image-20200717104319640.png)![image-20200717104419403](C:\Users\Jeon\AppData\Roaming\Typora\typora-user-images\image-20200717104419403.png)



## 마크다운(markdown)

> 마크타운은 개발자들의 메모장



## 1. 문법

### 1.1 Header

> 헤더는 제목을 표현할 떄 사용합니다.

 - h1(가장 큰 제목) 부터 h6(가장 작은 제목)까지 표현 가능합니다.
 - #의 개수로 표현합니다.

### 1.2 List

> 목록을 나열할 때 사용합니다. 순서가 있거나 없는 목록을 만들 수 있습니다.

 	1. 순서가 있는 목록
          	1. 1.을 누르고 스페이스바를 누르면 생성할 수 있습니다.
      	2. tab키를 누르면 하위 항목을 생성할 수 있고, SHIFT+TAB을 통해 
          상위로 이동도 가능합니다.

- 순서가 없는 목록

  - (하이픈)을 쓰고 스페이스바를 누르면 생성할 수 있습니다.
  - tab키를 누르면 하위 항목을 생성할 수 있고, SHIFT+TAB을 통해 
    상위로 이동도 가능합니다.

### 1.3 코드 블락

> 코드 블럭은 작성한 코드를 정리하거나 강조하고 싶은 부분을 나타낼때 사용합니다.````

- Inline

  - 인라인 블럭으로 처리하고 싶은 부분을 백틱(`)으로 감싸줍니다.
  - `예시`

- Block

  - 백틱을 세 번 입력하고 Enter를 누르면 생성됩니다.

  - ``` python
    import random
    choice = random.choice(range(1,46))
    ```

  ### 1.4 이미지

- 참고 : 윈도우10에서 win + shift + s 키를 누르면 손쉽게 캡처가 가능합니다.

 <img src="온라인1일차 20200717.assets/image-20200717112929315.png" alt="image-20200717112929315" style="zoom: 67%;" />

- `! [] ()`을 작성하고 `() `안에 이미지 주소를 입력합니다. `[]` 안에는 이미지 파일의 이름을 작성합니다.

  

### 1.5 Link

> 특정 주소로 링크를 걸 때 사용합니다.
>
> - `[] ()`을 작성하고 `() `안에 이미지 주소를 입력합니다. `[]` 안에는 이미지 파일의 이름을 작성합니다.
> - [구글](www.google.com)

### 1.6 Table

> 표를 작성하여 요소를 구분할 수 있습니다.

- `|`(파이프) 사이에 컬럼을 작성하고,  enter를 눌러줍니다.
- 마지막으로 파이프로 끝내주어야 합니다.
- `ctrl` + `enter` 해주시면 추가가 됩니다.

| 이름   | 성별 | 나이 |
| ------ | ---- | ---- |
| 전의수 | 남자 | 27   |
| 이현우 | 남자 | 21   |



## 2. 챗봇 퀘스트

[날씨 API](https://openweathermap.org/current#name)

key = 
url = f'https://api.openweathermap.org/data/2.5/weather?q=Daejeon&appid={key}'
response = requests.get(url).text



![image-20200717154805813](온라인1일차 20200717.assets/image-20200717154805813.png)

- bs4 