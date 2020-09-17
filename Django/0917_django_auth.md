# django - auth

### intro. 프로젝트시작

#### 가상환경

- ```
  python -m venv venv
  ```


#### Start Project

- `django-admin startproject {프로젝트 이름}`

#### Start app

- `python manage.py startapp articles`

#### app 등록

- `settings.py` 에 `articles` 등록

#### Base template 등록

- project 폴더에

  ```
  templates
  ```

  폴더를 등록하고

  ```
  settings.py
  ```

  의 TEMPLATES 경로를 바꿔준다.


#### urlpatterns

- ```
  path('articles/',include('articles/urls'))
  ```

  - project 폴더의 urls에서 여러개의 app이 존재할 때 views에 정의된 함수의 이름이 같은 경우를 위해 Project/urls.py 를 App/urls.py 로 옮긴 것
  - App/urls.py에 `app_name = 'articles'` 설정해야 project urls에서 app의 urls까지 경로를 찾아온다.

#### urls -> views -> templates

- urls에서 path를 지정하면, views.py의 함수 로직을 실행하고, 사용자에게 로직 결과를 templates를 통해 보여준다.



#### models

- models.py에서는 app에서 사용될 데이터베이스의 뼈대를 구축한다.
  - `python manage.py makemigrations`
  - 모델을 활성화 하기 전에 DB 설계도 작성을 하고 migrations 폴더 안에 정의한 class를 토대로 Django ORM이 우리에게 만들어준 설계도를 확인한다.
  - `python manage.py migrate`
  - migrate는 makemigrations로 만든 설계도를 실제 db.sqlite3 DB에 반영한다.



#### 1 . 비밀번호 변경

![image-20200917235524465](C:\Users\John YG\Desktop\TIL\Django\0917_django_auth.assets\image-20200917235524465.png)

- views.py

```python
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('articles:index')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form': form
    }
    return render(request, 'accounts/change_password.html', context)
```

> django 내부에 있는 PasswordChangeForm을 이용하여 비밀번호를 변경하는 form을 만든다, 
>
> 비밀번호변경은 로그인 된 상태여야만 설정할 수 있게 `decoration`을 이용하여 `@login_required`를 설정하였다,
>
> 또한 POST요청이 들어와야지 비밀번호를 변경 할 수 있게 하여 조건뭉르 사용하였고,
>
> 조건문 첫줄에 있는 `form`에는 현재 사용자의 비밀번호를 인자로 가지고 있어야 하기 때문에 `PasswordChangeForm(request.user, request.POST)` 형태로 받아야한다.
>
> `request.user`에는 비밀번호를 변경할 유저의 정보, 이후 POST로직에서는 user의 정보와 POST한 정보 중 old password의 일치를 확인하는 작업을 한 후 타당하다면 비밀번호 재설정이 완료된다.
>
> ###### 이 때 `update_session_auth_hash` 는 session update를 통해 웹사이트의 session_id를 재설정한 비밀번호로 바꿔줘서 비밀번호가 바껴도 로그인이 끊어지는 상황을 막아준다, 이 작업이 없다면, 기존에 웹사이트가 가지고 있던 session_id와 재설정한 password가 맞지 않아 로그인하지 않은 것처럼 보여진다.



- urls.py

```python
from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('change-password/', views.change_password, name='change_password'),
    ......
]

```

>경로에 `-` 표시를  할 때에는  주소창에 쓰여질 부분만 중간 하이퍼  모양을 넣고, 나머지는 언더바 형태로 저장한다.



- change-password.html

```python
{% extends 'base.html' %}

{% block content %}

<h2>비밀번호 변경</h2>
<form method="POST">
  {% csrf_token %}
  {{ form.as_ul}}
  <button type="submit">Save changes</button>
</form>

{% endblock %}
```

- base.html

```python
...
<body>
  <div class="container">
    {% if request.user.is_authenticated %}
    <h3>Hello, {{ user.username }}</h3>
    <a href="{% url 'accounts:update' %}">정보수정</a>
    <a href="{% url 'accounts:logout' %}">로그아웃</a>
    <a href="{% url 'accounts:change_password' %}">비밀번호 변경</a>
    {% else %}
      <h3>로그인을 해주세요</h3>
      <a href="{% url 'accounts:signup' %}">회원가입</a>
      <a href="{% url 'accounts:login' %}">로그인</a>
    {% endif %}

    {% block content %}
    {% endblock %}
...
```

> if 문을 사용하여 사용자가 로그인 되었을때 (`user.is_authenticated`) 비밀번호 변경 표시가 
>
> 나타나도록 설정하였다.





### 2 . 계정삭제

- views.py

```python
@login_required
def delete(request):
    if request.method == 'POST':
        request.user.delete()
        return redirect('articles:index')
    return render(request, 'accounts/delete.html')
```

