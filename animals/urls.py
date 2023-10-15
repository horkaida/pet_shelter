from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_all_animals, name='get_all_animals'),
    path('int:<animal_id>', views.get_animal, name='get_animal'),
    path('schedule', views.get_schedule, name='get_schedule'),
    path('feedback', views.get_animal_feedbacks, name='get_animal_feedbacks'),
]