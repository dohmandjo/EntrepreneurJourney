from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name = 'post_list'),
    path('create/', views.create_post, name = 'create_post'),
    path('post/<int:pk>/', views.post_detail, name = 'post_detail'),
    path('post/<int:pk>/comment', views.add_comment, name = 'add_comment'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.register, name='register'),
]