from django.urls import path
from . import views

# create url patterns for all views to display different pages
urlpatterns = [
    # Path for post_list page
    path('', views.post_list, name = 'post_list'),
    # Path for create_post page
    path('create/', views.create_post, name = 'create_post'),
    # Path for post_detail page
    path('post/<int:pk>/', views.post_detail, name = 'post_detail'),
    # Path for add_comment page
    path('post/<int:pk>/comment', views.add_comment, name = 'add_comment'),
    # Path for login page
    path('login/', views.user_login, name='login'),
    # Path for logout page
    path('logout/', views.user_logout, name='logout'),
    # Path for register page
    path('register/', views.register, name='register'),
]