>계정삭제 또한 login 상태여야 하기 떄문에 데코레이션을 이용하여 views.delete에 접근 할 수 있게 하였으며
>
>POST메소드 일때만 계정을 삭제하도록 설정하였다,
>
>POST메소드가 아니고 다른 메소드가 입력으로 들어온다면 링크를 다시 되돌려보낸다(?)



- delete.html

```python
{% extends 'base.html' %}

{% block content %}
<h1>회원정보 수정</h1>
<form action="" method="POST">
  {% csrf_token %}
  {{ form.as_p }}
  <input type="submit">
</form>
{% endblock %}
```



### 3. 암호화 알고리즘

```python
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
]
```

 `PBKDF2PasswordHasher` 의 코드를 보면

```
class PBKDF2PasswordHasher(BasePasswordHasher):
    """
    Secure password hashing using the PBKDF2 algorithm (recommended)

    Configured to use PBKDF2 + HMAC + SHA256.
    The result is a 64 byte binary string.  Iterations may be changed
    safely but you must rename the algorithm if you change SHA256.
    """
    algorithm = "pbkdf2_sha256"
    iterations = 36000
    digest = hashlib.sha256

    def encode(self, password, salt, iterations=None):
        assert password is not None
        assert salt and '$' not in salt
        if not iterations:
            iterations = self.iterations
        hash = pbkdf2(password, salt, iterations, digest=self.digest)
        hash = base64.b64encode(hash).decode('ascii').strip()
        return "%s$%d$%s$%s" % (self.algorithm, iterations, salt, hash)
```

`iterations` 의 기본값은 36000 번이고, `algorithm` 은 pbkdf2_sha256 이다.

- 모든 서버는 password 자체를 그대로 저장하지 않는다 (심각한 보안문제)
- 만약에 password를 내가 그대로 저장하면 무슨일이 일어날까?
  1. 나(관리자) - DB접속가능, 모든데이터 확인가능
     - 내가 모든 유저의 아이디 비번 내가 get할 수 있음.
  2. DB가 털렸을 때, 모든 내 이용자의 모든 정보가 털림
- Hash함수를 이용하여 비밀번호를 암화화 할 수 있다.
- 즉, DB가 있어도 비밀번호를 해독하지 못하도록 암호화 하는 것이다.



### 4. Logout

```python
def logout(request):
    logout(request)
    return redirect('accounts:login')
```

- 위와 같이 logout 함수로 지웠을 때에는 쿠키, DB에서 모두 session_id가 삭제된다.
- 이를 해결하기 위해서 ssesion만 지우는 아래와 같은 코드 작성을 통해 DB를 유지시킨다.

```python
from django.contrib.auth import logout as auth_logout

#session만 지우는 것!
def logout(request):
    auth_logout(request)
    return redirect('articles:index')
```



### 5. Django Form

 ```python
 # ModelForm 적용 전
 def new(request):
     return render(request, 'articles/new.html')
 
 def create(request):
     title = request.POST.get('title') 
     content = request.POST.get('content')
     article = Article(title=title, content=content)
     article.save()
     return redirect('articles:detail', article.pk)
 ```

```python
# ModelForm 적용 후
 def create(request):
     if request.method == 'POST':
         form = ArticleForm(request.POST, request.FILES)
         if form.is_valid():
             article = form.save()
             return redirect('articles:detail', article.pk)
     else: 
         form = ArticleForm()
     context = {
         'form': form,
     }
     return render(request, 'articles/create.html', context)
```

- Django ModelForm은 우리가 생성한 Model을 뼈대로 Form태그를 자동으로 작성해주는 것을 제공한다. 이를 통해서 조금 더 가독성있고 효율성있는 코딩을 할 수 있게 되었다.



### 6. Decoration - 수아가 보내준거

> 1. 비로그인상태로 POST로 delete 요청
> 2. login_required로 인해서 로그인 페이지로 redirect + next파라미터(/delete/)가지고
> 3. 로그인페이지에서 로그인 성공
> 4. next파라미터 주소로 redirect됨
> 5. require_POST로 인해 405 에러 발생
> 6. 405error! , redirect는 무조건 url요청이기에 GET!근데 POST만 들어갈 수있기 떄문에 에러!(method not allowed)로직상 같이 붙어 있으면 안됨!
> 7. 위의 다른 경우들은 다 GET도 처리할 수 있기 때문에 괜찮지만 delete는 post만이기 때문에 걸림
>
> 결론: login_required 데코레이터는 GET method요청을 처리할 수 있는 view에서만 사용

- `accounts` > `views.py` > `delete 뷰함수`

```python
@login_required2
@require_POST3
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')

#아래처럼 고침
@require_POST10
def delete(request, pk):
    if request.user.is_authenticated:
        article = Article.objects.get(pk=pk)
        article.delete()
        return redirect('articles:index')`
```

