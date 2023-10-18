from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_all_posts, name='get_all_posts'),
    path('<int:post_id>', views.get_post, name='get_post'),
]