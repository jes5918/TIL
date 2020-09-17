# django - auth



### 1 . 비밀번호 변경

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