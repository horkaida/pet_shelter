from django.shortcuts import render
import animals.models

def get_all_animals(request):
    animal_list = animals.models.Animal.objects.all()
    return render(request, 'animals/animals.html', {"animal_list":animal_list})

def get_animal(request, animal_id):
    animal = animals.models.Animal.objects.get(id=animal_id)
    return render(request, 'animals/animals.html', {"animal":animal})

def get_schedule(request):
    return render(request, 'animals/animals.html', {})


def get_animal_feedbacks(request):
    return render(request, 'animals/feedbacks.html', {})