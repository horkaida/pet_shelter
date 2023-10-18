from django.urls import path

from . import views

urlpatterns = [
    path('user', views.get_user, name='get_user'),
    path('user/history', views.get_user_history, name='get_user_history'),
    path('login', views.log_in, name='log_in'),
    path('logout', views.log_out, name='log_out'),
    path('register', views.register, name='register'),
]