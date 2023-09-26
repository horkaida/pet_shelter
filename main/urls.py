from django.urls import path

from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('contacts', views.get_our_contacts, name='get_our_contacts'),
]