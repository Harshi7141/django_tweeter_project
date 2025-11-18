from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('', views.tweet_list, name='tweet_page'),
    path('<int:tweet_id>/delete/', views.tweet_delete, name='tweet_delete'),
    path('tweet-create', views.tweet_create, name='tweet_create'),
    path('<int:tweet_id>/edit/', views.tweet_edit, name='tweet_edit'),
    path('register/', views.register, name='register'),
    # path('login/', views.login, name='login'),


]
