from django.urls import path
from . import views 


urlpatterns = [
    path('articles/', views.article_list_create),
    path('articles/<int:article_pk>/', views.article_detail_update_delete),
    path('articles/<int:article_pk>/comments/', views.create_comment),

    path('comments/', views.comment_list),
    path('comments/<int:comment_pk>/', views.comment_detail_update_delete),
]
