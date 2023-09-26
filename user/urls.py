from django.urls import path

from . import views

urlpatterns = [
    path('user', views.get_user, name='get_user'),
    path('user/history', views.get_user_history, name='get_user_history'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('register', views.register, name='register'),
]